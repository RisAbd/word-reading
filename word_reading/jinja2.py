

from jinja2 import Environment

from django.template.backends.jinja2 import Jinja2 as _Jinja2

from django.templatetags.static import static
from django.urls import reverse
from django.utils import timezone


def environment(**options) -> Environment:
    env = Environment(**options)
    env.filters.update()
    env.globals.update(
        static=static,
        url=reverse,
        now=timezone.now,
        min=min,
        max=max,
    )
    return env


class Jinja2(_Jinja2):
    app_dirname = 'jinja2_templates'
