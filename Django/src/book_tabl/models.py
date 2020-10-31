from django.db import models

class Book(models.Model):
    book_genres = models.CharField(
        'Жанр', 
        max_length = 200, 
        blank=True, null=True
    )

    book_name = models.CharField(
        'Название книги', 
        max_length = 200, 
        blank=False, null=False
    )

    book_author = models.CharField(
        'Автор', 
        max_length = 200, 
        blank=False, 
        null=False
    )

    book_publisher = models.CharField(
        'Издательство',
        max_length = 200,
        blank=False, null=False
    )

    isbn_code = models.CharField(
        "ISBN",
        default='', 
        max_length=20, 
        blank=False, null=False
    )
    book_price = models.DecimalField(
        "Цена в BYN",
        default=0.0,
        max_digits=10,
        decimal_places=2,
        blank=False, null=False
    )

    books_amount = models.PositiveIntegerField(
        "Количество",
        default=0,
        blank=False, null=False
    )


    
    def __str__(self):
        return f'Book #{self.pk}, name: {self.book_name} genre: {self.book_genres}, author: {self.book_author}, publisher: {self.book_publisher}, code: {self.isbn_code}, price: {self.book_price}, amount: {self.books_amount}'

class Comment(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete = models.CASCADE
    )

    user_name = models.CharField(
        'Имя пользователя',
        max_length = 55,
        blank=True, null=True
    )

    comment_text = models.CharField(
        'текст комментари',
        max_length = 300,
        blank=True, null=True
    )

    def __str__(self):
        return self.user_name


