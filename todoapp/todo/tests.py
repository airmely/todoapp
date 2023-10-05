from django.test import TestCase
from django.urls import reverse

from .models import *


class TasksModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Status.objects.create(name_status='Завершена')
        user = User.objects.create_user(username='testUser', password='testPasswordUser')

        cls.task = Tasks.objects.create(
            task='Тестовое задание',
            description='Это тестовое задание',
            status=Status.objects.get(name_status='Завершена'),
            user=user,
        )

    def test_task_str_method(self):
        self.assertEqual(str(self.task), 'Тестовое задание')

    def test_task_verbose_names(self):
        self.assertEqual(self.task._meta.verbose_name, 'Задача')
        self.assertEqual(self.task._meta.verbose_name_plural, 'Задачи')

    def test_task_date_created_auto_now_add(self):
        self.assertIsNotNone(self.task.date_created)

    def test_task_user_relationship(self):
        self.assertEqual(self.task.user.username, 'testUser')


class DeleteTaskTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.status = Status.objects.create(name_status='Завершена')
        cls.user = User.objects.create_user(username='testUser', password='testPasswordUser')
        cls.task = Tasks.objects.create(
            task='Тестовый пользователь',
            description='Это тестовое задание',
            status=cls.status,
            user=cls.user,
        )

    def test_delete_task(self):
        self.client.login(username='testUser', password='testPasswordUser')

        delete_url = reverse('delete_task', args=[self.task.id])

        response = self.client.post(delete_url)

        self.assertEqual(response.status_code, 302)
        self.assertIsNone(Tasks.objects.filter(id=self.task.id).first())


class UpdateTaskTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.status = Status.objects.create(name_status='Завершена')
        cls.user = User.objects.create_user(username='testUser', password='testPasswordUser')
        cls.task = Tasks.objects.create(
            task='Тестовый пользователь',
            description='Это тестовое задание',
            status=cls.status,
            user=cls.user,
        )

    def test_update_task(self):
        self.client.login(username='testUser', password='testPasswordUser')
        update_url = reverse('update_task', args=[self.task.id])
        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Редактирование задачи')

    def test_update_task_post(self):
        self.client.login(username='testUser', password='testPasswordUser')
        update_url = reverse('update_task', args=[self.task.id])
        update_task_data = {
            'task': 'Обновленная задача',
            'description': 'Обновленное описание',
            'status': self.status.id
        }

        response = self.client.post(update_url, update_task_data)
