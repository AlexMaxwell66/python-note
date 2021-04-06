content = []
with open('2020.txt') as fp:
    for line in fp.readlines():
        print(line)
        print(type(line))
        content.append((list(line.strip())))
        print(content)
res = 0
# 横向
for a in range(6):
    for b in range(3):
        if content[a][b] == '2' and content[a][b + 1] == '0' and content[a][b + 2] == '2' and content[a][b + 3] == '0':
            res += 1
# 斜向
for c in range(3):
    for d in range(3):
        if content[c][d] == '2' and content[c + 1][d + 1] == '0' and content[c + 2][d + 2] == '2' and content[c + 3][d + 3] == '0':
            res += 1
# 竖向
for e in range(3):
    for f in range(6):
        if content[e][f] == '2' and content[e + 1][f] == '0' and content[e + 2][f] == '2' and content[e + 3][f] == '0':
            res += 1

print(res)
