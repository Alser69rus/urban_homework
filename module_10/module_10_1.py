import threading
import time


def write_words(word_count: int, file_name: str):
    with open(file_name, "w", encoding="utf-8") as f:
        for i in range(word_count):
            f.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


if __name__ == "__main__":
    start = time.time()
    write_words(10, "example1.txt")
    write_words(30, "example2.txt")
    write_words(200, "example3.txt")
    write_words(100, "example4.txt")
    end = time.time()
    print(f"Работа потоков {end-start}")

    start = time.time()
    threads = [
        threading.Thread(target=write_words, args=(10, "example5.txt")),
        threading.Thread(target=write_words, args=(30, "example6.txt")),
        threading.Thread(target=write_words, args=(200, "example7.txt")),
        threading.Thread(target=write_words, args=(100, "example8.txt")),
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    end = time.time()
    print(f"Работа потоков {end - start}")