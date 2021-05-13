from collections import defaultdict


d = defaultdict(list)
# print(d)
d['python'].append("awesome")
# print(d)
d['something-else'].append("not relevant")
# print(d)
d['python'].append("language")
# print(d)
for i in d.items():
    print(i)

def_dict = defaultdict(list)
def_dict1 = defaultdict(list)
