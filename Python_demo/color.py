# Coder: Lee
# Time:  2022/11/4 21:02


print("\033[0;30;44m莫言语，且看那翩翩少年郎\033[0m")
print("\033[0;30;44m驾四海，驭八荒\033[0m")
print("\033[0;30;44m天高海阔凭鱼跃\033[0m")
print("\033[0;30;44m追风逐日赛凤凰\033[0m")

coincode = ['1001', '1002', '1003', '1004', '1005']
coinname = ['bitcoin', 'ethereum', 'AR', 'LTC', "Dogecoin"]

d = dict(zip(coincode, coinname))
print(d)
for item in d:
    print(item, d[item])

key = input("请输入你需要的Coin Code: ")
print(key, "的名称为: ", d.get(key))

