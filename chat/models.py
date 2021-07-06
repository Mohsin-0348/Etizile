from django.db import models

from django.contrib.auth import get_user_model

from bases.models import BaseModel
from rnd.models import BaseAdvertise

User = get_user_model()


class ChatConversation(BaseModel):
    ad_post = models.ForeignKey(BaseAdvertise, on_delete=models.CASCADE, null=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="seller")
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="buyer")

    class Meta:
        ordering = ['-created']
        db_table = "chat_conversations"


class ChatMessage(BaseModel):
    conversation = models.ForeignKey(ChatConversation, on_delete=models.CASCADE)
    message = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="message_sender")
    is_read = models.BooleanField(default=False,)
    file = models.FileField(
        upload_to="chat/",
        blank=True,
        null=True,
        verbose_name="Shared File",
        help_text="File shared in a conversation"
    )

    class Meta:
        db_table = "chat_messages"
        get_latest_by = "created"
