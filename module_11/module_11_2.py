import inspect


def introspection_info(obj) -> str:
    res = ""

    name = obj
    res += f"Объект исследования: {name}\n"

    cls = obj.__class__.__name__
    res += f"Тип: {cls}\n"

    if hasattr(obj, "__module__"):
        module = obj.__module__
    else:
        module = ""
    res += f"Модуль: {module}\n"

    res += f'{" атрибуты ":-^80}\n'
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    if attributes:
        for attr in attributes:
            res += f"{attr}:{getattr(obj,attr).__class__.__name__}\n"
    res += f'{" методы ":-^80}\n'
    methods = [attr for attr in dir(obj) if callable(getattr(obj, attr))]
    if methods:
        for method in methods:
            res += f"{method}()\n"

    return res


def introspection_info_2(obj) -> str:
    res = ""

    name = obj
    res += f"Объект исследования: {name}\n"

    cls = obj.__class__.__name__
    res += f"Тип: {cls}\n"

    module = inspect.getmodule(obj).__name__
    res += f"Модуль: {module}\n"

    res += f'{" атрибуты ":-^80}\n'
    attributes = inspect.getmembers(obj, lambda x: not callable(x))
    for attr, value in attributes:
        res += f"{attr}:{getattr(obj, attr).__class__.__name__}\n"

    res += f'{" методы ":-^80}\n'
    methods = inspect.getmembers(obj, lambda x: callable(x))
    if methods:
        for method, ref in methods:
            res += f"{method}()\n"
    return res


if __name__ == "__main__":

    class Example:
        class_attr = 42
        class_method = introspection_info

        def __init__(self):
            self._private_attr = 24
            self.public_attr = "123"

        def show(self):
            print("hi")

    ex = Example()
    print(introspection_info(Example))
    print()
    print(introspection_info(ex))
    print()
    print(introspection_info(introspection_info))
    print()
    print(introspection_info(Example.class_method))
    print()
    print(introspection_info(Example.class_attr))
    print()

    print(introspection_info_2(Example))
    print()
    print(introspection_info_2(ex))
    print()
