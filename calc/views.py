from django.shortcuts import render
from django.views import View

# Create your views here.


class HomeView(View):
    def get(self, request):

        context = {
            'message': "hi there. ",
        }
        return render(request, 'calc/home.html', context)