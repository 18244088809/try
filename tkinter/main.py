import random

num = random.randint(10,19)
print(num)

while True:
    result = int(input("请输入一个数字："))
    if result>num:
        print("大")
    elif result<num:
        print("小")
    else:
        print("对了")
        break