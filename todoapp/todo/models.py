from django.contrib.auth.models import User
from django.db import models


class Tasks(models.Model):
    task = models.CharField(max_length=50, verbose_name='Задача')
    description = models.TextField(verbose_name='Описание задачи')
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey('Status', on_delete=models.PROTECT, verbose_name='Статус', null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', null=False)

    def __str__(self):
        return self.task

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Status(models.Model):
    name_status = models.CharField(max_length=55, db_index=True)

    def __str__(self):
        return self.name_status
