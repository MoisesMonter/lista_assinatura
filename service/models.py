from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=False)

class SignatureList(models.Model):
    owner = models.ForeignKey(Client, related_name='signature_lists', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Signature(models.Model):
    signature_list = models.ForeignKey(SignatureList, related_name='signatures', on_delete=models.CASCADE)
    imagem_base64 = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
