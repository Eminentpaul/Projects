import re

# ops = "52CD+"
# d = list(ops)
#
# lists = []
#
# for l in d:
#     if l != 'C' and l != 'D' and l != '+':
#         lists.append(l)
#     elif l == 'C':
#         lists.pop()
#     elif l == 'D':
#         c = int(d[0]) * int(d[1])
#         lists.append(c)
#     elif l == '+':
#         e = int(lists[0]) + int(lists[1])
#         lists.append(e)
# total = 0
# for q in lists:
#     total += int(q)
#
# print(total)
#
# print(lists)

# z = [1,3, 5]
# c = [3, 5 ,2,3 ]
# print(z==c)
# print(c)
#
# newlist = c.copy()
# print(newlist)
#
# d = re.findall('welcome to Turing', 'welcome', 1)
# print(d)

# role = "Admin"
# im
# value = 121 ** 0.5
# if value % 1 == 0:
#     b = (value + 1)
#     result = b * b
#     print(value., " --> ", result)
# else:
#     print(-1)
# # print(1281 ** 0.5)p
# print(value)



# sentence = "This is another paulinus test"
#
#
# def get_sentence(s):
#     global l
#     don = s.split()
#     e = []
#     for l in don:
#         if len(l) >= 5:
#             c = list(l)
#             c.reverse()
#             v = "".join(x for x in c)
#             b = sentence.replace(l, v)
#
#             e.append(v)
#             # if len()
#             print(e)
#     # print(l)
#     print(b)
#
#
# # for b in e:
# #     if len(l) >= 5:
# #         print(sentence.replace(l, b))
#
#
#
#
# get_sentence(sentence)

# d = 51 + 12
# bin = []
# while d != 0:
#     c = d%2
#     bin.append(c)
#     f = d//2
#     d = f
# bin.reverse()
# print("".join(str(x) for x in bin))

# b = [5, 3, 2, 8, 1, 4]
# bin = []
# bins = []
# for l in b:
#     if l % 2 != 0:
#         c = l
#         bin.append(c)
#     if l % 2 == 0:
#         bins.append(l)
#
#     # print(b)
# bin.reverse()
# lg = bin + bins
# print(lg)
# num = 9
# if num == 1:
#     print('even')
# elif num == 2:
#     print('Prime')
# elif ((num // num == 1) and (num // 1 == num) and (num % 2 != 0)):
#     print("prime")
# elif num // 3 != 1:
#     print('even')
# elif num // 4 != 1:
#     print('even')
# elif num // 5 != 1:
#     print('even')
# elif num // 6 != 1:
#     print('even')
# elif num // 7 != 1:
#     print('even')
# elif num // 8 != 1:
#     print('even')
# elif num // 9 != 1:
#     print('even')
#
# else:
#     print('even')


# i = 9
# while i <= 19:
#     i += 1
#     print(i)
#     # i =+1

# i = 0
#
# while i in range(1, 10):
#     print("Paul ", i)
#



# num = [1, 2, 3, 2]
# b = num[-2] + 1
# c = num.pop()
# result = num.append(b)
# # print(num)
#
# nm = input("> ")
# d = list(nm)
# print(d)
# b = int(d[-2]) + 1
# d.pop()
# d.append(b)
# print()

# import string
# strings = "How Can Mirrors Be Real If Our Eyes Aren'T Real"
# should_equal = "How Can Mirrors Be Real If Our Eyes Aren't Real"
# print(string.capwords(strings))

# lists = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
# def find_it(seq):
#     for l in seq:
#         pass
#     if seq.count(l) % 2 != 0:
#         print(l)
#     else:
#         print(False)
#
# find_it(lists)

# d = "The sunset sets at twelve o' clock.".lower()
# b = [ord(c) for c in d]
# j = []
# for x in b:
#     if x >= 97:
#         l = int(x) - 96
#         j.append(l)
#     else:
#         l = int(x) - 13
#         j.append(l)
# print(j)
#
# print(b)


# l = "aeiou"
# b = "abracadabra"
# num_vowel = 0
# for x in b:
#     if x in l:
#         num_vowel += 1
#
# print(num_vowel)
# value = 25
# number = 25
# while number <= 100:
#     if value % 7 == 0:
#         print(value)
#     value += 1
#     number += 1
#
# class Point:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# point = Point()
# point.age

# s = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
# b = "abcdefghijklm"
# error = 0
# for i in s:
#     if i not in b:
#         error += 1
# totalError = f'{error}/{len(s)}'
# print(totalError)
#
# from re import sub
# print("{}/{}".format(len(sub("[a-m]",'',s)),len(s)))



# def tower_builder(n_floors):
#     tower = []
#     i = 1
#     while i <= n_floors:
#         tower.append( "*" * i)
#         i += 1
#     return tower
#
# p = tower_builder(5)
# print(p)

def open_or_senior(data):
    done = []
    for x in data:
        if x[0] >= 55 and x[1] > 7:
            done.append("Senior")
        else:
            done.append("Open")
    return print(done)


open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)])























