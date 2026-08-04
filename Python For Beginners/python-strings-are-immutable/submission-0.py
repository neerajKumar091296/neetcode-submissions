def remove_fourth_character(word: str) -> str:
    word_1 = word[:3]
    word_2 = word[4:]
    return word_1 + word_2


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
