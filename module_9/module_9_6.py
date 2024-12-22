def all_variants(text: str) -> str:
    for length in range(1, len(text) + 1):
        gen = batch(text, length)
        for variants in gen:
            yield variants


def batch(text: str, length: int):
    start = 0
    while start + length <= len(text):
        value = text[start : start + length]
        yield value
        start += 1


if __name__ == "__main__":
    a = all_variants("abc")
    for i in a:
        print(i)
