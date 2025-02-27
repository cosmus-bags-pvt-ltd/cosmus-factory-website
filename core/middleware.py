from django.shortcuts import redirect
from django.conf import settings
from django.urls import reverse

# from django.shortcuts import redirect
# from django.http import HttpResponseForbidden

# class PermissionMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # Redirect unauthorized users
#         if request.user.is_authenticated and not request.user.has_perm("finance.can_view_ledger"):
#             return HttpResponseForbidden("Access Denied")

#         return self.get_response(request)



class LoginRequiredMiddleware:
    """
    Middleware to enforce login for all views except login page and allowed URLs.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_urls = [reverse('login')]  # Add more if needed
        
        if not request.user.is_authenticated and request.path not in allowed_urls:
            return redirect(f"{reverse('login')}?next={request.path}")

        return self.get_response(request)