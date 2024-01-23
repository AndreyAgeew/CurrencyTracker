from django.db import models


class CurrencyRequest(models.Model):
    """
    Модель для хранения информации о запросах курса валют.
    """
    time = models.DateTimeField(auto_now_add=True)
    rate = models.FloatField()

    def __str__(self):
        """
        Строковое представление модели.
        """
        return f"{self.time} - {self.rate}"
