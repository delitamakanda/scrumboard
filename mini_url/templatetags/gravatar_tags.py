import hashlib
from django import template

try:
    # Python 3
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

register = template.Library()


@register.filter
def gravatar(email, size="75"):
    """
    {% load gravatar_tags %}
    {{ request.user.email|gravatar:"75" }}
    """
    gravatar_url = "//www.gravatar.com/avatar/" + \
        hashlib.md5(email.encode('utf-8')).hexdigest() + "?"
    gravatar_url += urlencode({'d': 'retro', 's': str(size)})
    return gravatar_url
