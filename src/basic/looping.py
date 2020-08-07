def count_to_10():
    for i in range(1, 11):
        print(i)


def loop_a_list(lista):
    for item in lista:
        print(item)


def loop_a_dictionary(dictionary):
    for key in dictionary:
        print("Este es el key:", key, "Este es el value:", dictionary[key])


def loop_strings(word):
    for letter in word:
        print(letter)


def string_operations(word):
    print(word[:5])
    print(word[:len(word)])
    print(word[5:])
    print(word[3:5])


def compare_strings(a, b, c):
    # if a in b:
    #     return f"{a} is contained in {b}"
    # else:
    #     return f"{a} is not contained in {b}"

    # if a is b:
    #     return f"{a} is contained in {b}"
    # else:
    #     return f"{a} is not contained in {b}"

    # if a in b and c == "leo":
    #     return True
    # else:
    #     return False

    if (a in b) or (c == "leo"):
        return True
    else:
        return False


def string_to_list_comparison(a, list):
    if a in list:
        return True
    else:
        return False


if __name__ == '__main__':
    # loop_a_list(['leo', 'mari', 'daniel'])
    # loop_a_dictionary({'name': 'leo'}
    # loop_strings("daniel")
    # string_operations("greenday")
    print(compare_strings("x", "y", "leo"))
    # print(string_to_list_comparison("daniel", ['leo', 'daniela', 'marinel']))
