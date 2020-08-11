from django.db import models


class Author(models.Model):
    author_firstname = models.CharField(max_length=100, verbose_name='Firstname')
    author_lastname = models.CharField(max_length=100, verbose_name='Lastname')
    author_joined_date = models.DateTimeField(auto_now=True, help_text='Joined: ')

    class Meta:
        ordering = ['-author_joined_date']

    def __str__(self):
        return '%s %s' % (self.author_lastname, self.author_firstname)


class Tag(models.Model):
    tag_title = models.CharField(max_length=100, help_text='Tag: ', unique=True)

    class Meta:
        ordering = ['tag_title']

    def __str__(self):
        return self.tag_title


class Post(models.Model):
    post_date = models.DateTimeField(auto_now=True)
    post_title = models.CharField(max_length=100, blank=False, help_text='give a title for the post')
    post_text = models.TextField(help_text='type here')
    post_author = models.ForeignKey(Author, related_name='author_posts', on_delete=models.SET_NULL, null=True)
    post_tags = models.ManyToManyField(Tag, help_text="Select a genre for this book")

    class Meta:
        ordering = ['-post_date', 'post_title']

    def __str__(self):
        return self.post_title
