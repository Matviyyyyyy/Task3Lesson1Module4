from django.db import models

class LibraryBook(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    isbn = models.CharField(max_length=256)
    available = models.BooleanField()

    class Meta:
        ordering = ["author"]
        verbose_name = "Library Book"
        verbose_name_plural = "Library Books"
        unique_together = [["isbn"]]

    def __str__(self):
        return f"{self.title} - {self.author}"

