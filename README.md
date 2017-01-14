# jinjaninja

Validate your Jinja templates for common mistakes or bad coding style

## Installing
```
pip install jinjaninja
```

## Usage

Validate a single template file (template.jinja)

```jinja
{% block content %}
<h1>{{title}}</h2>
    <p>Welcome to {% if package == 'jinjaninja'%}{{ package }}{%endif%}</p>
    {% block disclaimer %}
        <div class="disclaimer">
        {%  if disclaimer  %}
            {{ disclaimer_text  }}
        {%endif %}
        </div>
    {% endblock disclaimer %}
{% endblock %}
```

```sh
$ jinja-ninja template.jinja

>> template.jinja:1:4 Tags should have one (and only one) space {{title}
>> template.jinja:2:18 Tags should have one (and only one) space {% if package == 'jinjaninja'%}{{ package }}{%endif%}
>> template.jinja:5:8 Tags should have one (and only one) space {%  if disclaimer  %}
>> template.jinja:6:12 Tags should have one (and only one) space {{ disclaimer_text  }}
>> template.jinja:7:8 Tags should have one (and only one) space {%endif %}
>> template.jinja:10:0 Block closures should also have names {% endblock %}
```

You can also validate a list of files with `jinja-ninja template1.jinja template2.jinja template3.jinja ..`
