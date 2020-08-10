from django.db.models.signals import pre_save
from django.dispatch import receiver
from core.utils import generate_random_text
from django.utils.text import slugify

from questions.models import Question


@receiver(pre_save, sender=Question)
def question_slugify(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.content)
        random_text = generate_random_text()
        instance.slug = slug + '-' + random_text
