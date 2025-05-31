from django.http import HttpResponseForbidden

def user_is_self_or_admin(view_func):
    def wrapper(request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        if request.user.is_superuser or request.user.id == user_id:
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("دسترسی غیرمجاز")
    return wrapper
