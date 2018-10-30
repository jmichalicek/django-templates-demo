def get_language(request):
    lang = request.COOKIES.get('sdlLanguage') or 'en'
    return {
        'lang': lang
    }
