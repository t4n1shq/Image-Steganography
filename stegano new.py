from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext as scroll
from tkinter.ttk import Treeview,Scrollbar
from PIL import Image
from PIL import ImageTk as itk
import os
import hashlib
import tkinter.messagebox
import mysql.connector as con

obj = con.connect(host='localhost',user='root',passwd='lu44y',database='stego_user')
cursor = obj.cursor()

cursor.execute('select username,password from user')
user_pass_list = cursor.fetchall(); c=0
obj.close()

user_list=[]
# pass_list=[]
for name in user_pass_list:
    user_list.append(name[0])
    # pass_list.append(name[1])
    c+=1

def raise_frame(frame):
    frame.tkraise()

main = Tk()
# main window title and icon 
main.title('STEGANOGRAPHY')
icon = itk.PhotoImage(file = 'C:\\Users\\tanis\\OneDrive\\Pictures\\lock-icon.jpg')
main.iconphoto(True,icon)

# all frames with dimensions
login = Frame(main, width = 873, height = 300)
signup = Frame(main, width = 873, height = 300)
start = Frame(main, width = 873, height = 300)
about = Frame(main, width = 873, height = 300)
home = Frame(main, width = 873, height = 300)
Setting = Frame(main, width = 873, height = 300)
change_pass = Frame(main, width = 873, height = 300)
show_data = Frame(main, width = 873, height = 300)
# video = Frame(main, width = 873, height = 300)
encode = Frame(main, width = 873, height = 300)
decode = Frame(main, width = 873, height = 300)

bg = itk.PhotoImage(file = 'C:\\Users\\tanis\\OneDrive\\Pictures\\bg.jpg') # background image for frames

# frame configuration
for frame in (login, signup, start, about, home, Setting, change_pass, encode, decode, show_data):
    background = Label(frame, image = bg)
    background.place(x=0, y=0, width = 873, height = 300) # dimensions of bg.jpg 873 x 300

    frame.grid(row = 0, column = 0, sticky = W+E+N+S)
    frame.grid_propagate(0)

    if frame in (encode,decode,change_pass):
        frame.columnconfigure(2,weight = 3)
    elif frame in (login,signup,home,show_data):
        frame.columnconfigure(1,weight = 2)
        frame.columnconfigure(2,weight = 2)
    else:
        frame.columnconfigure(1,weight = 3)

# login
title_login = Label(login, text = 'WELCOME TO STEGANOGRAPHY', bg = '#06243f', fg = '#43bcdd')
title_login.config(font = ('Courier',17))
title_login.grid(row = 1, column = 1, columnspan = 2, sticky = W+E+N+S)

l_user = Label(login, text = 'Username :', bg = '#06243f', fg = '#43bcdd')
l_user.grid(row = 2, column = 1, padx = 10, pady = 20, ipadx = 20, sticky = E)

user = StringVar()
e_user = Entry(login, width = 20, textvariable = user)
e_user.grid(row = 2, column = 2, padx = 10, pady = 10, sticky = W)

l_passwd = Label(login, text = 'Password :', bg = '#06243f', fg = '#43bcdd')
l_passwd.grid(row = 3, column = 1, padx = 10, pady = 10, ipadx = 20, sticky = E)

passwd = StringVar()
e_passwd = Entry(login, width = 20, textvariable = passwd)
e_passwd.grid(row = 3, column = 2, padx = 10, pady = 10, sticky = W)

l_ask = Label(login, text = 'Do not have an account?', bg = '#06243f', fg = '#43bcdd')
l_ask.grid(row = 5, column = 1, pady = 4, ipadx = 70, columnspan = 2)

b_signup = Button(login, text = 'Signup', command = lambda:raise_frame(signup), bg = '#06243f', fg = '#43bcdd')
b_signup.grid(row = 6, column = 1, pady = 7, columnspan = 2)

def check():
    global ref_user
    ref_user = user.get()
    obj = con.connect(host='localhost',user='root',passwd='lu44y',database='stego_user')
    cursor = obj.cursor()
    cursor.execute(f'select password from user where username="{user.get()}"')
    password = cursor.fetchone()[0]
    obj.close()

    if user.get()=='' or passwd.get()=='':
        tkinter.messagebox.showinfo('Login Error!','Username or Password missing. Please enter complete information to proceed.')
    
    elif user.get() in user_list and hashlib.sha256(passwd.get().encode()).hexdigest()==password:
        raise_frame(home)

    else:
        tkinter.messagebox.showinfo('Login Error!','Username or Password incorrect.')

b_login = Button(login, text = 'Login', command = lambda:check(), bg = '#06243f', fg = '#43bcdd')
b_login.grid(row = 4, column = 1, pady = 7, columnspan = 2)

# signup
title_signup = Label(signup, text = 'SIGNUP', bg = '#06243f', fg = '#43bcdd')
title_signup.config(font = ('Courier',17))
title_signup.grid(row = 1, column = 1, columnspan = 2, sticky = W+E+N+S)

l_fname = Label(signup, text = 'First Name :', bg = '#06243f', fg = '#43bcdd')
l_fname.grid(row = 2, column = 1, padx = 10, pady = 10, ipadx = 20, sticky = E)

fname = StringVar()
e_fname = Entry(signup, width = 20, textvariable = fname)
e_fname.grid(row = 2, column = 2, padx = 10, pady = 10, sticky = W)

l_lname = Label(signup, text = 'Last Name :', bg = '#06243f', fg = '#43bcdd')
l_lname.grid(row = 3, column = 1, padx = 10, pady = 10, ipadx = 20, sticky = E)

lname = StringVar()
e_lname = Entry(signup, width = 20, textvariable = lname)
e_lname.grid(row = 3, column = 2, padx = 10, pady = 10, sticky = W)

l_user_s = Label(signup, text = 'Username :', bg = '#06243f', fg = '#43bcdd')
l_user_s.grid(row = 4, column = 1, padx = 10, pady = 0, ipadx = 20, sticky = E)

user_s = StringVar()
e_user_s = Entry(signup, width = 20, textvariable = user_s)
e_user_s.grid(row = 4, column = 2, padx = 10, pady = 10, sticky = W)

l_passwd_s = Label(signup, text = 'Password :', bg = '#06243f', fg = '#43bcdd')
l_passwd_s.grid(row = 5, column = 1, padx = 10, pady = 10, ipadx = 20, sticky = E)

passwd_s = StringVar()
e_passwd_s = Entry(signup, width = 20, textvariable = passwd_s)
e_passwd_s.grid(row = 5, column = 2, padx = 10, pady = 10, sticky = W)

def signup_sql():
    obj = con.connect(host='localhost',user='root',passwd='lu44y',database='stego_user')
    cursor = obj.cursor()
    password = hashlib.sha256(passwd_s.get().encode()).hexdigest()


    if fname.get()=='':
        tkinter.messagebox.showinfo('Signup Error!','Please enter first name.')

    elif lname.get()=='':
        tkinter.messagebox.showinfo('Signup Error!','Please enter last name.')

    elif user_s.get()=='':
        tkinter.messagebox.showinfo('Signup Error!','Please enter username.')

    elif user_s.get() in user_list:
        tkinter.messagebox.showinfo('Signup Error!','Username already taken.')

    elif passwd_s.get()=='':
        tkinter.messagebox.showinfo('Signup Error!','Please enter password.')

    else:
        cursor.execute(f'insert into user values({c+1},"{fname.get()}","{lname.get()}","{user_s.get()}","{password}")')
        obj.commit()
        obj.close()

        obj = con.connect(host='localhost',user='root',passwd='lu44y',database='stego_user')
        cursor = obj.cursor()
        cursor.execute(f'create table {user_s.get()}(id int auto_increment primary key, image_name char(50), image longblob)')
        obj.commit
        obj.close()

        os.mkdir(f'C:\\Users\\tanis\\OneDrive\\Desktop\\{user_s.get()}')
        tkinter.messagebox.showinfo('Account','Account created successfully')
        raise_frame(login)

b_signup = Button(signup, text = 'Create Account', command = lambda:signup_sql(), bg = '#06243f', fg = '#43bcdd')
b_signup.grid(row = 6, column = 1, pady = 15, columnspan = 2)


# home
title_home = Label(home, text = 'WELCOME TO STEGANOGRAPHY', bg = '#06243f', fg = '#43bcdd')
title_home.config(font = ('Courier',17))
title_home.grid(row = 1, column = 1, columnspan = 2, sticky = W+E+N+S)

'''b_image = Button(home, text = 'Image', command = lambda:raise_frame(image), bg = '#06243f', fg = '#43bcdd')
b_image.grid(row = 2, column = 1, padx = 390, pady = 20, sticky = W+N+E+S)'''
b_encode_h = Button(home, text = 'Encode', command = lambda:raise_frame(encode), bg = '#06243f', fg = '#43bcdd')
b_encode_h.grid(row = 2, column = 1, ipadx = 6, ipady = 5, padx = 10, pady = 10, sticky = E+N+S)

b_decode_h = Button(home, text = 'Decode', command = lambda:raise_frame(decode), bg = '#06243f', fg = '#43bcdd')
b_decode_h.grid(row = 2, column = 2, ipadx = 5, padx = 10, pady = 10, sticky = W+N+S)

b_settings = Button(home, text = 'Settings', command = lambda:raise_frame(Setting), bg = '#06243f', fg = '#43bcdd')
b_settings.grid(row = 3, column = 1, ipadx = 5, ipady = 5, padx = 10, pady = 10, sticky = E+N+S)

b_about = Button(home, text = 'About', command = lambda:raise_frame(about), bg = '#06243f', fg = '#43bcdd')
b_about.grid(row = 3, column = 2, ipadx = 9, padx = 10, pady = 10, sticky = W+N+S)

b_show_imgs = Button(home, text = 'Show Data', command = lambda:raise_frame(show_data), bg = '#06243f', fg = '#43bcdd')
b_show_imgs.grid(row = 4, column = 1, columnspan = 2, ipadx = 5, padx = 10, pady = 10, sticky = N+S)

b_quit = Button(home, text = 'Quit', command = lambda:exit(0), bg = '#06243f', fg = '#43bcdd')
b_quit.grid(row = 5, column = 1, columnspan = 2, ipadx = 21, padx = 10, pady = 10, sticky = N+S)

# about
with open(r'C:\Users\tanis\OneDrive\Desktop\aboutsteg.txt') as obj:
    global about_text
    about_text = obj.read()

t_about = scroll.ScrolledText(about, width = 30, height = 12, font = ("Courier", 12))
t_about.grid(row = 1, column = 1,padx = 20, pady = 15, sticky = W+E+N+S)
t_about.insert(END,about_text)

b_goback_a = Button(about, text = 'Go Back', command = lambda:raise_frame(home), bg = '#06243f', fg = '#43bcdd')
b_goback_a.grid(row = 2, column = 1, padx = 390, pady = 10, sticky = W+E+N+S)


# Setting

def delete_account():
    obj = con.connect(host='localhost',user='root',passwd='lu44y',database='stego_user')
    cursor = obj.cursor()

    cursor.execute(f'delete from user where username = "{ref_user}"')
    obj.commit()
    cursor.execute(f"drop table {ref_user}")
    obj.close()

b_encode_i = Button(Setting, text = 'Change Password', command = lambda:raise_frame(change_pass), bg = '#06243f', fg = '#43bcdd')
b_encode_i.grid(row = 1, column = 1, padx = 380, pady = 10, sticky = W+E+N+S)

b_decode_i = Button(Setting, text = 'Delete Account', command = lambda:delete_account(), bg = '#06243f', fg = '#43bcdd')
b_decode_i.grid(row = 2, column = 1, padx = 380, pady = 10, sticky = W+E+N+S)

b_back1 = Button(Setting, text = 'Go back', command = lambda:raise_frame(home), bg = '#06243f', fg = '#43bcdd')
b_back1.grid(row = 3, column = 1, padx = 390, pady = 10, sticky = W+E+N+S)

# Change_pass

l_old_pass = Label(change_pass, text = 'Enter old password:', bg = '#06243f', fg = '#43bcdd')
l_old_pass.grid(row = 1, column = 1, padx = 10, pady = 10, ipadx = 55, sticky = W)

e_old_pass = Entry(change_pass, width = 20)
e_old_pass.grid(row = 1, column = 2, padx = 10, pady = 10, sticky = W+N+E+S)

l_new_pass = Label(change_pass, text = "Enter new password:", bg = '#06243f', fg = '#43bcdd')
l_new_pass.grid(row = 2, column = 1, padx = 10, pady = 10, sticky = W)

e_new_pass = Entry(change_pass, width = 20)
e_new_pass.grid(row = 2, column = 2, padx = 10, pady = 10, sticky = W+N+E+S)

def change():
    obj = con.connect(host='localhost',user='root',passwd='lu44y',database='stego_user')
    cursor = obj.cursor()
    old_pass = hashlib.sha256(e_old_pass.get().encode()).hexdigest()
    new_pass = hashlib.sha256(e_new_pass.get().encode()).hexdigest()
    cursor.execute(f'select password from user where username="{ref_user}"')
    rs = cursor.fetchone()
    if old_pass==rs[0]:
        cursor.execute(f'update user set password="{new_pass}" where username="{ref_user}"')
        obj.commit()
        tkinter.messagebox.showinfo('Password Changed!','Your old password was changed successfully to '+e_new_pass.get())
    else:
        tkinter.messagebox.showinfo('Unmatched entry!','Old password entered does not match with the records. Try again')

obj.close()
b_change = Button(change_pass, text = 'Submit', command = lambda:change(), bg = '#06243f', fg = '#43bcdd')
b_change.grid(row = 3, column = 1, padx = 10, pady = 10, ipadx = 28, sticky = W)

b_back_pass = Button(change_pass, text = 'Go Back', command = lambda:raise_frame(home), bg = '#06243f', fg = '#43bcdd')
b_back_pass.grid(row = 4, column = 1, padx = 10, pady = 10, ipadx = 28, sticky = W)

# Show_data
tree = Treeview(show_data, height = 3)
tree["columns"] = (0,1)
tree.column("#0",width=0, stretch = NO)
tree.column(0,width=5)
tree.column(1,width=120)
tree.heading(0,text="Id")
tree.heading(1,text="Image_Name")

def view():
    obj = con.connect(host='localhost',user='root',passwd='lu44y',database='stego_user')
    cursor = obj.cursor()
    cursor.execute(f'select id,image_name from pan')
    d = cursor.fetchall()

    for i in d:
        tree.insert('','end', values = (i))

    obj.close()
    tree.grid(row = 2, column = 1, columnspan = 2, padx = 50, pady = 5, sticky = W+E)

    tree_scroll = Scrollbar(show_data, orient = 'vertical', command = tree.yview)
    tree_scroll.grid(row = 2, column = 2, sticky = E)
    tree.configure(yscrollcommand = tree_scroll.set)

b_view = Button(show_data, text = 'View', command = lambda:view(), bg = '#06243f', fg = '#43bcdd')
b_view.grid(row = 1, column = 1, ipadx = 14, padx = 10, pady = 10, sticky = E+N+S)

b_backs = Button(show_data, text = 'Go back', command = lambda:raise_frame(home), bg = '#06243f', fg = '#43bcdd')
b_backs.grid(row = 1, column = 2, ipadx = 8, padx = 10, pady = 10, sticky = W+N+S)

# encode

def e_file():
    global e_filename
    e_filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("png files","*.png"),("jpeg files","*.jpeg"),("all files","*.*")))

b_file_enc = Button(encode, text = 'choose a file', command = lambda:e_file(), bg = '#06243f', fg = '#43bcdd')
b_file_enc.grid(row = 1, column = 1, padx = 10, pady = 10, ipadx = 15, sticky = W)

l_data = Label(encode, text = 'Enter the secret message:', bg = '#06243f', fg = '#43bcdd')
l_data.grid(row = 2, column = 1, padx = 10, pady = 10, ipadx = 55, sticky = W)

# key = f.generate_key()   # CRYPTO
# f = Fernet(key)

data = StringVar()
e_data = Entry(encode, width = 20, textvariable = data)
e_data.grid(row = 2, column = 2, padx = 10, pady = 10, sticky = W+N+E+S)


l_newimg = Label(encode, text = "Enter the name of new image(with extension):", bg = '#06243f', fg = '#43bcdd')
l_newimg.grid(row = 3, column = 1, padx = 10, pady = 10, sticky = W)

e_newimg = Entry(encode, width = 20)
e_newimg.grid(row = 3, column = 2, padx = 10, pady = 10, sticky = W+N+E+S)

def genData(data1):

    newd = []

    for i in data1:
        try:
            newd.append(format(ord(i), '08b'))
        except:
            newd.append('{0:08b}'.format(i))
    return newd

def modPix(pix, data1):

    datalist = genData(data1)
    lendata = len(datalist)
    imdata = iter(pix)

    for i in range(lendata):

    # Extracting 3 pixels at a time
        pix = [value for value in imdata.__next__()[:3] +imdata.__next__()[:3] +imdata.__next__()[:3]]
        for j in range(0, 8):
            if (datalist[i][j] == '0' and pix[j]% 2 != 0):
                pix[j] -= 1

            elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                if(pix[j] != 0):
                    pix[j] -= 1
                else:
                    pix[j] += 1

        if (i == lendata - 1):
            if (pix[-1] % 2 == 0):
                if(pix[-1] != 0):
                    pix[-1] -= 1
                else:
                    pix[-1] += 1

        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1

        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]

def encode_enc(newimg, data1):
    w = newimg.size[0]
    x, y = 0, 0

    for pixel in modPix(newimg.getdata(), data1):

        # Putting modified pixels in the new image
        newimg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1

def encodes():
    data1 = data.get()
    
    img = Image.open(e_filename, 'r')

    if len(data1) == 0:
        raise ValueError('Data is empty')

    newimg = img.copy()
    encode_enc(newimg, data1)
    # saving image
    newimg_type = str(e_newimg.get().split(".")[1].upper()) # code
    # check path if exists
    '''if os.path.isdir(f'C:\\Users\\tanis\\OneDrive\\Desktop\\{ref_user}'):
        newimg.save(f'C:\\Users\\tanis\\OneDrive\\Desktop\\{ref_user}\\{e_newimg.get()}', newimg_type)
    else:
        os.mkdir(f'C:\\Users\\tanis\\OneDrive\\Desktop\\{ref_user}')'''
    newimg.save(f'C:\\Users\\tanis\\OneDrive\\Desktop\\{ref_user}\\{e_newimg.get()}', newimg_type)

    # storing image in database
    obj = con.connect(host='localhost',user='root',passwd='lu44y',database='stego_user')
    cursor = obj.cursor()

    user_query = f'insert into {ref_user}(image_name, image)'
    sql_insert_blob_query = user_query+" values(%s,%s)"
    # Convert data into tuple format
    insert_blob_tuple = (e_newimg.get(), newimg.tobytes()) # image to binary data
    cursor.execute(sql_insert_blob_query, insert_blob_tuple)
    
    obj.commit()
    obj.close()


b_process = Button(encode, text = 'Submit', command = lambda:encodes(), bg = '#06243f', fg = '#43bcdd')
b_process.grid(row = 4, column = 1, padx = 10, pady = 10, ipadx = 30, sticky = W)

b_backenc = Button(encode, text = 'Go Back', command = lambda:raise_frame(home), bg = '#06243f', fg = '#43bcdd')
b_backenc.grid(row = 5, column = 1, padx = 10, pady = 10, ipadx = 28, sticky = W)


# decode

def d_file():
    global d_filename,ask
    d_filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("png files","*.png"),("jpeg files","*.jpeg"),("all files","*.*")))

    l_ask = Label(decode, text = 'Is '+d_filename+' the image you want to decode?')
    l_ask.grid(row = 4, column = 1, padx = 10, pady = 10, sticky = W+E+N+S, columnspan = 3)

    b_yes = Button(decode, text = 'Yes', command = lambda:display_data(), bg = '#06243f', fg = '#43bcdd')
    b_yes.grid(row = 5, column = 1, padx = 390, pady = 10, sticky = W)

    b_no = Button(decode, text = 'No', command = lambda:raise_frame(home), bg = '#06243f', fg = '#43bcdd')
    b_no.grid(row = 5, column = 1, padx = 390, pady = 10, sticky = E)

b_file_dec = Button(decode, text = 'choose a file', command = lambda:d_file(), bg = '#06243f', fg = '#43bcdd')
b_file_dec.grid(row = 1, column = 1, padx = 390, pady = 10, sticky = W+N+E+S)

b_backdec = Button(decode, text = 'Go back', command = lambda:raise_frame(home), bg = '#06243f', fg = '#43bcdd')
b_backdec.grid(row = 2, column = 1, padx = 390, pady = 10, sticky = W+E+N+S)

def decodes():
    img = Image.open(d_filename,'r')

    data2 = ''
    imgdata = iter(img.getdata())

    while (True):
        pixels = [value for value in imgdata.__next__()[:3] +imgdata.__next__()[:3] +imgdata.__next__()[:3]]
        '''print(pixels)#test
        # string of binary data'''
        binstr = ''

        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'

        data2 += chr(int(binstr, 2))
        if (pixels[-1] % 2 != 0):
            return data2 #d.decode()

def display_data():
    data2 = decodes()
    
    t_dis = scroll.ScrolledText(decode, width = 30, height = 5, font = ('Courier', 12))
    t_dis.grid(row = 5, column = 1,padx = 10, pady = 10, sticky = W+E+N+S)
    t_dis.insert(END,'The secret message is '+data2)

raise_frame(login)
main.mainloop()