from pathlib import Path


class WordsFinder:
    def __init__(self, *files):
        self.file_names = files

    def get_all_words(self):
        return {
            file_name: self.get_words_from_file(file_name)
            for file_name in self.file_names
        }

    def get_words_from_file(self, file_name: str) -> list[str]:
        file = Path(file_name)
        if not file.exists():
            return []
        with open(file_name, "r", encoding="utf-8") as file:
            words = self.replace_punctuation(file.read()).lower().split()
        return [word for word in words if word]

    def replace_punctuation(self, string: str) -> str:
        punctuation = [",", ".", "=", "!", "?", ";", ":", " - "]
        return "".join([" " if ch in punctuation else ch for ch in string])

    def find(self, word: str) -> dict[str, int]:
        all_words = self.get_all_words().items()
        return {
            file_name: self.index_of_word(word, words) for file_name, words in all_words
        }

    def index_of_word(self, word: str, words: list[str]) -> int:
        word = word.lower()
        if word in words:
            return words.index(word) + 1
        else:
            return 0

    def count(self, word) -> dict[str, int]:
        all_words = self.get_all_words().items()
        return {file_name: words.count(word.lower()) for file_name, words in all_words}


if __name__ == "__main__":
    finder1 = WordsFinder(r"text\test_file.txt")
    print(finder1.get_all_words())  # Все слова
    print(finder1.find("TEXT"))  # 3 слово по счёту
    print(finder1.count("teXT"))  # 4 слова в тексте всего
    print()

    finder2 = WordsFinder(r"text\Mother Goose - Monday’s Child.txt")
    print(finder2.get_all_words())  # Все слова
    print(finder2.find("Child"))  # 2 слово по счёту
    print(finder2.count("Child"))  # 8 слова в тексте всего
    print()

    finder3 = WordsFinder(r"text\Rudyard Kipling - If.txt")
    print(finder3.get_all_words())  # Все слова
    print(finder3.find("if"))  # 1 слово по счёту
    print(finder3.count("if"))  # 14 слов в тексте всего
    print()

    finder4 = WordsFinder(r"text\Walt Whitman - O Captain! My Captain!.txt")
    print(finder4.get_all_words())  # Все слова
    print(finder4.find("captain"))  # 2 слово по счёту
    print(finder4.count("captain"))  # 10 слов в тексте всего
    print()

    finder5 = WordsFinder(
        r"text\Walt Whitman - O Captain! My Captain!.txt",
        r"text\Rudyard Kipling - If.txt",
        r"text\Mother Goose - Monday’s Child.txt",
    )
    print(finder5.get_all_words())  # Все слова
    print(finder5.find("the"))  # 14\109\41 слово по счёту
    print(finder5.count("the"))  # 18\7\2 слов в тексте всего
    print()
