# inp = input()
# num = ""
#
# for s in inp:
#     if(ord(s) in range(48,58)):
#         num+= s
# if ((len(inp)-len(num))) == int(num):
#     print(True, num)


################# HSL #########################################
string = input()
l = len(string)
count=0
# print(l)

# if (string.endswith('H')):
#     for(int j)

if(l>3):
    for i in range(l-2):
        for j in range(i+1,l-1):
            for k in range(j+1,l):
                if(string[i]+string[j]+string[k]=="HSL"):
                    count = count+1
    print(count)

elif(l==3):
    if(string=="HSL"):
        print(1)