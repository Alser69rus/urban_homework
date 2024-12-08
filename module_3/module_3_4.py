def single_root_words(root_word: str, *other_words) -> list[str]:
    root = root_word.lower()
    list_of_words = [s.lower() for s in other_words]
    return [
        s
        for i, s in enumerate(other_words)
        if root in list_of_words[i] or list_of_words[i] in root
    ]


result1 = single_root_words("rich", "richiest", "orichalcum", "cheers", "richies")
result2 = single_root_words("Disablement", "Able", "Mable", "Disable", "Bagel")
print(result1)
print(result2)
