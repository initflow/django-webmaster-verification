from .models import VerificationCode

WEBMASTER_VERIFICATION = {
    'bing': VerificationCode.objects.filter(engine='google').values_list('code', flat=True).first(),
    'google': VerificationCode.objects.filter(engine='google').values_list('code', flat=True),
    'majestic': VerificationCode.objects.filter(engine='majestic').values_list('code', flat=True),
    'yandex': VerificationCode.objects.filter(engine='yandex').values_list('code', flat=True),
    'alexa': VerificationCode.objects.filter(engine='alexa').values_list('code', flat=True),
}
