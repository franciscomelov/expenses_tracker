#https://twitter.com/jangiacomelli/status/1331170948150558723
#https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping
""" 
Build expense tracker CLI app.

Cover: 
[X]Add expense
[X]list expenses
[X]get expense --> Añadir busceda por producto
[X]edit expense 
[X]delete expense  -->DEcidir si al eliminar se recorreran los id
[X]Store expenses in TXT file. --> almost
 """
import csv
from datetime import datetime


#CLass para guardar epense unica
class Expense:
    def __init__(self,id, title, amount, created_at, tags):
        self.title =title
        self.amount =amount
        self.created_at=created_at
        self.tags = tags
        self.id = id

#Class para guardar diferentes expenses cada expense se guardara como un objeto 
#dentro del array self.expenses self.expenses =[{expense_1}, {expense:2},...]
class Expense_tracker:
    def __init__(self):
        self.expenses=[]
            
    #Añade solo un elemento
    def add(self,  title, amount, tags):
        if len(self.expenses)==0: # si es el primer expense id = 1
            id = 1
        else: # si hay mas de 1 id = id anterior mas 1 - porque al eliminar se perdera la continuidad del id 1,2,4
            id = getattr(self.expenses[len(self.expenses)-1],"id") +1
        # haciendo append a self.expenses            datetime regrea fecha y hora actual
        self.expenses.append(Expense(id,title, amount, datetime.now(), tags))

    #añade desde db.txt a self.expenses al inicia programa
    def super_add(self, id, title, amount, created_at, tags):
        self.expenses.append(Expense(int(id),title, amount, created_at, tags))

    def list(self):# itera sobre cada index de self.expenses
        for expense in self.expenses: # manda expense a self._print
            self._print(expense)

    def _print(self, expense):# imprime expense unica 
        print("*******************")
        print(expense.id)
        print(expense.title)
        print(expense.amount)
        print(expense.created_at)
        print(expense.tags)
        print("*******************")

    def get(self, title): # itera sobre cada expense de self.expenses si title coincide regresa la impresion
        for expense in self.expenses:
            if title == expense.title:
                self._print(expense)

    def edit(self,id):#itera sobre cada expense i compara parametro id con self.expenses.id
        for i, expense in enumerate(self.expenses):#enumerate regresa un entero desde 0 hasta n  sirve para sacar el index de expense que coinsidio
            if id == expense.id: #si coincide
                title = input("producto: ")   #pregunta por datos para cambiar
                amount = float(input("precio: "))
                tags = input("Ingresa cateorias separadas por coma =  desayuno,lacteso...: ").split(",")
                self.expenses[i] = Expense(id,title, amount, expense.created_at , tags) 
                #Remplaza  self.expenses[indice en base a i] id  y fecha queda igual

    def delete(self, id):#itera sobre cada exense 
        for i, expense in enumerate(self.expenses): 
            if id == expense.id: # si el id coinside
                del self.expenses[i] # lo elimina en base a i que es igual al index
                break #break for


    def _save(self,): #Al salir del programa se tiene que guardar en db.txt   self.expenses -->db.txt
        with open('db.txt', 'w') as f: #abre db.txt en modo write
            writer = csv.writer(f)
            writer.writerow(('id',"title", "amount", "created_at", "tags")) # escribe en cabecera cada key
            for expense in self.expenses: #iteara sobre cada expense y los añade cada expense en cada row
                writer.writerow( (expense.id,expense.title,expense.amount,expense.created_at,expense.tags) )

    def _test(self): #Para hacer pruebas
        a = type(getattr(self.expenses[len(self.expenses)-1],"id"))
        print(a)



def run():
    
    expense_tracker = Expense_tracker() #Crea objeto inical
    # Primer instruncion correra siempre al inicio y leera db.txt y lo guarda en mi class expense_tracker

    with open('db.txt', 'r', encoding="utf8") as f: # alinicar programa lee db.txt y excribe en mi objeto
        reader = csv.reader(f)
        for idx, row in enumerate(reader): #itera sbre cada linea de db.txt
            if idx == 0: # si la linea esta vacia no hace nada
                continue
            if row == []:
                continue
            expense_tracker.super_add(row[0], row[1], row[2],row[3],row[4])
            # si tienen informacion añade cada row[n] es un elemento de 6,cacahuates,5.0,2020-12-03,['chatarra']
            """ id,title,amount,created_at,tags
                2,papas,12.2,2020-12-03,"['comida', 'snack']" """

    while True:
        #MENU normal
        todo = input(""" ¿Que quieres hacer?
    1 - Add expense 
    2 - list expenses
    3 - get expense
    4 - edit expense
    5 - delete expense
    0 - Salir
        """)

        if todo == "1": # add
            print("Ingresa los datos")
            title = input("Producto : ")
            amount = float(input("Precio: "))
            tags = input("Ingresa cateorias separadas por coma =  desayuno,lacteso...: ").split(",")
            expense_tracker.add(title,amount,tags)
        elif todo == "2": #list
            expense_tracker.list()
        elif todo == "3": #get
            title = input("Ingresa el nombre del producto: ")
            expense_tracker.get(title)
        elif todo == "4":  # edit
            title = input("Ingresa el nombre del producto: ")
            expense_tracker.get(title)
            id = int(input("Ingresa el id del producto a editar: "))
            expense_tracker.edit(id)
        elif todo == "5": #delete
            title = input("Ingresa el nombre del producto: ")
            expense_tracker.get(title)
            id = int(input("Ingresa el id del producto a eliminar: "))
            expense_tracker.delete(id)
        elif todo == "0": 
            print("**ADIOS**")
            break
        elif todo == "99": expense_tracker._test() #para prueba
        else: print("Comando Equivocado")

    #al salir del proraga llama a expense_tracker._save() para guardar en deb.txt
    expense_tracker._save()

if __name__ == "__main__":
    run()