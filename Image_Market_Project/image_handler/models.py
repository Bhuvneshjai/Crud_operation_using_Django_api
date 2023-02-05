from django.db import models

# Create your models here.

# Category Model
class Category(models.Model):
    title = models.CharField(max_length = 100)
    describe = models.TextField()

    def __str__(self):
        return self.title

# Image Model
class Image(models.Model):
    title = models.CharField(max_length = 100)
    describe = models.TextField()
    image = models.ImageField(upload_to='images_uploader_folder')
    add_date = models.DateTimeField(auto_now = True)
    catgry = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return self.title