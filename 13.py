text="""
30/03/00
21/05/99
"""

res=[]

for line in text.split("\n"):
    for token in line.split("/"):
        res.append(token)

res=[i for i in res if i not in ""]

birth=[]
cnt=0
for i in range(int(len(res)/3)):
    tmp=[]
    for j in range(2,-1,-1):
        tmp.append(res[j+cnt])

    birth.append("".join(tmp))

    cnt+=3

print(birth)
