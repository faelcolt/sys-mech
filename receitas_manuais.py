from tkinter import *
from tkinter import ttk
import sqlite3


root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.widgets()
        self.lista_receitas()
        self.montaTabelas()
        self.root.mainloop()
    def tela(self):
        self.root.title("Receitas manuais - RfZorzi")
        self.root.configure(background= "lightgray");
        self.root.geometry("1000x600")
        self.root.resizable(TRUE, TRUE);
        self.root.minsize(width=800, height=500)
    def frames(self):
        ###     Primeiro Container da janela
        top = Frame(self.root, bd=2, bg="#383847", highlightbackground='gray65', highlightthickness=1, relief = 'ridge')
        top.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.1)
        self.top = top
        ###     Segundo Container da janela
        top2 = Frame(self.root, bd=2, bg='#383847', highlightbackground='gray65', highlightthickness=1, relief = 'ridge')
        top2.place(relx=0.52, rely=0.16, relwidth=0.46, relheight=0.1)
        self.top2 = top2
        ###     Terceiro Container da janela
        top3 = Frame(self.root, bd=2, bg='white', highlightbackground='gray65', highlightthickness=1, relief = 'ridge')
        top3.place(relx=0.02, rely=0.26, relwidth=0.96, relheight=0.5)
        self.top3 = top3
        ###     Quarto Container da janela
        top4 = Frame(self.root, bd=2, bg='#383847', highlightbackground='gray65', highlightthickness=1, relief = 'ridge')
        top4.place(relx=0.02, rely=0.78, relwidth=0.96, relheight=0.2)
        self.top4 = top4
    def widgets(self):


        self.lb_entrada = Label(self.top, text='Entrada', bg='#383847', fg='white', font=('dyuthi', 10, 'bold'))
        self.lb_entrada.place(relx= 0.05, rely=0.15, relwidth= 0.07)

        self.inp_entrada = Entry(self.top, fg='gray35').place(relx=0.05, rely=0.5, relwidth= 0.07)

        self.lb_saida = Label(self.top, text='Saida', bg='#383847', fg='white', font=('dyuthi', 10, 'bold'))
        self.lb_saida.place(relx=0.15, rely=0.15, relwidth= 0.07)

        self.inp_saida = Entry(self.top, fg='gray35').place(relx=0.15, rely=0.5, relwidth=0.07)

        self.lb_dia = Label(self.top, text = 'Dia', bg='#383847', fg='lightgray',
                            font=('verdana', 9, 'bold')).place(relx=0.35, rely=0.15, relwidth= 0.04)
        self.inp_dia = Entry(self.top, fg='gray35').place(relx=0.35, rely=0.5, relwidth=0.04)

        self.lb_mes = Label(self.top, text = 'Mês', bg='#383847', fg='lightgray',
                            font=('verdana', 9, 'bold')).place(relx=0.4, rely=0.15, relwidth= 0.04)
        self.inp_mes = Entry(self.top, fg='gray35').place(relx=0.4, rely=0.5, relwidth=0.04)

        self.lb_ano = Label(self.top, text = 'Ano', bg='#383847', fg='lightgray',
                            font=('verdana', 10, 'bold')).place(relx=0.45, rely=0.15, relwidth= 0.04)
        self.inp_ano = Entry(self.top, fg='gray35').place(relx=0.45, rely=0.5, relwidth=0.07)

        self.lb_obs = Label(self.top, text = 'Obs:', bg='#0e76a8', fg='lightgray',
                            font=('dyuthi', 10, 'bold')).place(relx=0.55, rely=0.15, relwidth= 0.07)
        self.inp_obs = Entry(self.top, fg='gray35').place(relx=0.55, rely=0.5, relwidth=0.3)

        self.bt_inserir = Button(self.top, text= 'Inserir', bg= "#0e76a8",bd = 1, highlightbackground='lightgray',
                    highlightthickness=1, fg="lightgray", font=('verdana', 12, 'bold'),
                    activebackground="#108ecb", activeforeground= "white")
        self.bt_inserir.place(relx=0.9, rely=0.2, relwidth=0.09, relheight=0.6)
        #####
        self.mes_listaLb = Label(self.top2, text= 'Mês', bg= 'gray', fg= 'lightgray',
                                 font=('Verdana', '7', 'bold'))
        self.mes_listaLb.place(relx=0.1, rely=0.19, relwidth=0.2, relheight=0.62)
        self.mesListaEntry = Frame(self.top2, bd=2)
        self.mesListaEntry.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mesListaEntry.columnconfigure(0, weight=1)
        self.mesListaEntry.rowconfigure(0, weight=1)
        self.mesListaEntry.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.9)
        self.corvar = StringVar(self.top2)
        self.coresV = {'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
                       'Outubro', 'Novembro', 'Dezembro'}
        self.corvar.set('Junho')
        self.popupMenu = OptionMenu(self.mesListaEntry, self.corvar, *self.coresV)
        self.popupMenu.grid(row=2, column=1)

        self.mesListaEntry.place(relx=0.1, rely=0.2, relwidth=0.2, relheight=0.6)

        self.ano_listaLb = Label(self.top2, text='Mês', bg='gray', fg='lightgray',
                                 font=('Verdana', '7', 'bold'))
        self.ano_listaLb.place(relx=0.4, rely=0.19, relwidth=0.15, relheight=0.62)
        self.anoListaEntry = Frame(self.top2, bd=2)
        self.anoListaEntry.grid(column=0, row=0, sticky=(N, W, E, S))
        self.anoListaEntry.columnconfigure(0, weight=1)
        self.anoListaEntry.rowconfigure(0, weight=1)
        self.anoListaEntry.place(relx=0.4, rely=0.1, relwidth=0.2, relheight=0.9)
        self.corvar2 = StringVar(self.top2)
        self.coresV2 = {'2020', '2021', '2022'}
        self.corvar2.set('2020')
        self.popupMenu = OptionMenu(self.anoListaEntry, self.corvar2, *self.coresV2)
        self.popupMenu.grid(row=2, column=1)

        self.anoListaEntry.place(relx=0.4, rely=0.2, relwidth=0.18, relheight=0.64)

        self.bt_select_month = Button(self.top2, text='Seleciona', bg="#0e76a8", bd=1, highlightbackground='lightgray',
                highlightthickness=1, fg="lightgray", font=('verdana', 12, 'bold'), activebackground="#108ecb",
                activeforeground="white").place(relx=0.65, rely=0.2, relwidth=0.3, relheight=0.6)

        self.entradas_totaisLb = Label(self.top4, text= 'Total Entrada')
        self.entradas_totaisLb.place(relx=0.08, rely=0.1, relwidth=0.12)
        self.entradas_totais = Entry(self.top4)
        self.entradas_totais.place(relx=0.08, rely=0.3, relwidth= 0.12)

        self.saidas_totaisLb = Label(self.top4, text = 'Total Saida')
        self.saidas_totaisLb.place(relx=0.23, rely=0.1, relwidth=0.12)
        self.saidas_totais = Entry(self.top4)
        self.saidas_totais.place(relx=0.23, rely=0.3, relwidth=0.12)

        self.saldo_totalLb = Label(self.top4, text= 'Saldo')
        self.saldo_totalLb.place(relx=0.68, rely=0.1, relwidth=0.12)
        self.saldo_total = Entry(self.top4)
        self.saldo_total.place(relx=0.68, rely=0.3, relwidth=0.12)
    def lista_receitas(self):
        self.barra = Scrollbar(self.top3, orient='vertical')#, command=self.OnVsb_Orc2)

        self.lista = ttk.Treeview(self.top3, height=10, yscrollcommand=self.barra.set,
                                           column=("col1", "col2", "col3", "col4", "col5", "col6"))

        self.lista.heading("#0", text="")
        self.lista.heading("#1", text="Entrada")
        self.lista.heading("#2", text="Saida")
        self.lista.heading("#3", text="Dia")
        self.lista.heading("#4", text="Mes")
        self.lista.heading("#5", text="Ano")
        self.lista.heading("#6", text="Obs")

        self.lista.column("#0", width=1)
        self.lista.column("#1", width=100)
        self.lista.column("#2", width=100)
        self.lista.column("#3", width=40)
        self.lista.column("#4", width=40)
        self.lista.column("#5", width=60)
        self.lista.column("#6", width=210)

        self.lista.place(relx=0.0, rely=0.01, relwidth=0.98, relheight=0.94)

        #self.lista.configure(yscroll=self.barraServProd.set)
        self.barra.place(relx=0.98, rely=0.01, relwidth=0.02, relheight=0.97)
        #self.lista.bind('<Double-1>', self.altera_itens_orc)
        #self.lista.bind('<Return>', self.altera_itens_orc)
        #self.lista.bind('<Delete>', self.altera_itens_orc_deletabt2)
    def conectabd(self):
        self.conn = sqlite3.connect("receita_manual.db")
        self.cursor = self.conn.cursor()
    def desconectabd(self):
        self.conn.close()
    def montaTabelas(self):
        self.conectabd(); print("Conectando ao banco de dados")
        ### Cria tabela servprod
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS receitas (
                cod INTEGER PRIMARY KEY,
                obs CHAR(200) NOT NULL,
    			entrada INTEGER(20),
    			saida INTEGER(20),
    			dia INTEGER(4),
    			mes INTEGER(4),
    			ano INTEGER(6) 			
            );
        """)
        self.conn.commit(); print("banco de dados ja criado")
        self.desconectabd(); print("desconectando ao banco de dados")




Application()