# Name: Huzaifa Shoeb, ID: 1925670
import re

months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}

input_file = open('inputDates.txt', 'r')
output_file = open('parsedDates.txt', 'w')

# yourdate = input() [Was using this line for part a of Homework
# Changed [yourdate, -1] to [input_file, -1] for part b.

for data in [input_file, -1]:
    if data == -1:
        break
    elif re.match(r'(\w+) (\d{1,2}), (\d{4})', data) is None:
        continue
    output = data.split(" ")
    output[0] = str(months[output[0]])
    output[1] = output[1].replace(",", "")
    result = "/".join(output)
    print(result)
    output_file.write(result)
    output_file.write('\n')
output_file.close()
input_file.close()
