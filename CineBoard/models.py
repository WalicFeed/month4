from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title of the movie')
    year = models.PositiveIntegerField(verbose_name='The year this movie came out')
    photo = models.ImageField(upload_to='CineBoard/photos/', null=True, blank=True)
    genre = models.CharField(max_length=50, verbose_name='The genre of the movie')
    creator = models.CharField(max_length=100, verbose_name='Name of the creator')
    describtion = models.TextField(verbose_name='Describtion of the movie', null=True, blank=True)
    score = models.IntegerField(verbose_name='The combined score of the movie')
    do_recommend = models.BooleanField(verbose_name='Do you recommend?', default=False)
    country_of_prodaction = models.CharField(max_length=100, verbose_name='Where it was created')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.title}'
