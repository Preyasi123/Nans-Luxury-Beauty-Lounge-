from django.shortcuts import render, redirect,get_object_or_404
from BeautyApp.models import CategoryDB, Hairservicedb, Skinservicedb, Nailservicedb, Makeupservicedb, Bodycareservicedb,ServiceDB,mycart
from WebApp.models import Contactdb,signupdb,Bookdb,Appointmentdb
from django.contrib import messages
from django.core.mail import send_mail
from BeautyLounge import settings
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle,Spacer,Image
import razorpay

# Create your views here.
def Home_page(request):
    cat = CategoryDB.objects.all()
    return render(request, "Home.html", {'category': cat})


def About_page(request):
    cat = CategoryDB.objects.all()
    return render(request, "About.html", {'category': cat})


def our_services(request):
    cat = CategoryDB.objects.all()
    ser1 = Hairservicedb.objects.all
    ser2 = Skinservicedb.objects.all
    ser3 = Nailservicedb.objects.all
    ser4 = Makeupservicedb.objects.all
    ser5 = Bodycareservicedb.objects.all
    return render(request, "Our_services.html", {'ser1': ser1, 'ser2': ser2, 'ser3': ser3, 'ser4': ser4, 'ser5': ser5,'category': cat})


def contact_page(request):
    cat = CategoryDB.objects.all()
    return render(request, "Contact.html", {'category': cat})


def save_contact(request):
    if request.method == "POST":
        cname = request.POST.get('name')
        cmail = request.POST.get('email')
        csub = request.POST.get('subject')
        cmsg = request.POST.get('message')
        obj = Contactdb(contact_name=cname, contact_mail=cmail, contact_sub=csub, contact_msg=cmsg)
        obj.save()
        return redirect(contact_page)


def filtered_services(request, cat_name):
    cat = CategoryDB.objects.all()
    category1 = CategoryDB.objects.filter(catg_name=cat_name).first()
    hair = Hairservicedb.objects.filter(Haircat_name=cat_name)
    skin = Skinservicedb.objects.filter(Skincat_name=cat_name)
    nail = Nailservicedb.objects.filter(Nailcat_name=cat_name)
    mkp = Makeupservicedb.objects.filter(Makeupcat_name=cat_name)
    body = Bodycareservicedb.objects.filter(Bodycarecat_name=cat_name)
    price_range = request.GET.get('price_range')

    # Define price ranges for filtering
    price_ranges = {
        '100-500': (100, 500),
        '500-1000': (500, 1000),
        '1000-15000': (1000, 15000),
        '15000-90000': (15000, float('inf')),
    }

    # Initialize querysets for each category
    hair_services = Hairservicedb.objects.all()
    skin_services = Skinservicedb.objects.all()
    nail_services = Nailservicedb.objects.all()
    makeup_services = Makeupservicedb.objects.all()
    body_services = Bodycareservicedb.objects.all()

    # Apply price filter if specified
    if price_range in price_ranges:
        min_price, max_price = price_ranges[price_range]
        hair_services = hair_services.filter(Hair_price__gte=min_price, Hair_price__lte=max_price)
        skin_services = skin_services.filter(Skin_price__gte=min_price, Skin_price__lte=max_price)
        nail_services = nail_services.filter(Nail_price__gte=min_price, Nail_price__lte=max_price)
        makeup_services = makeup_services.filter(Makeup_price__gte=min_price, Makeup_price__lte=max_price)
        body_services = body_services.filter(Bodycare_price__gte=min_price, Bodycare_price__lte=max_price)
    return render(request, "Filtered_Services.html",{'hair': hair, 'skin': skin, 'nail': nail, 'mkp': mkp, 'body': body, 'category': cat, 'category1': category1,'price_ranges':price_ranges,'hair_services':hair_services,'skin_services':skin_services,'nail_services':nail_services,'makeup_services':makeup_services,'body_services':body_services})


def single_services_hair(request, sid):
    cat = CategoryDB.objects.all()
    singledata1 = Hairservicedb.objects.get(id=sid)
    return render(request, "Single_Services.html", {'category': cat, 'singledata1': singledata1})



def single_services_skin(request, hid):
    cat = CategoryDB.objects.all()
    singledata2 = Skinservicedb.objects.get(id=hid)
    return render(request, "Single_Services2.html", {'category': cat, 'singledata2': singledata2})

def single_services_nail(request, nid):
    cat = CategoryDB.objects.all()
    singledata3 = Nailservicedb.objects.get(id=nid)
    return render(request, "Single_Services3.html", {'category': cat, 'singledata3': singledata3})

def single_services_makeup(request, mid):
    cat = CategoryDB.objects.all()
    singledata4 = Makeupservicedb.objects.get(id=mid)
    return render(request, "Single_Services4.html", {'category': cat, 'singledata4': singledata4})

def single_services_body(request, bid):
    cat = CategoryDB.objects.all()
    singledata5 = Bodycareservicedb.objects.get(id=bid)
    return render(request, "Single_Services5.html", {'category': cat, 'singledata5': singledata5})

def signup_page(request):
    return render(request,"SignupPage.html")

def save_signup(request):
    if request.method== "POST":
        nm = request.POST.get('suname')
        pwd = request.POST.get('supwd')
        cpwd = request.POST.get('sucpwd')
        ml = request.POST.get('sumail')
        obj=signupdb(signup_name=nm,  signup_pwd=pwd, signup_cpwd=cpwd,signup_mail=ml)
        if signupdb.objects.filter(signup_name=nm).exists():
            messages.warning(request, "User already exists..!")
        else:
            obj.save()
            subject = "Welcome to Nans Luxury Beauty Lounge"
            message = "Hello, " + obj.signup_name + "!!\n" "Welcome to Nans Luxury Beauty Lounge!! \nYou have successfully Registered your account. \n \n Thanking you \n Nans admin"
            from_email = settings.EMAIL_HOST_USER
            to_list = [obj.signup_mail]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
        messages.success(request, "Created your account succesfully..!")
        return redirect(signup_page)

def signin_page(request):
    return render(request,"SigninPage.html")

def save_signin(request):
    if request.method == "POST":
        a = request.POST.get('siname')
        b = request.POST.get('sipwd')
        c = request.POST.get('simail')
        if signupdb.objects.filter(signup_name=a, signup_pwd=b,signup_mail=c ).exists():
            request.session['signup_name']=a
            request.session['signup_pwd']=b
            request.session['signup_mail'] = c
            messages.success(request, "Welcome..!")
            return redirect(Home_page)
        else:
            messages.warning(request, "Invalid username or password...!")
            return redirect(signup_page)
    else:
        messages.warning(request, "User not found...!")
        return redirect(signup_page)

def logout_page(request):
    del request.session['signup_name']
    del request.session['signup_pwd']
    messages.success(request, "Logout successfully...!")
    return redirect(Home_page)


def save_booking(request):
    if request.method == "POST":
        nm = request.POST.get('bname')
        ml = request.POST.get('bmail')
        mob = request.POST.get('bmob')
        ser = request.POST.get('bservice')
        snm = request.POST.get('bsname')
        pr = request.POST.get('bprice')
        dt = request.POST.get('bdate')
        tm = request.POST.get('btime')
        obj=Bookdb(book_user=nm, book_mail=ml, book_mob=mob, book_service=ser,book_sername=snm,book_price=pr, book_date=dt, book_time=tm)
        obj.save()
        subject = "Welcome to Nans Luxury Beauty Lounge"
        message = "Hello, " + obj.book_user + "!!\n" "Welcome to Nans Luxury Beauty Lounge!! \nYou have successfully booked your service \n \n Thanking you \n Nans admin"
        from_email = settings.EMAIL_HOST_USER
        to_list = [obj.book_mail]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        # messages.success(request, "Thank You, You have booked successfully!")
        return redirect(Home_page)


def bookingHair(request, sid):
    cat = CategoryDB.objects.all()
    hcat = Hairservicedb.objects.get(id=sid)
    data = Bookdb.objects.filter(book_user=request.session['signup_name'])
    return render(request, 'bookhair.html', {'hcat': hcat, 'data': data,'category':cat})


def bookingSkin(request, hid):
    cat = CategoryDB.objects.all()
    scat = Skinservicedb.objects.get(id=hid)
    data = Bookdb.objects.filter(book_user=request.session['signup_name'])
    return render(request, 'bookSkin.html', {'scat': scat, 'data': data,'category':cat})

def bookingNail(request, nid):
    cat = CategoryDB.objects.all()
    ncat = Nailservicedb.objects.get(id=nid)
    data = Bookdb.objects.filter(book_user=request.session['signup_name'])
    return render(request, 'booknail.html', {'ncat': ncat, 'data': data,'category':cat})

def bookingMakeup(request, mid):
    cat = CategoryDB.objects.all()
    mcat = Makeupservicedb.objects.get(id=mid)
    data = Bookdb.objects.filter(book_user=request.session['signup_name'])
    return render(request, 'bookmakeup.html', {'mcat': mcat, 'data': data,'category':cat})

def bookingBodycare(request, bid):
    cat = CategoryDB.objects.all()
    bcat = Bodycareservicedb.objects.get(id=bid)
    data = Bookdb.objects.filter(book_user=request.session['signup_name'])
    return render(request, 'bookbody.html', {'bcat': bcat, 'data': data,'category':cat})

def save_booking(request):
    if request.method == "POST":
        nm = request.POST.get('bname')
        ml = request.POST.get('bmail')
        mob = request.POST.get('bmob')
        ser = request.POST.get('bservice')
        snm = request.POST.get('bsname')
        pr = request.POST.get('bprice')
        dt = request.POST.get('bdate')
        tm = request.POST.get('btime')
        obj=Bookdb(book_user=nm, book_mail=ml, book_mob=mob, book_service=ser,book_sername=snm,book_price=pr, book_date=dt, book_time=tm)
        obj.save()
        subject = "Welcome to Nans Luxury Beauty Lounge"
        message = "Hello, " + obj.book_user + "!!\n" "Welcome to Nans Luxury Beauty Lounge!! \nYou have successfully booked your service \n \n Thanking you \n Nans admin"
        from_email = settings.EMAIL_HOST_USER
        to_list = [obj.book_mail]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        # messages.success(request, "Thank You, You have booked successfully!")
        return redirect(payment_page)


def Searchbarfind(request):
    cat = CategoryDB.objects.all()
    # Check if the form was submitted
    if request.method == "POST":
        searched_term = request.POST.get('searched', '')
        # Check if search term is empty
        if not searched_term:
            messages.warning(request, "Please enter here to search !")
            return render(request, 'searchbar_page.html')
        # Query the databases for matching entries
        hair_results = Hairservicedb.objects.filter(Hair_name__icontains=searched_term)
        skin_results = Skinservicedb.objects.filter(Skin_name__icontains=searched_term)
        nail_results = Nailservicedb.objects.filter(Nail_name__icontains=searched_term)
        makeup_results = Makeupservicedb.objects.filter(Makeup_name__icontains=searched_term)
        bodycare_results = Bodycareservicedb.objects.filter(Bodycare_name__icontains=searched_term)

        # Prepare context
        context = {
            'hair_results': hair_results,
            'skin_results': skin_results,
            'nail_results': nail_results,
            'makeup_results': makeup_results,
            'bodycare_results': bodycare_results,
            'cat':cat

        }
        # Provide feedback if results are limited
        # if len(searched_term) == 1 and not (hair_results or skin_results or nail_results or makeup_results or bodycare_results):
        #     messages.info(request,
        #                   "Searching with a single letter may not yield many results. Try using more characters for better results.")

        # Check if there are any results
        if not (hair_results or skin_results or nail_results or makeup_results or bodycare_results):
            messages.error(request, "Sorry..! Your search does not exist..Please Try Again")

        return render(request, 'searchbar_page.html', context)

    # For GET requests, render the page with empty context
    return render(request, 'searchbar_page.html',{'cat':cat})

def bookhistory(request):
    cat = CategoryDB.objects.all()
    un=request.session['signup_name']
    history= Bookdb.objects.filter(book_user=un)
    return render(request,"booking_history_page.html",{'history':history,'cat':cat})


def booking_pdf(request, booking_id):
    booking = get_object_or_404(Bookdb, pk=booking_id)
    # Create a HttpResponse object with PDF mime type
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="booking_{booking_id}.pdf"'

    # Create a canvas
    pdf = SimpleDocTemplate(response, pagesize=letter)
    styles = getSampleStyleSheet()

    title_style = styles['Title']
    title_style.fontSize = 24  # Increase title font size

    # Body style
    body_style = styles['BodyText']
    body_style.fontSize = 12  # Increase body text font size

    # Title
    title = Paragraph("Booking Details", styles['Title'])
    content = []
    # Add the logo image
    # logo_path ='Assets/img/nicon.png'
    # logo = Image(logo_path, width=100, height=100)
    # content.append(logo)
    space = Spacer(1, 20)  # 20 units of vertical space
    # Booking Information
    booking_info = [
        [" "],
        ["Booking Username:", str(booking.book_user)],
        ["Booking Category :", booking.book_service],
        ["Booking Service :", booking.book_sername],
        ["Booking Price :", booking.book_price],
        ["Check-in Date:", str(booking.book_date)],
        ["Check-in Time:", str(booking.book_time)],
        # Add more details as needed
    ]

    #  Booking Invoice Table Style
    table_style = TableStyle([
        # Row label style (first column)
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#cc712f')),  # Background for left-side headings
        ('TEXTCOLOR', (0, 0), (0, -1), colors.black),  # Text color for left-side headings
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),  # Align left-side headings to the left
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),  # Font for left-side headings
        ('FONTSIZE', (0, 0), (0, -1), 16),  # Increase font size for left-side headings
        ('LEFTPADDING', (0, 0), (0, -1), 15),  # Increase left padding for left-side headings
        ('RIGHTPADDING', (0, 0), (0, -1), 15),  # Increase right padding for left-side headings
        ('TOPPADDING', (0, 0), (-1, -1), 12),  # Increase padding for all cells
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),

        # Data style (second column)
        ('BACKGROUND', (1, 0), (1, -1), colors.HexColor('#f5d8c3')),  # Background for data cells
        ('TEXTCOLOR', (1, 0), (1, -1), colors.black),  # Text color for data cells
        ('ALIGN', (1, 0), (1, -1), 'LEFT'),  # Align data to the left
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),  # Font for data
        ('FONTSIZE', (1, 0), (1, -1), 14),  # Increase font size for data cells
        ('LEFTPADDING', (1, 0), (1, -1), 15),  # Increase left padding for data cells
        ('RIGHTPADDING', (1, 0), (1, -1), 15),  # Increase right padding for data cells

        # Remove grid lines
        ('LINEBELOW', (0, 0), (-1, 0), 0, colors.transparent),  # No line below the heading row
        ('LINEBELOW', (0, 0), (-1, -1), 0, colors.transparent),  # No line below any row
    ])
    # Create Table
    booking_table = Table(booking_info)
    booking_table.setStyle(table_style)

    # Add elements to content
    content.append(title)
    content.append(space)
    content.append(booking_table)

    # Build PDF
    pdf.build(content)

    return response

def payment_page(request):
    # Retrieve the latest Bookdb object
    customer = Bookdb.objects.order_by('-id').first()

    # Ensure customer is not None (handling edge cases)
    if customer is None:
        return render(request, "PaymentPage.html", {'error': 'No customer found'})

    # Get the payment amount of the specified customer
    payy = customer.book_price

    # Remove any currency symbols and strip whitespace
    if isinstance(payy, str):
        payy = payy.replace('Rs.', '').strip()

    # Check if payy is a valid number
    try:
        # Convert the amount to paisa (smallest currency unit)
        amount = int(float(payy) * 100)  # Assuming payment amount in Rs.
    except ValueError:
        return render(request, "PaymentPage.html", {'error': 'Invalid payment amount'})

    # Convert amount to string for printing (if needed)
    payy_str = str(amount)

    # Debugging: Printing each character of the payment amount (optional)
    for i in payy_str:
        print(i)

    if request.method == "POST":
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_6zd4gObhULgiip', 'J1js7FOoH93A0SV70GlKMN22'))
        payment = client.order.create({'amount': amount, 'currency': order_currency, 'payment_capture': '1'})
        # You can add additional logic to handle the created payment object

    return render(request, "PaymentPage.html", {'customer': customer, 'payy_str': payy_str})

def productpage(request):
    cat = CategoryDB.objects.all()
    pro = ServiceDB.objects.all()
    return render(request,"ProductsPage.html",{'category': cat,'pro':pro})

def single_prod(request, pid):
    cat = CategoryDB.objects.all()
    prod = ServiceDB.objects.get(id=pid)
    return render(request, "Single_product.html", {'category': cat, 'prod': prod})
def Cart_page(request):
    cat = CategoryDB.objects.all()
    data=mycart.objects.filter(cart_username=request.session['signup_name'])
    total_price = 0
    shipping_charge =0
    Total_sum=0
    for i in data:
        total_price = total_price+i.cart_totalprice
        if total_price < 200:
            shipping_charge = 50
        else:
            shipping_charge = 0
        Total_sum= total_price+shipping_charge

    return render(request, "cartPage.html", {'cat':cat,'data':data,'total_price':total_price,'Total_sum':Total_sum,'shipping_charge':shipping_charge})

def save_cart_products(request):
    if request.method == "POST":
        p = request.POST.get('Username')
        q = request.POST.get('prodname')
        r = request.POST.get('quantity')
        s = request.POST.get('total')
        obj1=mycart(cart_username=p, cart_productname=q, cart_qty=r, cart_totalprice=s)
        obj1.save()
        messages.success(request, "Added to cart..!")
        return redirect(Cart_page)

def delete_cart(request,cartid):
    data = mycart.objects.filter(id=cartid)
    data.delete()
    messages.success(request, "Products deleted successfully..!")
    return redirect(Cart_page)

def payment_product_page(request):
    # Retrieve the latest Bookdb object
    customer = mycart.objects.order_by('-id').first()

    # Ensure customer is not None (handling edge cases)
    if customer is None:
        return render(request, "PaymentProductPage.html", {'error': 'No customer found'})

    # Get the payment amount of the specified customer
    payy = customer.cart_totalprice

    # Remove any currency symbols and strip whitespace
    if isinstance(payy, str):
        payy = payy.replace('Rs.', '').strip()

    # Check if payy is a valid number
    try:
        # Convert the amount to paisa (smallest currency unit)
        amount = int(float(payy) * 100)  # Assuming payment amount in Rs.
    except ValueError:
        return render(request, "PaymentProductPage.html", {'error': 'Invalid payment amount'})

    # Convert amount to string for printing (if needed)
    payy_str = str(amount)

    # Debugging: Printing each character of the payment amount (optional)
    for i in payy_str:
        print(i)

    if request.method == "POST":
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_6zd4gObhULgiip', 'J1js7FOoH93A0SV70GlKMN22'))
        payment = client.order.create({'amount': amount, 'currency': order_currency, 'payment_capture': '1'})
        # You can add additional logic to handle the created payment object
        return redirect(Home_page)
    return render(request, "PaymentProductPage.html", {'customer': customer, 'payy_str': payy_str})