import calendar
import json
from pprint import pprint
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plot
import pandas as pd
import numpy as np
from prettytable import PrettyTable

#======================ВЫВОД ВСЕХ СТУДЕНТОВ И СКОЛЬКО ИЗ КАЖДОЙ ГРУППЫ===========================
"""
with open('E:/course work/CTF MF.2022-02-10/db/users.json') as file:
    f = file.read()
    data = json.loads(f)

for text in data['results']:
    if text['affiliation'] is not None:
        print(f"Имя: {text['name']}, email: {text['email']}, группа: {text['affiliation']}")
    else:
        print(f"Имя: {text['name']}, email: {text['email']}, группа: не указана")

#Тут начинает считать, сколько из каждой группы
counts = dict()
for text in data['results']:
    if text['affiliation'] in counts.keys():
        counts[text['affiliation']] += 1
    else:
        counts[text['affiliation']] = 1

print("\nКоличество студентов в системе из каждой группы: ")
for key, value in counts.items():
    if key is not None:
        print(f"Группа \"{key}\" - {value} человек в системе")
    else:
        print(f"У {value} человек в системе группа не указана")
"""
#=============================================================================

#==================ВЫВОД СТУДЕНТОВ ОПРЕДЕЛЕННОЙ ГРУППЫ====================
"""
with open('E:/course work/CTF MF.2022-02-10/db/users.json') as file:
    f = file.read()
    data = json.loads(f)
group = input("Введите группу: ")

numStud = 0
for text in data['results']:
    if text['affiliation'] == group:
        print(text['name'], ':', text['email'])
        numStud += 1

if numStud == 0:
    print(f"Студентов группы {group} нет в системе. Проверьте введенные данные")
else:
    print(f"Количество студентов группы {group} в системе: {numStud}")
"""
#===========================================================================

#=================СКОЛЬКО У КОГО ПРАВИЛЬНЫХ ОТВЕТОВ==========================
"""
with open('E:/course work/CTF MF.2022-02-10/db/users.json') as file:
    f = file.read()
    users = json.loads(f)

with open('E:/course work/CTF MF.2022-02-10/db/solves.json') as file:
    f = file.read()
    solves = json.loads(f)
    
    for x in users['results']:
        result = 0
        for y in solves['results']:
            if x['id'] == y['user_id']:
                result += 1
        print(x['name'], ':', x['email'], ':', result)
"""
#======================================================

#===============У КОГО БОЛЬШЕ ВСЕГО РЕШЕННЫХ ЗАДАЧ===========
"""
with open('E:/course work/CTF MF.2022-02-10/db/users.json') as file:
    f = file.read()
    users = json.loads(f)

with open('E:/course work/CTF MF.2022-02-10/db/solves.json') as file:
    f = file.read()
    solves = json.loads(f)

max = 0
for x in users['results']:
    result = 0
    for y in solves['results']:
        if x['id'] == y['user_id']:
            result = result + 1
    if result >= max:
        winner = x
        max = result
print(winner['name'], ':', winner['email'], '-', max)
"""
#===========================================================================

#===========3 ЧЕЛОВЕКА С НАИБОЛЬШИМ КОЛИЧЕСТВОМ РЕШЕННЫХ ЗАДАЧ==============
"""
with open('E:/course work/CTF MF.2022-02-10/db/users.json') as file:
    f = file.read()
    users = json.loads(f)

with open('E:/course work/CTF MF.2022-02-10/db/solves.json') as file:
    f = file.read()
    solves = json.loads(f)

res = dict()
for x in users['results']:
    result = 0
    for y in solves['results']:
        if x['id'] == y['user_id']:
            result = result + 1
    res[x['name']] = result

sorted_tuple = sorted(res.items(), key=lambda x: x[1])
sorted_dict = dict(sorted_tuple)
for key in sorted_dict:
    print(f"{key} - {sorted_dict[key]}")

length = len(sorted_dict)
print('Всего студентов в системе:' , length)

max1 = sorted(sorted_dict.values())[-1]
max2 = sorted(sorted_dict.values())[-2]
max3 = sorted(sorted_dict.values())[-3]

for key, value in sorted_dict.items():
    if value == max1:
        for user in users['results']:
            if user['name'] == key:
                win_email = user['email']
        print(f"1 место по количеству решенных задач: {key} =  {value}, почта: {win_email}")
    if value == max2:
        for user in users['results']:
            if user['name'] == key:
                win_email = user['email']
        print(f"2 место по количеству решенных задач: {key} =  {value}, почта: {win_email}")
    if value == max3:
        for user in users['results']:
            if user['name'] == key:
                win_email = user['email']
        print(f"3 место по количеству решенных задач: {key} =  {value}, почта: {win_email}")
"""
#======================================================================

#=================ТЕ КТО ВОШЕЛ ПОД ОДНИМ IP В ОДИН ДЕНЬ=================
"""
with open('E:/course work/CTF MF.2022-02-10/db/tracking.json') as file:
    f = file.read()
    tracking = json.loads(f)

with open('E:/course work/CTF MF.2022-02-10/db/users.json') as file:
    f = file.read()
    users = json.loads(f)

for text in tracking['results']:
    for t in tracking['results']:
        text_date = datetime.fromisoformat((text['date'])).strftime('%Y-%m-%d')
        t_date = datetime.fromisoformat((t['date'])).strftime('%Y-%m-%d')
        if text['ip'] == t['ip'] and text['user_id'] != t['user_id'] and text_date == t_date and text['user_id'] < t['user_id']:
            for y in users['results']:
                if text['user_id'] == y['id']:
                    first = y['name']
                if t['user_id'] == y['id']:
                    second = y['name']

            print(f"{datetime.fromisoformat((text['date'])).strftime('%d %B %Y')} {first} (id: {text['user_id']}) и {second} (id: {t['user_id']}) вошли под одним IP: {text['ip']}")
"""
#===================================================================

#=========ВСЕ ОТВЕТЫ ПРАВИЛЬНЫЕ С ПЕРВОЙ ПОПЫТКИ====================
"""
with open('E:/course work/CTF MF.2022-02-10/db/users.json') as file:
    f = file.read()
    users = json.loads(f)

with open('E:/course work/CTF MF.2022-02-10/db/submissions.json') as file:
    f = file.read()
    submissions = json.loads(f)

    for x in users['results']:
        inccorect_answers = 0
        all_answers = 0
        for y in submissions['results']:
            if x['id'] == y['user_id']:
                all_answers += 1
                if y['type'] == 'incorrect':
                    inccorect_answers += 1

        if inccorect_answers == 0 and all_answers != 0:
            print(f"У {x['name']} нет неправильных ответов из {all_answers} решенных задач")
"""
#================================================================

#================КАКУЮ ЗАДАЧУ ЧАЩЕ РЕШАЮТ НЕВЕРНО=================
"""
with open('E:/course work/CTF MF.2022-02-10/db/challenges.json') as file:
    f = file.read()
    challenges = json.loads(f)

with open('E:/course work/CTF MF.2022-02-10/db/submissions.json') as file:
    f = file.read()
    submissions = json.loads(f)

max = 0
for x in challenges['results']:
    count = 0
    for y in submissions['results']:
        if x['id'] == y['challenge_id'] and y['type'] == 'incorrect':
            count += 1

    if(count > max):
        max = count
        winner = x

print (f"Задачу {winner['id']} решили неправильно {max} раз. \nЗадача \"{winner['name']}\": \n{winner['description']}")
"""
#======================================================================

#=================В КАКОЙ ДЕНЬ НЕДЕЛИ ЧАЩЕ РЕШАЮТ ЗАДАЧИ================
"""
def WeekDayRus (text):
    if text == "Monday":
        return "Понедельник"
    if text == "Tuesday":
        return "Вторник"
    if text == "Wednesday":
        return "Среда"
    if text == "Thursday":
        return "Четверг"
    if text == "Friday":
        return "Пятница"
    if text == "Saturday":
        return "Суббота"
    if text == "Sunday":
        return "Воскресенье"

with open('E:/course work/CTF MF.2022-02-10/db/submissions.json') as file:
    f = file.read()
    submissions = json.loads(f)

days = dict()
for data in submissions['results']:
    text_date = datetime.fromisoformat((data['date'])).strftime('%Y-%m-%d')
    dayOfWeek = datetime.strptime(text_date, '%Y-%m-%d').weekday()
    if dayOfWeek in days.keys():
        days[dayOfWeek] += 1
    else:
        days[dayOfWeek] = 1

max_count = max(days.values())
min_count = min(days.values())
for key, value in days.items():
    if max_count == value:
        dayRus = WeekDayRus(calendar.day_name[key])
        print(f"День недели, в который пользователи проявляют наибольшую активность: {dayRus}")

    if min_count == value:
        dayRus = WeekDayRus(calendar.day_name[key])
        print(f"День недели, в который пользователи проявляют наименьшую активность: {dayRus}")
"""
#================================================================

#===========В КАКОЕ ВРЕМЯ ДНЯ ЧАШЕ РЕШАЮТ=======================
"""
with open('E:/course work/CTF MF.2022-02-10/db/submissions.json') as file:
    f = file.read()
    submissions = json.loads(f)

times = dict()
for data in submissions['results']:
    text_time = datetime.fromisoformat((data['date'])).strftime('%H')
    time = int(text_time)

    if time in times.keys():
        times[time] += 1
    else:
        times[time] = 1

max = max(times.values())
for key, value in times.items():
    if max == value:
        print(f"Наибольшую активность пользователи проявляют в период времени с {key} до {key+1} часов")
"""
#=====================================================

#=========У ДВУХ ЮЗЕРОВ РЕШЕНЫ ОДИНАКОВЫЕ ЗАДАЧИ=========
"""
def printgroup(gr):
    if gr is not None:
        return gr
    else:
        return ''

with open('E:/course work/CTF MF.2022-02-10/db/solves.json') as file:
    f = file.read()
    solves = json.loads(f)

with open('E:/course work/CTF MF.2022-02-10/db/users.json') as file:
    f = file.read()
    users = json.loads(f)

for x in users['results']:
    for y in users['results']:
        listX = list()
        listY = list()
        if x['id'] < y['id']:
            for data in solves['results']:
                if x['id'] == data['user_id']:
                    listX.append(data['challenge_id'])
                if y['id'] == data['user_id']:
                    listY.append(data['challenge_id'])

        listX.sort()
        listY.sort()
        if len(listX) != 0 and len(listY) != 0:
            if listX == listY:
                print(f"У {x['name']} - {printgroup(x['affiliation'])} и {y['name']} - {printgroup(y['affiliation'])} решены одинаковые задачи (всего {len(listX)})")

"""
#=============================================================

#======У КОГО БЫСТРО РЕШАЮТСЯ ЗАДАЧИ============================

with open('E:/course work/CTF MF.2022-02-10/db/users.json') as file:
    f = file.read()
    users = json.loads(f)

with open('E:/course work/CTF MF.2022-02-10/db/submissions.json') as file:
    f = file.read()
    submissions = json.loads(f)

print("Пользователи, решившие задания за время, меньшее чем 2 минуты:")
for user in users['results']:
    listOftimes = list()
    for data in submissions['results']:
        if user['id'] == data['user_id'] and data['type'] == 'correct':
            text_time = datetime.fromisoformat((data['date'])).strftime('%y-%m-%d %H:%M:%S')
            time = datetime.strptime(text_time, '%y-%m-%d %H:%M:%S')
            listOftimes.append(time)

    count = 0
    oops = 1
    if len(listOftimes) != 0:
        while count <= len(listOftimes)-2:
            if listOftimes[count+1]-listOftimes[count] <= timedelta(minutes=2):
                oops += 1
            count += 1
        if oops != 1:
            print(f"Пользователь {user['name']} (id: {user['id']}) решил {oops} вопросов из {len(listOftimes)} решенных удивительно быстро")

#==============КАКОЙ ПРОЦЕНТ ПРАВИЛЬНЫЙ ОТ ОБЩЕГО ЧИСЛА РЕШЕННЫХ==================
"""
with open('E:/course work/CTF MF.2022-02-10/db/users.json') as file:
    f = file.read()
    users = json.loads(f)

with open('E:/course work/CTF MF.2022-02-10/db/submissions.json') as file:
    f = file.read()
    submissions = json.loads(f)

for user in users['results']:
    all_answers = 0
    correct_answers = 0
    for data in submissions['results']:
        if user['id'] == data['user_id']:
            all_answers += 1
            if data['type'] == "correct":
                correct_answers += 1
    if all_answers != 0:
        percent = round(correct_answers/all_answers * 100, 2)
        print(f"У {user['name']} (id: {user['id']}) {correct_answers} правильных ответов из {all_answers} попыток решения: {percent}%")
"""
#==============================================================

#=========ПРОЦЕНТ ПРАВИЛЬНЫХ ОТВЕТОВ В КАЖДОЙ КАТЕГОРИИ=========
"""
with open('E:/course work/CTF MF.2022-02-10/db/submissions.json') as file:
    f = file.read()
    submissions = json.loads(f)

with open('E:/course work/CTF MF.2022-02-10/db/challenges.json') as file:
    f = file.read()
    challenges = json.loads(f)

allanswers = dict()
correctanswers = dict()
for data in submissions['results']:
    for task in challenges['results']:
        if data['challenge_id'] == task['id']:
            if task['category'] in allanswers.keys():
                allanswers[task['category']] += 1
            else:
                allanswers[task['category']] = 1

            if data['type'] == "correct":
                if task['category'] in correctanswers.keys():
                    correctanswers[task['category']] += 1
                else:
                    correctanswers[task['category']] = 1

for key, value in allanswers.items():
    percent = round(correctanswers[key] / value * 100, 2)
    print(f"Процент решений задач в категории \"{key}\": {percent}%. Всего ответов: {value}, правильных: {correctanswers[key]}")
"""
#=========================================================

#======ГРАФИК КОЛ-ВА ОТВЕТОВ В ДНИ НЕДЕЛИ==============
"""
def WeekDayRus (text):
    if text == "Monday":
        return "Понедельник"
    if text == "Tuesday":
        return "Вторник"
    if text == "Wednesday":
        return "Среда"
    if text == "Thursday":
        return "Четверг"
    if text == "Friday":
        return "Пятница"
    if text == "Saturday":
        return "Суббота"
    if text == "Sunday":
        return "Воскресенье"

with open('E:/course work/CTF MF.2022-02-10/db/submissions.json') as file:
    f = file.read()
    submissions = json.loads(f)

days = dict()
for data in submissions['results']:
    text_date = datetime.fromisoformat((data['date'])).strftime('%Y-%m-%d')
    dayOfWeek = datetime.strptime(text_date, '%Y-%m-%d').weekday()
    dayRus = WeekDayRus(calendar.day_name[dayOfWeek])
    if dayRus in days.keys():
        days[dayRus] += 1
    else:
        days[dayRus] = 1

plot.subplots_adjust(bottom = 0.2)
plot.xticks(rotation=45)
plot.title("Количество ответов по дням недели")
plot.ylabel('Количество ответов')
plot.bar(days.keys(), days.values())
plot.savefig('E:/course work/Отчёт по дням недели.png')
plot.show()
"""
#===============КОЛ-ВО ОТВЕТОВ ПО ЧАСАМ=========================
"""
with open('E:/course work/CTF MF.2022-02-10/db/submissions.json') as file:
    f = file.read()
    submissions = json.loads(f)

times = dict()
for data in submissions['results']:
    text_time = datetime.fromisoformat((data['date'])).strftime('%H')
    time = int(text_time)

    if time in times.keys():
        times[time] += 1
    else:
        times[time] = 1

i = 0
while i < 24:
    if i not in times.keys():
        times[i] = 0
    i += 1

sorted_times = dict()
list_keys = list(times.keys())
list_keys.sort()
for i in list_keys:
    sorted_times[i] = times[i]

hours = []
values = []
for key, value in sorted_times.items():
    hour = f"{key}:00"
    hours.append(hour)
    values.append(value)

plot.figure(figsize=(8,6))
plot.xticks(rotation=45)
plot.title("Количество ответов по времени дня")
plot.ylabel('Количество ответов')
plot.bar(hours, values)
plot.savefig('E:/course work/Отчёт по времени дня.png')
plot.show()
"""
#======================================================

#=========ГРАФИК: КОЛ-ВО ОТВЕТОВ В КАЖДЫЙ МЕСЯЦ=========
"""
with open('E:/course work/CTF MF.2022-02-10/db/submissions.json') as file:
    f = file.read()
    submissions = json.loads(f)

months = dict()
for data in submissions['results']:
    text_month = datetime.fromisoformat((data['date'])).strftime('%Y-%m')
    if text_month in months.keys():
        months[text_month] += 1
    else:
        months[text_month] = 1

plot.plot(months.keys(), months.values(), color = 'b', linewidth = 2)
plot.title("Количество ответов по месяцам")
plot.ylabel('Количество ответов')
plot.minorticks_on()
plot.grid(which='major', color = 'k', linewidth = 1)
plot.grid(which='minor', color = 'k', linestyle = ':')
plot.savefig('E:/course work/Отчёт по месяцам (кол-во ответов).png')
plot.show()
"""
#===================================================

#======СКОЛЬКО ЗАДАЧ РЕШИЛА КАЖДАЯ ГРУППА=========
"""
with open('E:/course work/CTF MF.2022-02-10/db/users.json') as file:
    f = file.read()
    users = json.loads(f)

with open('E:/course work/CTF MF.2022-02-10/db/submissions.json') as file:
    f = file.read()
    submissions = json.loads(f)

groups = dict()
for x in users['results']:
    for y in submissions['results']:
        if x['id'] == y['user_id'] and y['type'] == 'correct':
            if x['affiliation'] in groups.keys():
                groups[x['affiliation']] += 1
            else:
                groups[x['affiliation']] = 1

groups["Не указана"] = groups.pop(None)
plot.title("Количество правильных ответов по группам")
plot.ylabel('Количество ответов')
plot.bar(groups.keys(), groups.values(), color = 'g')
plot.savefig('E:/course work/Отчёт по группам (кол-во правильных ответов).png')
plot.show()
"""
#=====================================================

#======В ПРОЦЕНТАХ СКОЛЬКО КАЖДАЯ ГРУППА РЕШИЛА=========
"""
with open('E:/course work/CTF MF.2022-02-10/db/users.json') as file:
    f = file.read()
    users = json.loads(f)

with open('E:/course work/CTF MF.2022-02-10/db/submissions.json') as file:
    f = file.read()
    submissions = json.loads(f)

groups = dict()
all_answers = 0
for x in users['results']:
    for y in submissions['results']:
        if x['id'] == y['user_id']:
            all_answers += 1
            if x['affiliation'] in groups.keys():
                groups[x['affiliation']] += 1
            else:
                groups[x['affiliation']] = 1

groups["Не указана"] = groups.pop(None)

for key, value in groups.items():
    groups[key] = round(value / all_answers * 100,2)

plot.figure(figsize=(7,5))
plot.pie(groups.values(), labels=groups.keys(), autopct='%.2f%%')
plot.axis('equal')
plot.title(f"Использование платформы по группам \n Всего попыток решения: {all_answers}")
plot.savefig('E:/course work/Использование платформы по группам.png')
plot.show()
"""
#===============================================================

#==========КОЛ-ВО ОТВЕТОВ И КОЛ-ВО ПРАВИЛЬНЫХ ПО КАТЕГОРИЯМ======
"""
with open('E:/course work/CTF MF.2022-02-10/db/submissions.json') as file:
    f = file.read()
    submissions = json.loads(f)

with open('E:/course work/CTF MF.2022-02-10/db/challenges.json') as file:
    f = file.read()
    challenges = json.loads(f)


answers = dict()
for data in submissions['results']:
    for task in challenges['results']:
        if data['challenge_id'] == task['id']:
            if task['category'] in answers.keys() and data['type'] == "correct":
                answers[task['category']]['all answers'] += 1
                answers[task['category']]['correct answers'] +=1
            elif task['category'] in answers.keys() and data['type'] != "correct":
                answers[task['category']]['all answers'] += 1
            elif task['category'] not in answers.keys() and data['type'] == "correct":
                answers[task['category']] = {'all answers': 1, 'correct answers': 1}
            else:
                answers[task['category']] = {'all answers': 1, 'correct answers': 0}

sorted_answers = dict()
list_keys = list(answers.keys())
list_keys.sort()
for i in list_keys:
    sorted_answers[i] = answers[i]

index = np.arange(len(sorted_answers))
df = pd.DataFrame(sorted_answers.values())
df.plot(kind='bar', figsize = (8,8.5))
plot.title('Количество всех и правильных ответов по категориям')
plot.subplots_adjust(bottom = 0.5, top = 0.9)
plot.xticks(rotation=90)
plot.xticks(index, sorted_answers.keys())
plot.savefig('E:/course work/Количество ответов по категориям.png')
plot.show()
"""
#===========ТАБЛИЦА ДЛЯ ГРУППЫ: КОЛ_ВО РЕШЕННЫХ ЗАДАЧ В КАТЕГОРИИ================
"""
def rows(key, value):
    str = [key]
    for i in value:
        str.append(value[i])
    return str

def fields(lis):
    str = ["Name"]
    for i in lis:
        str.append(i)
    return str

with open('E:/course work/CTF MF.2022-02-10/db/submissions.json') as file:
    f = file.read()
    submissions = json.loads(f)

with open('E:/course work/CTF MF.2022-02-10/db/users.json') as file:
    f = file.read()
    users = json.loads(f)

with open('E:/course work/CTF MF.2022-02-10/db/challenges.json') as file:
    f = file.read()
    challenges = json.loads(f)

group = input("Введите группу: ")
count = 0
for data in users['results']:
    if data['affiliation'] == group:
        count += 1
if count == 0:
    print("Такой группы нет в системе. Проверьте введенные данные!")
    quit()

answers = dict()
categories = list()

for sub in submissions['results']:
    for user in users['results']:
        if sub['type'] == "correct" and sub['user_id'] == user['id'] and user['affiliation'] == group:
            userName = user['name']
            for chall in challenges['results']:
                if sub['challenge_id'] == chall['id']:
                    if userName in answers.keys() and chall['category'] in answers[userName].keys():
                        answers[userName][chall['category']] +=1
                    elif userName in answers.keys() and chall['category'] not in answers[userName].keys():
                        answers[userName][chall['category']] = 1
                    elif userName not in answers.keys():
                        answers[userName] = {f"{chall['category']}": 1}

                    if chall['category'] not in categories:
                        categories.append(chall['category'])


sorted_answers = dict()
list_keys = categories
list_keys.sort()
for key, value in answers.items():
    for i in list_keys:
        if i in answers[key].keys():
            if key in sorted_answers.keys():
                sorted_answers[key][i] = value[i]
            else:
                sorted_answers[key] = {f"{i}": value[i]}
        else:
            sorted_answers[key][i] = 0

mytable = PrettyTable()
mytable.field_names = [x for x in fields(list_keys)]
for key, value in sorted_answers.items():
    mytable.add_row([x for x in rows(key, value)])
print(mytable)

with open(f'E:/course work/Отчёт для группы {group}.txt', 'w') as f:
    table = mytable.get_string()
    f.write(f"Группа: {group}\n")
    f.write(table)
    f.write('\n')
"""
#============================================================

#===============ОТЧЁТ ДЛЯ ГРУППЫ ПО СЕМЕСТРУ=================
"""
def rows(key, value):
    str = [key]
    for i in value:
        str.append(value[i])
    return str

def fields(lis):
    str = ["Name"]
    for i in lis:
        str.append(i)
    return str

with open('E:/course work/CTF MF.2022-02-10/db/submissions.json') as file:
    f = file.read()
    submissions = json.loads(f)

with open('E:/course work/CTF MF.2022-02-10/db/users.json') as file:
    f = file.read()
    users = json.loads(f)

with open('E:/course work/CTF MF.2022-02-10/db/challenges.json') as file:
    f = file.read()
    challenges = json.loads(f)

group = input("Введите группу: ")
count = 0
for data in users['results']:
    if data['affiliation'] == group:
        count += 1
if count == 0:
    print("Такой группы нет в системе. Проверьте введенные данные!")
    quit()

answers = dict()
categories = list()

for sub in submissions['results']:
    for user in users['results']:
        text_date = datetime.fromisoformat((sub['date'])).strftime('%Y-%m-%d')
        date = datetime.strptime(text_date, '%Y-%m-%d')
        if sub['type'] == "correct" and sub['user_id'] == user['id'] and user['affiliation'] == group:
            if date > datetime(2021, 9, 1) and date < datetime(2022, 1, 1):
                userName = user['name']
                for chall in challenges['results']:
                    if sub['challenge_id'] == chall['id']:
                        if userName in answers.keys() and chall['category'] in answers[userName].keys():
                            answers[userName][chall['category']] +=1
                        elif userName in answers.keys() and chall['category'] not in answers[userName].keys():
                            answers[userName][chall['category']] = 1
                        elif userName not in answers.keys():
                            answers[userName] = {f"{chall['category']}": 1}

                        if chall['category'] not in categories:
                            categories.append(chall['category'])


sorted_answers = dict()
list_keys = categories
list_keys.sort()
for key, value in answers.items():
    for i in list_keys:
        if i in answers[key].keys():
            if key in sorted_answers.keys():
                sorted_answers[key][i] = value[i]
            else:
                sorted_answers[key] = {f"{i}": value[i]}
        else:
            sorted_answers[key][i] = 0

mytable = PrettyTable()
mytable.field_names = [x for x in fields(list_keys)]
for key, value in sorted_answers.items():
    mytable.add_row([x for x in rows(key, value)])
print(mytable)

with open(f'E:/course work/Отчёт для группы {group} за семестр.txt', 'w') as f:
    table = mytable.get_string()
    f.write(f"Группа: {group}\n")
    f.write(f"Отчёт по количеству решенных задач в каждой категории за период 09.2021 - 01.2022\n")
    f.write(table)
    f.write('\n')
"""
#==========================================================================

#============ОТЧЕТ ДЛЯ ГРУППЫ: СКОЛЬКО ПРОЦЕНТОВ ЗАДАНИЙ В КАЖДОЙ КАТЕГОРИИ РЕШИЛ СТУДЕНТ===========
"""
def rows(key, value):
    str = [key]
    for i in value:
        str.append(value[i])
    return str

def fields(lis):
    str = ["Name"]
    for i in lis:
        str.append(i)
    return str

with open('E:/course work/CTF MF.2022-02-10/db/submissions.json') as file:
    f = file.read()
    submissions = json.loads(f)

with open('E:/course work/CTF MF.2022-02-10/db/users.json') as file:
    f = file.read()
    users = json.loads(f)

with open('E:/course work/CTF MF.2022-02-10/db/challenges.json') as file:
    f = file.read()
    challenges = json.loads(f)

group = input("Введите группу: ")
count = 0
for data in users['results']:
    if data['affiliation'] == group:
        count += 1
if count == 0:
    print("Такой группы нет в системе. Проверьте введенные данные!")
    quit()

cat = dict()
for challenge in challenges['results']:
    if challenge['category'] in cat.keys():
        cat[challenge['category']] +=1
    else:
        cat[challenge['category']] = 1

answers = dict()
categories = list()

for sub in submissions['results']:
    for user in users['results']:
        if sub['type'] == "correct" and sub['user_id'] == user['id'] and user['affiliation'] == group:
            userName = user['name']
            for chall in challenges['results']:
                if sub['challenge_id'] == chall['id']:
                    if userName in answers.keys() and chall['category'] in answers[userName].keys():
                        answers[userName][chall['category']] +=1
                    elif userName in answers.keys() and chall['category'] not in answers[userName].keys():
                        answers[userName][chall['category']] = 1
                    elif userName not in answers.keys():
                        answers[userName] = {f"{chall['category']}": 1}

                    if chall['category'] not in categories:
                        categories.append(chall['category'])


sorted_answers = dict()
list_keys = categories
list_keys.sort()
for key, value in answers.items():
    for i in list_keys:
        if i in answers[key].keys():
            if key in sorted_answers.keys():
                sorted_answers[key][i] = f"{round(value[i] / cat[i] * 100, 2)} %"
            else:
                sorted_answers[key] = {f"{i}": f"{round(value[i] / cat[i] * 100, 2)} %"}
        else:
            sorted_answers[key][i] = 0

mytable = PrettyTable()
mytable.field_names = [x for x in fields(list_keys)]
for key, value in sorted_answers.items():
    mytable.add_row([x for x in rows(key, value)])
print(mytable)

with open(f'E:/course work/Отчёт для группы {group} в процентах.txt', 'w') as f:
    table = mytable.get_string()
    f.write(f"Группа: {group}\n")
    f.write(table)
    f.write('\n')
"""
#====================================================================