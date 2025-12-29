from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import CookCreateForm, DishTypesSearchForm, DishSearchForm, CookSearchForm
from .models import Cook, Dish, DishType

def index(request):

    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()

    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_dish_types": num_dish_types,
    }

    return render(request, "kitchen/index.html", context)


class DishTypeListView(generic.ListView):
    model = DishType
    paginate_by = 5

    def get_context_data(
        self, *, object_list = ..., **kwargs
    ):
        context = super(DishTypeListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = DishTypesSearchForm(
            initial={"name": name}
        )

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("name")

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class DishTypeDetailView(generic.DetailView):
    model = DishType
    queryset = DishType.objects.prefetch_related("dishes")


class DishTypeCreateView(generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeUpdateView(generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeDeleteView(generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 5

    def get_context_data(
        self, *, object_list = ..., **kwargs
    ):
        context = super(DishListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = DishSearchForm(
            initial={"name": name}
        )

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("name")

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class DishDetailView(generic.DetailView):
    model = Dish
    queryset = Dish.objects.select_related("dish_type").prefetch_related("cooks")


class DishCreateView(generic.CreateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-list")


class DishUpdateView(generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-list")


class DishDeleteView(generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")


class CookListView(generic.ListView):
    model = Cook
    paginate_by = 5

    def get_context_data(
        self, *, object_list = ..., **kwargs
    ):
        context = super(CookListView, self).get_context_data(**kwargs)

        username = self.request.GET.get("username", "")

        context["search_form"] = CookSearchForm(
            initial={"username": username}
        )

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        username = self.request.GET.get("username")

        if username:
            queryset = queryset.filter(username__icontains=username)

        return queryset



class CookDetailView(generic.DetailView):
    model = Cook
    queryset = Cook.objects.prefetch_related("dishes")


class CookCreateView(generic.CreateView):
    model = Cook
    form_class = CookCreateForm
    success_url = reverse_lazy("kitchen:cook-list")


class CookUpdateView(generic.UpdateView):
    model = Cook
    form_class = CookCreateForm
    success_url = reverse_lazy("kitchen:cook-list")


class CookDeleteView(generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")
