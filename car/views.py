from django.shortcuts import render, redirect
from django.views.generic import DetailView, TemplateView
from .models import Car, Order
from .forms import CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.


class CarDetails(DetailView):
    template_name = "car_details.html"
    pk_url_kwarg = "id"
    model = Car

    def post(self, request, *args, **kwargs):
        form = CommentForm(self.request.POST)
        car = self.get_object()
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        car = self.object
        comments = car.comments.all()
        form = CommentForm()
        context["comments"] = comments
        context["form"] = form
        return context


@login_required()
def orderCar(request, id):
    car = Car.objects.get(pk=id)
    if car.quantity > 0:
        car.quantity -= 1
        car.save()
        order = Order(user=request.user, car=car)
        order.save()
        messages.success(request, "You Have Successfully Buy The Car!")
    else:
        messages.warning(request, "This Car Is Stock Out!")
    return redirect("profile")
