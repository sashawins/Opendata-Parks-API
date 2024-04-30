from django.shortcuts import render
from parks_app.models import Park
import json


def get_parks(request):
    all_parks = None
    if 'name' in request.GET:
        name = request.GET['name']
        result = Park.objects.filter(name__icontains=name).order_by('-id')
        all_parks = []

        for park in result:
            park_data = {
                'name': park.name,
                'category': park.category,
                'description': park.description,
                'location': park.location,
                'id': park.id,
                'image': json.loads(park.image),
            }
            all_parks.append(park_data)

    return render (request, 'parks/park.html', { "all_parks": all_parks})


def park_detail(request, id):
    park = Park.objects.get(id=id)
    park.image = json.loads(park.image)
    print(park)
    return render(request, 'parks/park_detail.html', {'park': park})
