# task 2
ages = [2, 12, 12, 14, 15, 16, 16, 17, 18, 14, 20, 20]
ages1 = [2, 4, 12, 14, 15, 16, 16, 17, 18, 14, 20, 20]


def common_data(ages, ages1):
    for x in ages:
        for y in ages1:
            if x == y:
             return "true"
        else:
             return "false"
print(common_data(ages, ages1))


