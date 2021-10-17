from pprint import pprint
import re

import csv

with open("phonebook_raw.csv", encoding='UTF-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)



new_list = []
# создаем новый список, в который будем записывать изменения исходного файла

for stri in contacts_list:
  pattern = r"(\w+)[\s,*](\w+)[\s,*](\w+)"

  text = str(stri)
  subst = r"\1,\2,\3"

  result = re.sub(pattern, subst, text)
  new_list.append((result))
# создаем регулярку для выравнивания ФИО


for string in contacts_list:
  pattern = r"(\+7\s*|8)(\s*|\()(\d\d\d)(\)|\s*|-)\s*(\d\d\d)(\s*|-)(\d\d)(\s*|-)(\d\d)(,|\s|)"

  text = str(string)
  subst = r"+7(\3)\5-\7-\9"

  result = re.sub(pattern, subst, text)
  new_list.append((result))
# создаем регулярку для выравнивания телефонов


for string in contacts_list:
  pattern = r"((\s|\s*\()(доб. )(\d+)(\s*|\))"

  text = str(string)
  subst = r" доб.\3"

  result = re.sub(pattern, subst, text)
  new_list.append((result))
# создаем регулярку для прибавления добавочного номера


with open("phonebook_new.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')

  datawriter.writerows(new_list)

#записываем получившиеся данные в новый файл CSV

