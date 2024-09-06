import os.path
f = input("Enter a filename: ")
if not os.path.isfile(f):
    quit("file not found")
with open(f, "r") as file:
    file_text = file.read()

words_by_initial = {}
for word in file_text.split():
    word = word.strip(",. !?")
    initial = word[0]
    if initial in words_by_initial:
        words_by_initial[initial].add(word)
    else:
        words_by_initial[initial] = set()
        words_by_initial[initial].add(word)

for l in sorted(words_by_initial):
    print(l)
    words = words_by_initial[l]
    for word in words:
        print("  " + word)