from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book, Check
from .serializer import BookSerializer, CheckSerializer

@api_view(["GET", "POST"])
def book_list(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    serializer = BookSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)

@api_view(["GET", "PUT", "DELETE"])
def book_detail(request, pk):
    book = Book.objects.get(pk=pk)

    if request.method == "GET":
        serializer = BookSerializer(book)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = BookSerializer(book, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    book.delete()
    return Response(status=204)


@api_view(["GET", "POST"])
def check_list(request):
    if request.method == "GET":
        checks = Check.objects.all()
        serializer = CheckSerializer(checks, many=True)
        return Response(serializer.data)

    serializer = CheckSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)