from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime

# Create your views here.

from .forms import RenewBookForm
from .models import Book, Author, BookInstance, Genre
from django.views import generic

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view listing books on loan to current user.
    """
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

def index(request):
    """
    View function for homepage of site
    """

    #Generate counts of some of the main objects
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()

    #Available books (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count() # all() is implied by default

    # Number of visits to this view, as counted in the Session variable.
    num_visits=request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits+1

    return render(
        request,
        'index.html',
        context={
            'num_books': num_books,
            'num_instances':num_instances,
            'num_instances_available':num_instances_available,
            'num_authors':num_authors,
            'num_visits':num_visits,
        },
    )


class BookListView(generic.ListView):
    model = Book
    paginate_by = 3
    """ Example customisation
    context_object_name = 'my_book_list'   # your own name for the list as a template variable
    queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location
    """

class BookDetailView(generic.DetailView):
    model = Book

# generic author views
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 3

class AuthorDetailView(generic.DetailView):
    model = Author


@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request, pk):
    """
    Viewfunction for renewing a specific BookInstance by librarian
    """
    book_inst=get_object_or_404(BookInstance, pk = pk)

    # If this is a POST request then proecss the Form data
    if request.method == 'POST':

        #Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)

        #Check if the form is valid:
        if form.is_valid():
            # process the data inform.cleaned_data as required (here we just write it to the model due_back field
            book_inst.due_back = form.cleaned_data['renewal_date']
            book_inst.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('catalog:index'))


    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date,})

    return render(request, 'catalog/book_renew_librarian.html', {'form': form, 'bookinst':book_inst})


#generic edit views
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# from .models import Author

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    initial={'date_of_death':'12/10/2016',}

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['first_name','last_name', 'date_of_birth', 'date_of_death']

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('catalog:authors')


















