from __future__ import unicode_literals, absolute_import
from django.conf import settings


def get_language(request):
    lang = request.COOKIES.get('sdlLanguage') or settings.LANGUAGE_CODE
    return {
        'lang': lang
    }
