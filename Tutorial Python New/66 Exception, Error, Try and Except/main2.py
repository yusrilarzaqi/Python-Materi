# Membuat exception

# from numbers import Number

# def sum(a, b):
#     if not isinstance(a , Number) or not isinstance(b, Number):
#         raise "input harus angka"
#     return a + b


# print(sum(10, 20))

NUMBER = 0

# try:
#     result = 10/0
# except Exception as e:
#     print(e)

try:
    result = 10/0
except ZeroDivisionError as e:
    print(e)

