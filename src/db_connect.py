import sqlite3
from .scripts import *
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton
import re

async def restore_table(db_file):
    
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    try:
        sql = '''DROP TABLE elements;'''
        cursor.execute(sql)
    except:
        pass 

    sql = '''
     CREATE TABLE elements (
            code TEXT,
            category_1 TEXT,
            category_2 TEXT,
            category_3 TEXT,
            category_4 TEXT,
            category_5 TEXT,
            category_6 TEXT,
            category_7 TEXT,
            gesn TEXT
        );
    '''
    cursor.execute(sql)

    conn.commit()
    cursor.close()
    conn.close()

async def fill_db(db_file):

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    sql = '''
        INSERT INTO elements (code, category_1, category_2, category_3, category_4, category_5, category_6, category_7, gesn)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''

    columns = await extract_columns()

    for row in columns:
        cursor.execute(sql, row)
    
    conn.commit()
    cursor.close()
    conn.close()

async def get_kbrd(cats):
    unique = set(item[0] for item in cats)
    unique = list(unique)

    unique = [item for item in unique if item is not None]
    if len(unique) == 0:
        return None


    button_list = []
    for cat in unique:
        button_list.append(KeyboardButton(text=cat))

    buttons=[]
    #for i in range(0, len(button_list), 2):
    ## Добавляем по два элемента в подсписок
    #    if i + 1 < len(button_list):
    #        buttons.append([button_list[i], button_list[i + 1]])
    #    else:
    #        # Если элемент остается один, добавляем его отдельно
    #        buttons.append([button_list[i]])
    for i in button_list:
        buttons.append([i])
    
    keyboard_cat = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return keyboard_cat

async def find_cat(db_file, cat):
    
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    sql = f'''
       SELECT {cat} FROM elements;
    '''

    cursor.execute(sql)
    cat1 = cursor.fetchall()

    cursor.close()
    conn.close()

    keyboard_cat1 = await get_kbrd(cat1)
    

    return keyboard_cat1

async def find_cat_not1(db_file, cat, ans):
    
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    match = re.search(r'(\d+)$', cat)
    if match:
        # Извлечение числа из строки
        current_number = int(match.group(1))
        # Уменьшаем число на 1
        new_number = current_number - 1
        # Формируем новую строку
        new_category = re.sub(r'\d+$', str(new_number), cat)

    sql = f'''
       SELECT {cat} FROM elements WHERE {new_category} = "{ans}";
    '''


    cursor.execute(sql)
    cat1 = cursor.fetchall()

    cursor.close()
    conn.close()

    keyboard_cat1 = await get_kbrd(cat1)

    if keyboard_cat1 == None:
        gesn = await find_number(new_category, ans, db_file)
        if gesn == None:
            return "ГЭСН не найден"
        else:
            answer = "Подходящие ГЭСН: " + gesn
            print(gesn)
            xml = ""
            try: 
                xml = await get_gesn(gesn)
                answer += "\n" + xml
            except:
                answer += "\n Описание ГЭСН не найдено"
            
            return answer
    

    return keyboard_cat1

async def find_number(cat, name, db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    sql = f'''
    SELECT gesn FROM elements WHERE {cat} = '{name}'; 
    '''
    
    cursor.execute(sql)
    gesn = cursor.fetchall()

    cursor.close()
    conn.close()

    if gesn == None:
        return None
    else:
        return gesn[0][0]
