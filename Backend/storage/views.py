from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import user, call, Ticket, Lead
from .serializers import UserSerializer, CallSerializer, TicketSerializer, LeadSerializer


# -------- USER --------
@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user(request, pk):
    try:
        usr = user.objects.get(pk=pk)
    except user.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    usr.delete()
    return Response({'message': 'User deleted'}, status=status.HTTP_204_NO_CONTENT)


# -------- CALL --------
@api_view(['POST'])
def create_call(request):
    serializer = CallSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_call(request, pk):
    try:
        call_instance = call.objects.get(pk=pk)
    except call.DoesNotExist:
        return Response({'error': 'Call not found'}, status=status.HTTP_404_NOT_FOUND)
    call_instance.delete()
    return Response({'message': 'Call deleted'}, status=status.HTTP_204_NO_CONTENT)


# -------- TICKET --------
@api_view(['POST'])
def create_ticket(request):
    serializer = TicketSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_ticket(request, pk):
    try:
        ticket_instance = Ticket.objects.get(pk=pk)
    except Ticket.DoesNotExist:
        return Response({'error': 'Ticket not found'}, status=status.HTTP_404_NOT_FOUND)
    ticket_instance.delete()
    return Response({'message': 'Ticket deleted'}, status=status.HTTP_204_NO_CONTENT)


# -------- LEAD --------
@api_view(['POST'])
def create_lead(request):
    serializer = LeadSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_lead(request, pk):
    try:
        lead_instance = Lead.objects.get(pk=pk)
    except Lead.DoesNotExist:
        return Response({'error': 'Lead not found'}, status=status.HTTP_404_NOT_FOUND)
    lead_instance.delete()
    return Response({'message': 'Lead deleted'}, status=status.HTTP_204_NO_CONTENT)
