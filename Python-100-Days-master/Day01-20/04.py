"""
将华氏温度转换为摄氏温度

Version: 1.0
Author: xwc
"""
#1
# f = float(input('请输入华氏温度: '))
# c = (f - 32) / 1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f, c))
# print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')

# #2
# import math
# pi = math.pi
# r = float(input('input the r:'))
# area = pi * r * r
# print(f'the area is {area:.4f}')
# perimeter = 2 * pi * r
# print('the perimeter is %.4f' % perimeter)
# print(f'{perimeter = :.2f}')  # 输出：perimeter = 34.56
# print(f'{area = :.2f}')       # 输出：area = 95.03

#3
year = int(input('请输入年份: '))
is_leap = (year % 4 ==0 and year % 100 !=0 or year % 400 ==0)
print(f'{year}是闰年吗? {is_leap}')