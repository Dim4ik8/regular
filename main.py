import csv
import re
import os


def get_right_phones(phonebook):
    pattern = r'(\+7|8)[\s(]{0,2}(\d\d\d)[)\s-]{0,2}(\d\d\d)[\s-]{0,2}(\d\d)[-\s]{0,2}(\d\d)'
    subst = r'+7(\2)\3-\4-\5'
    pattern_1 = r'[\s(]{0,2}(доб.)\s(\d+)[),]{0,2}'
    subst_1 = r' доб.\2,'

    book = []
    ext_book = []
    for item in phonebook:
        book.append(re.sub(pattern, subst, item))
    for elem in book:
        ext_book.append(re.sub(pattern_1, subst_1, elem))

    return ext_book


def read_write(phonebook):
    phone_book = []
    new_book = []
    names = []
    with open(phonebook, newline='', encoding='UTF-8') as csvfile:
        phone_book_reader = csv.DictReader(csvfile)
        fieldnames = phone_book_reader.fieldnames
        for row in phone_book_reader:
            phone_book.append(row)

    for i in phone_book:
        ws = ' '
        if i['lastname'].count(ws) == 1:
            q = i['lastname'].split(' ')
            i['lastname'] = q[0]
            i['firstname'] = q[1]

        elif i['lastname'].count(ws) == 2:
            q = i['lastname'].split(' ')
            i['lastname'] = q[0]
            i['firstname'] = q[1]
            i['surname'] = q[2]

        elif i['firstname'].count(ws) == 1:
            q = i['firstname'].split(' ')
            i['firstname'] = q[0]
            i['surname'] = q[1]

    for row in phone_book:
        last_first_dict = (row['lastname'], row['firstname'])
        names.append(last_first_dict)

    unique_names = list(set(names))

    for last, first in unique_names:

        new_row = {}
        count = names.count((last, first))
        if count > 1:
            for row in phone_book:

                if row['lastname'] == last and row['firstname'] == first:
                    for fieldname in phone_book_reader.fieldnames:
                        if row[fieldname] != '':
                            new_row[fieldname] = row[fieldname]

            new_book.append(new_row)

        else:
            for row in phone_book:
                if row['lastname'] == last and row['firstname'] == first:
                    new_book.append(row)

    with open('new_book.csv', 'w', newline='', encoding='UTF-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()
        writer.writerows(new_book)


def main():
    with open('phonebook_raw.csv', newline='', encoding='UTF-8') as csvfile:
        book = []
        for line in csvfile:
            book.append((line).strip())

    book_with_right_phones = get_right_phones(book)

    with open("right_phone_book.csv", "w", encoding='UTF-8') as f:
        f.writelines([line + '\n' for line in book_with_right_phones])

    read_write('right_phone_book.csv')

    os.remove(('right_phone_book.csv'))


if __name__ == '__main__':
    main()
