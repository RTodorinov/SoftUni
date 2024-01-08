import os
counter = 0

# ако сложим while true: и няма counter ще работи без да спира.
while counter < 3:
    counter += 1
    var = os.system("start cmd")
    var1 = os.system("start notepad")
    var2 = os.system("microsoftedge")

    print(var)
    print(var1)
    print(var2)
