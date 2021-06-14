from .models import Category

def categories(requests):
    return {
        'categories': Category.objects.all()
    }