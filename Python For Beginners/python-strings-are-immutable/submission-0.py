def remove_fourth_character(word: str) -> str:
    main_word = word[:3] + word[4:]
    return main_word
    pass


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
