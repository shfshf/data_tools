import numpy as np

list = []
with open('./data/entity.txt', 'r') as f:
    for line in f:
        list.append(line.strip())

list_less = np.array(list)
list_re = np.unique(list_less)  # 去重

with open("./data/entity_l.txt", "w") as f:
    for item in sorted(list_re):
        f.writelines(item)
        f.writelines('\n')
    f.close()
