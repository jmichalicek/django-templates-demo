from django.views.generic import TemplateView
import os

class TranslateViaIncludes(TemplateView):
    """
    A temporary placeholder view to redirect to after login until we have the correct view.
    """
    template_name = 'via_includes/index.html'


class TranslateViaInheritance(TemplateView):
    """
    A temporary placeholder view to redirect to after login until we have the correct view.
    """
    template_name = 'via_inheritance/index.html'

    def get_template_names(self):
        """
        This uses the cookie to determine the name of the template for the user's selected language.  It passes an english translation
        as a fallback to that, and then further falls back to the base template_name in case this page is not translated at all.
        """
        lang = self.request.COOKIES.get('sdlLanguage') or 'en'
        base, ext = self.template_name.split('.')
        requested = u'%s.%s.%s' % (base, lang, ext)
        default = u'%s.en.%s' % (base, ext)

        return [requested, default, self.template_name]


class TranslateViaTemplateTag(TemplateView):
    """
    A temporary placeholder view to redirect to after login until we have the correct view.
    """
    template_name = 'via_template_tag/index.html'