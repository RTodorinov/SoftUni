

# tail = input()
# body = input()
# head = input()

# meerkat_list = list()
# meerkat_list.append(head)
# meerkat_list.append(body)
# meerkat_list.append(tail)
# print(meerkat_list)


''' direct swapping in lists'''

# tail = input()
# body = input()
# head = input()
#
# meerkat = [tail, body, head]
# meerkat[0], meerkat[2] = meerkat[2], meerkat[0]
# print(meerkat)

''' using temp for swap'''
# tail = input()
# body = input()
# head = input()
#
# meerkat = [tail, body, head]
# temp = meerkat[0]
#
# meerkat[0] = meerkat[2]
# meerkat[2] = temp
#
# print(meerkat)

tail = input()
body = input()
head = input()

meerkat = [head, body, tail]
print(meerkat)
