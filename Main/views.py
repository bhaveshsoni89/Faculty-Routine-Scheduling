from django.shortcuts import render, redirect
from User_details.models import *
from Leave_Request.models import *
from Report.models import *
from Daily_activity.models import *
from Events.models import *
from User_details.forms import *
from Leave_Request.forms import *
from Report.forms import *
from Add_Subject.models import *
from Daily_activity.forms import *
from Main.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from smtplib import *
import smtplib
from django.contrib.auth.decorators import login_required
# import zerosms
from twilio.rest import Client


def index(request):
    templates = 'temp.html'
    context = {}
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.name = request.POST.get('name')
            form.email = request.POST.get('email')
            form.comment = request.POST.get('comments')

            from_email = 'info.faculty123@gmail.com'
            password = 'admin@pass'
            subject = 'Test mail form project'
            to = 'bhaveshsoni.soni89@gmail.com'
            message = 'Add_Subject : ' + subject + '\n' + form.name + '\n' + form.email + '\n' + form.comment

            try:
                smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
                smtpobj.starttls()
                smtpobj.login(from_email, password)
                smtpobj.sendmail(from_email, to, message)
                messages.success(request, 'Your request has been sent successfully !!!')
                smtpobj.close()
                return render(request, 'temp.html')

            except SMTPException:
                messages.error(request, ' Oops ! Mail Not Sent !!!')
                return render(request, 'temp.html')

        else:
            messages.error(request, "Oops ! Request could not sent !!!")
            return render(request, 'temp.html')

    else:
        return render(request, templates, context)


def Login(request):
    model = SignUp()
    username = model.email
    if request.method == "GET":
        if 'action' in request.GET:
            action = request.GET.get('action')
            if action == 'logout':
                if 'username' in request.session:
                    request.session.flush()
                    logout(request)
                    return redirect('Login')
        if 'username' in request.session:
            model.email = request.session['username']
            print(request.session.set_expiry(300))  # session lifetime in seconds(from now)
            print(request.session.get_expiry_date())  # datetime.datetime object which repre

    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST.get('email'), password=request.POST.get('password'))
            if user:
                if user.is_staff:

                    request.session['username'] = model.email
                    login(request, user)
                    messages.success(request, 'Successfully LoggedIn...')
                    return redirect('loggedIn')
                else:
                    return redirect('wait')
            else:
                messages.error(request, 'Invalid Credentials !!!')
                return redirect('Login')
        else:
            messages.error(request, 'Email or Password Incorrect !!!')
            return redirect('Login')
    return render(request, 'login(f).html', {'form': LoginForm(), 'username': model.email})


@login_required(login_url='/Login/')
def loggedIn(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            comments = request.POST.get('comments')

            from_email = ''
            password = ''
            subject = 'Test mail form project'
            to = ''
            message = 'Add_Subject : ' + subject + '\n' + name + '\n' + email + '\n' + comments

            try:
                smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
                smtpobj.starttls()
                smtpobj.login(from_email, password)
                smtpobj.sendmail(from_email, to, message)
                messages.success(request, 'Your request has been sent successfully')
                smtpobj.close()
                return render(request, 'loggedIn.html')

            except SMTPException:
                messages.error(request, ' Mail Not Sent !!!')
                return render(request, 'loggedIn.html')

        else:
            messages.error(request, "Request could not sent !!!")
            return render(request, 'loggedIn.html')
    else:
        if 'action' in request.GET:
            action = request.GET.get('action')
            if action == 'logout':
                if 'username' in request.session:
                    request.session.flush()
                    logout(request)
                    return redirect('Login')
        return render(request, 'loggedIn.html', {})


def signup(request):
    form = SignForm()
    model = SignUp()
    if request.method == "POST":
        form = SignForm(request.POST, request.FILES)
        if form.is_valid():
            model.name = request.POST.get('name')
            model.email = request.POST.get('email')
            form.password = request.POST.get('password')
            form.confirm = request.POST.get('confirm')
            model.dob = request.POST.get('dob')
            model.contact = request.POST.get('contact')
            model.gender = request.POST.get('gender')
            model.qualification = request.POST.get('qualification')
            model.experience = request.POST.get('experience')
            model.designation = request.POST.get('designation')
            model.profile = request.FILES['profile']
            try:
                User.objects.get(username=model.email)
                messages.error(request, 'User already exists !!!')
                return render(request, 'signup(f).html')
            except User.DoesNotExist:

                model.save(SignUp())
                User.objects.create_user(username=model.email, password=form.password, email=model.email,
                                         first_name=model.name)
                messages.success(request, 'Signup Successfully !!!')
                return render(request, 'login(f).html')

        else:
            messages.error(request, 'Please fill the form properly !!!')
            return redirect('signup')
    else:
        return render(request, 'signup(f).html', {'form': form})


@login_required(login_url='/Login/')
def report(request):
    templates = 'report.html'
    context = {}
    if request.method == "POST":
        form = ReportForm(request.POST)
        model = Report()
        if form.is_valid():
            model.Title = request.POST.get('Title')
            model.report = request.POST.get('report')
            model.sender = request.user.first_name
            model.save(report)
            messages.success(request, 'Report is generated successfully !!!')
            return render(request, 'loggedIn.html')
        else:
            messages.error(request, 'Oops ! Report can not generated !!! ')
            render(request, 'report.html')
    else:
        if 'action' in request.GET:
            action = request.GET.get('action')
            if action == 'logout':
                if 'username' in request.session:
                    request.session.flush()
                    logout(request)
                    return redirect('Login')
        return render(request, templates, context)


def wait(request):
    return render(request, 'Wait.html')


@login_required(login_url='/Login/')
def profile(request):
    if request.method == 'GET':
        if 'action' in request.GET:
            action = request.GET.get('action')
            if action == 'logout':
                if 'username' in request.session:
                    request.session.flush()
                    logout(request)
                    return redirect('Login')
        obj = SignUp.objects.filter(email=request.user)
        return render(request, 'profile.html', {'obj': obj})


@login_required(login_url='/Login/')
def daily(request):
    if request.method == 'POST':
        form = DailyForm(request.POST)
        model = DailyActivity()

        if form.is_valid:
            model.year = request.POST.get('select1')
            model.sub = request.POST.get('select2')
            model.lecture = request.POST.get('lecture')
            model.summary = request.POST.get('summary')
            model.faculty = request.user.first_name

            messages.success(request, 'You have successfully updated today&\'s activity !!!')
            model.save(DailyActivity())
            return render(request, 'loggedIn.html')
        else:
            messages.error(request, 'Couldn&#39;t update your activity !!!')
            return render(request, 'daily.html')
    else:
        if 'action' in request.GET:
            action = request.GET.get('action')
            if action == 'logout':
                if 'username' in request.session:
                    request.session.flush()
                    logout(request)
                    return redirect('Login')
        instance = Subject2ndYEar.objects.all()
        instance2 = Subject3rdYEar.objects.all()
        instance3 = Subject4thYEar.objects.all()
        return render(request, 'daily.html', {'instance': instance, 'instance1': instance2, 'instance3': instance3})


@login_required(login_url='/Login/')
def leave(request):
    form = LeaveForm()
    model = LeaveRequest()
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid:
            model.Application = request.POST.get('leave')
            model.Sender = request.user.first_name
            model.Sender_mail = request.user.email
            model.save(LeaveRequest())
            messages.success(request, 'Your request has been sent successfully')
            return render(request, 'loggedIn.html' )
        else:
            return render(request, 'leave.html')
    else:
        if 'action' in request.GET:
            action = request.GET.get('action')
            if action == 'logout':
                if 'username' in request.session:
                    request.session.flush()
                    logout(request)
                    return redirect('Login')
        print(request.user.first_name)
        return render(request, 'leave.html', {'form': form})


def events(request):
    if 'action' in request.GET:
        action = request.GET.get('action')
        if action == 'logout':
            if 'username' in request.session:
                request.session.flush()
                logout(request)
                return redirect('Login')
    event = AddEvent.objects.all().order_by('id')
    upevent = UpcomingEvent.objects.all()
    context = {'event': event, 'upevent': upevent}
    return render(request, 'event.html', context)


'''
def editProfile(request):
    post = get_object_or_404(SignUp, email=request.user)
    update = SignUp.objects.filter(email=request.user)
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            post.author = request.user
            post.save()
            return render(request, 'profile.html')

        else:
            messages.error(request, 'Oops! Profile Could not updated')
            return render(request, 'profile.html')
    else:
        if 'action' in request.GET:
            action = request.GET.get('action')
            if action == 'logout':
                if 'username' in request.session:
                    request.session.flush()
                    logout(request)
                    return redirect('Login')
        return render(request, 'edit.html', {'form': EditForm, 'update': update})
'''


def sendsms(request):
    form = SmsForm()
    if request.method == "POST":
        form = SmsForm(request.POST)
        if form.is_valid():
            form.sendto = request.POST.get('sendto')
            form.message = request.POST.get('message')
            account_sid = ''
            auth_token = ''
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                    body=form.message,
                    from_='',
                    to=form.sendto
                        )
            print(message.sid)
            # zerosms.sms(phno=sender, passwd=password, receivernum=form.sendto, message=form.message)
            messages.success(request, 'SMS sent successfully !!!')
            return render(request, 'sms_sending.html')
        else:
            messages.error(request, 'SMS not sent !!!')
            return render(request, 'sms_sending.html')
    else:
        return render(request, 'sms_sending.html', {'form': form})


def accept(request):
    instance = get_object_or_404(LeaveRequest, id=2)
    from_email = ''
    password = ''
    subject = 'Leave Granted'
    to = instance.Sender_mail
    message = 'Add_Subject : ' + subject + '\n' + 'Your leave request has been granted !!!'

    try:
        smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpobj.starttls()
        smtpobj.login(from_email, password)
        smtpobj.sendmail(from_email, to, message)
        messages.success(request, 'Leave Granted')
        smtpobj.close()
        return render(request, 'loggedIn.html')

    except SMTPException:
        messages.error(request, ' Mail Not Sent !!!')
        return HttpResponse('<h1>Thank you</h1>')


