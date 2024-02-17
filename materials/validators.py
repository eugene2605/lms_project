import re
from rest_framework.serializers import ValidationError


class LinkValidator:

    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value):
        text = dict(value).get(self.fields)
        if text:
            reg = re.findall('https?:\/\/\S+', text)
            links = [r for r in reg if 'youtube' not in r]
            if links:
                raise ValidationError('Размещать ссылки на сторонние образовательные платформы или личные сайты — нельзя!')
