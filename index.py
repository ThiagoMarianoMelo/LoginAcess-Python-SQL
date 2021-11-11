#importação de bibliotecas para auxilio de construção de pagina
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser

#criando a janela com tkinter
janela = Tk()
janela.title("DP Systems - Acess Panel")
janela.geometry("600x300")
janela.configure(background="white")
janela.resizable(width=False, height=False)
janela.attributes("-alpha", 0.9)
janela.iconbitmap(default="C:/Users/thiag/OneDrive/Imagens/Imagens de trabalho/logoIcon.ico")

#dividindo tela em duas partes mantendo 5 px de separacao
LeftFrame = Frame(janela,width = 200, height = 300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)
RightFrame = Frame(janela,width = 395, height = 300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

#colocando logo dentro do sistema
logo = PhotoImage(file="C:/Users/thiag/OneDrive/Imagens/Imagens de trabalho/logo.png")
LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE") #localizao da logo!
LogoLabel.place(x=50, y=100)

#criacao do campo do usuario
UserLabel = Label(RightFrame, text="Username: ", font=("Arial", 17), bg="MIDNIGHTBLUE", fg="White")
UserLabel.place(x=20,y=100)
UserEntry = Entry(RightFrame, width=20)
UserEntry.place(x=150, y=105)


#criacao do campo senha
PasswordLabel = Label(RightFrame, text="Password: ", font=("Arial", 17), bg="MIDNIGHTBLUE", fg="White")
PasswordLabel.place(x=20,y=150)
PasswordEntry = Entry(RightFrame, width=20,show="*")
PasswordEntry.place(x=150, y=158)

#funcao do bota login
def Login():

    UserLogin = UserEntry.get()
    PasswordLogin = PasswordEntry.get()

    DataBaser.cursor.execute("""
    SELECT USER,PASSWORD FROM Users
    WHERE User = ? and Password = ?
    """, (UserLogin, PasswordLogin))
    VerifyLogin = DataBaser.cursor.fetchone()
    try:
        if UserLogin in VerifyLogin and PasswordLogin in VerifyLogin:
            messagebox.showinfo(title="Login Info",message="login performed")
    except:
        messagebox.showerror(title="Login Info",message="Login failed")

#criacao de botao login
LoginButton = ttk.Button(RightFrame,text="login",width=10,command=Login)
LoginButton.place(x=200,y=220)

#funcao do botao registrar
def Register():
    #removendo botoes de login
    LoginButton.place(x=99999)
    RegisterButton.place(x=99999)
    UserLabel.place(x=99999)
    UserEntry.place(x=99999)
    PasswordEntry.place(x=99999)
    PasswordLabel.place(x=99999)

    #iniciando campos de cadastro
    Name = Label(RightFrame,text="Name: ",font=("Arial",17),bg="MIDNIGHTBLUE",fg="White")
    Name.place(x=30,y=50)
    NameEntry = Entry(RightFrame, width=20)
    NameEntry.place(x=150,y=60)

    RegisterUserLabel = Label(RightFrame, text="Username: ", font=("Arial", 17), bg="MIDNIGHTBLUE", fg="White")
    RegisterUserLabel.place(x=20, y=140)
    RegisterUserEntry = Entry(RightFrame, width=20)
    RegisterUserEntry.place(x=150, y=148)

    RegisterPasswordLabel = Label(RightFrame, text="Password: ", font=("Arial", 17), bg="MIDNIGHTBLUE", fg="White")
    RegisterPasswordLabel.place(x=20, y=180)
    RegisterPasswordEntry = Entry(RightFrame, width=20,show="*")
    RegisterPasswordEntry.place(x=150, y=188)

    EmailLabel = Label(RightFrame,text="Email: ",font=("Arial",17), bg="MIDNIGHTBLUE",fg="White")
    EmailLabel.place(x=30,y=95)
    EmailEntry = Entry(RightFrame,width=20)
    EmailEntry.place(x=150,y=103)


    #criacao dos botoes
    def RegisterToDataBase():
        Name = NameEntry.get()
        Email = EmailEntry.get()
        User = RegisterUserEntry.get()
        Password = RegisterPasswordEntry.get()

        #verificando se todos os dados foram preenchidos
        if Name == "" or Email == "" or User == "" or Password == "" :
            messagebox.showerror(title="Register Error", message="Fill all the fields")
        else:
            DataBaser.cursor.execute("""
            INSERT INTO Users (Name,Email,User,Password) VALUES(?, ?, ?,?)
               """,(Name,Email, User, Password))
            DataBaser.conn.commit()
            messagebox.showinfo(title="Register Info",message="Successful Register")

    #criacao dos botoes da area de registro
    TrueRegisterButtom = ttk.Button(RightFrame,text="Register",width=10,command=RegisterToDataBase)
    TrueRegisterButtom.place(x=200,y=250)

    # funcao do botao voltar
    def BackToLogin():
        Name.place(x=99999)
        NameEntry.place(x=99999)
        RegisterUserEntry.place(x=999999)
        RegisterPasswordLabel.place(x=9999999)
        RegisterUserLabel.place(x=999999)
        RegisterPasswordEntry.place(x=999999)
        TrueRegisterButtom.place(x=99999)
        BackButtom.place(x=999999)
        EmailEntry.place(x=99999)
        EmailLabel.place(x=99999)

        UserLabel.place(x=20, y=100)
        UserEntry.place(x=150, y=105)

        PasswordLabel.place(x=20,y=150)
        PasswordEntry.place(x=150, y=158)

        LoginButton.place(x=200, y=220)
        RegisterButton.place(x=100, y=220)

    BackButtom = ttk.Button(RightFrame, text="Back", width=10,command=BackToLogin)
    BackButtom.place(x=100, y=250)


#Criacao do botao de registro
RegisterButton = ttk.Button(RightFrame,text="Register",width=10,command=Register)
RegisterButton.place(x=100,y=220)

janela.mainloop()