word = "summer bootcamp"
#1
print(word.title())
#2
print(f"{word[0].upper()}{word[1:14]}{word[-1].upper()}")
#3
s = "L"
print(f"{s}{word[8:11]}")
#4
print(f"{word[11:14]}{word[4].upper()}")
#5
print(f"{word[-3].upper()}{word[5].upper()}")
#6
new = word.replace(" ", "l")
print (new.isalpha())