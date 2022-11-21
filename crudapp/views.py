from django.shortcuts import render,redirect
from crudapp.models import delete_user
import mysql.connector

# Create your views here.

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "crud"
)

mycursor = con.cursor()



def user(request):
    if request.method=="POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        password= request.POST.get('password')

        sql = "INSERT INTO users(name,email,phone,password) VALUES(%s,%s,%s,%s)"
        val = (name,email,phone,password)
        mycursor.execute(sql,val)
        con.commit()
    return render(request,'user.html')


def home(request):
    sql = "SELECT * FROM users"
    mycursor.execute(sql)
    results = mycursor.fetchall() 
    return render(request,"index.html",{'results':results})

def delte(request,id):
    # sql = "SELECT * FROM users"
    # mycursor.execute(sql)
    # results = mycursor._fetch_row()
    # delete ="DELETE FROM users WHERE id=results"
    # mycursor.execute(delete)
    # con.commit()
    delt_user =delete_user.objects.get(id=id)
    delt_user.delete()
    return redirect("/home")  

  
