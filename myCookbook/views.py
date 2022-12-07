from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views import View
from .models import User, Recipe, Category
from .forms import UserForm, RecipeForm
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib import messages
from itertools import zip_longest
import random

def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return list(zip_longest(fillvalue=fillvalue, *args))

def index(request):
    allRecipes = list(Recipe.objects.all())
    randomRecipes = random.sample(allRecipes,3)
    return render(request, "myCookbook/index.html", {'recipes':randomRecipes})


class addRecipe(View):
    def get(self, request):
        recipeForm = RecipeForm
        return render(request, "myCookbook/addRecipe.html", {"form": recipeForm})

    def post(self, request):
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            newRecipe = form.save(commit=False)
            newRecipe.author = request.user
            instructions = request.POST.getlist('instructions')
            ingredients = request.POST.getlist('ingredients')
            ingredients = grouper(3,ingredients)
            newRecipe.instructions = instructions
            newRecipe.ingredients = ingredients
            newRecipe.save()
            form.save_m2m()
        
        messages.success(request, f'Recipe posted!')
        return render(request, 'myCookbook/index.html', {"form":form})

class FilteredListView(ListView):
    filterset_class = None
    
class CategoryView(ListView):
    model = Recipe
    template_name = 'myCookbook/allRecipes.html'
    context_object_name = 'recipes'
    paginate_by = 9

    def get_queryset(self, *args, **kwargs):
        return Recipe.objects.filter(categories__name__icontains = self.kwargs.get('category'))

class RecipeListView(ListView):
    model = Recipe
    template_name = 'myCookbook/allRecipes.html'
    context_object_name = 'recipes'
    paginate_by = 9
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(name__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all().order_by('name')
        return context

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'myCookbook/allRecipes.html'

def contactUs(request):
    return render(request, "myCookbook/contactUs.html")

def signUp(request):
    userForm = UserForm
    return render(request, "myCookbook/signUp.html", {"form": userForm})


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        bio = request.POST["bio"]
        theme = request.POST["theme"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "myCookbook/signUp.html", {'form': UserForm,
                                                              "message": "Passwords must match."
                                                              })

        # Attempt to create new user
        try:
            user = User.objects.create_user(
                username=username, email=email, password=password, theme=theme, bio=bio)
            user.save()
        except IntegrityError:
            return render(request, "myCookbook/signUp.html", {'form': UserForm,
                                                              "message": "Username already taken."
                                                              })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "myCookbook/index.html")


def myCookbook(request):
    return render(request, "myCookbook/myCookbook.html")


def profile(request):
    currentUser = User.objects.get(username = request.user)
    recipes = Recipe.objects.filter(author=currentUser)
    numRecipes = len(recipes)
    User.objects.filter(username=request.user).update(num_recipes_posted=numRecipes)
    return render(request, "myCookbook/profile.html", {'user':currentUser, 'recipes':recipes})

class deleteRecipe(DeleteView):
    model = Recipe
    success_url = reverse_lazy('profile')
    template_name = 'myCookbook/profile.html'

class editRecipe(UpdateView):
    model = Recipe
    fields = ["name",'description','categories','num_servings','min','image']
    success_url = 'myCookbook/profile.html'

