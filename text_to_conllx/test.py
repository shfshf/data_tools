import random
from zhon.hanzi import punctuation

aa = "今天的天气？"
print(aa[-1])
punctuation_str = punctuation
print(type(punctuation_str))
print("中文标点符合：", punctuation_str)
if aa[-1] in punctuation_str:
    aa = aa[:-1]
print(aa)
# for i in punctuation:
#     if aa[-1] == i:
#         cc = aa[-1]
#     else:
#         cc = aa
#     print(cc)


# from zhon.hanzi import punctuation
#
# str = '今天周五，下班了，好开心呀！！'
# punctuation_str = punctuation
# print("中文标点符合：", punctuation_str)
# for i in punctuation:
#     str = str.replace(i, '')
# print(str)  # 今天周五下班了好开心呀