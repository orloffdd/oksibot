import xml.etree.ElementTree as ET

filename = "xml/ГЭСН.xml"
# Загрузка XML из файла
tree = ET.parse(filename)
root = tree.getroot()

# Код, который ищем
target_code = "27-06-009"

# Ищем элемент <Section> с нужным кодом
section = root.find(f".//Section[@Code='{target_code}']")

# Список для хранения результатов
results = []

if section is not None:
    # Проходим по всем элементам <NameGroup> внутри найденной секции
    for name_group in section.findall("NameGroup"):
        begin_name = name_group.get('BeginName')  # Извлекаем BeginName
        # Проходим по всем элементам <Work> внутри каждого <NameGroup>
        for work in name_group.findall("Work"):
            work_code = work.get('Code')
            end_name = work.get('EndName')  # Извлекаем EndName
            if work_code.startswith(target_code):  # Проверяем, начинается ли код с target_code
                # Создаём словарь для текущей работы
                work_dict = {begin_name: end_name, "Resources": {}}
                # Ищем все <Resource> и заполняем словарь
                for resource in work.findall("Resources/Resource"):
                    resource_end_name = resource.get('EndName')
                    quantity = resource.get('Quantity')
                    if resource_end_name and quantity:  # Убедимся, что end_name и quantity существуют
                        work_dict["Resources"][resource_end_name] = quantity
                # Добавляем словарь в список результатов
                results.append({work_code: work_dict})

# Вывод результатов
result_str = ""
for result in results:
    for key, value in result.items():
        result_str += f"\nКод работы: {key}\n"
        for k, v in value.items():
            if k != "Resources":
                result_str += f"{k}: {v}\n"
            else:
                result_str += "Ресурсы:\n"
                for resource_name, quantity in v.items():
                    result_str += f"  {resource_name}: {quantity}\n"

print(result_str)
