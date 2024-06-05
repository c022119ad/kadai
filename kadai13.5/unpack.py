# 要素数と変数の数が一致する場合
a, b, c = [0, 1, 2]
print("リスト", a, b, c)
a, b, c = (0, 1, 2)
print("タプル", a, b, c)
a, b, c = {0, 1, 2}
print("集合", a, b, c)
a, b, c = {0:0, 1:1, 2:2}
print("辞書", a, b, c)
a, b, c = "012"
print("文字列", a, b, c)


print("-"*10)
# 要素数より変数が少ない場合
# a, b, c = [0, 1, 2, 3, 4]  # エラー
a, b, *c = [0, 1, 2, 3, 4]
print(a, b, c)
a, *b, c = [0, 1, 2, 3, 4]
print(a, b, c)
*a, b, c = [0, 1, 2, 3, 4]
print(a, b, c)
# a, *b, *c = [0, 1, 2, 3, 4]
# print(a, b, c)

# 右辺がタプルの場合
a, b, *c = (0, 1, 2, 3, 4)
print(a, b, c)


print("-"*10)
# 要素数より変数が多い場合
a, b, *c = [0, 1, 2]  # 同数の場合
print(a, b, c)
a, b, *c = [0, 1]
print(a, b, c)
*a, b, c = [0, 1]
print(a, b, c)