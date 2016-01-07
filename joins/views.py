from django.shortcuts import render, HttpResponseRedirect, Http404
from .models import Join
from django.conf import settings

# Create your views here.
from .forms import EmailForm, JoinForm

#Fuction for get ref_id
import uuid
def get_ref_id():
    ref_id = str(uuid.uuid4())[:11].replace('-','').lower()
    try:
        id_exists = Join.objects.get(ref_id=ref_id)
        get_ref_id()
    except:
        return ref_id

#Function for get ip address
def get_ip(request):
    try:
        x_foreard = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_foreard:
            ip = x_foreard.splite(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
    except:
        ip = ""
    return ip

def share(request,ref_id):
        # join_obj = Join.objects.get(ref_id=ref_id)
        # friends_referred = Join.objects.filter(friend = join_obj)
        # count = join_obj.referral.all().count()
        # ref_url = "http://127.0.0.1:8000/?ref=%s" %(join_obj.ref_id)
        # context = {"ref_id":join_obj.ref_id, "count":count, "ref_url":ref_url}
        # template = "joins/share.html"
        # return render(request, template, context)
    try:
        join_obj = Join.objects.get(ref_id=ref_id)
        friends_referred = Join.objects.filter(friend = join_obj)
        count = join_obj.referral.all().count()
        # ref_url = "http://127.0.0.1:8000/?ref=%s" %(join_obj.ref_id)
        ref_url = settings.SHARE_URL+str(join_obj.ref_id)
        context = {"ref_id":join_obj.ref_id, "count":count, "ref_url":ref_url}
        template = "joins/share.html"
        return render(request, template, context)
    except:
        raise Http404


def index(request):
    try:
        join_id = request.session['join_id_ref']
        obj = Join.objects.get(id=join_id)
        # print "the obj is %s" %(obj.email)
    except:
        obj = None
    #This is using Django regular form
    # form = EmailForm(request.POST or None)
    # if form.is_valid() :
    #     print form.cleaned_data['email']


    #This is using models form
    form = JoinForm(request.POST or None)
    if form.is_valid():
        new_join = form.save(commit = False)
        email = form.cleaned_data['email']
        new_join_old, created = Join.objects.get_or_create(email=email)
        if created:
            new_join_old.ref_id = get_ref_id()
            if not obj == None:
                new_join_old.friend = obj
            new_join_old.ip_address = get_ip(request)
            new_join_old.save()
        return HttpResponseRedirect("/joins/%s" %(new_join_old.ref_id))
        # new_join.ip_address = get_ip(request)
        # new_join.save()
    # form = TestForm(request.POST or None)
    context = {"form":form}
    template = "joins/index.html"
    return render(request, template, context)