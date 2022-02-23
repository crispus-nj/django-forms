from django.shortcuts import render
from .forms import PizzaForm, MultiplePizzForm
from django.forms import formset_factory
from .models import Pizza


def homepage(request):
    return render(request, 'pizza/home.html')

def order(request):
    multi_form = MultiplePizzForm()
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        # print(filled_form)
        # , request.FILES
        if filled_form.is_valid():
            created_pizza_pk = filled_form.save()
            pizza_pk = created_pizza_pk.id
            note = f'Thanks for ordering! Your order %s , %s and %s pizza is on its ways!' %(filled_form.cleaned_data['size'], 
                                                                                            (filled_form.cleaned_data['topping1']), 
                                                                                            (filled_form.cleaned_data['topping2']))
            new_form = PizzaForm()
            return render(request, 'pizza/order.html', {'pizza_pk': pizza_pk,'pizzaform': new_form, 'note': note, 'multi_form': multi_form })
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'pizzaform': form , 'multi_form': multi_form})

def pizzas(request):
    number_of_pizza= 2
    multi_form = MultiplePizzForm(request.GET)
    if multi_form.is_valid():
        number_of_pizza = multi_form.cleaned_data['number']
        # print('number of pizza', number_of_pizza)
    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizza)
    # print("PizzaformSet:  ", PizzaFormSet)
    formSet = PizzaFormSet()
    # print("formSet", formSet)
    if request.method == 'POST':
        filled_formset= PizzaFormSet(request.POST)
        print(filled_formset)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data['topping1'])
            note = 'Pizza have Been Ordered!'
        else :
            note = 'Order was not created! Please try again!'
        return render(request, 'pizza/pizzas.html', {'note':note, 'formSet': formSet})
    else: 
        return render(request, 'pizza/pizzas.html', {'formSet': formSet})
    


def edit_order(request, pk):
    pizza = Pizza.objects.get(pk=pk)
    form = PizzaForm(instance=pizza)
    print(form)

    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = 'Order has been updated successfully!'
            return render(request, 'pizza/edit_order.html', {'form': form, 'pizza': pizza, 'note':note})

    return render(request, 'pizza/edit_order.html', {'form': form, 'pizza': pizza})




