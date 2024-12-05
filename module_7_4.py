team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
team1_name = "Мастера кода"
team2_name = "Волшебники Данных"

if score_1 > score_2:
    result = f"Победа команды {team1_name}"
elif score_1 == score_2 and team1_time > team2_time:
    result = f"Победа команды {team1_name}"
elif score_1 < score_2:
    result = f"Победа команды {team2_name}"
elif score_1 == score_2 and team1_time < team2_time:
    result = f"Победа команды {team2_name}"
else:
    result = "Ничья!"

tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total

# 'Использование %'
print("В команде %s участников: %d " % (team1_name, team1_num))
print("Итого сегодня в командах участников: %d и %d" % (team1_num, team2_num))

# Использование format():
print("Команда {} решила задач: {}".format(team2_name, score_2))
print(
    "{team2_name} решили задачи за {team2_time} с".format(
        team2_time=team2_time, team2_name=team2_name
    )
)

# Использование f-строк:
print(f"Команды решили {score_1} и {score_2} задач.")
print(f"Результат битвы: {result}!")
print(
    f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!."
)
