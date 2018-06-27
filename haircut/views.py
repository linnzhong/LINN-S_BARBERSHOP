from django.shortcuts import render 


def home_page(request): 

    if request.method == 'POST':
        time = request.POST.get('time')   
        bn =request.POST.get("barber_name")
        cn =request.POST.get("customer_name")
        context = {'time': time, 'customer_name': cn, 'barber_name': bn}
        return render(request, 'haircut/home_page.html', context)
    
    return render(request, 'haircut/home_page.html') 