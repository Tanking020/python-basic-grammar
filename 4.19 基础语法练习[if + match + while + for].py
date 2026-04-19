# try:
#     test_number = int(input("请输入年份"))
#
#     if test_number%400 == 0 or (test_number%100 != 0 and test_number%4 == 0):
#         print("闰年")
#     else:
#         print("平年")
# except ValueError:
#     print("请输入有效数字！")
#（以上为每行注释，后面采用三引号多行注释）


#a,b,c = int(input("请输入边长1")) , int(input("请输入边长2")) , int(input("请输入边长3"))

#尝试用循环的方式输入
"""
sides = []
try:
    for i in range(1,4):
        side = float(input(f"请输入边长{i}:"))
        if side <= 0:
            print("边长必须大于0！")
            exit()
        sides.append(side)
except ValueError:
    print("边长格式异常")

a,b,c = sides
A = a**2
B = b**2
C = c**2
if a + b <= c or b + c <= a or a + c <= b:
    print("这不是一个三角形")
    exit()

if a == b == c:
    print("这是一个等边三角形")
elif a == b or b == c or a == c:
    #注意等腰直角三角形的可能性
    if A + B == C or B + C == A or A + C == B:
        print("这是一个等腰直角三角形")
    else:
        print("这是一个等腰三角形")
elif A + B == C or B + C == A or A + C == B:
    print("这是一个直角三角形")
else:
    print("这是一个普通三角形")
"""

"""
#计算器书写
try:
    number_1 = float(input("请输入数字1:"))
    operator = input("请输入运算符:")
    number_2 = float(input("请输入数字2:"))
except ValueError:
    print("字符输入有误！！！")
    exit()

match operator:
    case "+":
        number_3 = number_1 + number_2
    case "-":
        number_3 = number_1 - number_2
    case "*":
        number_3 = number_1 * number_2
    case "/":
        if number_2 == 0:
            print("除数不能为0！！！")
            exit()
        else:
            number_3 = number_1 / number_2
    case _ :
        print("输入有误！！！")
        exit()

print(f"{number_1} {operator} {number_2} = {number_3}")
"""

"""
#计算1到100之间所有偶数的累加之和
i=1
total = 0
while i <= 100:
    if i % 2 == 0:
        total += i
    i += 1
print(f"1到100之间的所有偶数之和为{total}")
"""

"""
total = 0
for i in range(100,501):
    if i % 3 == 0:
        total += i
print(f"100到500之间所有3的倍数的数字之和为：{total}")
"""

#另外一种方法（步长法）
"""
total = 0
for i in range(102,501,3):
    total += i
print(f"100到500之间所有3的倍数的数字之和为：{total}")
"""

