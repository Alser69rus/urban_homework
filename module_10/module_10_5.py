import multiprocessing
import time
from pathlib import Path


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"Время выполнения {end-start:.3f} c")
        return res

    return wrapper


def read_info(filename):
    all_data = []
    with Path(filename).open("r", encoding="utf8") as f:
        while True:
            line = f.readline()
            if not line:
                break
            all_data.append(line)
    print(f"В файле '{filename}' всего {len(all_data)} строк.")


def up_count():
    for _ in range(100500):
        x = 1


@timeit
def line_call(filenames):
    print("Линейный вызов")
    for file in filenames:
        read_info(file)


@timeit
def pool_call(filenames):
    print("Параллельный вызов через пул процессов")
    cpu = multiprocessing.cpu_count()
    print(f"Число процессов: {cpu}")
    with multiprocessing.Pool(cpu) as pool:
        pool.map(read_info, filenames)


if __name__ == "__main__":
    filenames = [Path("./files") / Path(f"file {number}.txt") for number in range(1, 5)]

    line_call(filenames)
    print()

    pool_call(filenames)
    print()
