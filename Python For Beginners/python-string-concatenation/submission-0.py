def concatenate(s1: str, s2: str) -> str:
    combine = s1 + s2
    len_c = len(combine)
    if len_c <= 10:
        return combine
    else:
        return "Too long!"
    pass




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
