from django.db import models
from django.forms.models import model_to_dict

class FoodItem(models.Model):
    """Stoers nutrient data for every food item"""
    S_NO = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    short_description = models.TextField()
    image_url = models.URLField()
    type = models.CharField(max_length=50)
    calories = models.FloatField()
    total_fat = models.FloatField()
    saturated_fat = models.FloatField()
    trans_fat = models.FloatField()
    cholesterol = models.FloatField()
    sodium = models.FloatField()
    carbohydrate = models.FloatField()
    dietary_fiber = models.FloatField()
    sugar = models.FloatField()
    protein = models.FloatField()
    calcium = models.FloatField()
    iron = models.FloatField()
    potassium = models.FloatField()
    vitamin_a = models.FloatField()
    vitamin_b1 = models.FloatField()
    vitamin_b2 = models.FloatField()
    vitamin_b3 = models.FloatField()
    vitamin_b4 = models.FloatField()
    vitamin_b5 = models.FloatField()
    vitamin_b6 = models.FloatField()
    vitamin_b9 = models.FloatField()
    vitamin_b12 = models.FloatField()
    vitamin_c = models.FloatField()
    vitamin_d = models.FloatField()
    vitamin_e = models.FloatField()
    vitamin_k = models.FloatField()
    phosphorus = models.FloatField()
    magnesium = models.FloatField()
    zinc = models.FloatField()
    copper = models.FloatField()
    recommended_portion = models.FloatField()

    def __str__(self):
        return self.name
    
    @classmethod
    def all_as_list_of_dict(cls):
        """Returns list consisting of each object after serialization"""
        food_items = cls.objects.all()
        food_items_list = [model_to_dict(item) for item in food_items]
        return food_items_list
