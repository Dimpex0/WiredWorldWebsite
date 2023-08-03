from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views import generic as views

from WiredWorldProject.account.models import Profile
from WiredWorldProject.like.models import Like


@login_required
def like_product(request, pk):
    profile = Profile.objects.get(client=request.user)
    Like.objects.create(profile=profile, product_id=pk)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def unlike_product(request, pk):
    profile = Profile.objects.get(client=request.user)
    like = Like.objects.filter(profile=profile, product_id=pk)
    if like.exists():
        like.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class LikeListView(LoginRequiredMixin, views.ListView):
    model = Like
    template_name = 'like/index.html'
