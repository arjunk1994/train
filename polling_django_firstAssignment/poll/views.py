from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from poll.models import pollstr


def pol(request):
    return render(request,'front.html')
def Pollinternal(request):
    if request.method == "POST":
        aid = request.POST.get('a1')
        temp=pollstr()
        data=pollstr()
        data = pollstr.objects.get(order='only')
        d1=data.votes1
        d2=data.votes2
        d3=data.votes3
        d4=data.votes4
        bid=int(aid)
        if(bid==1):
            d1=str(int(d1)+1)
        if(bid==2):
            d2=str(int(d2)+1)
        if(bid==3):
            d3=str(int(d3)+1)
        if(bid==4):
            d4=str(int(d4)+1)
        temp.order='only'
        temp.vote1=d1 ,
        temp.vote2=d2,
        temp.vote3=d3,
        temp.vote4=d4
        pollstr.objects.filter(order='only').update(votes1=d1, votes2=d2,votes3=d3,votes4=d4,)

        vata=pollstr.objects.get(order='only')

        data_dict = {'da': vata}
        return render(request, 'pie.html',context=data_dict)
    data = pollstr.objects.get(order='only')
    data_dict = {'da': data}
    return render(request, 'test.html', context=data_dict)