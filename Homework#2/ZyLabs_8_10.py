# Name: Huzaifa Shoeb, ID: 1925670

word = str(input())
joint_word = word.replace(" ", "")
new = joint_word[::-1]

if joint_word == new:
    print('{} is a palindrome'.format(word))
else:
    print('{} is not a palindrome'.format(word))
