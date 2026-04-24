#集合set: 无序，不可重复，可修改
#pop操作会删除随机元素并且返回被删除的元素
#交并差集合运算会返回新集合(后面加_update会修改原集合返回空值)，pop以外的修改会返回空值，要区分开
#定义空集合只能用set()而不是{}

#案例处理：
"""
football_set = {"wanglin","zenniu","duntian","tianyunzi","hanli","lifeiyu","wuchou","zilin"}

basketball_set = {"zhangtie","dongjuren","wanglin","jianglaodao","ziniu","wangchan","hanli","tianyunzi","lihuayuan","lifeiyu","yunlu"}

french_set = {"xumu","wangzhuo","shisan","hupao","jianglaodao","tianyunzi","hongdie","lifeiyu","hanli","zengniu"}

art_set = {"duntian","tianyunzi","hanli","hupao","jianglaodao","zilin"}

#找出同时选修了法语和艺术的学生
# 方式一：
# f_a_set = french_set.intersection(art_set)
# print(f_a_set)

#方式2：&表示交集
f_a_set = french_set & art_set
print(f_a_set)

# 找出选修了足球但是没选修篮球的学生——差集
# f_d_b = football_set.difference(basketball_set)
# print(f_d_b)

# 也可以用减号表示差运算(在本案例中最简单)
# f_d_b = football_set - basketball_set
# print(f_d_b)

# 方式三：集合推导式
f_d_b = {s for s in football_set if s not in basketball_set}
print(f_d_b)

# 统计每一个学生选修的课程数量
# 1、获取到学生名单（采用|取并集）（也可用union操作）
all_set = football_set | basketball_set | art_set |french_set
print(all_set)

# 2、获取每一个学生选修的课程数量(需要可重复性，所以这里用列表)
all_list = [*football_set, *basketball_set, *art_set, *french_set]

for s in all_list:
    print(f"{s}选修了{all_list.count(s)}门课程")
"""

#字典dict：存储键值对（key:value）类型数据,哈希表和映射也是这种存储类型
#！！！字典中的value可以是任何类型的数据，而key不能为可变类型（如：列表，集合，字典）！！！
#key重复的话后面的值会覆盖前面的值

#字典的三种遍历方式！
"""
dict1 = {"haha":1,"xixi":2,"wuwu":3}

for k in dict1.keys():#按键遍历
    print(f"{k} : {dict1[k]}")

for k in dict1.values():#按值遍历（不方便输出键）
    print(f"{k}")

for item in dict1.items():#按键值对遍历1
    print(f"{item[0]} : {item[1]}")

for k,v in dict1.items():#按键值对遍历2（解包的方式）
    print(f"{k} : {v}")
"""

# 案例：开发购物车管理系统并实现其增删改查
gwc = dict()
while True:
    tr = input("欢迎来到首页！输入数字0进入购物车管理系统,输入数字6将退出本系统：")
    if tr == "0":
        while True:
            print("购物车管理系统为您服务")
            print()
            print("操作1：增加商品至购物车")
            print("操作2：修改购物车中的商品")
            print("操作3：删除购物车中的商品")
            print("操作4：查询购物车中的商品")
            print("操作5：返回上一级菜单")
            print()
            tr0 = input("请选择操作1-5：")

            if tr0 == "1":
                while True:
                    try:
                        tr1 = input("是否需要(继续)录入：")
                        if tr1 == "否":
                            break
                        elif tr1 == "是":
                            name = input("请输入商品名称：")
                            price = float(input("请输入商品价格："))
                            quantity = int(input("请输入商品数量："))
                            gwc[name] = (price, quantity)
                            print(f"此次增加后的购物车内容为{gwc}")
                    except ValueError as e:#将错误变量赋值给e！！！
                        print(f"格式错误变量为{e}")
                        print(f"格式错误变量类型为{type(e)}")
                        print("价格必须为数字！数量必须为整数！判断句只能输入“是”或者“否”！")
                        continue

                print(f"增加后的购物车共{len(gwc)}件商品，内容：{gwc}")

            elif tr0 == "2":
                while True:
                    try:
                        tr2 = input("请问是否需要(继续)修改商品：")
                        if  tr2 == "否":
                            break
                        elif tr2 == "是":
                            name = input("请输入商品名称：")
                            if name in gwc:
                                price = float(input("请输入商品价格："))
                                quantity = int(input("请输入商品数量："))
                                gwc[name] = (price, quantity)
                                print(f"此次修改后的购物车内容：{gwc}")
                            else:
                                print("此商品在购物车中不存在！")
                                print(f"当前购物车内容：{gwc}")
                        else:
                            print("请输入“是”或者“否”！")
                    except ValueError as e:
                        print(f"格式错误变量为{e}")
                        print(f"格式错误变量类型为{type(e)}")
                        print("价格必须为数字！数量必须为整数！")
                        continue

                print(f"修改后的购物车共{len(gwc)}件商品，内容：{gwc}")

            elif tr0 == "3":
                while True:
                    tr3 = input("请问是否需要（继续）删除商品：")
                    if tr3 == "否":
                        break
                    elif tr3 == "是":
                        name = input("请输入要删除商品的名字：")
                        if name in gwc:
                            del gwc[name]
                            key = list(gwc.keys())
                            print(f"已经为您删除{name}商品，购物车剩余商品为{key}")
# gwc.keys() 返回的是 dict_keys(['香蕉', '橙子'])，不是 (['香蕉', '橙子'])，这里转换为列表提升可读性
                        else:
                            print("该商品不在购物车内！")
                            print(f"当前购物车内容：{gwc}")
                    else:
                        print("请输入“是”或者“否”！")

                print(f"删除后的购物车共{len(gwc)}件商品，内容：{gwc}")

            elif tr0 == "4":
                while True:
                    tr4 = input("您是否需要查询购物车中的商品：")
                    if tr4 == "否":
                        break
                    elif tr4 == "是":
                        if gwc == {}:
                            print("购物车为空！")
                        else:
                            for k,v in gwc.items():
                                print(f"商品名称：{k}，商品价格：{v[0]},商品数量：{v[1]}")
                    else:
                        print("请输入“是”或者“否”！")

            elif tr0 == "5":
                print("为您返回上一级菜单！")
                break

            else:
                print("您输入的数字有误，或出现格式错误！")

    elif tr == "6":
        print("已为您退出系统！")
        break
    else:
        print("您输入的数字有误，或出现格式错误！请重新输入")