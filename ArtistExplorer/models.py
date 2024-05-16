from django.db import models

class Artists(models.Model):
    ArtistId = models.AutoField(primary_key=True )
    Name = models.CharField(max_length=255)
    Description = models.TextField(null=True)
    Popularity = models.IntegerField()
    Image = models.ImageField(upload_to='images/')
    Followers = models.TextField(null=True)

    def __str__(self):
        return self.Name
