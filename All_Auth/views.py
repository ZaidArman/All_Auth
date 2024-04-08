# views.py
from allauth.socialaccount.models import SocialAccount

def apple_login_callback(request):
    # Extract user data from the request, such as email, name, etc.
    # You can use the SocialAccount model to access the user's Apple account data
    social_account = SocialAccount.objects.get(provider='apple', user=request.user)
    apple_email = social_account.extra_data['email']
    # Perform any necessary actions and redirect the user to a specific URL
    return redirect('home')