from django.shortcuts import render

# Create your views here.

def home(request):
   variables = {
       "var1" : None,
       "var2" : None,
       "var3" : "cazzcode"
    }

   return render(request, 'home.html', variables)

#Escenario C
"""def home(request):
   variables = {
       "var1" : None,
       "var2" : None,
       "var3" : "cazzcode"
    }

   return render(request, 'home.html', context={'variables':variables})"""