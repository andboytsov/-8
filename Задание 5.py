import random

# Списки предметов
common_items = ["Common Item 1", "Common Item 2", "Common Item 3"]
rare_items = ["Rare Item 1", "Rare Item 2", "Rare Item 3"]
epic_items = ["Epic Item 1", "Epic Item 2", "Epic Item 3"]
legendary_items = ["Legendary Item 1", "Legendary Item 2"]

# Шансы выпадения
drop_chances = {"Common": 0.7, "Rare": 0.2, "Epic": 0.1, "Legendary": 0.05}

# Счётчики выпавших предметов
common_count = 0
rare_count = 0
epic_count = 0
legendary_count = 0

# Открытие 20 лутбоксов
for _ in range(20):
    # Генерация случайного числа для определения качества предмета
    chance = random.random()
    
    if chance < drop_chances["Common"]:
        common_count += 1
    elif chance < drop_chances["Common"] + drop_chances["Rare"]:
        rare_count += 1
    elif chance < drop_chances["Common"] + drop_chances["Rare"] + drop_chances["Epic"]:
        epic_count += 1
    else:
        legendary_count += 1

# Проверка на условия удачи
luck_message = ""
if epic_count > 3:
    luck_message = "(удача!)"
if legendary_count > 1:
    luck_message = "(большая удача!)"

# Вывод результатов
print(f"Common: {common_count}, Rare: {rare_count}, Epic: {epic_count}, Legendary: {legendary_count} {luck_message}")

# Список полученных предметов с цветами
items_list = ["\033[0m" + f"Common: {item}" for item in common_items[:common_count]] + \
             ["\033[34m" + f"Rare: {item}" for item in rare_items[:rare_count]] + \
             ["\033[35m" + f"Epic: {item}" for item in epic_items[:epic_count]] + \
             ["\033[33m" + f"Legendary: {item}" for item in legendary_items[:legendary_count]]

print("\n".join(items_list))