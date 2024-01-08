# def age_assignment(*args, **kwargs):
#     persons = {}
#     for name in args:
#         persons[name] = kwargs[name[0]]
#     result = sorted(persons.items(), key=lambda x: x[0])
#     final_result = []
#     for name, age in result:
#         final_result.append(f"{name} is {age} years old.")
#     return "\n".join(final_result)


def age_assignment(*args, **kwargs):
    result = ""
    for name in args:
        for key in kwargs:
            if name[0] == key:
                # kwargs[name] = kwargs.pop(key)
                kwargs[name] = kwargs[key]
                del kwargs[key]
                break
    for name, age in sorted(kwargs.items(), key=lambda x: x[0]):
        result += f"{name} is {age} years old.\n"
    return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
