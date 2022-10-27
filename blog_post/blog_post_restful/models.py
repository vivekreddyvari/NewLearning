from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

# Create your models here.

# status of blog
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


# BlogList table
class BlogList(models.Model):
    """ Blog List Model
        Purpose: stores blog list columns to represent a blog at user-level
    """
    title = models.CharField(max_length=100, blank=False, unique=True)
    description = models.CharField(max_length=500, blank=False)
    date_created = models.DateTimeField(auto_now=True)
    author_name = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='bloglists',
                                    default='1')
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    # image = models.ImageField(upload_to='media')

    # Meta
    class Meta:
        """ The Meta servers the purpose of
        ordering the blog-posts based on data created.
        The newly created blogs are shown first.
        """
        ordering = ['-date_created']

    # title
    def __str__(self):
        return "()".format(self.title)

    @receiver(post_save, sender=User)
    def create_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)


