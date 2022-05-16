from jinja2 import Template

data = '''Модуль Jinja вместо
определния {{name}}
продоставляет соответсвующее значкение'''

tm = Template(data)
msg = tm.render(name='Test')

print(msg)

data = '''{% raw %}Модуль Jinja вместо
определния {{name}}
продоставляет соответсвующее значкение{% endraw %}'''

tm = Template(data)
msg = tm.render(name='Test')

print(msg)

link = '''В HTML-документе ссылки определяются так:
<a href="#">Ссылка</a>'''

tm = Template("{{ link | e}}")
msg = tm.render(link=link)
print(msg)

cities = [{'id': 1, 'city': 'City1'},
          {'id': 5, 'city': 'City2'},
          {'id': 7, 'city': 'City3'},
          {'id': 8, 'city': 'City4'},
          {'id': 11, 'city': 'City5'}]

link = '''<select name="cities">
{% for c in cities -%}
{% if c.id > 6 -%}
    <option value="{{ c['id'] }}">{{ c['city'] }}</option>
{%elif c.city == "City1" -%}
    <option>{{c['city']}}</option>
{%else -%}
    {{c['city']}}
{% endif -%}
{% endfor -%}
</select>'''

tm = Template(link)

msg = tm.render(cities=cities)

print(msg)


