from django.db import models

Orientations_Choices = [
    ( 1, "בשרים" ),
    ( 2 , "סושיות" ),
    ( 3 , "איטלקי" ),
    ( 4 , "בר מסעדה" ),
    ( 5 , "אסייתי" ),
    ( 6 , "דגים" ),
    ( 7 , "מזרחי" ),
    ( 8 , "מקסיקני" ),
    ( 9 , "גריל בר" ),
    ( 10 , "ביתי" ),
    ( 11 , "טבעוני" ),
    ( 12 , "הודי" ),
    ( 13 , "אמריקאי" ),
    ( 14 , "צמחוני" ),
    ( 14 , "ים תיכוני" ),
    ( 14 , "תימני" ),
    ( 14 , "דרום אמריקאי" ),
    ( 14 , "טאפאס" ),
    ( 14 , "אירופאי" ),
    ( 14 , "אפריקאי" ),
    ( 14 , "לטיני" ),
    ( 14 , "צ'רקסי" ),
]

Geolocation_Choices = [
    ( 1, "עפולה" ),
    ( 2 , "חיפה" ),
    ( 3 , "ירושליים" ),
    ( 4 , "תל אביב" ),
    ( 5 , "טבריה" ),
    ( 6 , "רמת ישי" ),
    ( 7 , "קריית שמונה" ),
]


class Restaurnat(models.Model):
    restaurant_name = models.CharField(max_length=100)
    orientation_requierd = models.IntegerField(choices=Orientations_Choices)
    geolocation = models.IntegerField(choices=Geolocation_Choices)
    has_private_room = models.BooleanField(default=False)


    def __str__(self):
        return self.restaurant_name


class Tag(models.Model):
    short_description_text = models.CharField(max_length=150, verbose_name="describe the tag meaning")
    restaurants = models.ManyToManyField(Restaurnat, through='TagMatch')

    def __str__(self):
        return self.short_description_text


class TagMatch(models.Model):
    restaurant = models.ForeignKey(Restaurnat, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)



    
