"""
每隔1秒输出一次“hello, world”，持续1小时

Author: 骆昊
Version: 1.1
"""
# import time

# # 方法一
# for i in range(5):
#     print('hello, world')
#     time.sleep(1)

#计算1到100的和
# total=0
# for i in range(1,101):
#     total += i
# print(total)

# #偶数求和
# total=0
# for i in range(0,101,2):
#     total += i
# print(total)
# print(sum(range(2, 101, 2)))

# """
# 从1到100的整数求和

# Version: 1.1
# Author: 骆昊
# """
# total = 0
# i = 1
# while i <= 100:
#     total += i
#     i += 1
# print(total)

# """
# 从1到100的偶数求和

# Version: 1.1
# Author: 骆昊
# """
# total = 0
# i = 2
# while i <= 100:
#     total += i
#     i += 2
# print(total)

# """
# 打印乘法口诀表

# Version: 1.0
# Author: 骆昊
# """
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f'{i}×{j}={i * j}', end='\t')
#     print()

# #判断素数
# a = int(input('a number: '))
# max_divisor = int(a ** 0.5)
# is_prime = True
# for i in range(2, max_divisor + 1):
#     if a % i == 0:
#         print(f'{a} 可以被 {i} 整除')
#         is_prime = False
#         break
# if is_prime:
#     print(f'{a} 是素数')
# else:
#     print(f'{a} 不是素数')


#欧几里得算法来找最大公约数
"""
输入两个正整数求它们的最大公约数

Version: 1.1
Author: 骆昊
"""
x = int(input('x = '))
y = int(input('y = '))
while y % x != 0:
    x, y = y % x, x
print(f'最大公约数: {x}')
