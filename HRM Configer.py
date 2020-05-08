                         #### STARTING PAGE OF HRM ####
                       #### MCA 2rd YEAR MINI PROJRCT ####
                #### TEAM MAMBER :- AJEET & SHIVAM SHUKLA ####

from tkinter import *
from datetime import datetime
from time import time
import psycopg2
hrm = psycopg2.connect(
    user = 'postgres',
    host = 'localhost',
    password = '12345',
    database = 'hrm',
    port = '5432')
cur = hrm.cursor()

start = time()
root = Tk()
root.title('HOME RENT MANAGEMENT(HRM)...')
canvas = Canvas(root,width = 800,height = 700)
root.geometry('800x700+200+1')
photo = PhotoImage(file='F:\\Hi-tech\\house1.png')
canvas.create_image(0,0,image = photo,anchor=NW)
canvas.pack()
root.after(2000,root.destroy)
root.mainloop()

###############################################################################################################
###############################################################################################################
           ##### SING IN WINDOWS #####

def Singin():
    root = Tk()
    root.title('HOME RENT MANAGEMENT(HRM)....')
    root.geometry('800x700+200+1')
    canvas = Canvas(root,width = 800,height = 700)
    photo = PhotoImage(file='F:\\Hi-tech\\image1.png')
    canvas.create_image(0,0,image = photo, anchor = NW)
    canvas.create_text(205,88,fill='ghost white',text = 'UserName',anchor = W,font = ("purisa",20,'bold'))
    canvas.create_text(205,178,fill ='ghost white',text = 'Mobile No',anchor = W,font=('purisa',20,'bold'))
    canvas.create_text(205,268,fill ='ghost white',text = 'Email Id',anchor = W,font=('purisa',20,'bold'))
    canvas.create_text(205,358,fill ='ghost white',text = 'Aadhaar No',anchor = W,font=('purisa',20,'bold'))
    canvas.create_text(205,448,fill ='ghost white',text = 'Password',anchor = W,font=('purisa',20,'bold'))
    canvas.create_text(205,538,fill ='ghost white',text = 'Confirm Password',anchor = W,font=('purisa',20,'bold'))
    canvas.pack() 
    
    ##### The text code #####
    name = StringVar(value = '')
    Entry(root,justify = 'center',bd=4,textvariable = name,width =21,font =('vardana',25,'bold')).place(x=205,y=107)
    mobile = IntVar(value = '') 
    Entry(root,justify = 'center',bd=4,textvariable = mobile,width =21,font =('vardana',25,'bold')).place(x=205,y=197)
    email_id = StringVar(value = '')
    Entry(root,justify = 'center',bd=4,textvariable = email_id,width =21,font =('vardana',25,'bold')).place(x=205,y=287)
    aadhaar_no = IntVar(value = '')
    Entry(root,justify = 'center',bd=4,textvariable = aadhaar_no,width =21,font =('vadana',25,'bold')).place(x=205,y=377)
    password = StringVar(value = '')
    text5 = Entry(root,justify = 'center',bd=4,textvariable = password,width =21,font =('vardana',25,'bold')).place(x=205,y=467)
    con_password = StringVar(value = '')
    Entry(root,justify = 'center',show = '*',bd=4,textvariable = con_password,width =21,font =('vardana',25,'bold')).place(x=205,y=557)
    canvas.pack()
    email = ''
    aadhaar_card_no  = 0
    
    ##### DATABASE CODE #####       
    def save_detail():
        try:
            ##### MOBILE NO VALIDATION #####    
            mob_no = str(mobile.get())
            if(len(mob_no) == 10):
                global mobile_no
                mobile_no = mobile.get()
                
            else:
                canvas.create_text(518,175,fill ='ghost white',text=" (' PLEASE ENTER 10th DIGITS MOBILE NO ')",font=('arial',13,'bold'))
                
            ##### AADHAAR NO VALIDATION #####    
            aadhaarCard = str(aadhaar_no.get())
            if(len(aadhaarCard) == 12):
                global aadhaar_num
                aadhaar_num = aadhaar_no.get()
            else:
                canvas.create_text(555,358,fill ='ghost white',text=" (' PLEASE ENTER 12th DIGITS AADHAAR NO ')",font=('arial',13,'bold'))
               
            ##### PASSWORD VALIDATION #####    
            if(password.get() == con_password.get()):
                container = (1,name.get(),mobile_no,email_id.get(),aadhaar_num,password.get(),con_password.get())
                query = 'INSERT INTO registation Values(%s,%s,%s,%s,%s,%s,%s)'
                cur.execute(query,container)
                hrm.commit() 
                logindata()
            else:     
                canvas.create_text(610,540,fill ='ghost white',text=" (' PLEASE RECHECK THE PASSWORD ')",font=('arial',13,'bold'))
            
        except Exception as e:
            canvas.create_text(445,650,fill = 'ghost white',text='PLEASE  FILL  ALL  DETAIL',font=('arial',14,'bold'))
                   
    ##### The Login & Sunmit Buttion ###### 
    Button(root,padx=10,pady=4,bg='ghost white',bd='5',text='submit',font=('arial',14,'bold'),command = lambda:(save_detail())).place(x=205,y=620)
    Button(root,padx=20,pady=4,bg='ghost white',bd='0',text='login',font=('arial',17,'bold'),command = lambda:(logindata())).place(x=610,y=40)
    root.mainloop()

###############################################################################################################
###############################################################################################################

##### THE LOG IN PAGE ######   
def logindata():
    login = Toplevel()
    canvas = Canvas(login, width = 800,height = 700)
    login.geometry('800x700+200+1')
    photo = PhotoImage(file='F:\\Hi-tech\\image1.png')
    canvas.create_image(0,0,image=photo,anchor=NW)
    canvas.create_text(340,70,fill='ghost white',text = 'Login',anchor = W,font = ("purisa",30,'bold'))
    canvas.create_text(205,220,text="UserName",fill="ghost white",anchor = W,font=('purisa',20,'bold'))
    canvas.create_text(205,320,text="Password",fill='ghost white',anchor = W,font=('purisa',20,'bold'))
    
    user_name = StringVar(value='')
    Entry(login,justify = 'center',bd=4,textvariable = user_name,width = 21,font =('vardan',25,'bold')).place(x=205,y=240)
    password = StringVar(value ='')
    Entry(login,justify = 'center',bd=4,show='*', textvariable = password,width = 21,font =('vardana',25,'bold')).place(x=205,y=340)

    
    ##### DATABASE #####
    def verified_password():
        try:
            query1 = 'SELECT user_name,password,aadhaar_no,email_id FROM registation WHERE user_name = %s;'
            cur.execute(query1,[user_name.get()])
            hrm.commit()
            secure = cur.fetchall()
            global aadhaar_card_no
            aadhaar_card_no = secure[0][2]
            global email
            email = secure[0][3]
            if(secure[0][0] == user_name.get() and secure[0][1] == password.get()):
                switch()
            else:
                canvas.create_text(400,500,text = 'PLEASE  ENTER  VALID  USERNAME  &  PASSWORD',fill='ghost white',font=('arial',15,'bold'))
        except Exception as e:
            canvas.create_text(400,500,text = 'PLEASE  ENTER  VALID  USERNAME  &  PASSWORD',fill='ghost white',font=('arial',15,'bold'))
    canvas.pack()    
    ##### SUBMIT BUTTION #####
    Button(login,padx=10,pady=4,bg='ghost white',bd='5',text='submit',font=('arial',14,'bold'),command=lambda:(verified_password())).place(x=205,y=407)
    login.mainloop()
    
###############################################################################################################
###############################################################################################################
##### SWITCH THE ACCOUNT LANDLORD & RENT  #####
def switch():        
      switch = Toplevel() 
      canvas = Canvas(switch,width = 800,height = 700)
      switch.geometry('800x700+200+1')
      photo = PhotoImage(file = 'F:\Hi-tech\\image1.png')
      canvas.create_image(0,0,image = photo,anchor = NW)
      photo1 = PhotoImage(file='F:\\Hi-tech\\tenant.png')
      photo2 = PhotoImage(file='F:\\Hi-tech\\landlord.png')
         
      ##### LANDLORD AND TENANT BUTTON #####
      query = "SELECT aadhaar_no FROM tenant Where aadhaar_no = %s"
      cur.execute(query,[aadhaar_card_no])
      tenant_ad = cur.fetchall()
      
      def check_tenant():
          if(len(tenant_ad)!=0):
              pass
          else:
              landlord()
      query1 = "SELECT email_id FROM landlord Where email_id = %s"
      cur.execute(query1,[email])
      landlord_em = cur.fetchall()
      def check_landlord():
          if(len(landlord_em)!=0):
              pass
          else:
              tenantinfo()
      ##### LANDLORD OR TENANT BUTTON #####
      Button(switch,image = photo2,bd=0,command=lambda:(check_tenant())).place(x=200,y=210)
      Button(switch,image = photo1,bd=0,command=lambda:(check_landlord())).place(x=200,y=390)
      canvas.pack()
      switch.mainloop() 


####################################################################################################################
###############################################################################################################
##### LANDLORD RRGISTATION WINDOWS #####
def landlord():
      land = Toplevel()
      canvas = Canvas(land,width=800,height=700)
      land.geometry('800x700+200+1')
      photo = PhotoImage(file='F:\\Hi-tech\\image1.png')
      canvas.create_image(0,0,anchor=NW,image=photo)

      ##### TEXT INFO #####
      canvas.create_text(274,33,text='FirstName',fill='ghost white',font=('vardana',20,'bold'))
      canvas.create_text(274,118,text='LastName',fill='ghost white',font=('vardana',20,'bold'))
      canvas.create_text(240,204,text='State',fill='ghost white',font=('vardana',20,'bold'))
      canvas.create_text(235,290,text='City',fill='ghost white',font=('vardana',20,'bold'))
      canvas.create_text(240,374,text='Venu',fill='ghost white',font=('vardana',20,'bold'))
      canvas.create_text(242,460,text='Block',fill='ghost white',font=('vardana',20,'bold'))
      canvas.create_text(320,543,text='Number of Room',fill='ghost white',font=('vardana',20,'bold'))
      canvas.create_text(315,627,text='One Room Price',fill='ghost white',font=('vardana',20,'bold'))
      

      ##### ENTRY BLOCK #####
      f_name = StringVar(value ='')
      Entry(land,justify = 'center',bd=4,textvariable = f_name,width =21,font =('vardana',25,'bold')).place(x=205,y=50)

      l_name = StringVar(value='')
      Entry(land,justify = 'center',bd=4,textvariable = l_name,width =21,font =('vardana',25,'bold')).place(x=205,y=135)

      state = StringVar(value='')
      Entry(land,justify = 'center',bd=4,textvariable = state,width =21,font =('vardana',25,'bold')).place(x=205,y=220)

      city = StringVar(value='')
      Entry(land,justify = 'center',bd=4,textvariable = city,width =21,font =('vardana',25,'bold')).place(x=205,y=305)

      venu = StringVar(value='')
      Entry(land,justify = 'center',bd=4,textvariable = venu,width =21,font =('vardana',25,'bold')).place(x=205,y=390)

      block = StringVar(value='')
      Entry(land,justify = 'center',bd=4,textvariable = block,width =21,font =('vardana',25,'bold')).place(x=205,y=475)

      number_of_room = StringVar(value='')
      Entry(land,justify = 'center',bd=4,textvariable = number_of_room ,width =21,font =('vardana',25,'bold')).place(x=205,y=560)

      one_room_price = StringVar(value='')
      Entry(land,justify = 'center',bd=4,textvariable = one_room_price,width =21,font =('vardana',25,'bold')).place(x=205,y=645)

      ##### DATABASE CODE #####       
      def save_landroad_detail():
          try: 
              container = (f_name.get(),l_name.get(),state.get(),city.get(),venu.get(),"Block "+block.get(),number_of_room.get(),one_room_price.get(),email)
              query1 = "INSERT INTO landlord VALUES(1,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
              cur.execute(query1,container)
              hrm.commit()
              thanks()
          except Exception as e:
              canvas.create_text(298,670,text = 'PLEASE  FILL  ALL  DETAIL ',fill='ghost white',font=('arial',15,'bold'))
              
      canvas.pack()
      ##### SUBMIT BUTTON #####
      Button(land,padx=10,pady=5,bg='ghost white',bd='3',text='submit',font=('arial',14,'bold'),command = lambda:(save_landroad_detail())).place(x=642,y=643)
 
      ##### THANKS WINDOWS #####
      def thanks():
          tk = Toplevel()
          canvas = Canvas(tk,width=800,height=700)
          tk.geometry('800x700+200+1')
          photo1 = PhotoImage(file='F://Hi-tech//image1.png')
          canvas.create_image(0,0,image=photo1,anchor=NW)
          canvas.create_text(360,350,text='  Thanks\n      For\n  Visit Us',fill='ghost white',font=('arial',80,'bold'))
          canvas.pack()
          tk.mainloop()
      land.mainloop()
  
############################################################################################################################
############################################################################################################################
 
def tenantinfo():
    tenant = Toplevel()
    canvas = Canvas(tenant,width =800,height=700)
    tenant.geometry('800x700+200+1')
    photo = PhotoImage(file='F:\\Hi-tech\\image1.png')
    canvas.create_image(0,0,anchor=NW,image = photo,)
    
    date = datetime.today()
    current_date = " "+str(date.day)+' \\ '+str(date.month)+' \\ '+str(date.year)

               ##### NAME ENTRY #####
    canvas.create_text(610,70,fill='ghost white',text='Date:'+current_date,font=('arial',20,'bold'))
    canvas.create_text(275,115,fill='ghost white',text='First Name',font=('vardana',20,'bold'))
    canvas.create_text(275,210,fill='ghost white',text='Last Name',font=('vardana',20,'bold'))

               ##### GENDER CHOICE #####
    canvas.create_text(253,315,fill='ghost white',text='Gender',font=('vardana',20,'bold'))
    canvas.create_text(265,355,fill='ghost white',text='Mail',font=('vardana',17,'bold'))
    canvas.create_text(385,355,fill='ghost white',text='Femail',font=('vardana',17,'bold'))
    canvas.create_text(510,355,fill='ghost white',text='Other',font=('vardana',17,'bold'))

             ##### STATUS FOR RELACTIONSHIP #####
    canvas.create_text(248,400,fill='ghost white',text='Status',font=('vardana',20,'bold'))
    canvas.create_text(320,440,fill='ghost white',text='Single',font=('vardana',17,'bold'))
    canvas.create_text(500,440,fill='ghost white',text='Married',font=('vardana',17,'bold'))
    

    ##### DATABASE CODE #####
    def database():
          try:
              if(len(first_name.get()) > 0 and len(last_name.get()) > 0):
                  save_data = (aadhaar_card_no,first_name.get(),last_name.get(),var.get(),var1.get())
                  query = "INSERT INTO tenant VALUES(%s,%s,%s,%s,%s)"
                  cur.execute(query,save_data)
                  hrm.commit()
                  booking_venu()
              else:
                  canvas.create_text(320,610,fill ='ghost white',text=' PLEASE  FILL  ALL  DETAIL ',font=('vardana',15,'bold'))                  
          except Exception as e:
              canvas.create_text(320,610,text = 'PLEASE  FILL  ALL  DETAIL ',fill='ghost white',font=('arial',15,'bold'))
              
    ##### REDUCE STEP #####
    def alredy_user():
      try:
          query1 = "SELECT first_name,last_name FROM tenant where aadhaar_no = %s"
          cur.execute(query1,[aadhaar_card_no])
          tenant_name = cur.fetchall()
          digit = len(tenant_name)
          if(digit == 0):
              canvas.create_text(470,590,fill ='ghost white',text='YOU  ARE  NOT  REGISTED',font=('vardana',17,'bold'))
          else:
              alredy_user = tenant_name[0][0]+' '+tenant_name[0][1]
              select_duration()
      except Exception as e:
          canvas.create_text(470,590,fill ='ghost white',text='YOU  ARE  NOT  REGISTED',font=('vardana',17,'bold'))
          print(e)
    canvas.pack()
    
                    ##### RADIO BUTTON OF GENDER #####
    var = StringVar(value = '0')
    Radiobutton(tenant,bg = 'gray1',font = 30,value ='Mail',variable = var).place(x=303,y=340)
    Radiobutton(tenant,bg = 'gray1',font = 30,value ='Femail',variable = var).place(x=435,y=340)
    Radiobutton(tenant,bg = 'gray1',font = 30,value ='Other',variable = var).place(x=555,y=340)

     
                    ##### RADIO BUTTON GENDER #####
    var1 = StringVar(value ='0')
    Radiobutton(tenant,bg = 'gray1',font = 30,value ='single',variable = var1).place(x=370,y=425)
    Radiobutton(tenant,bg = 'gray1',font = 30,value ='married',variable = var1).place(x=555,y=425)
    
 
                   #### ENTRY BOX YOUR TEXT ####
    global first_name
    first_name = StringVar(value = '')
    Entry(tenant,justify = 'center',bd=4,textvariable = first_name,width = 21,font=('arial',25,'bold')).place(x=205,y=135)
    global last_name
    last_name = StringVar(value = '')   
    Entry(tenant,justify = 'center',bd=4,textvariable = last_name,width = 21,font=('arial',25,'bold')).place(x=205,y=230)
    Button(tenant,padx=10,pady=4,bg='ghost white',bd='5',text='submit',font=('arial',14,'bold'),command = lambda:(database())).place(x=205,y=506)
    Button(tenant,padx=10,pady=4,bg='ghost white',bd='5',text='If you already register',font=('arial',14,'bold'),command = lambda:(alredy_user())).place(x=350,y=506)
    tenant.mainloop()
    
######################################################################################################
############################################################################################################################
##### SELECT VENU/PLACE WINDOWS #####
def booking_venu():
    venu = Toplevel()
    canvas = Canvas(venu,width=800,height=700)
    venu.geometry('800x700+200+1')
    photo = PhotoImage(file ='F:\\Hi-tech\\image1.png')
    canvas.create_image(0,0,image=photo,anchor=NW)

    ##### DROP DOWN LIST NAME #####
    canvas.create_text(370,50,text='Select Venu',fill='ghost white',font=('arial',25,'bold'))
    canvas.create_text(118,150,text='State',fill='ghost white',font=('arial',20,'bold'))
    canvas.create_text(280,150,text='City',fill='ghost white',font=('arial',20,'bold'))
    canvas.create_text(460,150,text='Place',fill='ghost white',font=('arial',20,'bold'))
    canvas.create_text(635,150,text='Block',fill='ghost white',font=('arial',20,'bold'))
            
    #####  LIST BOX #####
    lbx = Listbox(venu,font=('vardana',15),width=50,height= 14,bg='Indianred4',fg='white')
    table = ['Landlord','Avaliable Room','Room Price']
    row_format1 = "{:<23}   {:<29}   {:}"
    row_format = "{:<33}   {:<38}   {:}"
    lbx.insert(0,row_format1.format(*table,sp=" "))
    lbx.insert(1,'__________________________________________________')
    lbx.place(x=50,y=320)
    canvas.pack()
    
    def check():
        if(clicked3.get()=='Vjay Nager'):
            lbx.delete(2,END)
            list_data()
        if(clicked3.get()=='Govind Puram'):
            lbx.delete(2,END)
            list_data1()
    ##### VJAY NAGER LANDLORD #####
    def list_data():
        ##### BLOCK A #####
        query = "SELECT first_name,number_of_room,one_room_price,block FROM landlord where block=%s And venu = %s"
        cur.execute(query,[clicked5.get(),clicked3.get()])
        no = 1
        global list_clon
        list_clon = cur.fetchall()
        for item in list_clon:
            no+=1
            lbx.insert(no,row_format.format(*item,sp=" "))
        lbx.insert(no+1,'*********************************************************************')
    
          
    ##### GOVIND PURAM LANDLORD #####                             
    def list_data1():
        query = "SELECT first_name,number_of_room,one_room_price,block FROM landlord where block=%s And venu = %s"
        cur.execute(query,[clicked4.get(),clicked3.get()])
        no = 1
        global list_clon
        list_clon = cur.fetchall()
        for item in list_clon:
            no+=1
            lbx.insert(no,row_format.format(*item,sp=" "))
        lbx.insert(no+1,'*********************************************************************')
          
        
    ##### STATES FOR THE DROP DOWN LIST #####
    state = ['Uttar Pradesh','Bhair']
    clicked1 = StringVar()
    clicked1.set('Select')
    drop1 =OptionMenu(venu,clicked1,*state,)
    drop1.config(width=10,font=('arial',10))
    drop1.place(x=85,y=175)

    ##### CITIES FOR THE DROP DOWN LIST #####
    cite = ['Ghazibad','Noida','Bulandshahr']
    clicked2 = StringVar()
    clicked2.set('Selcet')
    drop2=OptionMenu(venu,clicked2,*cite)
    drop2.config(width=10,font=('arial',10))
    drop2.place(x=255,y=175)

    def block_select(self):
        if('Govind Puram' == clicked3.get()):
            ##### DROP DOWN LIST FOR GOVIND PURAM BLOCK #####
            global clicked4
            no = 1
            block = ['Block A','Block B','Block C']
            clicked4 = StringVar()
            drop4 = OptionMenu(venu,clicked4,*block)
            drop4.config(width=10,font=('arial',10))
            drop4.place(x=600,y=175)
        else:
            
            ##### DROP DOWN LIST FOR VIJAY NAGER BLOCK  #####
            global clicked5
            block = ['Block A','Block B','Block C','Bolck D']
            clicked5 = StringVar()
            drop5 = OptionMenu(venu,clicked5,*block)
            drop5.config(width=10,font=('arial',10))
            drop5.place(x=600,y=175)
            
                  
    ##### CITIES FOR THE DROP DOWN LIST #####
    vplace = ['Vjay Nager','Govind Puram']
    clicked3 = StringVar()
    clicked3.set('Select')
    drop3=OptionMenu(venu,clicked3,*vplace,command=block_select)
    drop3.config(width=10,font=('arial',10))
    drop3.place(x=425,y=175)

    ##### DROP DOWN LIST BLOCK  #####
    value = ''
    clicked6 = StringVar()
    clicked6.set('Select')
    drop6 = OptionMenu(venu,clicked6,value)
    drop6.config(width=10,font=('arial',10))
    drop6.place(x=600,y=175)
    
    ##### DATABASE #####
    def database():
        try:
            index = lbx.curselection()
            global name
            name = list_clon[index[0]-2][0]

            query1 = "SELECT number_of_room from landlord where first_name = %s"
            cur.execute(query1,[name])
            room_no = cur.fetchall()
            Available_room = room_no[0][0] - 1
            
            full_name = first_name.get()+' '+last_name.get()
            query2 = "INSERT INTO landlordortenant(landlord_name,available_room_no,tenant_name) VALUES(%s,%s,%s)"
            cur.execute(query2,[name,Available_room,full_name])

            query3 = "UPDATE landlord SET number_of_room = %s Where first_name = %s"
            cur.execute(query3,[Available_room,name])
            hrm.commit()
      
            if(clicked3.get() == 'Govind Puram'):
                save_data = (clicked1.get(),clicked2.get(),clicked3.get(),clicked4.get(),name,aadhaar_card_no)      
            else:
                save_data = (clicked1.get(),clicked2.get(),clicked3.get(),clicked5.get(),name,aadhaar_card_no)
                  
            query4 = "UPDATE tenant SET state = %s,city = %s,venu = %s,block = %s ,landlord_name = %s WHERE aadhaar_no = %s"
            cur.execute(query4,save_data)
            hrm.commit()
            select_duration()
        except Exception as e:
            canvas.create_text(177,270,text = 'PLEASE  SELECT  ALL  DETAIL',fill='ghost white',font=('arial',17,'bold'))
            
    ##### SUBMIT OR CHECK BUTTTON #####
    Button(venu,padx=10,pady=4,bg='ghost white',bd='5',text='submit',font=('arial',14,'bold'),command=lambda:(database())).place(x=635,y=600)
    Button(venu,padx=10,pady=3,bg='ghost white',bd='5',text='Check',font=('arial',14,'bold'),command = check).place(x=610,y=230)  
    venu.mainloop()
######################################################################################################
##################################################################################################
###### SELECT-TIME DURATION ######
def select_duration():
    pay = Toplevel()
    canvas = Canvas(pay,width=800,height=700)
    pay.geometry('800x700+200+1')
    photo = PhotoImage(file='F:\\Hi-tech\\image1.png')
    canvas.create_image(0,0,image= photo,anchor=NW)
    canvas.create_text(190,150,text='Time Duration',fill='ghost white',font=('arial',20,'bold'))
    canvas.create_text(600,150,text='Select Month\'s',fill='ghost white',font=('arial',20,'bold'))
    canvas.create_text(155,385,text='Monthly',fill='ghost white',font=('arial',25,'bold'))
    canvas.create_text(515,385,text='One Time',fill='ghost white',font=('arial',25,'bold'))
    
    
    canvas.create_line(430,425,710,425,width = 10,fill='gray1')
    canvas.create_line(435,420,435,510,width = 10,fill='gray1')
    canvas.create_line(708,420,708,510,width = 12,fill='gray1')
    canvas.create_line(430,510,713,510,width = 10,fill='gray1')
    
    canvas.create_line(75,425,355,425,width = 10,fill='gray1')
    canvas.create_line(80,420,80,510,width = 10,fill='gray1')
    canvas.create_line(360,420,360,510,width = 10,fill='gray1')
    canvas.create_line(75,510,365,510,width = 10,fill='gray1')
    canvas.pack()
   
    Label(pay,bg='Indianred4',fg='white',padx = 130, pady = 5,text = '',font=('vardana',40,'bold')).place(x = 440,y = 430)
    Label(pay,bg='Indianred4',fg='white',padx = 133, pady = 5,text = '',font=('vardana',40,'bold')).place(x = 85,y = 430)
    
    ##### DROP DOWN OPTION #####
    month = []
    for i in range(0,12):
        month.append(str(i+1)+'th'+'Month')
    clicked1 = StringVar()
    clicked1.set('Select')
    drop = OptionMenu(pay,clicked1,*month,command = lambda a :(house_amount()))
    drop.config(width=10,font=('arial',10))
    drop.place(x=102,y=170)


    ##### DROP DOWN OPTION #####
    month = ['Junary','February','March','April','June','July','August','Setember','October','November','December']
    clicked2 = StringVar()
    clicked2.set('Select')
    drop = OptionMenu(pay,clicked2,*month)
    drop.config(width=10,font=('arial',10))
    drop.place(x=580,y=170)
    
######################################################################################################
######################################################################################################
    ##### CONFIRM DATA WINDOWS #####
    def confirm_data():
        query = "SELECT * from tenant where aadhaar_no = %s"
        cur.execute(query,[aadhaar_card_no])
        hrm.commit()
        result = cur.fetchall()
        confd = Toplevel()
        canvas = Canvas(confd,width = 800,height = 700)
        confd.geometry('800x800+200+1')
        photo = PhotoImage(file= 'F:\\Hi-Tech\\image1.png')
        canvas.create_image(0,0,image = photo,anchor = NW)
        canvas.create_text(390,60,text='Confidential Detail',fill='ghost white',font = ('arial',30,'bold'))
          
        address = ""+result[0][5]+' '+result[0][6]+'\n'+result[0][7]+' '+result[0][8]
          
        canvas.create_text(250,140,text='Aadhaar No',fill='ghost white',font = ('arial',20,'bold'))
        canvas.create_text(240,185,text='Frist Name',fill='ghost white',font = ('arial',20,'bold'))
        canvas.create_text(240,230,text='Last Name',fill='ghost white',font = ('arial',20,'bold'))
        canvas.create_text(218,275,text='Gender',fill='ghost white',font = ('arial',20,'bold'))
        canvas.create_text(210,320,text='Status',fill='ghost white',font = ('arial',20,'bold'))
        canvas.create_text(220,365,text='Address',fill='ghost white',font = ('arial',20,'bold'))
        canvas.create_text(260,435,text='Time Duration',fill='ghost white',font = ('arial',20,'bold'))
        canvas.create_text(210,480,text='Month',fill='ghost white',font = ('arial',20,'bold'))
        canvas.create_text(224,520,text='Payment',fill='ghost white',font = ('arial',20,'bold'))

        canvas.create_line(95,100,700,100,width = 10,fill='ghost white',dash=(8,8))
        canvas.create_line(100,110,100,565,width = 10,fill='ghost white',dash=(8,8))        
        canvas.create_line(695,95,695,580,width = 10,fill='ghost white',dash=(8,8))
        canvas.create_line(95,575,700,575,width = 10,fill='ghost white',dash=(8,8))
        canvas.pack() 
           
        Label(confd,text=result[0][0],bg = 'gray13',fg ='ghost white',font=('arial',15,'bold')).place(x=450,y=125)
        Label(confd,text=result[0][1],bg = 'gray13',fg ='ghost white',font=('arial',15,'bold')).place(x=450,y=170)
        Label(confd,text=result[0][2],bg = 'gray13',fg ='ghost white',font=('arial',15,'bold')).place(x=450,y=215)
        Label(confd,text=result[0][3],bg = 'gray13',fg ='ghost white',font=('arial',15,'bold')).place(x=450,y=260)
        Label(confd,text=result[0][4],bg = 'gray13',fg ='ghost white',font=('arial',15,'bold')).place(x=450,y=305)
        Label(confd,text=address,bg = 'gray20',fg ='ghost white',font=('arial',15,'bold')).place(x=450,y=350)
        Label(confd,text=result[0][9],bg = 'gray20',fg ='ghost white',font=('arial',15,'bold')).place(x=450,y=419)
        Label(confd,text=result[0][10],bg = 'gray20',fg ='ghost white',font=('arial',15,'bold')).place(x=450,y=464)
        Label(confd,text=result[0][11],bg = 'gray20',fg ='ghost white',font=('arial',15,'bold')).place(x=450,y=509)

        ##### PAY BUTTON #####
        Button(confd,padx=20,pady=3,bg='ghost white',bd='5',text='Pay',font=('arial',17,'bold'),command = lambda:(payment())).place(x=600,y=600)

######################################################################################################
######################################################################################################
    ##### PAYMENT WINDOWS #####
        def payment():
            qr = Toplevel()
            canvas = Canvas(qr,width=800,height=700)
            qr.geometry('800x700+200+1')
            photo = PhotoImage(file='F:\\Hi-tech\\image1.png')
            photo1 = PhotoImage(file='F:\\Hi-tech\\QR.png')
            canvas.create_image(0,0,image=photo,anchor=NW)
            canvas.create_image(100,100,image=photo1,anchor=NW)
            canvas.create_text(380,75,fill='ghost white',text='Scan and Pay',font=('arial',30,'bold'))
            canvas.pack()
            qr.mainloop() 
        confd.mainloop()
        
    ##### DATABASE #####
    def house_amount():    
        query = "SELECT one_room_price FROM landlord WHERE first_name = %s"
        cur.execute(query,[name])
        price = cur.fetchone()
        global amount
        amount = price[0]
        Label(pay,bg='Indianred4',fg ='white',padx = 43, pady = 5,text = str(amount)+',rs',font=('vardana',40,'bold')).place(x = 85,y = 430)    
        
        Allmonth = []
        for i in range(0,13):
            Allmonth.append(str(i)+'-th'+'Month')
       
        for a in range(0,13):
            if(Allmonth[a]==clicked1.get()):
                #a+=1
                break
        if(a <= 5):
            global total_amount
            total_amount = a * price[0]
            Label(pay,bg='Indianred4',fg='white',padx = 22, pady = 5,text = str(total_amount)+',rs',font=('vardana',40,'bold')).place(x = 440,y = 430)

        elif(a >= 5 or a <= 10):
            total_amount = a * price[0]
            Label(pay,bg='Indianred4',fg='white',padx = 15, pady = 5,text = str(total_amount)+',rs',font=('vardana',40,'bold')).place(x = 440,y = 430)
            
        else:    
            total_amount = a * price[0]
            Label(pay,bg='Indianred4',fg='white',padx = 18, pady = 5,text = str(total_amount)+',rs',font=('vardana',40,'bold')).place(x = 440,y = 430)
            
    ##### DATABASE CODE #####               
    def database():
        if(radval.get() == 1):
            remain_cost = total_amount - amount
            pad_amount = amount   
        else: 
            remain_cost = 0
            pad_amount = total_amount
           
        full_name = first_name.get()+' '+last_name.get()
        query1 = "UPDATE landlordortenant SET pay_amount =%s,remain_amount =%s,total_amount =%s,time_duration =%s Where tenant_name =%s"
        cur.execute(query1,[pad_amount,remain_cost,total_amount,clicked1.get(),full_name])
        
        save_data = (clicked1.get(),clicked2.get(),amount,aadhaar_card_no)
        query2 = "UPDATE tenant SET time_duration = %s,month =%s,pay_amount=%s WHERE aadhaar_no = %s"
        cur.execute(query2,save_data)
        hrm.commit()
        confirm_data()

    ##### RADIO BUTTON #####    
    radval = IntVar(value = 2)
    Radiobutton(pay,variable = radval,value = 1,bg='gray1').place(x=230,y=374)
    Radiobutton(pay,variable = radval,value = 0,bg='gray1').place(x=605,y=374)

    ##### SUBMIT BUTTON #####
    Button(pay,padx=10,pady=4,bg='ghost white',bd='5',text='Submit',font=('arial',17,'bold'),command=lambda:(database())).place(x=570,y=560)   
    pay.mainloop()

Singin()





