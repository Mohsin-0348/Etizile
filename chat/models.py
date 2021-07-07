from django.db import models
from django.contrib.auth import get_user_model

# define local imports
from bases.models import BaseModel
from rnd.models import BaseAdvertise

User = get_user_model()  # define user model


class ChatConversation(BaseModel):
    """
        store seller and buyer conversation information for an advertise
    """
    ad_post = models.ForeignKey(BaseAdvertise, on_delete=models.CASCADE, null=True)  # define reference advertise post
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                               related_name="seller")  # define seller user account
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                              related_name="buyer")  # define buyer user account

    class Meta:
        ordering = ['-created']  # define default filter as created
        db_table = "chat_conversations"  # define table name for database


class ChatMessage(BaseModel):
    """
        store message of seller or buyer for a conversation
    """
    conversation = models.ForeignKey(ChatConversation, on_delete=models.CASCADE,
                                     related_name='chat_message')  # define reference conversation for a message
    message = models.TextField()  # define message body
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_sender",
                               null=True)  # define sender of the message
    is_read = models.BooleanField(default=False)  # if receiver user read the message or not
    file = models.FileField(
        upload_to="chat/",
        blank=True,
        null=True,
        verbose_name="Shared File",
        help_text="File shared in a conversation"
    )  # store a file information if uploaded

    class Meta:
        db_table = "chat_messages"  # define table name for database
        get_latest_by = "created"  # define latest queryset by created
