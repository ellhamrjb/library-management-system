from django.db import models
from django.contrib.auth.models import User
from books.models import Book

class Borrowing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(blank=True, null=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"


class Return(models.Model):
    borrowing = models.OneToOneField(Borrowing, on_delete=models.CASCADE)
    return_date = models.DateField(auto_now_add=True)
    fine = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Return record for {self.borrowing.book.title}"

