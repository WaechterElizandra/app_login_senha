#importação necessaria
from tkinter import *
import sqlite3
import tkinter.messagebox

#criando conexão com banco de dados 
conn = sqlite3.connect("bancodedados.db")
c = conn.cursor()

#criando a tela
tela_login = Tk()

#classe com funções 
class App:
    #função que instancia o app
    def __init__(self, *args, **kwargs):
        #declara o objeto criado
        self.tela_login = tela_login

        #dimensões da tela
        self.tela_login.geometry("400x400+500+200")

        #titulo da tela
        self.tela_login.title("Aula Python")
        
        # aqui controlamos se  a tela vai maximizar ou não
        self.tela_login.resizable(False,False)
        
        #executa a função inicial
        self.inicial()
        tela_login.mainloop()
#função que mostra a primeira tela do sistema, tela de login
    def inicial(self, *args, **kwargs):
        #instancia um frame novo para abrir a tela de login
        self.login_frame = Frame(master=self.tela_login, width=399, height=399, bg='#202021')
        self.login_frame.pack(side=RIGHT)

        #label para informar o acesso ao sistema
        self.label_login = Label(master=self.login_frame, font=('arial 22 bold'),text ='acesso ao sistema!', bg='#202021', foreground='white')
        self.label_login.place(x=15, y=5)
        
        #label que infor o campo de login
        self.nome = Label(master=self.login_frame, text="Digite aqui o login.", font=('arial 10 bold'), foreground='white', bg='#202021')
        self.nome.place(x=15, y=65)

        #aqui cria o campo de entrada de dados para nome de usuario
        self.nomeusuario = Entry(master=self.login_frame, width=26, font=('arial 19 bold'))
        self.nomeusuario.place(x=15, y=95)

        #aqui seta o focus
        self.nomeusuario.focus()

        #aqui cria a label para informar o campo de senha
        self.senha = Label(master=self.login_frame, text="Digite aqui a senha.", font=('arial 10 bold'),foreground='white', bg='#202021')
        self.senha.place(x=15, y=135)

        #aqui cria o campo de entrada de senha
        self.senhausuario = Entry(master=self.login_frame, show='*', width=26, font=('arial 19 bold'))
        self.senhausuario.place(x=15, y=160)

        #aqui cria os botoes da tela de login
        self.btn_adicionar = Button(master=self.login_frame, text="Entrar", width=25, height=2, bg='blue', fg='white', font=('arial 8 bold'), command=self.testa_usuario)
        self.btn_adicionar.place(x=10, y=210)
        self.btn_limpar=Button(master=self.login_frame, text="Limpar",width=25, height=2, bg='orange', fg='white', font=('arial 8 bold'),command=self.limpacamposlogin)
        self.btn_limpar.place(x=200, y=210)
        self.btn_novo =Button(master=self.login_frame, text="Novo",width=52, height=2, bg='green', fg='white', font=('arial 8 bold'),command=self.cadastro)
        self.btn_novo.place(x=10, y=260)

        #função que abre a tela de cadastro de usuários
    def cadastro(self, *args, **kwargs):

        #fecha o frame
        self.login_frame.pack_forget()

        #cria um novo frame
        self.cadastro_frame = Frame(master=self.tela_login, width=399, height=399, bg='#202021')
        self.cadastro_frame.pack(side=RIGHT)

        #label cadastro
        self.label_cadastro = Label(master=self.cadastro_frame,text="CADASTRO DE USUÁRIOS", font=('arial 10 bold'),foreground='white',bg='#202021').place(x=10, y=5)

        #label nome usuario
        self.label_nome=Label(master=self.cadastro_frame, text="Nome de usuario", foreground='white', font=('arial 10 bold'),bg='#202021').place(x=10, y=35)

        #campo de entrada de texto nome de usuario
        self.nomeusuariow = Entry(master=self.cadastro_frame,width=26, font=('arial 19 bold'))
        self.nomeusuariow.place(x=15, y=60)

        #seta o facus no campo no campo usuario
        self.nomeusuariow.focus()

        #label email
        self.label_email= Label(master=self.cadastro_frame, text="Email do usuario",foreground='white', font=('arial 10 bold'), bg='#202021').place(x=10, y=100)

        #campo de entrada email
        self.emailusuariow = Entry(master=self.cadastro_frame, width=26, font=('arial 19 bold'))
        self.emailusuariow.place(x=15, y=125)

        #label login
        self.label_login = Label(master=self.cadastro_frame, text="Login do usuario", foreground='white', font=('arial 10 bold'),bg='#202021').place(x=10, y= 160)

        #campo de entrada login
        self.loginusuariow = Entry(master=self.cadastro_frame, width=26, font=('arial 19 bold'))
        self.loginusuariow.place(x=15, y= 185)

        #label senha
        self.label_senha = Label(master=self.cadastro_frame, text="Senha do usuário", foreground='white', font=('arial 10 bold'), bg='#202021').place(x=10, y=220)

        #campo de entrada de senha
        self.senhausuariow= Entry(master=self.cadastro_frame, show='*', width=26, font=('arial 19 bold'))
        self.senhausuariow.place(x=15, y=245)

        #botoes da tela de cadastro salvar voltar limpar
        self.btn_salvar =Button(master=self.cadastro_frame, text="Salvar", width=25, height=2, bg='green', font=('arial 8 bold'),fg='white', command=self.salvausuario)
        self.btn_salvar.place(x=10, y=285)

        self.btn_limparr= Button(master=self.cadastro_frame,  text="Limpar", width=25, height=2, bg='orange', font=('arial 8 bold'),fg='white', command=self.limpacampos)
        self.btn_limparr.place(x= 200, y=285)

        self.btn_voltar =Button(master=self.cadastro_frame, text="Voltar", width=52, height=2, bg='steelblue', font=('arial 8 bold'), fg='white', command=self.voltarmenu)
        self.btn_voltar.place(x=10, y=335)

        #função que volta a tela de login
    def voltarmenu(self, *args, **kwargs):
        self.inicial()
        self.cadastro_frame.pack_forget()

        #função que limpa os campos de usuário
    def limpacampos(self, *args, **kwargs):
        self.nomeusuariow.delete(0,END)
        self.emailusuariow.delete(0,END)
        self.loginusuariow.delete(0,END)
        self.senhausuariow.delete(0, END)

        #função que cria a telaprincipal do sistema
    def principal(self, *args, **kwargs):
        #fecha o frame
        self.login_frame.pack_forget()

        #cria o frame novo para tela principal
        self.principal_frame = Frame(master=self.tela_login, width=399, height=399, bg='#202021')
        self.principal_frame.pack(side=RIGHT)

        #label da tela inicial
        self.label_telainicial= Label(master=self.principal_frame, text="TELA INICIAL", font=('arial 10 bold'), foreground='white', bg='#202021').place(x=0, y=5)

        #botão usuario
        self.btn_usuarios = Button(master=self.principal_frame, text="USUÁRIOS", width=20, height=2, bg='green',fg='white', command=self.abrecadastrousuario)
        self.btn_usuarios.place(x=15, y=30)

        #função abre cadastro de usuario
    def abrecadastrousuario(self, *args, **kwargs):
        #fecha o frame
        self.login_frame.pack_forget()
        #cria novo frame
        self.cadastro_frame =Frame(master=self.tela_login, width=399, height=399, bg='#202021')
        self.cadastro_frame.pack(side=RIGHT)
        #label cadastro
        self.label_cadastro= Label(master=self.cadastro_frame, text="CADASTRO DE USUÁRIOS", font=('arial 10 bold'),foreground='white', bg='#202021').place(x=10, y=5)
        #label nome usuário
        self.label_nome = Label(master=self.cadastro_frame, text="Nome de usuário", foreground='white',font=('arial 20 bold'), bg='#202021').place(x=10, y=35)
        #campo de entrada de texto nome de usuário
        self.nomeusuariow = Entry(master=self.cadastro_frame, width=26, font=('arial 19 bold'))
        self.nomeusuariow.place(x=15, y=60)
        #seta o focus no campo nome de usuario
        #label email
        self.label_email = Label(master=self.cadastro_frame, text="E-mail do usuário", foreground='white', font=('arial 10 bold'), bg='#202021').place(x=10, y=100)

        #campo entrada de email
        self.emailusuariow = Entry(master=self.cadastro_frame, width=26, font=('arial 19 bold'))
        self.emailusuariow.place(x=15, y=125)

        #label login
        self.label_login = Label(master=self.cadastro_frame, text="Login do usuário", foreground='white',font=('arial 10 bold'), bg='#202021').place(x=10, y=160)

        #campo de entrada de login
        self.loginusuariow = Entry(master=self.cadastro_frame,width=26, font=('arial 19 bold'))
        self.loginusuariow.place(x=15, y=185)

        #label senha
        self.label_senha = Label(master=self.cadastro_frame, text="Senha do usuário", foreground='white', font=('arial 10 bold'), bg='#202021').place(x=10, y=220)
        
        #campo de entrada de senha
        self.senhausuariow = Entry(master=self.cadastro_frame, show='*',width=26, font=('arial 19 bold'))
        self.senhausuariow.place(x=15, y=245)

        #botões do cadastro
        self.btn_salvar = Button(master=self.cadastro_frame, text="Salvar", width=25, height=2, bg='green', font=('arial 8 bold'), fg='white')
        self.btn_salvar.place(x=10, y=285)
        self.btn_limpar =Button(master=self.cadastro_frame, text="Limpar", width=25, height=2, bg='orange', font=('arial 8 bold'), fg='white')
        self.btn_limpar.place(x=200, y=285)
        self.btn_voltar = Button(master=self.cadastro_frame, text="Voltar", width=52, height=2, bg='steelblue', font=('arial8 bold'), fg='white')
        self.btn_voltar.place(x=10, y=335)
        #função que limpa os campos da tela de login
    def limpacamposlogin(self, *args, **kwargs):
        self.nomeusuario.delete(0,END)
        self.senhausuario.delete(0,END)
        self.nomeusuario.focus()

        #função que confere usuário e senha no banco
    def testa_usuario(self, *args,**kwargs):
        self.nomeusuario1 = self.nomeusuario.get()
        self.senhausuario1 = self.senhausuario.get()

        #aqui controla se os campos estão vazios
        if self.nomeusuario1 =='' or self.senhausuario1 == '':
            tkinter.messagebox.showinfo('Incompleto', 'Campos vazios')
        else:
            #variavel recebe o resultado da sql
            buscausuario = "SELECT *FROM Usuario WHERE nome_usuario=?, and senha_usuario =?"

            #variável que recebe o valor do status da execução do sql
            
            sqlres = c.execute(buscausuario, (self.nomeusuario1, self.senhausuario1))

            #laço de repetição que confere que veio resultado do sql
            for c in sqlres:
                #se o laço acontecer vai executar a função principal
                self.principal()

    #função que salva usuário
    def salvausuario(self, *args, **kwargs):
        #get recupera o valor digitado no campo de entrada de texto
        self.nomeusuario3 = self.nomeusuariow.get()
        self.emailusuario3 = self.emailusuariow.get()
        self.loginusuario3 = self.loginusuariow.get()
        self.senhausuario3 = self.senhausuariow.get()

        if self.nomeusuario3 == '' or self.emailusuario3 == '' or self.loginusuario3 == '' or self.senhausuario3 == '':
            tkinter.messagebox.showinfo('Preencha')

        else:
            #cria uma variavel que vai receber a execução do insert no banco de dados
            insera = 'INSERT INTO Usuario(nome_usuario, email_usuario, login_usuario, senha_usuario)VALUES(?,?,?,?)'
        c.execute(insera,(self.nomeusuario3, self.emailusuario3, self.loginusuario3, self.senhausuario3))

        #commit é  comando para executar alguma alteração no banco de dados

        # executa a função de voltar para o menu
        self.voltarmenu()


            
#rodando a aplicação            
App ()