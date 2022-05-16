from jinja2 import Template

cars = [
    {'model': 'Audi', 'price': 23000},
    {'model': 'Skoda', 'price': 17300},
    {'model': 'Volvo', 'price': 44300},
    {'model': 'Volkswagen', 'price': 21300},
]

tpl = "Суммарная цена автомобилей {{ cs | sum(attribute='price') }}"
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tpl = "Суммарная цена автомобилей {{ cs | sum }}"
tm = Template(tpl)
msg = tm.render(cs=digits)
print(msg)

tpl = "Максимальная цена автомобиля {{cs | max(attribute='price')}}"
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)

persons = [
    {'name': 'Name1', 'old': 18, 'weight': 78.5},
    {'name': 'Name2', 'old': 28, 'weight': 82.3},
    {'name': 'Name3', 'old': 38, 'weight': 64.1},
    {'name': 'Name4', 'old': 48, 'weight': 77.6},
]

tpl = '''
{%- for u in users -%}
{% filter upper %} {{u.name}} {% endfilter %}
{% endfor -%}
'''

tm = Template(tpl)
msg = tm.render(users=persons)
print(msg)

html = '''
{%- macro input(name, value='', type='text', size=20) -%}
    <input type="{{ type }}" name="{{ name }}" value="{{value | e}}" size="{{ size }}">
{%- endmacro %}

<p> {{ input('username')}}
<p> {{ input('email')}}
<p> {{ input('password')}}
'''

tm = Template(html)
msg = tm.render()
print(msg)


html = '''
{% macro list_users(list_of_users) -%}
    <ul>
    {% for u in list_of_users -%}
        <li>{{u.name}} {{caller(u)}}
    {%- endfor %}
    </ul>
{%- endmacro %}

{% call(user) list_users(users) %}
    <ul>
    <li>age: {{user.old}}
    <li>weight: {{user.weight}}
    </ul>
{% endcall -%}
'''

tm = Template(html)
msg = tm.render(users=persons)
print(msg)
