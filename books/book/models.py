from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateTimeField('birth date')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book:author_info', args=[self.pk])


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('publication date')
    image = models.FileField(upload_to="", blank=True, null=True)

    def __str__(self):
        return f"{str(self.author)}. {self.title}"

    def get_absolute_url(self):
        return reverse('book:book_info', args=[self.pk])
