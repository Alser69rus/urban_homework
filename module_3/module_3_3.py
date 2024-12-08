def print_params(a=1, b="строка", c=True):
    print(a, b, c)


print("default params are: a=1, b='строка',c=True")
print("no params: ", end="")
print_params()
print("first positional param 10: ", end="")
print_params(10)
print("named param b=25: ", end="")
print_params(b=25)
print("list param c=[1,2,3]: ", end="")
print_params(c=[1, 2, 3])
print("all params 100, 200, 300: ", end="")
print_params(100, 200, 300)

values_list = [3.14, [1, 2, 3], {"x": 0, "y": 1}]
values_dict = {"a": "a", "b": 0, "c": 2.71}
print("unpack list: ", end="")
print_params(*values_list)
print("unpack dict: ", end="")
print_params(**values_dict)
values_list_2 = ["a", 1984]
print("unpack only 2 params: ", end="")
print_params(*values_list_2, 42)
