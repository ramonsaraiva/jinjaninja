# jinjaninja

Validate your Jinja templates for common mistakes or bad coding style

## Installing
```sh
pip install jinjaninja
```

## Usage

### Validate a single template file

```jinja
{% block content %}
<h1>{{title}}</h1>
    <p>Welcome to {% if package == 'jinjaninja'%}{{ package }}{%endif%}</p>
    {% block disclaimer % }
        <div class="disclaimer">
        {%  if disclaimer  %}
            { { disclaimer_text }}
        {%endif %}
        </div>
    {% endblock disclaimer %}
{% endblock %}
```

```sh
$ jinja-ninja template.jinja

>> template.jinja:2:5 Tags should have one (and only one) space `{{title}}`
>> template.jinja:3:19 Tags should have one (and only one) space `{% if package == 'jinjaninja'%}{{ package }}{%endif%}`
>> template.jinja:4:25 Brackets should not have any spaces in-between `% }`
>> template.jinja:6:9 Tags should have one (and only one) space `{%  if disclaimer  %}`
>> template.jinja:7:13 Brackets should not have any spaces in-between `{ {`
>> template.jinja:8:9 Tags should have one (and only one) space `{%endif %}`
>> template.jinja:11:1 Block closures should also have names `{% endblock %}`
```

### Validate a list of files

`jinja-ninja template1.jinja template2.jinja template3.jinja ..`

### Validate specific directories

`jinja-ninja templates`

### Validate everything

`jinja-ninja *`
