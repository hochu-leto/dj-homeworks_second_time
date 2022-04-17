from django.urls import path

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', MeasureView.as_view()),  # подключаем маршруты из приложения measurement

]
