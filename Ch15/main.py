# def division(x, y):
#     try:
#         ans = x / y
#     except ZeroDivisionError:
#         return 'Can''t be devided by zero !'
#     else:
#         return ans
#
# print(division(9,0))
# print(division(9,1))

# def wordsNum(f):
#     try:
#         with open(f) as file:
#             data = file.read()
#     except FileNotFoundError:
#         return f'{f} was not found !'
#     else:
#         print(type(data))
#         wlist = data.split()
#         return len(wlist)
#
# print(wordsNum('data1.txt'))
# print(wordsNum('data2.txt'))
# print(wordsNum('data3.txt'))

import logging

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s : %(message)s')
# logging.debug('logging message, DEBUG')
# logging.info('logging message, INFO')
# logging.warning('logging message, WARNING')
# logging.error('logging message, ERROR')
# logging.critical('logging message, CRITICAL')

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s : %(message)s')
# logging.debug('開始')
# for i in range(5):
#     logging.debug(f'目前索引: {i}')
# logging.debug('結束')

# logging.basicConfig(filename='system log.txt',level=logging.DEBUG, format='%(asctime)s - %(levelname)s : %(message)s')
# logging.debug('程式開始')
# def factorial(n):
#     logging.debug(f'Factorial {n} 計算開始')
#     ans = 1
#     for i in range(1, n + 1):
#         ans *= i
#         logging.debug('i = ' + str(i) + ', ans: ' + str(ans))
#     logging.debug('程式結束')
#     return ans
#
# num = 5
# print(f'Factorial({num}) = {factorial(num)}')
#
# logging.disable(logging.CRITICAL)

# def fac(n):
#     if n == 1:
#         return n
#     else:
#         return (n*fac(n-1))
# print(fac(5))

