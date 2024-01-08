x = "global"


def outer():
    x = "local"

    def inner():
        nonlocal x  # promenq w gorniq scope x

        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x  # promenq globalniq x
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()


print(x)
outer()
print(x)


# global
# outer: local
# inner: nonlocal
# outer: nonlocal
# global: changed!
