from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import product
from django.utils import timezone


# Create your views here.
def main(request):
    return render(request, "index.html")

@login_required
def create(request):
    if request.method == 'POST':
        # Check if all the data has been entered
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['image'] and request.FILES['icon']:
            item = product()
            # Add stuff to database
            item.title = request.POST['title']
            item.body = request.POST['body']

            # check if URL has http:// in it or not
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                # url is okay as it contains http:// or htttp://
                # We can add it to the database
                item.url = request.POST['url']
            else:
                # First append http:// at the begining of the url
                item.url = 'http://' + request.POST['url']
            # url check over

            item.icon = request.FILES['icon']
            item.image = request.FILES['image']
            item.pub_date = timezone.datetime.now()

            item.hunter = request.user

            item.save()
            return redirect('/product/'+ str(item.id))

        else:
            return render(request, 'create.html', {'error': 'One or more Fields of the form are empty'})

    else:
        return render(request, 'create.html')

def details(request, product_id):
    item = get_object_or_404(product, pk=product_id)
    print(item.title)
    return render(request, 'details.html', {'item' : item})
