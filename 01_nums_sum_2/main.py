numbers_sum = 0
file_from = open("numbers.txt", "r", encoding="utf8")
for line in file_from:
    clear_line = line.rstrip()
    if clear_line:
        numbers_sum += int(clear_line)
file_from.close()

file_in = open("answer.txt", "w", encoding="utf8")
file_in.write(str(numbers_sum))
file_in.close()
