from django.http import JsonResponse
from .models import CurrencyRequest
from .services import get_currency_data
from datetime import datetime, timedelta, timezone


def get_current_usd(request):
    """
    Получает текущий курс доллара к рублю и возвращает его в формате JSON,
    а также показывает 10 последних запросов.
    """
    # Проверяем, когда был сделан последний запрос
    last_request_time = CurrencyRequest.objects.last().time if CurrencyRequest.objects.exists() else None

    if last_request_time and datetime.now(timezone.utc) - last_request_time < timedelta(seconds=10):
        # Если с последнего запроса прошло менее 10 секунд
        rate = CurrencyRequest.objects.last().rate
    else:
        # Получаем актуальный курс через ЦБ РФ
        rate = get_currency_data('USD')

        # Сохраняем запрос в базу данных
        CurrencyRequest.objects.create(rate=float(rate))

    # Получаем 10 последних запросов
    last_requests = CurrencyRequest.objects.order_by('-time')[:10].values('time', 'rate')

    # Форматирование данных для ответа
    last_requests_formatted = [
        {
            'time': request_obj['time'].strftime('%Y-%m-%d %H:%M:%S'),
            'rate': request_obj['rate']
        }
        for request_obj in last_requests
    ]

    response_data = {
        'current_rate': float(rate),
        'last_requests': last_requests_formatted
    }

    return JsonResponse(response_data, json_dumps_params={'indent': 2})