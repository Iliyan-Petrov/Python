str="I love chocolate very much."
words = str.split()

with open("example.txt", "w") as f:
 for word in words:
  f.write(word)
  f.write("\n")