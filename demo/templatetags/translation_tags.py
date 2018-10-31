from django import forms, template
import copy
from django.conf import settings

register = template.Library()

@register.simple_tag(takes_context=True)
def include_trans(context, template_name):
    lang = context.get('lang') or settings.LANGUAGE_CODE
    request = getattr(context, 'request', None)
    if request:
        lang = request.COOKIES.get('sdlLanguage') or settings.LANGUAGE_CODE
        
    try:
        base, ext = template_name.rsplit('.', 1)
    except ValueError:
        base = template_name
        ext = ''
    requested = u'%s.%s.%s' % (base, lang, ext)
    default = u'%s.%s.%s' % (base, settings.LANGUAGE_CODE, ext)
    requested = requested.rstrip('.')
    default = default.rstrip('.')

    t = template.loader.select_template([requested, default, template_name])
    c2 = copy.copy(context)
    c2.update({'lang': lang})
    return t.render(c2)
