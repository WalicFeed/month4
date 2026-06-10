from django.db import models


class HorseTourCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class HorseTour(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название тура')
    description = models.TextField(verbose_name='Описание тура')
    duration_hours = models.IntegerField(verbose_name='Продолжительность (часы)')
    categories = models.ManyToManyField(HorseTourCategory, verbose_name='Категории тура', related_name='tours')
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0, null=True)

    def __str__(self):
        return f"{self.title} - {', '.join([c.name for c in self.categories.all()])}"


class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    personal_number = models.CharField(max_length=20, verbose_name='Персональный номер')
    email = models.EmailField(verbose_name='Email', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.personal_number})"

class Horse(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя лошади')
    breed = models.CharField(max_length=100, verbose_name='Порода')
    age = models.IntegerField(verbose_name='Возраст')
    person = models.OneToOneField(Person, on_delete=models.CASCADE, verbose_name='Владелец', related_name='horse', null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.breed}, {self.age} лет)"


class Comment(models.Model):
    tour = models.ForeignKey(HorseTour, on_delete=models.CASCADE, verbose_name='Тур',related_name='comments')
    author = models.CharField(max_length=100, verbose_name='Автор')
    text = models.TextField(verbose_name='Текст комментария')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Комментарий от {self.author} к '{self.tour.title}'"
