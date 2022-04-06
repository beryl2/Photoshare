from django.shortcuts import render

category_images = [
    {
        "name": "pets",
        "images": [
            {
                "src":'https://media.istockphoto.com/photos/closeup-portrait-of-funny-ginger-cat-wearing-sunglasses-isolated-on-picture-id1188445864?k=20&m=1188445864&s=612x612&w=0&h=0vuJeOxJr8Lu3Q1VdT1z7t6HcM8Oj7EVJe3CexGnH_8=', 
                "pk":1,
                "category": "pets",
            },
        ]
    },
    {
        "name": "money",
        "images": [
            {
                "src":"https://www.investopedia.com/thmb/sfFOpKbj8TUyJkvfKarzAI8WV90=/2121x1414/filters:fill(auto,1)/GettyImages-1222040206-f0faae8379c54ff58961774f75be3065.jpg",
                "pk": 10,
                "category": "money",
            },
            {
                "src": "https://picsum.photos/400",
                "pk": 11,
                "category": "money"
            }
        ]
    },
    {
        "name": "books",
        "images": [
            {
                "src":"https://media.wired.com/photos/5be4cd03db23f3775e466767/master/pass/books-521812297.jpg",
                "pk": 20,
                "category": "books",
            },
        ]
    },
    {
        "name": "food",
        "images": [
            {
                "src": "https://picsum.photos/seed/food/300",
                "pk": 30,
                "category": "food"
            }
        ]
    },
    {
        "name":"nature",
        "images": [
            {
                "src":"https://thumbs.dreamstime.com/b/beautiful-rain-forest-ang-ka-nature-trail-doi-inthanon-national-park-thailand-36703721.jpg",
                "pk":40,
                "category":"nature"
            }
        ]
    }
]

# Create your views here.
def viewgallery(request):
    category = request.GET.get('category', 'all')

    categories = [cat['name'] for cat in category_images]
    images = []
    if category == 'all':
        # If user requests for all images
        for cat in category_images:
            images += cat['images']
    else:
        # if user requests for images from a specific category
        for cat in category_images:
            if cat['name'] == category:
                images = cat['images']
                break
    
    context = {
        "categories": categories,
        "images": images
    }
    return render(request, 'photos/gallery.html', context)


def viewphoto(request, pk):
    image =  None
    for category in category_images:
        for i  in category['images']:
            if i["pk"] == pk:
                image = i
                break
    
    context = { "image": image }
    return render(request, 'photos/photo.html', context)


def addphoto(request):
    return render(request, 'photos/add.html')
