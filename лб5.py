import re

# задание 1

with open('task1-ru.txt', 'r', encoding='utf-8') as file:
    text = file.read()

words_6_letters = re.findall(r'\b\w{6}\b', text)
words_8_letters = re.findall(r'\b\w{8}\b', text)
numbers = re.findall(r'\b\d+(?:[.,]\d+)?\b', text)

print(numbers, words_6_letters, words_8_letters)

# задание 2

with open('task2.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

content_values = re.findall(r'\bcontent="([^"]+)"', html_content)

print(content_values)

# задание 3

import csv

with open('task3.txt', 'r', encoding='utf-8') as file:
    task3_content = file.read()

ids = re.findall(r'\b\d+\b', task3_content)
emails = re.findall(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b', task3_content)
dates = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', task3_content)
websites = re.findall(r'\bhttps?://[^\s]+\b', task3_content)
last_names = re.findall(r'\b[A-Z][a-z]+\b', task3_content)

data_table = list(zip(ids, last_names, emails, dates, websites))

output_csv_path = 'task3_normalized.csv'
with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["ID", "Last Name", "Email", "Registration Date", "Website"])
    csv_writer.writerows(data_table)


