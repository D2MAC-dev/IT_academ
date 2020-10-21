from django.db import models

class Book(models.Model):
    book_genres = models.CharField('Жанр', max_length = 200)
    book_name = models.CharField('Название книги', max_length = 200)
    book_author = models.CharField('Автор', max_length = 200)
    book_publisher = models.CharField('Издательство', max_length = 200)

class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    user_name = models.CharField('Имя пользователя', max_length = 55)
    comment_text = models.CharField('текст комментари', max_length = 300)
