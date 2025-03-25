word=input("camel case :")


word=list(word)
for i in range(len(word)):
    if word[i]==word[i].upper():
        word[i]=word[i].lower()
        word.insert(i,"_")



snake_case=""
for car in word:
    snake_case+=car

print(snake_case)
