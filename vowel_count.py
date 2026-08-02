
def count_vowels(s):
    if len(s) == 0:
        return 0

    if s[0].lower() in "aeiou":
        return 1 + count_vowels(s[1:])
    else:
        return count_vowels(s[1:])

string = input("Enter a string: ")

print("Number of vowels:", count_vowels(string))
