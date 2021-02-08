from django.core.paginator import Paginator
from django.shortcuts import render
from websiteApp.models import Reservation


# Create your views here.
def messages_view(request):
    messages = Reservation.objects.filter(
        is_processed=False).order_by('send_date')
    paginator = Paginator(messages, 2)
    page = request.GET.get('page')
    messages_page = paginator.get_page(page)
    return render(request, 'messages.html', context={'items': messages_page})
