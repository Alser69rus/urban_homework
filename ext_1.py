# Дано
grades = [
    [5, 3, 3, 5, 4],
    [2, 2, 2, 3],
    [4, 5, 5, 2],
    [4, 4, 3],
    [5, 5, 5, 4, 5],
]  # Список оценок учеников отсортированных по алфавиту
students = {
    "Johnny",
    "Bilbo",
    "Steve",
    "Khendrik",
    "Aaron",
}  # Множество с фамилиями учеников


def average(gr: list) -> float:
    """Средний бал для списка оценок"""
    return sum(gr) / len(gr)


sorted_student_list = sorted(list(students))
result = {key: average(grade) for key, grade in zip(sorted_student_list, grades)}

print("Дано:")
print("Список студентов:", sorted_student_list)
print("Отсортированный список оценок:", grades)
print("Ответ:")
print("Средний балл студентов:", result)
