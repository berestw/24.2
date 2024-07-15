from celery import shared_task
from django.core.mail import send_mail

from config import settings
from lms.models import Subscription


@shared_task
def send_email(course):
    subscriptions = Subscription.objects.filter(course=course)
    if subscriptions:
        course_name = subscriptions[0].course.title
        emails = []
        for subscription in subscriptions:
            emails.append(subscription.user.email)
            send_mail(f"Обновление курса {course_name}",
                      f"По вашей подписке {course_name} вышел новый урок!",
                      settings.EMAIL_HOST_USER, emails)
