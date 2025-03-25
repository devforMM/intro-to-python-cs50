liste=[]
while True:
    try:
      prompt=input().upper()
      liste.append(prompt)





    except EOFError:
        break
dic={}

liste.sort()
for item in liste:
   dic[item]=liste.count(item)

for key in dic:
   print(f"{dic.get(key)} {key}")
