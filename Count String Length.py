inp = input("Enter value: ")
print(inp)
a = inp[1:]
b = inp[0]
c = int(b)
print(a)
print(type(b),type(c))

if c == len(a):
    print(True)

# try:
#     if type(int(b)) == type(int(c)):
#         print(True)
#     # b = int(inp[0])
# except Exception as e:
#     print(e)
# print(type(b))

#
# part = [inp[index[0]] for index in b]
# print(part)
#
# if b != int(b):
#     print(False)
    # b.append(inp[0])
#
# print(b)