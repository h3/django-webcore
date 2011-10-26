from django.conf import settings

THEME = getattr(settings, 'JQUERYMOBILE_THEME', 'a')

def jquerymobile_theme(request):
    return {
        'jquerymobile_theme': THEME,
    }
