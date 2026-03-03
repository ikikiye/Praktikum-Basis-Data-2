li=[100,200,300,400]
li.append(500)

print("Test Print 1")
print(li[0])

li.remove(100)
li.append(100)

li.append(190)
li.append(90)
panjang_list = len(li)
print("\nTest Print 2")
for i in range(panjang_list):
    if i == 0:
        print(li[i])
    elif li[i]<li[i-1]:
        print(li[i], "(-)")
    else:
        print(li[i], "(+)")