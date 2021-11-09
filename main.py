import csv
import re


def get_right_names(phonebook):
    pattern = r'^(\w+)[,\s](\w+)[,\s](\w+|,)'
    subst = r'\1,\2,\3'
    book = []
    for item in phonebook:
        book.append(re.sub(pattern, subst, item))
    return book

def get_right_phones(phonebook):
    pattern = r'[+78][\s(]{0,2}(\d\d\d)[)\s-]{0,2}(\d\d\d)[\s-]{0,2}(\d\d)[-\s]{0,2}(\d\d)[\s,]'
    subst = r'+7(\1)\2-\3-\4,'
    book = []
    for item in phonebook:
        book.append(re.sub(pattern, subst, item))
    return book


def main():


    with open('phonebook_raw.csv', newline='', encoding='UTF-8') as csvfile:
        book = []
        for line in csvfile:
            book.append((line).strip())

    for i in book:
        print(i)
    book_with_right_names = get_right_names(book)

    print('-'*50)

    for i in book_with_right_names:
        print(i)

    book_with_right_phones = get_right_phones(book_with_right_names)

    print('-' * 50)

    for i in book_with_right_phones:
        print(i)


if __name__ == '__main__':

    main()