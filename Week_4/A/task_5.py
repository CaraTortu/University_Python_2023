def countVowels(s: str) -> int:
    return sum([1 for i in s if i in "aeiou"])

print(countVowels("soup"))
