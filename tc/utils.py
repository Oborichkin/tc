import re

def to_camel(text: str) -> str:
    s = text.replace("-", " ").replace("_", " ")
    s = s.split()
    if len(text) == 0:
        return text
    return s[0] + "".join(i.capitalize() for i in s[1:])


pattern = re.compile(r'(?<!^)(?=[A-Z])')
def to_snake(text: str) -> str:
    return pattern.sub('_', text).lower()
