def word_count_startswith_c(l: str, c: str) -> int:
    return sum([1 for i in l.split(" ") if i.startswith(c)])

print(word_count_startswith_c("this is a weird sencente tic tac toe", "t"))

