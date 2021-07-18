word = input().upper()

unique_char = list(set(word))

cnt_list = []
for char in unique_char:
    cnt = word.count(char)
    cnt_list.append(cnt)

if(cnt_list.count(max(cnt_list)) > 1):
    print("?")
else:
    idx = cnt_list.index(max(cnt_list))
    print(unique_char[idx])

