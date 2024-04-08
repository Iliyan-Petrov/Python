print("Enter a word")
word = input()
lowerWord = word.lower()

vowels = ["a", "e", "i", "o", "u"]

x=0

for i in range(len(lowerWord)):
    if lowerWord[i] in vowels:
        x += vowels.count(lowerWord[i])

print(x)




