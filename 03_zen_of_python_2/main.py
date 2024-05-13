text = open("zen.txt").read().lower()
letters = [c for c in text if c in "abcdefghijklmnopqrstuvwxyz"]
print(len(letters), len(text.split()), len(text.split("\n")), min(letters, key=letters.count), sep="\n")

