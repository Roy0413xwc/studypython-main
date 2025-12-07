"""
BMI计算器

Version: 1.0
Author: 骆昊
"""
# height = float(input('身高(cm)：'))
# weight = float(input('体重(kg)：'))
# bmi = weight / (height / 100) ** 2
# print(f'{bmi = :.1f}')
# if 18.5 <= bmi < 24:
#     print('你的身材很棒！')
# else:
#     print('需要适当调整饮食和运动习惯！')

# status_code = int(input('响应状态码: '))
# if status_code == 400:
#     description = 'Bad Request'
# elif status_code == 401:
#     description = 'Unauthorized'
# elif status_code == 403:
#     description = 'Forbidden'
# elif status_code == 404:
#     description = 'Not Found'
# elif status_code == 405:
#     description = 'Method Not Allowed'
# elif status_code == 418:
#     description = 'I am a teapot'
# elif status_code == 429:
#     description = 'Too many requests'
# else:
#     description = 'Unknown status Code'
# print('状态码描述:', description)



# status_code = int(input('响应状态码: '))
# match status_code:
#     case 400: description = 'Bad Request'
#     case 401: description = 'Unauthorized'
#     case 403: description = 'Forbidden'
#     case 404: description = 'Not Found'
#     case 405: description = 'Method Not Allowed'
#     case 418: description = 'I am a teapot'
#     case 429: description = 'Too many requests'
#     case _: description = 'Unknown Status Code'
# print('状态码描述:', description)

"""
计算三角形的周长和面积

Version: 1.0
Author: 骆昊
"""
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    perimeter = a + b + c
    print(f'周长: {perimeter}')
    s = perimeter / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f'面积: {area}')
else:
    print('不能构成三角形')