import re

'''
Invalid space between tags: { {, { %, } }, ..

Invalid code style:
    - {{something}}
    - {{ something}}, {% something%}`
    - {{something }}, {%something %}`
    - {{  something  }}, {%  something  %}, {{   something   }}, ..
    - {{ something  }}, {% something  %}, {{ something   }}, ..
    - {{  something }}, {%  something %}, {{   something }}, ..

Invalid block closure: {% endblock %} (requires the block name)
'''
EXPRESSIONS = (
    ('Brackets should not have any spaces in-between',
        r'\{\s+(\{|%)|(\}|%)\s+\}'),
    ('Tags should have one (and only one) space',
        (r'\{(\{|%)\w+(.+\w+)?(\}|%)\}|'
         r'\{(\{|%)\s+\w+(.+\w+)?(\}|%)\}|'
         r'\{(\{|%)\w+(.+\w+)?\s+(\}|%)\}|'
         r'{(\{|%)\s{2,}\w+(.+\w+)?\s{2,}(\}|%)\}|'
         r'{(\{|%)\s+\w+(.+\w+)?\s{2,}(\}|%)\}|'
         r'{(\{|%)\s{2,}\w+(.+\w+)?\s+(\}|%)\}')),
    ('Block closures should also have names',
        r'\{% endblock %\}'),
)

class ValidationError(object):
    '''Stores the information of a validation error'''

    def __init__(self, filename, line, position, message, code):
        self.filename = filename
        self.line = line
        self.position = position
        self.message = message
        self.code = code

    def __repr__(self):
        return '{}:{}:{} {} `{}`'.format(
            self.filename, self.line, self.position[0], self.message, self.code)

def validate_line(filename, line, line_n):
    '''
    Returns a list of validation errors in the current line.
    The line is tested against all EXPRESSIONS defined
    '''
    line_errors = []
    for expr in EXPRESSIONS:
        for result in re.finditer(expr[1], line):
            error = ValidationError(
                filename, line_n, result.span(), expr[0], result.group())
            line_errors.append(error)
    return line_errors

def validate_template(filename):
    '''Returns a list of validation errors in the template file'''
    template_errors = []

    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            template_errors += validate_line(filename, line, i)

    return template_errors
