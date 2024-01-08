a = ['x', 'y', 'z']

for i in range(len(a)):
    el = a[i]
    print(el, i)

for i, el in enumerate(a):
    print(el, i)

# enumerate e съкратена версия на горния запис за да вземем елемента и индекса му
