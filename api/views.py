from django.db import connection
from django.http import JsonResponse
from django.views import View

class Health(View):
    def get(self, request):
        return JsonResponse({'status': 'ok'})

class Ready(View):
    def get(self, request):
        try:
            with connection.cursor() as cursor:
                cursor.execute('SELECT 1')
            return JsonResponse({'status': 'ready', 'database': 'ready'})
        except:
            return JsonResponse({'status': 'not okay', 'database': 'not ready'})


# 5
