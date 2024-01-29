from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 255)
    content = models.TextField()
    # image
    # tag
    # category
    # author
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)

    class Meta:
        # app_label

        # more usef
        ordering = ['created_date']

    def __str__ (self):
        return self.title
    
    def ChangeStatus(self, s):
        self.status = s