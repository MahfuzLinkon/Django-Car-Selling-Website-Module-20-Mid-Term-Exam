from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, UpdateView
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from brand.models import Brand
from car.models import Car, Order


def home(request, brand_slug=None):
    brands = Brand.objects.all()
    if brand_slug:
        brand = Brand.objects.get(slug=brand_slug)
        cars = Car.objects.filter(brand=brand)
    else:
        cars = Car.objects.all()
    return render(request, "home.html", {"brands": brands, "cars": cars})


class UserRegisterView(CreateView):
    template_name = "auth.html"
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("login")

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Register"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Account Created Successfully, Login Now !")
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = "auth.html"

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self) -> str:
        return reverse_lazy("profile")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Login"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Logged In Successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, "Invalid Username Or Password!")
        return super().form_invalid(form)


@method_decorator(login_required, name="dispatch")
class UserProfileView(TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        o = Order.objects.filter(user=self.request.user)
        context["orders"] = Order.objects.filter(user=self.request.user)
        return context


def updateProfile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Updated Successfully")
        return redirect("update-profile")
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, "profile_update.html", {"form": form})


class UserChangePassword(PasswordChangeView):
    template_name = "auth.html"
    success_url = reverse_lazy("profile")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Change Password"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Password Changed Successfully!")
        return super().form_valid(form)
