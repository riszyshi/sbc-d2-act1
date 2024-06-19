word = "summer bootcamp"
print(word.title())
print(f"{word[0].upper()}{word[1:14]}{word[-1].upper()}")

s = "L"
print(f"{s}{word[8:11]}")

print(f"{word[-3].upper()}{word[5].upper()}")

new = word.replace(" ", "l")
print (new.isalpha())