from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    img = models.ImageField(blank= True, null= True)
    created_at = models.DateTimeField(auto_now_add=True)   
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        create_time = self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        update_time = self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        return f'제목: {self.title}, 생성시간: {create_time}, 수정시간: {update_time}'
    