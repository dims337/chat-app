from django.contrib.auth import get_user_model
from django.db import models

# message model (to save and preload our messages)

User = get_user_model()

class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_message', on_delete=models.CASCADE)
    Content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username


    def last_10_messages(self):
        #load only last 10 messages

        return Message.objects.order_by('-timestamp').all()[:10]
        #(-timestamp)=reverse order, from newer messages
            