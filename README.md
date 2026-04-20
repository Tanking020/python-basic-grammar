# python-basic
basic-grammar
# Python 基础练习：循环与条件判断

**学习日期**：2026.04.19

---

## 📚 今日学习内容

| 知识点 | 练习题目 | 状态 |
|:---|:---|:---:|
| `while` 循环 | 1到100所有偶数和 | ✅ |
| `for` 循环 | 100到500所有3的倍数和 | ✅ |
| `range()` 函数 | 理解左闭右开区间 | ✅ |
| 条件判断 | 三角形类型判断 | ✅ |
| 异常处理 | 简单计算器 | ✅ |
| 列表操作 | 三角形边长输入 | ✅ |

---

## 💻 代码示例

### 1. 1到100偶数和（while循环）

```python
i = 1
total = 0
while i <= 100:
    if i % 2 == 0:
        total += i
    i += 1
print(f"1到100之间的所有偶数之和为{total}")  # 2550
```

### 2. 100到500所有3的倍数和（for循环）

```python
total = 0
for i in range(100, 501):
    if i % 3 == 0:
        total += i
print(f"100到500之间所有3的倍数的数字之和为：{total}")  # 39900
```

### 3. 三角形判断

```python
sides = []
for i in range(1, 4):
    side = float(input(f"请输入边长{i}："))
    sides.append(side)

a, b, c = sorted(sides)

if a + b <= c:
    print("这不是一个三角形")
elif a == b == c:
    print("等边三角形")
elif a == b or b == c:
    if a**2 + b**2 == c**2:
        print("等腰直角三角形")
    else:
        print("等腰三角形")
elif a**2 + b**2 == c**2:
    print("直角三角形")
else:
    print("普通三角形")
```

### 4. 简单计算器

```python
try:
    num1 = float(input("请输入数字1:"))
    op = input("请输入运算符:")
    num2 = float(input("请输入数字2:"))
except ValueError:
    print("输入有误！")
    exit()

match op:
    case "+": result = num1 + num2
    case "-": result = num1 - num2
    case "*": result = num1 * num2
    case "/":
        if num2 == 0:
            print("除数不能为0！")
            exit()
        result = num1 / num2
    case _:
        print("运算符有误！")
        exit()

print(f"{num1} {op} {num2} = {result}")
```

---

## 🧠 关键知识点总结

### `range(a, b)` 的区间
- **左闭右开**：包含 `a`，不包含 `b`
- 示例：`range(2, 6)` → `2, 3, 4, 5`

### `exit()` vs `break`
| 方法 | 作用 |
|:---|:---|
| `exit()` | 结束整个程序 |
| `break` | 只退出当前循环 |
| `return` | 只退出当前函数 |

### 列表 `append()`
- 向列表末尾添加元素
- `sides.append(side)` 将 `side` 加入 `sides` 列表

### 解包赋值
```python
a, b, c = sides  # 列表元素分别赋给 a, b, c
```

---

## 📁 文件结构

```
Python-Basics-Learning/
├── README.md
├── 01_even_sum.py          # 1-100偶数和
├── 02_multiples_sum.py     # 100-500的3倍数和
├── 03_triangle.py          # 三角形判断
├── 04_calculator.py        # 简单计算器
└── 05_loop_examples.py     # 循环综合练习
```

---

## 🔄 后续计划

- [ ] 函数封装练习
- [ ] 文件读写操作
- [ ] 小游戏开发（猜数字、剪刀石头布）
- [ ] 继续数值分析算法实现

---

## 📖 参考资料

- [Python 官方文档](https://docs.python.org/3/)
- [廖雪峰 Python 教程](https://www.liaoxuefeng.com/wiki/1016959663602400)

---

*持续更新中...*
```

---

## 二、如果你想要更简洁的版本

```markdown
# Python 基础练习 (2026.04.19)

## 练习列表

1. **1-100偶数和** → `01_even_sum.py`
   - while循环 + 取模判断
   - 结果：2550

2. **100-500的3倍数和** → `02_multiples_sum.py`
   - for循环 + range() + 取模判断
   - 结果：39900

3. **三角形判断** → `03_triangle.py`
   - 边长输入 → 存在性判断 → 类型判断
   - 支持等边、等腰、等腰直角、直角、普通三角形

4. **简单计算器** → `04_calculator.py`
   - 异常处理 + match-case + 除零保护

## 关键收获

- `range(a, b)` 是左闭右开区间 `[a, b)`
- `exit()` 结束整个程序，`break` 只结束循环
- 列表用 `[]`，`append()` 添加元素
- 解包赋值 `a, b, c = [1, 2, 3]`
```

## 2026.04.20
## Python 列表与循环综合练习

**My Python Learning Journey (我的 Python 学习之路)**

转码预备役 | 记录从零开始系统学习 Python

---

## 📚 今日学习内容

| 知识点 | 练习题目 | 状态 |
|:---|:---|:---:|
| 嵌套循环 | 长方形打印、99乘法表 | ✅ |
| 循环控制 | `break`、`continue`、`exit()` | ✅ |
| 登录验证逻辑 | `while True` + 条件判断 | ✅ |
| 异常处理 | `try-except` 捕获输入错误 | ✅ |
| 随机数生成 | 猜数字游戏 | ✅ |
| 列表切片 | `s[1:5:2]` | ✅ |
| 列表增删改查 | `append`、`insert`、`pop`、`remove` | ✅ |
| 列表排序 | `sort()`、`reverse()`、`key=len` | ✅ |
| 列表合并 | `+`、`[*a,*b]`、`extend()` | ✅ |
| 列表去重 | 遍历 + `in` 判断 | ✅ |
| 数据统计 | 最大值、最小值、平均值 | ✅ |

---

## 💻 代码示例

### 1. 长方形打印

```python
try:
    a = int(input("请输入长方形的宽："))
    b = int(input("请输入长方形的长："))
except ValueError:
    print("请输入整数！！！")
    exit()

for i in range(a):
    for j in range(b):
        print("*", end="")
    print()
```

### 2. 99乘法表

```python
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={i * j}", end=" ")
    print()
```

### 3. 登录验证系统（优化版）

```python
while True:
    name = input("请输入账号：")
    key = input("请输入密码：")

    if name == "" or key == "":
        print("账号或密码不能为空！！！")
        continue

    valid = ((name == "admin" and key == "666888") or
             (name == "zhangsan" and key == "123456") or
             (name == "taoge" and key == "888666"))

    if not valid:
        print("账号或密码错误，请重新输入！！！")
        continue
    else:
        print("登录成功，进入B站首页~")
        break
```

### 4. 猜数字游戏

```python
import random

random_number = random.randint(1, 100)

while True:
    try:
        user_num = int(input("请输入数字:"))
    except ValueError:
        print("您输入的格式有误！！！")
        continue
    
    if user_num > random_number:
        print("您输入的数字比实际数字更大")
    elif user_num < random_number:
        print("您输入的数字比实际数字更小")
    else:
        print("您输入的数字就是实际数字！！！")
        break
```

### 5. 列表操作综合

```python
s = [1, 22, 7, 33, 4, 4, 5]

# 切片
s1 = s[1:5:2]

# 增删改查
s.append(7)
s.reverse()
s.sort()
s.sort(reverse=True)
s.insert(2, 90)
s.pop(2)
s.remove(7)

# 按长度排序
b = ["111", "22", "1", "aaa"]
b.sort(key=len)
b.sort(key=len, reverse=True)
```

### 6. 10个数字的统计

```python
s = []

for i in range(10):
    s.append(int(input(f"请输入数字{i+1}:")))

s.sort(reverse=True)
print(s)

max_value = s[0]
min_value = s[-1]
average = sum(s) / len(s)
print(f"最大值:{max_value}, 最小值:{min_value}, 平均值:{average}")
```

### 7. 列表合并 + 排序 + 去重（三种方法）

```python
num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]

# 方法1：+ 拼接（最简洁）
num = num_list1 + num_list2

# 方法2：解包合并
num = [*num_list1, *num_list2]

# 方法3：extend（修改原列表）
num_list1.extend(num_list2)
num = num_list1

# 统一处理：排序 + 去重
num.sort()
num_new = []
for x in num:
    if x not in num_new:
        num_new.append(x)

print(num_new)
```

---

## 🧠 核心知识点总结

### 1. `break` vs `continue` vs `exit()`

| 关键字 | 作用 |
|:---|:---|
| `break` | 退出当前循环 |
| `continue` | 跳过本次循环，继续下一次 |
| `exit()` | 退出整个程序 |

**注意**：`break` 和 `continue` 只作用于最内层循环。

### 2. 列表操作返回值

| 操作 | 返回值 | 是否修改原列表 |
|:---|:---|:---|
| `lst.append(x)` | `None` | ✅ 修改 |
| `lst.insert(i, x)` | `None` | ✅ 修改 |
| `lst.pop(i)` | 被删除的值 | ✅ 修改 |
| `lst.remove(x)` | `None` | ✅ 修改 |
| `lst.sort()` | `None` | ✅ 修改 |
| `lst.reverse()` | `None` | ✅ 修改 |
| `lst + [x]` | 新列表 | ❌ 不修改 |
| `[*lst1, *lst2]` | 新列表 | ❌ 不修改 |

**重要记忆**：会修改原列表的方法通常返回 `None`，不能赋值给变量。

### 3. `pop()` vs `del`

| 方法 | 返回值 | 删除范围 |
|:---|:---|:---|
| `pop()` | 被删除的值 | 单个元素（默认最后一个） |
| `del` | 无 | 单个元素 / 切片 / 整个列表 |

### 4. 列表合并的三种方式

| 方法 | 代码 | 是否创建新列表 |
|:---|:---|:---|
| `+` 拼接 | `new = a + b` | ✅ 是 |
| 解包合并 | `new = [*a, *b]` | ✅ 是 |
| `extend()` | `a.extend(b)` | ❌ 否（修改 a） |

### 5. 列表去重（经典方法）

```python
result = []
for x in original_list:
    if x not in result:
        result.append(x)
```

### 6. `in` 运算符

```python
if num0 not in num_new:  # 判断元素是否在列表中
```

`in` 返回布尔值（`True`/`False`），是列表查找的常用方法。

---

## 🐛 今日 Debug 记录

| 错误 | 原因 | 解决方案 |
|:---|:---|:---|
| `IndexError` | 空列表用 `s[i]` 赋值 | 用 `append()` 添加元素 |
| `ValueError` | 输入非数字 | 用 `try-except` 捕获 |
| 随机数每次都变 | 随机数生成在循环内 | 移到循环外生成一次 |
| 登录验证空值漏检 | 密码错误后没检空值 | 用 `while True` + `continue` 统一处理 |
| `append()` 返回 `None` | 误以为返回新列表 | 单独一行使用，不赋值 |

---

## 📁 文件结构

```
Python-Learning-2026.04.20/
├── README.md
├── 01_rectangle.py         # 长方形打印
├── 02_multiplication.py    # 99乘法表
├── 03_login_system.py      # 登录验证系统
├── 04_guess_number.py      # 猜数字游戏
├── 05_list_operations.py   # 列表操作综合
├── 06_number_stats.py      # 10个数字统计
└── 07_list_merge_dedup.py  # 列表合并+排序+去重
```

---

## 🔄 后续计划

- [ ] 函数基础（定义、参数、返回值）
- [ ] 模块与包的导入
- [ ] 文件读写操作
- [ ] 面向对象基础（暂缓）

---

## 📖 参考资料

- [Python 官方文档](https://docs.python.org/3/)
- [廖雪峰 Python 教程](https://www.liaoxuefeng.com/wiki/1016959663602400)

---

*持续更新中...* 🚀
