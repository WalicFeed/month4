from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class DuneBook(models.Model):
    title = models.CharField(max_length=100, verbose_name="Book Title")
    author = models.CharField(max_length=100, default="Frank Herbert")
    planet = models.CharField(max_length=100, verbose_name="Planet")
    house = models.CharField(max_length=100, verbose_name="Noble House")
    main_character = models.CharField(max_length=100, verbose_name="Main Character")
    genre = models.CharField(max_length=100, verbose_name="Genre")
    short_description = models.TextField(verbose_name="Short Description")
    full_description = models.TextField(verbose_name="Full Description")
    publication_year = models.PositiveIntegerField(verbose_name="Publication Year")
    reservation_count = models.PositiveIntegerField(
        verbose_name="Reservation Count",
        default=0,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        help_text="You can reserve this book up to 5 times."
    )
    note = models.TextField(
        verbose_name="Note",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    can_be_bought_url = models.URLField(verbose_name="Can Be Bought URL", blank=True, null=True)

    def __str__(self):
        return self.title