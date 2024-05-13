from os.path import exists


alphabet_en = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_ru = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
numbers = "0123456789"


def caesar(alphabet, letter, caesar_key):
    index = alphabet.find(letter) + caesar_key

    if index > len(alphabet) - 1:
        index = index % len(alphabet)

    return alphabet[index]


def get_alphabet(letter):
    if letter in alphabet_en:
        return alphabet_en

    if letter in alphabet_ru:
        return alphabet_ru

    if letter in alphabet_en.lower():
        return alphabet_en.lower()

    if letter in alphabet_ru.lower():
        return alphabet_ru.lower()

    if letter in numbers:
        return numbers

    return None


def main():
    if not exists("text.txt"):
        print("File not Found!")
        exit()

    cipher_file = open("cipher_text.txt", "w+")
    clean_file = open("text.txt", "r")
    text_list = clean_file.readlines()
    caesar_key = 1

    for line in text_list:
        caesar_line = ""

        for letter in line:
            alphabet = get_alphabet(letter)

            if alphabet != None:
                caesar_line += caesar(alphabet, letter, caesar_key)
            else:
                caesar_line += letter

        caesar_key += 1

        cipher_file.write(caesar_line)

    print("Before: ")
    clean_file.seek(0)
    print(clean_file.readlines())

    print("After: ")
    cipher_file.seek(0)
    print(cipher_file.readlines())

    cipher_file.close()
    clean_file.close()

    print("Everything is Done!")


if __name__ == "__main__":
    main()
