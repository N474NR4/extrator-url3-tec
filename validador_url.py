import re

url = "alura.com"
padrao_url = re.compile('(http(s)?://)?(www.)?alura.com(.br)?')
match = padrao_url.match(url)

if not match:
    raise ValueError("A URL não é válida.")

print("A URL é válida")














