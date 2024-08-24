from django.shortcuts import render,redirect
from BeautyApp.models import CategoryDB,ServiceDB,Hairservicedb,Skinservicedb,Nailservicedb,Makeupservicedb,Bodycareservicedb
from WebApp.models import Contactdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError




# Create your views here.
def index_page(request):
    return render(request,"index.html")

def category_page(request):
    return render(request, "Add_category.html")

def save_category(request):
    if request.method == "POST":
        cgname=request.POST.get('cname')
        cgdesc=request.POST.get('cdesc')
        cgimage=request.FILES['cimage']
        obj=CategoryDB(catg_name=cgname, catg_desc=cgdesc, catg_image=cgimage)
        obj.save()
        return redirect(category_page)


def category_display(request):
    data=CategoryDB.objects.all()
    return render(request,"Display_category.html",{'data':data})

def category_edit(request,catid):
    data=CategoryDB.objects.get(id=catid)
    return render(request,"Edit_category.html", {'data':data})

def update_category(request,catid):
    if request.method == "POST":
        cgname = request.POST.get('cname')
        cgdesc = request.POST.get('cdesc')
        try:
            cgimage = request.FILES['cimage']
            fs =FileSystemStorage()
            file = fs.save(cgimage.name,cgimage)
        except MultiValueDictKeyError:
            file = CategoryDB.objects.get(id=catid).catg_image
        CategoryDB.objects.filter(id=catid).update(catg_name=cgname, catg_desc=cgdesc, catg_image=file)
        return redirect(category_display)

def category_delete(request,catid):
    data=CategoryDB.objects.filter(id=catid)
    data.delete()
    return redirect(category_display)

def service_page(request):
    cat=CategoryDB.objects.all()
    return render(request,"Add_service.html", {'cat':cat})

def save_service(request):
    if request.method == "POST":
        catn = request.POST.get('catname')
        snm = request.POST.get('sname')
        cpr = request.POST.get('sprice')
        sdsc = request.POST.get('sdesc')
        simg = request.FILES['simage']
        obj=ServiceDB(Category=catn, Service_name=snm, Service_price=cpr, Service_desc=sdsc, Service_image=simg)
        obj.save()
        return redirect(service_page)

def service_display(request):
    data=ServiceDB.objects.all()
    return render(request, "Display_service.html",{'data':data})

def service_edit(request,sid):
    data=ServiceDB.objects.get(id=sid)
    return render(request,"Edit_service.html", {'data':data})


def update_service(request,sid):
    if request.method == "POST":
        catn = request.POST.get('catname')
        snm = request.POST.get('sname')
        cpr = request.POST.get('sprice')
        sdsc = request.POST.get('sdesc')
        try:
            simg = request.FILES['simage']
            fs1 = FileSystemStorage()
            file1 = fs1.save(simg.name, simg)
        except MultiValueDictKeyError:
            file1 = ServiceDB.objects.get(id=sid).Service_image
        ServiceDB.objects.filter(id=sid).update(Category=catn, Service_name=snm, Service_price=cpr, Service_desc=sdsc, Service_image=file1)
        return redirect(service_display)

def delete_service(request,sid):
    data = ServiceDB.objects.filter(id=sid)
    data.delete()
    return redirect(service_display)

# ************************************************************************************
# HAIR CARE
def hairservice_page(request):
    Hcat=Hairservicedb.objects.all()
    return render(request, "Add_Hair_Care.html", {'Hcat':Hcat})

def save_hair_data(request):
    if request.method == "POST":
        hcgname=request.POST.get('hcatname')
        hcat=request.POST.get('shcname')
        hname=request.POST.get('shname')
        hprice=request.POST.get('shprice')
        hdesc=request.POST.get('shdesc')
        himage=request.FILES['shimage']
        obj=Hairservicedb(Haircat_name=hcgname, Hair_category=hcat, Hair_name=hname, Hair_price=hprice, Hair_desc=hdesc, Hair_image=himage)
        obj.save()
        return redirect(hairservice_page)

def hair_care_display(request):
    Hccat=Hairservicedb.objects.all()
    return render(request, "Diplay_hair_care.html",{'Hccat':Hccat})

def hair_care_edit(request,hcid):
    Hcdata=Hairservicedb.objects.get(id=hcid)
    return render(request,"Edit_hair_care.html", {'Hcdata':Hcdata})

def update_Hair_service(request,hcid):
    if request.method == "POST":
        hcgname = request.POST.get('hcatname')
        hcat = request.POST.get('shcname')
        hname = request.POST.get('shname')
        hprice = request.POST.get('shprice')
        hdesc = request.POST.get('shdesc')
        try:
            himage = request.FILES['shimage']
            fs2 = FileSystemStorage()
            file2 = fs2.save(himage.name, himage)
        except MultiValueDictKeyError:
            file2 = Hairservicedb.objects.get(id=hcid).Hair_image
        Hairservicedb.objects.filter(id=hcid).update(Haircat_name=hcgname, Hair_category=hcat, Hair_name=hname, Hair_price=hprice, Hair_desc=hdesc, Hair_image=file2)
        return redirect(hair_care_display)

def hair_care_delete(request, hcid):
    Hcdata=Hairservicedb.objects.get(id=hcid)
    Hcdata.delete()
    return redirect(hair_care_display)
# *********************************************************************************************************
def skinservice_page(request):
    return render(request,"Add_skin_care.html")

def save_skin_data(request):
    if request.method == "POST":
        scgname=request.POST.get('scatname')
        scat=request.POST.get('sscname')
        sname=request.POST.get('scname')
        sprice=request.POST.get('scprice')
        sdesc=request.POST.get('scdesc')
        simage=request.FILES['scimage']
        obj=Skinservicedb(Skincat_name=scgname, Skin_category=scat, Skin_name=sname, Skin_price=sprice, Skin_desc=sdesc, Skin_image=simage)
        obj.save()
        return redirect(skinservice_page)

def skin_care_display(request):
    Sccat=Skinservicedb.objects.all()
    return render(request, "Display_skin_care.html",{'Sccat':Sccat})

def skin_care_edit(request,scid):
    Scdata=Skinservicedb.objects.get(id=scid)
    return render(request,"Edit_skin_care.html", {'Scdata':Scdata})

def update_Skin_service(request,scid):
    if request.method == "POST":
        scgname = request.POST.get('scatname')
        scat = request.POST.get('sscname')
        sname = request.POST.get('scname')
        sprice = request.POST.get('scprice')
        sdesc = request.POST.get('scdesc')
        try:
            simage = request.FILES['scimage']
            fs3 = FileSystemStorage()
            file3 = fs3.save(simage.name, simage)
        except MultiValueDictKeyError:
            file3 = Skinservicedb.objects.get(id=scid).Skin_image
        Skinservicedb.objects.filter(id=scid).update(Skincat_name=scgname, Skin_category=scat, Skin_name=sname, Skin_price=sprice, Skin_desc=sdesc, Skin_image=file3)
        return redirect(skin_care_display)


def skin_care_delete(request, scid):
    Scdata=Skinservicedb.objects.get(id=scid)
    Scdata.delete()
    return redirect(skin_care_display)
# *********************************************************************************************************
def nailservice_page(request):
    return render(request,"Add_Nail_care.html")

def save_nail_data(request):
    if request.method == "POST":
        ncgname=request.POST.get('ncatname')
        ncat=request.POST.get('nhcname')
        nname=request.POST.get('nhname')
        nprice=request.POST.get('nhprice')
        ndesc=request.POST.get('nhdesc')
        nimage=request.FILES['nhimage']
        obj=Nailservicedb(Nailcat_name=ncgname, Nail_category=ncat, Nail_name=nname, Nail_price=nprice, Nail_desc=ndesc, Nail_image=nimage)
        obj.save()
        return redirect(nailservice_page)


def nail_care_display(request):
    Nccat=Nailservicedb.objects.all()
    return render(request, "Display_nail_care.html",{'Nccat':Nccat})

def nail_care_edit(request,ncid):
    Ncdata=Nailservicedb.objects.get(id=ncid)
    return render(request,"Edit_nail_care.html", {'Ncdata':Ncdata})

def update_Nail_service(request,ncid):
    if request.method == "POST":
        ncgname = request.POST.get('ncatname')
        ncat = request.POST.get('nhcname')
        nname = request.POST.get('nhname')
        nprice = request.POST.get('nhprice')
        ndesc = request.POST.get('nhdesc')
        try:
            nimage = request.FILES['nhimage']
            fs4 = FileSystemStorage()
            file4 = fs4.save(nimage.name, nimage)
        except MultiValueDictKeyError:
            file4 = Nailservicedb.objects.get(id=ncid).Nail_image
        Nailservicedb.objects.filter(id=ncid).update(Nailcat_name=ncgname, Nail_category=ncat, Nail_name=nname, Nail_price=nprice, Nail_desc=ndesc, Nail_image=file4)
        return redirect(nail_care_display)

def nail_care_delete(request, ncid):
    Ncdata=Nailservicedb.objects.get(id=ncid)
    Ncdata.delete()
    return redirect(nail_care_display)
# ******************************************************************************************************
def makeupservice_page(request):
    return render(request,"Add_Makeup.html")

def save_makeup_data(request):
    if request.method == "POST":
        mcgname=request.POST.get('mcatname')
        mcat=request.POST.get('mcname')
        mname=request.POST.get('mname')
        mprice=request.POST.get('mprice')
        mdesc=request.POST.get('mdesc')
        mimage=request.FILES['mimage']
        obj=Makeupservicedb(Makeupcat_name=mcgname, Makeup_category=mcat, Makeup_name=mname, Makeup_price=mprice, Makeup_desc=mdesc, Makeup_image=mimage)
        obj.save()
        return redirect(makeupservice_page)


def makeup_display(request):
    Mkcat = Makeupservicedb.objects.all()
    return render(request,"Display_makeup.html",{'Mkcat': Mkcat})


def makeup_edit(request,mkid):
    Mkdata = Makeupservicedb.objects.get(id=mkid)
    return render(request,"Edit_makeup.html",{'Mkdata': Mkdata})

def update_makeup_service(request,mkid):
    if request.method == "POST":
        mcgname = request.POST.get('mcatname')
        mcat = request.POST.get('mcname')
        mname = request.POST.get('mname')
        mprice = request.POST.get('mprice')
        mdesc = request.POST.get('mdesc')
        try:
            mimage = request.FILES['mimage']
            fs5 = FileSystemStorage()
            file5 = fs5.save(nimage.name, mimage)
        except MultiValueDictKeyError:
            file5 = Makeupservicedb.objects.get(id=mkid).Makeup_image
        Makeupservicedb.objects.filter(id=mkid).update(Makeupcat_name=mcgname, Makeup_category=mcat, Makeup_name=mname, Makeup_price=mprice, Makeup_desc=mdesc, Makeup_image=file5)
        return redirect(makeup_display)
def makeup_delete(request, mkid):
    Mkdata=Makeupservicedb.objects.get(id=mkid)
    Mkdata.delete()
    return redirect(makeup_display)
# *************************************************************************************************************************


def Body_care_service_page(request):
    return render(request,"Add_body_care.html")

def save_Body_care_data(request):
    if request.method == "POST":
        bcgname=request.POST.get('bcatname')
        bcat=request.POST.get('sbcname')
        bname=request.POST.get('sbname')
        bprice=request.POST.get('sbprice')
        bdesc=request.POST.get('sbdesc')
        bimage=request.FILES['sbimage']
        obj=Bodycareservicedb(Bodycarecat_name=bcgname, Bodycare_category=bcat, Bodycare_name=bname, Bodycare_price=bprice, Bodycare_desc=bdesc, Bodycare_image=bimage)
        obj.save()
        return redirect(Body_care_service_page)

def bodycare_display(request):
    Bccat = Bodycareservicedb.objects.all()
    return render(request,"Display_bodycare.html",{'Bccat': Bccat})

def bodycare_edit(request,bcid):
    Bcdata = Bodycareservicedb.objects.get(id=bcid)
    return render(request,"Edit_body_care.html",{'Bcdata': Bcdata})

def update_bodycare_service(request,bcid):
    if request.method == "POST":
        bcgname = request.POST.get('bcatname')
        bcat = request.POST.get('sbcname')
        bname = request.POST.get('sbname')
        bprice = request.POST.get('sbprice')
        bdesc = request.POST.get('sbdesc')
        try:
            bimage = request.FILES['sbimage']
            fs6 = FileSystemStorage()
            file6 = fs6.save(nimage.name, bimage)
        except MultiValueDictKeyError:
            file6 = Bodycareservicedb.objects.get(id=bcid).Bodycare_image
        Bodycareservicedb.objects.filter(id=bcid).update(Bodycarecat_name=bcgname, Bodycare_category=bcat, Bodycare_name=bname, Bodycare_price=bprice, Bodycare_desc=bdesc, Bodycare_image=file6)
        return redirect(bodycare_display)

def bodycare_delete(request, bcid):
    Bcdata=Bodycareservicedb.objects.get(id=bcid)
    Bcdata.delete()
    return redirect(bodycare_display)


def contact_display(request):
    Cdata = Contactdb.objects.all()
    return render(request, "Display_Contact.html", {'Cdata': Cdata})


def contact_delete(request, contid):
    data = Contactdb.objects.filter(id=contid)
    data.delete()
    return redirect(contact_display)

