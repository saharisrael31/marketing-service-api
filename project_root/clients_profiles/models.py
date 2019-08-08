from django.db import models

User_Category_Choices = [
    (1, "new before payment"),
    (2, "new first time payment"),
    (3, "second time payment"),
    (4, "returning client"),
]

Area_Choices = [
    (1, "Darom"),
    (2, "Tzafon"),
    (3, "Mercaz"),
]

Restaurant_Category_Choices = [
    (1, "fast food"),
    (2, "delux"),
    (3, "other..."),
]

class Account(models.Model):
    first_name = models.CharField(max_length=100)
    seconed_name =models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 12)
    user_category = models.IntegerField(choices=User_Category_Choices)

    def __str__(self):
        return self.name


class Profile(models.Model):
    name_of_business = models.CharField(max_length=100)
    area = models.IntegerField(choices=Area_Choices)
    cosher = models.BooleanField(default=False)
    romantic = models.BooleanField(default=False)
    has_private_room = models.BooleanField(default=False)
    restaurant_category =models.IntegerField(choices=Restaurant_Category_Choices)

    def __str__(self):
        return self.name_of_business