from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import datetime
# import logging
from house_inventory.forms import *
from house_inventory.models import *


##logger = logging.getLogger(__name__)

def hello(request):
    return HttpResponse("Hello world")

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def item_add(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
##            logger.info(cd['item'])
            dbItem = Item(name=cd['item_name'])
            dbItem.save()
            return HttpResponseRedirect('/item/thanks/')
    else:
        form = AddItemForm()
    return render(request, 'item_add.html', {'form': form})

def item_thanks(request):
    html = []
    html.append('<tr><td>Thanks!</td></tr>')
    return HttpResponse('<table>%s</table>' % '\n'.join(html))



##def current_datetime(request):
##    now = datetime.datetime.now()
##    return render(request, 'current_datetime.html', {'current_date': now})
##
##def hours_ahead(request, offset):
##    try:
##        offset = int(offset)
##    except ValueError:
##        raise Http404()
##    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
##    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
##    return HttpResponse(html)
##

