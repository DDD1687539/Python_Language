# Coder: Lee
# Time:  2022/11/4 20:43

lst = []
for i in range(0, 5):
    goods = input("请输入商品编号和商品名称进行入库，每次只能输入一件商品:\n$ ")
    lst.append(goods)

for item in lst:
    print(item)

print("=======================")
print(lst)

cart = []
while True:
    num = input("请输入要购买的商品编号: ")
    for item in lst:
        if item.find(num) != -1:
            cart.append(item)
            break
    if num == 'q':
        break

print("你购物车里已经选好的商品为: ")
for item in cart:
    print(item)


