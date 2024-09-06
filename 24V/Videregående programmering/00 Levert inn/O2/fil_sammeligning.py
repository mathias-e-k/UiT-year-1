FILE_A = "test.txt"
FILE_B = "test2.txt"

file_a_words = set(open(FILE_A).read().split())
file_b_words = set(open(FILE_B).read().split())

print("Num of unique words:", len(file_a_words | file_b_words))
print("All unique words:", file_a_words | file_b_words)
print("Unique words that are found in both files:", file_a_words & file_b_words)
print("Words that are found in file A but not in file B:", file_a_words - file_b_words)
print("Words that are found in file B but not in file A:", file_b_words - file_a_words)
print("Words that are found file A or file B, but not both:", file_b_words ^ file_a_words)
