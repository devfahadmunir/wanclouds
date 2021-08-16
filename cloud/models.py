from django.db import models
from django.contrib.auth.models import User

# this is the databasemodel for items


class item(models.Model):
    id = models.AutoField
    # user is here as foriegn key
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField(max_length=4000)
    # data is autogenrated by system and saved in field
    date = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(
        null=True, blank=True, default="default.jpg", upload_to="items_pics")  # images are stored in database along there correct directory path

    def __str__(self):   # this funtion used to display name insted of objects
        return self.item_name
