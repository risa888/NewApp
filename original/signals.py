from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from core.utils import generate_random_string
from original.models import Post

@receiver(pre_save, sender=Post)
def add_slug_to_post(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.title)
        random_string = generate_random_string()
        instance.slug = slug + "-" + random_string