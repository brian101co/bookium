from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

def upload_avatar_image(instance, filename):
    return f"users/profiles/{instance.user.username}/{filename}"

class Profile(models.Model):
    avatar = ProcessedImageField(
        upload_to=upload_avatar_image, 
        processors=[ResizeToFill(100, 100)],
        format="JPEG",
        options={"quality":80},
        blank=True,
        null=True
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)

    def __str__(self):
        return f"{self.user.username}'s profile "

User.profile = property(lambda u:Profile.objects.get_or_create(user=u)[0])
