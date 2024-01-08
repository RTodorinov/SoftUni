from functools import wraps


def test_decorator(func):
    @wraps(func)
    def test_wrapper(*arg):
        print("Starting")
        func()
        print("End")

    return test_wrapper


@test_decorator
def test():
    """test documentation"""
    print("Test")


print(test.__name__)
print(test.__doc__)

# използване на wraps
