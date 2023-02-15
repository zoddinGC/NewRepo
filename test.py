"""
    Docstring
"""


def bold(func):
    def wrapper():
        text_b = "<b>" + func() + "</b> "
        text_b += "\033[1;32mWOW!\033[m"
        return text_b
    return wrapper


@bold
def formatted_text():
    text = "That is a function "
    text += "and it has Hello World!"
    return text


def not_formatted_text():
    return "Hello World?!?"


print(formatted_text())
print(not_formatted_text())
