calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(s: str) -> tuple[int, str, str]:
    count_calls()
    length = len(s)
    lower = s.lower()
    upper = s.upper()
    return length, upper, lower


def is_contains(string: str, list_to_search: list[str]) -> bool:
    count_calls()
    lst = [s.lower() for s in list_to_search]
    s = string.lower()
    return s in lst


print(string_info("Capybara"))
print(string_info("Armageddon"))
print(is_contains("Urban", ["ban", "BaNaN", "urBAN"]))  # Urban ~ urBAN
print(is_contains("cycle", ["recycling", "cyclic"]))  # No matches
print(calls)
