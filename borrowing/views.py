from django.shortcuts import render
from rest_framework import generics
from .models import Borrowing, Return
from .serializers import BorrowingSerializer, ReturnSerializer
from .models import Borrowing
from .models import Return

def return_list_view(request):
    returns = Return.objects.filter(borrowing__user=request.user)
    return render(request, 'borrowing/return_list.html', {'returns': returns})


def borrow_list_view(request):
    borrowings = Borrowing.objects.filter(user=request.user)
    return render(request, 'borrowing/borrow_list.html', {'borrowings': borrowings})


class BorrowingListCreateView(generics.ListCreateAPIView):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer


class BorrowingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer


class ReturnListCreateView(generics.ListCreateAPIView):
    queryset = Return.objects.all()
    serializer_class = ReturnSerializer


class ReturnDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Return.objects.all()
    serializer_class = ReturnSerializer

