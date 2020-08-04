# -*- coding: utf-8 -*-
# create a load interface
import tkinter as tk
import tkinter.messagebox
import pickle

# 创建的登陆窗口
window = tk.Tk()
window.title('Welcome To Study System')
window.geometry('450x300')

# 设置窗口的图片
canvas = tk.Canvas(height=300, width=500)
imagefile = tk.PhotoImage(file='/home/zmq/untitled/study.png')
image = canvas.create_image(0, 0, anchor='nw', image=imagefile)
canvas.pack(side='top')

# 设置用户名和密码输入框
tk.Label(window, text='user').place(x=100, y=150)
tk.Label(window, text='passwd').place(x=100, y=190)

# 输入用户名，设定输入框
var_usr_name = tk.StringVar()
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=150)

# 输入密码，设定输入框
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=190)


# 登陆函数
def usr_log_in():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        with open('usr_info.pickle', 'rb') as usr_file:  # 判断用户名是否存在
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usr_info.pickle', 'rb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:  # 判断已存在的用户名和输入的密码是否匹配
            tk.messagebox.showinfo(title='Welcome',
                                   message='Thanks for your use ' + usr_name)
        else:
            tk.messagebox.showerror(message='your password is wrong')
    elif usr_name == '' or usr_pwd == '':  #判断用户名或者密码是否为空
        tk.messagebox.showerror(message='username or password is empty')
    else:
        is_signup = tk.messagebox.askyesno("hello", "you haven't registered yet")
        if is_signup:
            usr_sign_up()


# 注册函数
def usr_sign_up():

    def signtowcg():
        nn = new_name.get()
        np = new_pwd.get()
        npf = new_pwd_confirm.get()

        try:
            with open('usr_info.pickle', 'rb') as usr_file:
                exist_usr_info = pickle.load(usr_file)
        except FileNotFoundError:
            exist_usr_info = {}

        if nn in exist_usr_info:
            tk.messagebox.showerror(message='Sorry the username already existes, Please re-entry')
        elif nn == '' or np == '':
            tk.messagebox.showerror('Error', 'username or password is empty')
        elif np != npf:
            tk.messagebox.showerror('Error', 'password is not same')
        else:
            exist_usr_info[nn] = np
            with open('usr_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo(message='Congratulations, registered successfully')
            window_sign_up.destroy()

    window_sign_up = tk.Toplevel(window)  #注册窗口
    window_sign_up.geometry('500x300')
    window_sign_up.title('sign up')

    new_name = tk.StringVar()  #注册用户名、密码和密码确认窗口的输入栏
    tk.Label(window_sign_up, text='username: ').place(x=10, y=10)
    tk.Entry(window_sign_up, textvariable=new_name).place(x=150, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='password: ').place(x=10, y=50)
    tk.Entry(window_sign_up, textvariable=new_pwd, show='*').place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='re-entry: ').place(x=10, y=90)
    tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*').place(x=150, y=90)

    bt_confirm_sign_up = tk.Button(window_sign_up, text='confirm the registration',
                                   command=signtowcg)
    bt_confirm_sign_up.place(x=150, y=130)


def usr_sign_quit():  # 退出登陆函数
    window.destroy()


# 登陆、注册和退出按钮
bt_login = tk.Button(window, text='sign in', command=usr_log_in)
bt_login.place(x=140, y=230)
bt_logup = tk.Button(window, text='sign up', command=usr_sign_up)
bt_logup.place(x=210, y=230)
bt_signquit = tk.Button(window, text='quit', command=usr_sign_quit)
bt_signquit.place(x=280, y=230)

# 循环主函数
window.mainloop()
