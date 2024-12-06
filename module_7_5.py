import os
import time
from pathlib import Path

directory = "."
ignore_list = [r".\.git", r".\.venv", r".\.idea"]


def need_ignore(root: str) -> bool:
    return any([root.startswith(pattern) for pattern in ignore_list])


# os
for root, dirs, files in os.walk(directory):
    if need_ignore(root):
        continue
    for file in files:
        parent_dir = root
        file_path = os.path.join(root, file)
        stat = os.stat(file_path)
        file_size = stat.st_size
        file_time = stat.st_atime
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time))
        print(
            f"Обнаружен файл: {file}, Путь: {file_path}, Размер: {file_size} байт,"
            f" Время изменения: {formatted_time}, Родительская директория: {parent_dir}"
        )


# pathlib
def ignore_dir(root) -> bool:
    return any([root.is_relative_to(pattern) for pattern in ignore_list])


files = [
    (root, file)
    for root, dirs, files in Path(directory).walk()
    for file in files
    if not ignore_dir(root)
]

files_info = [
    (
        f"Обнаружен файл: {file}, Путь: {root/file}, Размер: {(root/file).stat().st_size} байт,"
        f" Время изменения: "
        f"{time.strftime("%d.%m.%Y %H:%M", time.localtime((root/file).stat().st_atime))}"
        f", Родительская директория: {root}"
    )
    for root, file in files
]
for info in files_info:
    print(info)
