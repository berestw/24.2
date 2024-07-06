from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lms.models import Lesson, Course, Subscription
from user.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@yandex.ru')
        self.course = Course.objects.create(title='test_course', content='test', owner=self.user)
        self.lesson = Lesson.objects.create(title='test_lesson', content='test', owner=self.user, course=self.course)
        self.client.force_authenticate(user=self.user)

    def test_lesson_create(self):
        url = reverse('lms:create_lesson')
        data = {
            'title': 'test',
            'content': 'test',
            'course': self.course.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse('lms:update_lesson', args=(self.lesson.pk,))
        data = {
            "title": "test2",
        }

        response = self.client.patch(url, data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('title'), 'test2')

    def test_lesson_retrieve(self):
        url = reverse('lms:retrieve_lesson', args=(self.lesson.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_delete(self):
        url = reverse('lms:destroy_lesson', args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_lesson_list(self):
        url = reverse('lms:lesson_list')
        response = self.client.get(url)
        data = response.json()
        result = {'count': 1,
                  'next': None,
                  'previous': None,
                  'results': [{'id': self.lesson.pk,
                               'title': self.lesson.title,
                               'content': self.lesson.content,
                               'image': None,
                               'url': None,
                               'course': self.lesson.course.pk,
                               'owner': self.lesson.owner.pk}]
                  }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@mail.ru')
        self.course = Course.objects.create(title='test_course', content='test', owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_subscription_create(self):
        url = reverse('lms:subscription_create')
        data = {
            "course": self.course.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Subscription.objects.all().count(), 1)
        self.assertEqual(response.json(), {"message": "подписка добавлена"})

    def test_subscription_delete(self):
        url = reverse('lms:subscription_create')
        data = {
            "course": self.course.pk
        }
        self.client.post(url, data)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Subscription.objects.all().count(), 0)
        self.assertEqual(response.json(), {"message": "подписка удалена"})
