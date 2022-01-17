# pos = -1
#
# def search(list, n):
#     l = 0
#     u = len(list)-1
#
#     while l <= u:
#         mid = (l+u) // 2
#
#         if list[mid] == n:
#             globals()['pos'] = mid
#             return True
#         else:
#             if list[mid] < n:
#                 l = mid
#             else:
#                 u = mid
#
#
# list = [4, 7, 8, 12, 45, 99, 102, 702, 10987, 56666]
# n = 10987
#
# if search(list, n):
#     print('Found at', pos + 1)
# else:
#     print('Not Found')


pos = -1

def search(list, n):
    l = 0
    u = len(list) -1

    while l <= u:
        mid = (l+u) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid
            else:
                u = mid

list = [4, 5, 23, 443, 12]
n = 443

if search(list, n):
    print('Found at', pos + 1)
else:
    print("Not found")

