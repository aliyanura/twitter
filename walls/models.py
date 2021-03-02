from django.db import models
from django.contrib.auth.models import User


class Wall(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='walls')
    description = models.TextField()

    def __str__(self):
        return f"{self.owner} wall"

    def get_posts_count(self):
        return Post.objects.filter(topic__board=self).count()

    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by('-created_at').first()


class Post(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='posts')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='posts', null=True, blank=True)

    def __str__(self):
        return f"{self.message}, creator: {self.creator}"

# def like_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     user = request.user
#     if request.method == "POST":
#         self.like += 1


    class Meta:
        ordering = ('created_at',)


class Comment(models.Model):
    message = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                              related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='create_comments')
    
    def __str__(self):
        return f"{self.message}, commentator: {self.created_by}"

    class Meta:
        ordering = ('created_at',)


class Following(models.Model):
    target = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='targets')

    def __str__(self):
        return f"{self.target} is followed by {self.follower}"
