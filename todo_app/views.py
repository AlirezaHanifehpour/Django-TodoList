from django.shortcuts import render,redirect
from django.views import View
from .models import Book

class HomeView(View): 
    def get(self,request):
        books = Book.objects.all()
        book_name = request.GET.get('add')
        if book_name: 
            new_book = Book.objects.create(name=book_name)
            new_book.save()
            return redirect('todo_app:home')
        context = {
            'books':books
        }
        return render(request,'index.html',context=context)

def remove_book(request,book_id): 
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('todo_app:home')

def clear_book(request):
    Book.objects.all().delete()
    return redirect('todo_app:home')
