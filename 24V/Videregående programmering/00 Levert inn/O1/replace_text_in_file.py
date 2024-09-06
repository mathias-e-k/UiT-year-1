import os.path
f = input("Enter a filename: ")
if not os.path.isfile(f):
    quit("file not found")
old_string = input("Enter the old string to be replaced: ")
new_string = input("Enter the new string to replace the old string: ")
file_text = open(f, "r").read()
occurences_replaced = file_text.count(old_string)
file_text = file_text.replace(old_string, new_string)

file = open(f, "w")
file.write(file_text)
file.close()

print(f"Successfully replaced {occurences_replaced} occurrence{'' if occurences_replaced==1 else 's'} of '{old_string}' with '{new_string}'")
