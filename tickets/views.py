from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Ticket
from .form import CreateTicketForm, UpdateTicketForm
"""For Customers"""

#creating a ticket
def create_ticket(request):
    if request.method == 'POST':
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            var  = form.save(commit=False)
            var.created_by = 'Pending'
            var.save()
            messages.info(request, 'Your tikeck has been successfully submitted. na engineer would be assigned soon.')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong. Please check your form input and try again.')
            return redirect('create-ticket')
    else:
        form = CreateTicketForm()
        context = {'form': form}
        return render(request, 'tickets/create_ticket.html', context)
    

#update a ticket
def update_ticket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateTicketForm(request.POST)
        if form.is_valid():
            var  = form.save(commit=False)
            var.created_by = 'Pending'
            var.save()
            messages.info(request, 'Your tikeck has been updated and all the changes are saved in the Database.')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong. Please check your form input and try again.')
            # return redirect('create-ticket')
    else:
        form = UpdateTicketForm()
        context = {'form': form}
        return render(request, 'tickets/update_ticket.html', context)
    

# Get all tickets
def all_tickets(request):
    tickets = Ticket.objects.filter(created_by=request.user)
    context = {'tickets': tickets}
    return render(request, 'tickets/all_tickets.html', context)


"""For Engineers"""
# views tickets queue
def ticket_queue(request):
    tickets = Ticket.objects.filter(ticket_status='Pending')
    context = {'tickets': tickets}
    return render(request, 'tickets/all_ticket_queue.html', context)