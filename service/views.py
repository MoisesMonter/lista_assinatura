from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Client, SignatureList, Signature
from .serializers import ClientSerializer, SignatureListSerializer, SignatureSerializer
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner.user == request.user

class SignatureListViewSet(viewsets.ModelViewSet):
    queryset = SignatureList.objects.all()
    serializer_class = SignatureListSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        client = get_object_or_404(Client, user=self.request.user)
        serializer.save(owner=client)

    def get_queryset(self):
        client = get_object_or_404(Client, user=self.request.user)
        return SignatureList.objects.filter(owner=client)

class SignatureViewSet(viewsets.ModelViewSet):
    queryset = Signature.objects.all()
    serializer_class = SignatureSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        signature_list = get_object_or_404(SignatureList, id=self.kwargs['signature_list_id'], owner__user=self.request.user)
        serializer.save(signature_list=signature_list)

    def get_queryset(self):
        client = get_object_or_404(Client, user=self.request.user)
        if client.is_owner:
            return Signature.objects.filter(signature_list__owner=client)
        return Signature.objects.filter(signature_list__owner=client)

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
