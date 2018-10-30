from django import forms, template
import copy

register = template.Library()

@register.simple_tag(takes_context=True)
def include_trans(context, template_name):
    request = getattr(context, 'request', None)
    if request:
        lang = request.COOKIES.get('sdlLanguage') or 'en'
    else:
        lang = 'en'

    try:
        base, ext = template_name.split('.')
    except ValueError:
        base = template_name
        ext = ''
    requested = u'%s.%s.%s' % (base, lang, ext)
    default = u'%s.en.%s' % (base, ext)
    requested = requested.rstrip('.')
    default = default.rstrip('.')

    t = template.loader.select_template([requested, default, template_name])
    c2 = copy.copy(context)
    c2.update({'lang': lang})
    return t.render(c2)
