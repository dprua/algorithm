info_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']

string = input()

for char in info_list:
    string = string.replace(char,'^')

print(len(string))