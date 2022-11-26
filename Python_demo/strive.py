# Coder: Lee
# Time:  2022/11/4 15:51

# fp = open("slogan.txt", 'w', encoding='utf-8')
# print("奋斗成绩更好的你", file=fp)
# fp.close()

with open("slogan.txt", 'w', encoding='utf-8') as wfile:
    print("驾四海, 驭八荒", file=wfile)
