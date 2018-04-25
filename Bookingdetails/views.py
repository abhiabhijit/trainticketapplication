from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserForm,ProfileForm
from django.contrib import messages
from .models import Ticketdetails
from django.template import Context, loader, RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('home')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
def retrievebookings(request):

        latest_bookings = Ticketdetails.objects.filter(user=request.user)
        # print(latest_bookings)
        if len(latest_bookings)==0:
            messages.warning(request, ('ALERT No bookings done!!!!'))

            return redirect('home')

        t = loader.get_template('bookings.html')
        context_dict = {
            'latest_bookings': latest_bookings,
        }
        return render(request, 'bookings.html', context=context_dict)

    # latest_bookings = Ticketdetails.objects.filter(user=request.user)
    # t = loader.get_template('bookings.html')
    # context_dict = {
    #     'latest_bookings': latest_bookings,
    #
    # }
    # return render(request, 'bookings.html', context=context_dict)


    # c = Context(context_dict)


    # return HttpResponse(t.render(c))



def ticket_details(request,pnr):
    detail=Ticketdetails.objects.get(pnr=pnr)
    # print(detail.pnr)
    context_dict = {
        'pnr': detail.pnr,
        'trainname': detail.trainname  ,
        'source':  detail.source ,
        'destination': detail.destination ,
        'journey_date': detail.journey_date ,
        'no_of_passengers': detail.no_of_passengers ,
    }
    return render(request, 'specific_ticket.html', context=context_dict)

    return HttpResponse("hiiiii")
# def profile(request):
#     form=ProfileForm(request.POST or None)
#
#     if form.is_valid():
#
#         form.save(commit=True)  # yes? save to database
#     else:
#         print(form.errors)
#     return render(request,'profile.html',{'form': form})


