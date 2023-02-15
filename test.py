"""
    Docstring
"""


def bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper


@bold
def formatted_text():
    return "Hello world!"


def not_formatted_text():
    return "Hello World?!?"


print(formatted_text())
print(not_formatted_text())
