from django.db import models
from django.contrib.auth.models import User


class Wall(models.Model):
    description = models.CharField(max_length=150)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.description


class Post(models.Model):
    message = models.TextField()
    wall = models.ForeignKey(Wall, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='posts', null=True, blank=True)

    def __str__(self):
        return f"{self.message}, creator: {self.created_by}"


class Comment(models.Model):
    message = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.message}, commentator: {self.created_by}"



class Following(models.Model):
    target = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='targets')
    followers_list = []
    followers_list.append(follower)

    def __str__(self):
        return f"{self.target} is followed by {self.followers_list}"
