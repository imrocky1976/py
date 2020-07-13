from django.db import models
from django.db import connection
from django.urls import reverse

# Create your models here.

class BookManager(models.Manager):
    """
    Book.objects.book_count('Python')
    """
    def book_count(self, keyword):
        return self.filter(name__icontains=keyword).count()

class ShihjBookManager(models.Manager):
    """
    重写默认的返回对象方法： Book.shihj_objects.all()
    """
    def get_query_set(self):
        #a = Author.objects.filter(first_name="Haojie")
        return super(ShihjBookManager, self).get_query_set().filter(author__first_name='Haojie')

class AuthorManager(models.Manager):
    def first_names(self, last_name):
        cursor = connection.cursor()
        cursor.execute("""
            select distinct first_name 
            from books_author
            where last_name = %s""", [last_name])
        return [row[0] for row in cursor.fetchall()]

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name='电子邮件')

    objects = AuthorManager()

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def _get_full_name(self):
        "Returns the person's full name."
        return u'%s %s' % (self.first_name, self.last_name)
    
    full_name = property(_get_full_name)


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

    objects = BookManager()
    shihj_objects = ShihjBookManager()

    class Meta:
        ordering = ['name']

    def get_author_name(self):
        author_name = ''
        for a in self.author.all():
            full_name = a.first_name + ' ' + a.last_name
            author_name += full_name + ','
        if author_name.endswith(','):
            author_name = author_name[:-1]
        return author_name

