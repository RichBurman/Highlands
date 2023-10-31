from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import CustomUser, UserProfile
from .forms import UserProfileForm
from allauth.account.views import PasswordChangeView
from allauth.account.forms import SignupForm
from django.contrib import messages


@login_required
def user_profile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your Profile has been updated successfully')
            return redirect('user:profile')
        else:
            messages.error(request, 'Profile update has failed. Please correct the errors below.')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'user/user_profile.html', {'user': user, 'form': form})


class MyPasswordChangeView(PasswordChangeView):
    success_url = '/user/profile/'


def edit_profile(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save(request)
            messages.success(request, 'Your Profile has been updated successfully')
            return redirect('user:profile')
        else:
            messages.error(request, 'Profile update has failed. Please correct the errors below.')
    else:
        form = SignupForm(instance=request.user)

    return render(request, 'user/edit_profile.html', {'form': form})