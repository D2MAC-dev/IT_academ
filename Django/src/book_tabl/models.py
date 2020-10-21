from django.db import models

class Book(models.Model):
    book_genres = models.CharField('Жанр', max_length = 200, blank=False, null=False)
    book_name = models.CharField('Название книги', max_length = 200, blank=False, null=False)
    book_author = models.CharField('Автор', max_length = 200, blank=False, null=False)
    book_publisher = models.CharField('Издательство', max_length = 200,blank=False, null=False)

    def __str__(self):
        return f'{self.book_genres} {self.book_name} {self.book_author}'

class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    user_name = models.CharField('Имя пользователя', max_length = 55, blank=True, null=True)
    comment_text = models.CharField('текст комментари', max_length = 300, blank=True, null=True)

    def __str__(self):
        return self.user_name
