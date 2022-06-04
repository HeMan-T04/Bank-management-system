import pymysql

def displayall():
    try:
        cn=pymysql.connect(host="localhost",user="root",password="%s"%(q),db="banking")
        cursor=cn.cursor()
        count=cursor.execute("select * from accountdetails")
        rs=cursor.fetchall()
        for record in rs:
            print(record)
        cn.close()
    except:
        print("\033[0;37;40munable to connect with database")
    

def createaccount():
    cn=pymysql.connect(host="localhost",user="root",password="%s"%(q),db="banking")
    try:
        a=int(input("\033[0;37;40mEnter account number"))
        b=input("\033[0;37;40mEnter account holder name")
        c=input("\033[0;37;40mEnter type of account")
        d=int(input("\033[0;37;40mEnter amount deposited"))
        e=input("\033[0;37;40mEnter address of account holder")
        f=input("\033[0;37;40mEnter state account holder living in")
        g=input("\033[0;37;40mEnter country")
        h=input("\033[0;37;40mEnter Date of birth")
        i=input("\033[0;37;40mEnter account open date")
        j=int(input("\033[0;37;40mEnter aadhar number"))
        k=int(input("\033[0;37;40mEnter pan number if available (if not put'00')"))
        l=int(input("\033[0;37;40mEnter locker number if available (if not put'00')"))
        m=input("\033[0;37;40mEnter passbook number ")
        n=input("\033[0;37;40mEnter debitcard number if available (if not put'--')")
        o=input("\033[0;37;40mEnter creditcard number if available (if not put'--')")
        p=input("\033[0;37;40mEnter password if available (if not put'--')")
        cursor=cn.cursor()
        n=cursor.execute("insert into accountdetails values(%s,'%s','%s',%s,'%s','%s','%s','%s','%s',%s,%s,%s,'%s','%s','%s','%s')" %(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p))
        if(n>0):
            print("\033[0;37;40mRecord inserteded successfully")
            cn.commit()
        else:
            cn.rollback()
    except:
        print("\033[0;37;40mError")
        cn.rollback()
    cn.close()

def deleteaccount():
    cn=pymysql.connect(host="localhost",user="root",password="%s"%(q),db="banking")
    try:
        x=int(input("\033[0;37;40mEnter account number to be deleted"))
        cursor=cn.cursor()
        n=cursor.execute("delete from accountdetails where accno=%s"%(x))
        if(n>0):
            print("\033[0;37;40mRecord deleted successfully")
            cn.commit()
        else:
            print("\033[0;37;40mRecord not Found")
    except:
        print("\033[0;37;40merror")
        cn.rollback()
    cn.close()

def withdraw():
    try:
        cn=pymysql.connect(host="localhost",user="root",password="%s"%(q),db="banking")
        cursor=cn.cursor()
        x=int(input("\033[0;37;40mENTER ACCOUNT NO."))
        n=cursor.execute("select * from accountdetails where accno=%s"%(x))
        rs=cursor.fetchone()
        if n==1:
            print(rs[0],',',rs[1],',',rs[2],',',rs[3])
            y=int(input("\033[0;37;40mEnter amount to withdraw"))
            #   yes or no
            if rs[3]>=y:
                cursor.execute("update accountdetails set amount=amount-%s where accno=%s"%(y,x))
                cn.commit()
                print("\033[0;37;40mBalance after withdrawl is ",rs[3]-y)
            else:
                print("\033[0;37;40mWithdrawl is not possible. Balance is insufficient")
                cn.rollback()
        else:
            print("\033[0;37;40mCustomer account number is not valid")
    except:
        print("\033[0;37;40mUnable to connect")    
    cn.close()

def deposit():
    try:
        cn=pymysql.connect(host="localhost",user="root",password="%s"%(q),db="banking")
        cursor=cn.cursor()
        x=int(input("\033[0;37;40mENTER ACCOUNT NO."))
        n=cursor.execute("select * from accountdetails where accno=%s"%(x))
        rs=cursor.fetchone()
        if n==1:       #if rs is not None
            print(rs[0],',',rs[1],',',rs[2],',',rs[3])
            y=int(input("\033[0;37;40mEnter Amount to be deposited"))
            cursor.execute("update accountdetails set amount=amount+%s where accno=%s"%(y,x))
            cn.commit()
            print("\033[0;37;40mNew Amount is ",rs[3]+y)
        else:
            print("\033[0;37;40mAccount number is not valid. Transaction Aborted")
            cn.rollback()
    except:
         print("\033[0;37;40munable to connect with database")
    cn.close()

def searchbyaccountno():
    try:
        cn=pymysql.connect(host="localhost",user="root",password="%s"%(q),db="banking")
        cursor=cn.cursor()
        x=int(input("\033[0;37;40mEnter account number whose details are to be shown"))
        n=cursor.execute("select * from accountdetails where accno=%s"%(x))
        rs=cursor.fetchone()
        if rs is not None:
            print(rs)
        else:
            print("\033[0;37;40mRecord not found")
    except:
        print("\033[0;37;40mCannot connect to the database")
    cn.close()

def searchbyname():
    try:
        cn=pymysql.connect(host="localhost",user="root",password="%s"%(q),db="banking")
        cursor=cn.cursor()
        x=input("\033[0;37;40mEnter account holder name whose details are to be shown")
        n=cursor.execute("select * from accountdetails where name='%s'"%(x))
        rs=cursor.fetchone()
        if rs is not None:
            print(rs)
        else:
            print("\033[0;37;40mRecord not found")
    except:
        print("\033[0;37;40mCannot connect to the database")
    cn.close()

def searchbytypeofacc():
    try:
        cn=pymysql.connect(host="localhost",user="root",password="%s"%(q),db="banking")
        cursor=cn.cursor()
        x=input("\033[0;37;40mEnter the type of account")
        n=cursor.execute("select * from accountdetails where typeofacc='%s'"%(x))
        rs=cursor.fetchall()
        if rs is not None:
            print(rs)
        else:
            print("\033[0;37;40mRecord not found")
    except:
        print("\033[0;37;40mCannot connect to the database")
    cn.close()
def checkbalance():
    try:
        cn=pymysql.connect(host="localhost",user="root",password="%s"%(q),db="banking")
        cursor=cn.cursor()
        x=int(input("\033[0;37;40mEnter account number whose details are to be shown"))
        n=cursor.execute("select * from accountdetails where accno=%s"%(x))
        rs=cursor.fetchone()
        if rs is not None:
            print(rs[0],',',rs[1],',',rs[2],',',rs[3])
        else:
            print("\033[0;37;40mRecord not found")
    except:
        print("\033[0;37;40mCannot connect to the database")
    cn.close()
def searchbyaadharnumber():
    cn=pymysql.connect(host="localhost",user="root",password="%s"%(q),db="banking")
    try:
        x=input("\033[0;37;40mEnter aadhar number to search")
        cursor=cn.cursor()
        n=cursor.execute("select * from accountdetails where aadharno=%s"%(x))
        rs=cursor.fetchall()
        if(n>0):
            for record in rs:
                print(record)
        else:
            print("\033[0;37;40mRecord is not present")
    except:
        print("\033[0;37;40mError in data handling....Process stopped")
    cn.close()
def searchbypan():
    cn=pymysql.connect(host="localhost",user="root",password="%s"%(q),db="banking")
    try:
        x=int(input("\033[0;37;40mEnter PAN number to search"))
        if x==0:
            print("\033[0;37;40mthere is no pan number given by customer") 
            pass
        else:
            cursor=cn.cursor()
            n=cursor.execute("select * from accountdetails where pan=%s"%(x))
            rs=cursor.fetchall()
            if(n>0):
                for record in rs:
                    print(record)
            else:
                print("\033[0;37;40mRecord is not present")
    except:
        print("\033[0;37;40mError in data handling....Process stopped")
    cn.close()
def searchbycreditcardno():
    cn=pymysql.connect(host="localhost",user="root",password="%s"%(q),db="banking")
    try:
        x=input("\033[0;37;40mEnter creditcard number to search")
       
        cursor=cn.cursor()
        n=cursor.execute("select * from creditcard where creditcardno=%s"%(x))
        rs=cursor.fetchall()
        if(n>0):
            for record in rs:
                print(record)
        else:
            print("\033[0;37;40mRecord is not present")
    except:
        print("\033[0;37;40mError in data handling....Process stopped")
    cn.close()
def searchbydebitcardno():
    cn=pymysql.connect(host="localhost",user="root",password="%s"%(q),db="banking")
    try:
        x=input("\033[0;37;40mEnter debitcard number to search")
        cursor=cn.cursor()
        n=cursor.execute("select * from debitcard where debitcardno=%s"%(x))
        rs=cursor.fetchall()
        if(n>0):
            for record in rs:
                print(record)
        else:
            print("\033[0;37;40mRecord is not present")
    except:
        print("\033[0;37;40mError in data handling....Process stopped")
    cn.close()
def createdebitcard():
    cn=pymysql.connect(host="localhost",user="root",password="%s"%(q),db="banking")
    try:
        a=input("\033[0;37;40mEnter account number")
        y=input("\033[0;37;40mEnter debit card holder name")
        z=input("\033[0;37;40mEnter debit card number")
        b=input("\033[0;37;40mEnter issue date")
        c=input("\033[0;37;40mEnter cvv")
        d=input("\033[0;37;40mEnter PIN")
        cursor=cn.cursor()
        n=cursor.execute("insert into debitcard values('%s','%s','%s','%s','%s','%s')" %(a,y,z,b,c,d))
        if(n>0):
            cn.commit()
        else:
            cn.rollback()
        v=cursor.execute("select * from accountdetails where accno='%s'"%(a))
        rs=cursor.fetchone()
        if v==1:
            print(rs[0],',',rs[1],',',rs[2],',',rs[3])
            if rs[13]=='--':
                cursor.execute("update accountdetails set debitcardno='%s' where accno='%s'"%(z,a))
                cn.commit()
                print("\033[0;37;40mdebitcard created successfully")
            else:
                print("\033[0;37;40mdebit card already available")
                cn.rollback()
    except:
        print("\033[0;37;40aDebit Card already available")
        cn.rollback()
    cn.close() 
def createcreditcard():
    cn=pymysql.connect(host="localhost",user="root",password="%s"%(q),db="banking")
    try:
        a=int(input("\033[0;37;40mEnter account number"))
        y=input("\033[0;37;40mEnter credit card holder name")
        z=input("\033[0;37;40mEnter credit card number")
        b=input("\033[0;37;40mEnter issue date")
        c=input("\033[0;37;40mEnter cvv")
        d=input("\033[0;37;40mEnter PIN")
        e=input("\033[0;37;40mEnter Loanpending")
        cursor=cn.cursor()
        n=cursor.execute("insert into creditcard values(%s,'%s','%s','%s','%s','%s','%s')" %(a,y,z,b,c,d,e))
        if(n>0):
            cn.commit()
        else:
            cn.rollback()
        v=cursor.execute("select * from accountdetails where accno=%s"%(a))
        rs=cursor.fetchone()
        if v==1:
            print(rs[0],',',rs[1],',',rs[2],',',rs[3])
            if rs[14]=='--':
                cursor.execute("update accountdetails set creditcardno=%s where accno=%s"%(z,a))
                cn.commit()
                print("\033[0;37;40mcreditcard created successfully")
            else:
                print("\033[0;37;40mcreditcard already available")
                cn.rollback()
    except:
        print("\033[0;37;40merror")
        cn.rollback()
    cn.close()
def deletecreditcard():
    cn=pymysql.connect(host="localhost",user="root",password="%s"%(q),db="banking")
    try:
        x=input("\033[0;37;40mEnter account number whose credit card to be deleted")
        cursor=cn.cursor()
        n=cursor.execute("delete from creditcard where accno='%s'"%(x))
        if(n>0):
            cn.commit()
        else:
            print("\033[0;37;40mRecord not Found")
        z="--"
        m=cursor.execute("update accountdetails set creditcardno='%s' where accno='%s'"%(z,x))
        v=cursor.execute("select * from accountdetails where accno=%s"%(x))
        rs=cursor.fetchone()
        print(rs[0],',',rs[1],',',rs[2],',',rs[3])
        if(m>0):
            print("\033[0;37;40mCredit Card removed successfully")
            cn.commit()
        else:
            print("\033[0;37;40mRecord not Found")
        
    except:
        print("\033[0;37;40merror")
        cn.rollback()
    cn.close()
def deletedebitcard():
    cn=pymysql.connect(host="localhost",user="root",password="%s"%(q),db="banking")
    try:
        x=input("\033[0;37;40mEnter account number whose debit card to be deleted")
        cursor=cn.cursor()
        n=cursor.execute("delete from debitcard where accno='%s'"%(x))
        if(n>0):
            cn.commit()
        else:
            print("\033[0;37;40mRecord not Found")
        z="--"
        m=cursor.execute("update accountdetails set debitcardno='%s' where accno='%s'"%(z,x))
        v=cursor.execute("select * from accountdetails where accno=%s"%(x))
        rs=cursor.fetchone()
        print(rs[0],',',rs[1],',',rs[2],',',rs[3])
        if(m>0):
            print("\033[0;37;40mDebit Card removed successfully")
            cn.commit()
        else:
            print("\033[0;37;40mRecord not Found")
        
    except:
        print("\033[0;37;40merror")
        cn.rollback()
    cn.close()
def Checkloanpending():
    try:
        cn=pymysql.connect(host="localhost",user="root",password="%s"%(q),db="banking")
        cursor=cn.cursor()
        x=int(input("\033[0;37;40mEnter account number whose details are to be shown"))
        n=cursor.execute("select * from creditcard where accno=%s"%(x))
        rs=cursor.fetchone()
        if rs is not None:
            print(rs[0],',',rs[1],',',rs[2])
            print("\033[0;37;40mYOUR LOAN PENDING IS ",rs[6])
        else:
            print("\033[0;37;40mRecord not found")
    except:
        print("\033[0;37;40mCannot connect to the database")
    cn.close()
def Dpinchange():
    cn=pymysql.connect(host="localhost",user="root",password="%s"%(q),db="banking")
    try:
        x=input("\033[0;37;40mEnter Account Number whose Debit Card pin is to be updated")
        y=input("\033[0;37;40mEnter New PIN")
        cursor=cn.cursor()
        N=cursor.execute("update debitcard set pin='%s' where accno='%s'" %(y,x))
        if(N>0):
            print("\033[0;37;40mRecord updated successfully")
            cn.commit()
        else:
            print("\033[0;37;40mRecord not found")
    except:
        print("\033[0;37;40merror")
        cn.rollback()
    cn.close()
def Cpinchange():
    cn=pymysql.connect(host="localhost",user="root",password="%s"%(q),db="banking")
    try:
        x=int(input("\033[0;37;40mEnter Account Number whose Credit Card pin is to be updated"))
        y=int(input("\033[0;37;40mEnter New PIN"))
        cursor=cn.cursor()
        N=cursor.execute("update creditcard set pin=%s where accno=%s" %(y,x))
        if(N>0):
            print("\033[0;37;40mRecord updated successfully")
            cn.commit()
        else:
            print("\033[0;37;40mRecord not found")
    except:
        print("\033[0;37;40merror")
        cn.rollback()
    cn.close()
def updateaddress():
    cn=pymysql.connect(host="localhost",user="root",password="%s"%(q),db="banking")
    try:
        x=input("\033[0;37;40mEnter Account Number whose Address is to be updated")
        y=input("\033[0;37;40mEnter New Address")
        cursor=cn.cursor()
        N=cursor.execute("update accountdetails set address='%s' where accno='%s'" %(y,x))
        if(N>0):
            print("\033[0;37;40mRecord updated successfully")
            cn.commit()
        else:
            print("\033[0;37;40mRecord not found")
    except:
        print("\033[0;37;40merror")
        cn.rollback()
    cn.close()
def updatestate():
    cn=pymysql.connect(host="localhost",user="root",password="%s"%(q),db="banking")
    try:
        x=input("\033[0;37;40mEnter Account Number whose State is to be updated")
        y=input("\033[0;37;40mEnter New State")
        cursor=cn.cursor()
        N=cursor.execute("update accountdetails set state='%s' where accno='%s'" %(y,x))
        if(N>0):
            print("\033[0;37;40mRecord updated successfully")
            cn.commit()
        else:
            print("\033[0;37;40mRecord not found")
    except:
        print("\033[0;37;40merror")
        cn.rollback()
    cn.close()
def updatecountry():
    cn=pymysql.connect(host="localhost",user="root",password="%s"%(q),db="banking")
    try:
        x=int(input("\033[0;37;40mEnter Accno whose country needs to be updated"))
        y=input("\033[0;37;40mEnter New Country")
        cursor=cn.cursor()
        N=cursor.execute("update emp set country=%s where accno=%s" %(y,x))
        if(N>0):
            print("\033[0;37;40mRecord updated successfully")
            cn.commit()
        else:
            print("\033[0;37;40mRecord not found")
    except:
        print("\033[0;37;40merror")
        cn.rollback()
    cn.close()
def Addpan():
    cn=pymysql.connect(host="localhost",user="root",password="%s"%(q),db="banking")
    try:
        x=int(input("\033[0;37;40mEnter Accno whose PAN needs to be updated"))
        y=int(input("\033[0;37;40mEnter New PAN"))
        cursor=cn.cursor()
        N=cursor.execute("update emp set pan=%s where accno=%s" %(y,x))
        if(N>0):
            print("\033[0;37;40mRecord updated successfully")
            cn.commit()
        else:
            print("\033[0;37;40mRecord not found")
    except:
        print("\033[0;37;40merror")
        cn.rollback()
    cn.close()
def updatelockerno():
    cn=pymysql.connect(host="localhost",user="root",password="%s"%(q),db="banking")
    try:
        x=int(input("\033[0;37;40mEnter Accno whose locker no. needs to be updated"))
        y=int(input("\033[0;37;40mEnter New Locker No."))
        cursor=cn.cursor()
        N=cursor.execute("update emp set lockerno=%s where accno=%s" %(y,x))
        if(N>0):
            print("\033[0;37;40mRecord updated successfully")
            cn.commit()
        else:
            print("\033[0;37;40mRecord not found")
    except:
        print("\033[0;37;40merror")
        cn.rollback()
    cn.close()
def removelocker():
    cn=pymysql.connect(host="localhost",user="root",password="%s"%(q),db="banking")
    try:
        x=input("\033[0;37;40mEnter account number whose locker to be removed")
        z='0'
        cursor=cn.cursor()
        n=cursor.execute("update accountdetails set lockerno='%s' where accno='%s'"%(z,x))
        if(n>0):
            cn.commit()
            print("\033[0;37;40mlocker removed succesfully")
        else:
            print("\033[0;37;40mno locker available to be removed")
    except:
        print("\033[0;37;40merror")
        cn.rollback()
    cn.close()
def updatepassword():
    cn=pymysql.connect(host="localhost",user="root",password="%s"%(q),db="banking")
    try:
        x=int(input("\033[0;37;40mEnter Accno whose password needs to be updated"))
        y=int(input("\033[0;37;40mEnter New Password"))
        cursor=cn.cursor()
        N=cursor.execute("update emp set password=%s where accno=%s" %(y,x))
        if(N>0):
            print("\033[0;37;40mRecord updated successfully")
            cn.commit()
        else:
            print("\033[0;37;40mRecord not found")
    except:
        print("\033[0;37;40merror")
        cn.rollback()
    cn.close()

q=input("enter your SQL password(DO NOT ENTER YOUR SQL PASSWORD INCORRECT OR WILL CAUSE AN ERROR)")

def intro():
    print("\t\t\t\t**********************")
    print("\t\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t\t\t**********************")
    
    
intro()
x=input("enter whether you are EMPLOYEE OR CUSTOMER->")
y="123456789"
if (x.upper())=="EMPLOYEE":
    p=input("ENTER PASSWORD:")
    if p==y:
        pass
    else:
        print("WRONG PASSWORD")
        exit()

while (x.upper())=="EMPLOYEE":
    print("1. Display All Records")
    print("2. Create Account")
    print("3. Delete Account")
    print("4. Create Debit Card")
    print("5. Create Credit Card")
    print("6. Search by Account Number")
    print("7. Search by Name")
    print("8. Search By Type of Account")
    print("9. Search By Aadhar Number")
    print("10. Search By PAN Number")
    print("11. Search By Credit Card Number")
    print("12. Search By Debit Card Number")
    print("13. Delete Credit Card")
    print("14. Delete Debit Card")
    print("15. Update Address")
    print("16. Update State")
    print("17. Update Country")
    print("18. Add PAN")
    print("19. Add/Update Locker Number")
    print("20. Remove Locker")
    print("21. Add/Update Password")
    ch=int(input("Enter your choice"))
    if ch==1:
        displayall()
    elif ch==2:
        createaccount()
    elif ch==3:
        deleteaccount()
    elif ch==4:
        createdebitcard()
    elif ch==5:
        createcreditcard()
    elif ch==6:
        searchbyaccountno()
    elif ch==7:
        searchbyname()
    elif ch==8:
        searchbytypeofacc()
    elif ch==9:
        searchbyaadharnumber()
    elif ch==10:
        searchbypan()
    elif ch==11:
        searchbycreditcardno()
    elif ch==12:
        searchbydebitcardno()
    elif ch==13:
        deletecreditcard()
    elif ch==14:
        deletedebitcard()
    elif ch==15:
        updateaddress()
    elif ch==16:
        updatestate()
    elif ch==17:
        updatecountry()
    elif ch==18:
        Addpan()
    elif ch==19:
        updatelockerno()
    elif ch==20:
        removelocker()
    elif ch==21:
        updatepassword()
    else:
        print("\t\t\t\tBrought To You By:")
        print("\t\t\t\tHemant & Vasudev")
        break
while x=="CUSTOMER":
    print("1. WITHDRAW MONEY ")
    print("2. DEPOSIT MONEY")
    print("3. CHECK BALANCE")
    print("4. CHECK LOAN PENDING")
    print("5. CHANGE DEBIT CARD PIN")
    print("6. CHANGE CREDIT CARD PIN")
    ch=int(input("Enter your choice"))
    if ch==1:
        withdraw()
    elif ch==2:
        deposit()
    elif ch==3:
        checkbalance()
    elif ch==4:
        Checkloanpending()
    elif ch==5:
        Dpinchange()
    elif ch==6:
        Cpinchange()
    else:
        print("\033[0;37;40m\t\t\t\tBrought To You By:")
        print("\033[0;37;40m\t\t\t\tHemant & Vasudev")
        break
   