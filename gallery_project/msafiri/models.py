from django.db import models

# Create your models here.
class Image(models.Model):
    img = models.FileField(upload_to='pic/%y/')
    title = models.CharField(max_length=255)
    img_description = models.TextField()
    # category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    location =models.ForeignKey('Location', on_delete=models.CASCADE, null=True)
    category = models.ManyToManyField('Category')

    def __str__(self):
        return self.title

    @classmethod
    def all_images(cls, self):
        return Image.objects.all()

    @classmethod
    def search_by_category(cls,search_images):
        images = Image.objects.filter(category__name__icontains=search_images)
        return images

    @classmethod
    def view_location(cls,name):
        location = cls.objects.filter(location=name)
        return location

    @classmethod
    def view_category(cls,cat):
        category = cls.objects.filter(category=cat)
        return category

    class Meta:
        ordering = ['-id']

class Location(models.Model):
    location_name = models.CharField(max_length=255)
    def __str__(self):
        return self.location_name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


    