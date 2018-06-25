from django.shortcuts import render

def home_page(request):

	if request.method == 'POST':
		Item = request.POST.get('item')
		address = request.POST.get("address")

		return render(request,'haircut/home_page.html',{'item': item,'address':address})

		return render(request,'haircut/home_page.html')