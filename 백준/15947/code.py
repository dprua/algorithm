init = "baby sukhwan tururu turu very cute tururu turu in bed tururu turu baby sukhwan" #0~13
#print(len(init.replace(" ",""))) # 65
store = init.split(" ")
#2 3 6 7 10 11
#print(len(store)) 14
n = int(input())

cycle = int(n / len(store))
namage = n % len(store)

for idx in range(len(store)):
    if 'turu' in store[idx]:
        store[idx] = store[idx] + ('ru'*cycle)

#print(store)
namage-=1
if namage == 2 or namage == 3 or namage == 6 or namage == 7 or namage == 10 or namage == 11:
    if len(store[namage]) >= 12:
        count = int((len(store[namage])-2) / 2)
        print("tu"+'+ru*'+str(count))
    else:
        print(store[namage])
else:
    print(store[namage])