# #100以内的素数
# for input_num in range(2, 101):
#     is_prime = True
#     a = input_num **0.5
#     for i in range(2, int(a)+1):
#         if input_num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(f"{input_num}是素数")

#例子2：斐波那契数列，斐波那契数列的特点是数列的前两个数都是 1，从第三个数开始，每个数都是它前面两个数的和。
# 斐波那契数列的前 10 个数是：1, 1, 2, 3, 5, 8, 13, 21, 34, 55
a, b = 1, 1
print(a)
print(b)
for num in range(3,21):
    a, b = b, a + b
    print(b)