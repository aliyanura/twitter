from django.db import models
from django.contrib.auth.models import User


class Wall(models.Model):
    description = models.CharField(max_length=150)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')


class Post(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    likes_count = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='posts', null=True, blank=True)

    def __str__(self):
        return f"{self.message}, creator: {self.created_by}"

    class Meta:
        ordering = ('-created_at',)


class Comment(models.Model):
    message = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_comments_count(self):
        pass
    def __str__(self):
        return f"{self.message}, commentator: {self.created_by}"


class Like(models.Model):
    is_pressed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='likes')


class Following(models.Model):
    target = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='targets')

    def __str__(self):
        return f"{self.target} is followed by {self.follower}"


class Image(models.Model):
    image = models.ImageField(upload_to='user', null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='image')
