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

## 2026.04.22
## Python 列表推导式、字符串操作、元组与数据嵌套实战

**My Python Learning Journey (我的 Python 学习之路)**

转码预备役 | 记录从零开始系统学习 Python

---

## 📚 今日学习内容

| 知识点 | 练习题目 | 状态 |
|:---|:---|:---:|
| 列表推导式 | 生成平方列表、条件筛选 | ✅ |
| 字符串操作 | `find()`、`count()`、`upper()`、`split()`、`strip()`、`replace()` | ✅ |
| 邮箱格式验证 | `count()` + `in` 运算符 | ✅ |
| 元组定义 | 单元素元组需要逗号 | ✅ |
| 元组组包与解包 | `a,b,c = 100,200,300` | ✅ |
| 元组嵌套 | 学生成绩表 | ✅ |
| 数据统计 | 总分、平均分、最高/最低分 | ✅ |
| `\t` 制表符 | 表格对齐 | ✅ |

---

## 💻 代码示例

### 1. 列表推导式

```python
# 生成1-20的平方列表
num_list = [i**2 for i in range(1, 21)]
print(num_list)

# 从列表中提取偶数并计算平方
num_list = [19, 23, 54, 64, 87, 20, 109, 232, 123, 43, 26, 55, 72]
num_list2 = [i**2 for i in num_list if i % 2 == 0]
print(num_list2)

# 提取正数
list1 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]
list2 = [i for i in list1 if i > 0]
print(list2)
```

### 2. 字符串常用操作

```python
s = "python"

# 查找子串
print(s.find("th"))   # 2（索引位置）

# 统计次数
print(s.count("t"))   # 2

# 大小写转换
print(s.upper())      # PYTHON
print(s.lower())      # python

# 分割字符串
print(s.split("t"))   # ['py', 'hon']

# 去除指定字符
print(s.strip("p"))   # ython

# 替换子串
print(s.replace("p", "o"))  # oython

# 检查开头
print(s.startswith("py"))   # True

# 检查存在
print("th" in s)      # True
```

### 3. 邮箱格式验证

```python
email = input("请输入邮箱：")
if email.count("@") == 1 and "." in email:
    print("邮箱格式输入正确")
else:
    print("邮箱格式输入错误")
```

### 4. 元组组包与解包

```python
# 组包：把多个值打包成元组
a, b, c = 100, 200, 300
print(a, b, c)  # 100 200 300

# 交换变量（解包）
c, a, b = a, b, c
print(a, b, c)  # 200 300 100

# 单元素元组必须有逗号
t1 = (100,)   # ✅ 元组
t2 = (100)    # ❌ 整数
```

### 5. 学生成绩分析（元组嵌套实战）

```python
students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李木碗", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周铁", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐利果", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "遁天", 66, 59, 72),
)

# 打印表格（使用 \t 对齐）
print("学号\t姓名\t语文\t数学\t英语\t总分\t平均分")

for stu_id, name, chinese, math, english in students:
    total = chinese + math + english
    avg = total / 3
    print(f"{stu_id}\t{name}\t{chinese}\t{math}\t{english}\t{total}\t{avg:.1f}")

# 统计各科最高/最低分
chinese_scores = [s[2] for s in students]
math_scores = [s[3] for s in students]
english_scores = [s[4] for s in students]

print(f"语文：最高{max(chinese_scores)}，最低{min(chinese_scores)}")
print(f"数学：最高{max(math_scores)}，最低{min(math_scores)}")
print(f"英语：最高{max(english_scores)}，最低{min(english_scores)}")

# 找出平均分大于90的学生
for stu_id, name, chinese, math, english in students:
    if (chinese + math + english) / 3 > 90:
        print(f"{name}是优秀学生")
```

---

## 🧠 核心知识点总结

### 1. 列表推导式语法

```python
# 基础语法
[表达式 for 变量 in 可迭代对象]

# 带条件
[表达式 for 变量 in 可迭代对象 if 条件]

# 示例
[i**2 for i in range(1, 21)]                    # 平方列表
[i for i in list1 if i > 0]                     # 筛选正数
[i**2 for i in num_list if i % 2 == 0]          # 偶数平方
```

### 2. 字符串 vs 列表

| 特性 | 列表 | 字符串 |
|:---|:---|:---|
| 可变性 | ✅ 可变 | ❌ 不可变 |
| 修改操作 | 修改原列表，返回 `None` | 返回新字符串 |
| 典型操作 | `append()`、`pop()`、`sort()` | `upper()`、`replace()`、`split()` |

### 3. 元组要点

```python
# 定义
t = (1, 2, 3)           # 元组
t = (100,)              # 单元素元组（必须有逗号）
t = 100, 200, 300       # 不加括号也可以

# 只有两种查询操作
t.index(100)   # 查找位置
t.count(100)   # 统计次数

# 组包与解包
a, b, c = 100, 200, 300      # 组包
c, a, b = a, b, c            # 解包交换
```

### 4. 字符串常用方法

| 方法 | 作用 | 返回值 |
|:---|:---|:---|
| `s.find(sub)` | 查找子串 | 索引（找不到返回-1） |
| `s.count(sub)` | 统计次数 | 整数 |
| `s.upper()` | 转大写 | 新字符串 |
| `s.lower()` | 转小写 | 新字符串 |
| `s.split(sep)` | 分割 | 列表 |
| `s.strip(chars)` | 去除两端字符 | 新字符串 |
| `s.replace(old, new)` | 替换 | 新字符串 |
| `s.startswith(prefix)` | 检查开头 | `True`/`False` |
| `sub in s` | 检查存在 | `True`/`False` |

### 5. `\t` 制表符

- 作用：对齐文本，跳到下一个制表位
- 常用场景：打印表格、对齐多列数据
- 与空格的区别：自动对齐，不受内容长度影响

---

## 🐛 今日易错点

| 易错点 | 正确理解 |
|:---|:---|
| `(100)` 是元组吗？ | ❌ 不是，是整数。元组需要逗号 `(100,)` |
| 字符串方法修改原字符串？ | ❌ 不修改，返回新字符串 |
| `s.find()` 找不到返回什么？ | 返回 `-1`（不报错） |
| 列表推导式 `if` 放哪里？ | 放在 `for` 后面 |

---

## 📁 文件结构

```
Python-Learning-2026.04.22/
├── README.md
├── 01_list_comprehension.py   # 列表推导式
├── 02_string_operations.py    # 字符串操作
├── 03_email_validate.py       # 邮箱验证
├── 04_tuple_pack_unpack.py    # 元组组包解包
└── 05_student_scores.py       # 学生成绩分析
```

---

## 🔄 后续计划

- [ ] 字典与集合操作
- [ ] 函数基础（定义、参数、返回值）
- [ ] 文件读写操作

---

## 📖 参考资料

- [Python 官方文档](https://docs.python.org/3/)
- [廖雪峰 Python 教程](https://www.liaoxuefeng.com/wiki/1016959663602400)

---

*持续更新中...* 🚀
