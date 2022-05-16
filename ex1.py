from jinja2 import Template

name = "Test"
age = 28

tm = Template("Hello my name is {{ n }}, i'm {{ a }}")

msg = tm.render(n=name, a=age)

print(msg)
