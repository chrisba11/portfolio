from .views import hello_world


patterns = [
    path('', hello_world, name='hello_world'),
]
