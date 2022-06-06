import logging
from typing import Dict, Union

from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

logger = logging.getLogger(__name__)


@shared_task
def send_feedback_mail(message_form: Dict[str, Union[int, str]]) -> None:
    logger.info(f"Send message: '{message_form}'")
    model_user = get_user_model()
    user_obj = model_user.objects.get(pk=message_form["user_id"])
    send_mail(
        "TechSupport Help",  # subject (title)
        message_form["message"],  # message
        user_obj.email,  # send from
        ["techsupport@braniac.com"],  # send to
        fail_silently=False,
    )
    return None
