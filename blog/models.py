from django.db import models


# Create your models here.
class BlogAuthor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    bio = models.TextField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Category(models.Model):
    name = models.CharField(max_length=20)


class Blog(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    blogger = models.ForeignKey(BlogAuthor, on_delete=models.CASCADE)
    categories = models.ManyToManyField('Category', related_name='posts')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']


class Comment(models.Model):
    author = models.CharField(max_length=30)
    body = models.CharField(max_length=300)
    create_date = models.DateField(auto_now_add=True)
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE, primary_key=True, )

    def __str__(self):
        return self.body

    class Meta:
        ordering = ['-create_date']
