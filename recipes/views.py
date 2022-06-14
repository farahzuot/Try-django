from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect , get_object_or_404
from django.forms.models import modelformset_factory # model form for queryset.
from .models import Recipe, RecipeIngredient
from .forms import RecipeForm , RecipeIngredientForm
# Create your views here.
# CRUD -> Create, Retrieve, Update, Delete.
# FBV (Function based view) this may have much redundant code. -> CBS (Class based view)

@login_required
def recipe_list_view(request):
    qs = Recipe.objects.filter(user=request.user)
    context = {
        'object_list' : qs,
    }
    return render(request, 'recipes/list.html' , context=context)

@login_required
def recipe_detail_view(request,id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    context = {
        'object' : obj,
    }
    return render(request, 'recipes/detail.html' , context=context)

@login_required
def recipe_create_view(request):
    form = RecipeForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        # commit = false, means do not save the data to DB.
        obj = form.save(commit=False)
        obj.user = request.user #since we have @login_required
        obj.save()
        return redirect(obj.get_absolute_url())

    return render(request, 'recipes/create-update.html' , context=context)



@login_required
def recipe_update_view(request,id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    form = RecipeForm(request.POST or None, instance=obj)
    form_2 = RecipeIngredientForm(request.POST or None)
    # formset = modelformset_factory(model, form=ModelForm , extra=0)
    RecipeIngredientFormset = modelformset_factory(RecipeIngredient, form=RecipeIngredientForm
     , extra=0)
    qs = obj.recipeingredient_set.all()
    formset = RecipeIngredientFormset(request.POST or None, queryset=qs)
    context = {
        'form': form,
        'formset' : formset,
        'object': obj,
    }
    if all([form.is_valid() , formset.is_valid()]):
        # if the forms were'nt associated (do not have inner relation), then only make commit = true and this will save the data.
        parent = form.save(commit=False)
        parent.save()
        for form in formset:
            child = form.save(commit=False)
            if child.recipe is None:
                child.recipe = parent
            child.save()
        context['message'] = 'Data saved.'

    return render(request, 'recipes/create-update.html' , context=context)



