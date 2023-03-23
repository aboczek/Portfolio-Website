from django.conf import settings


def context(request):
    debug_flag = settings.DEBUG
    return {"debug_flag":debug_flag}
