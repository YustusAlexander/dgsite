from shop.models import Category

menu = [{'title': 'Home', 'url_name': 'home'},
        {'title': 'Recipes', 'url_name': 'recipes'},
        {'title': 'About', 'url_name': 'about'},
        {'title': 'Addpage', 'url_name': 'addpage'},
        {'title': 'Login', 'url_name': 'login'},
        ]

class DataMixin:
        def get_user_context(self, **kwargs):
                context = kwargs
                cats = Category.objects.all()
                context['menu'] = menu
                context['title'] = menu[0]['title']
                if 'cat_selected' not in context:
                        context['cat_selected'] = 0
                return context