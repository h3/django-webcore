from django.conf import settings

def get_real_ip(request):
    try:
        return request.META['HTTP_X_FORWARDED_FOR'].split(",")[0]
    except KeyError:
        return request.META['REMOTE_ADDR']

def get_captcha_args(request, challenge_field='recaptcha_challenge_field', response_field='recaptcha_response_field'):
    return [
        request.POST[challenge_field],
        request.POST[response_field],
        settings.RECAPTCHA_PRIVATE_KEY,
        get_real_ip(request),
        ]
