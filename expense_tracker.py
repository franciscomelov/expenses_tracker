#!/usr/bin/env python3.10

import csv
from datetime import datetime


class Expense:
    def __init__(self, id, title, amount, created_at, tags):
        self.title = title
        self.amount = amount
        self.created_at = created_at
        self.tags = tags
        self.id = id


# self.expense_tracker =[{expense_1}, {expense_2},...]
class Expense_tracker:
    def __init__(self):
        self.expenses = []

    def add(self):
        print("Ingresa los datos")
        title = input("Producto : ")
        amount = float(input("Precio: "))
        tags = input("Ingresa cateorias separadas por coma =  desayuno,lacteso...: ").split(",")
        if len(self.expenses) == 0:  # si es el primer expense id = 1
            id = 1
        else:  # si hay mas de 1 id = id anterior mas 1 - porque al eliminar se perdera la continuidad del id 1,2,4
            id = getattr(self.expenses[len(self.expenses) - 1], "id") + 1
        # haciendo append a self.expenses            datetime regrea fecha y hora actual
        self.expenses.append(Expense(id, title, amount, datetime.now(), tags))

    # Adds from db.txt to self.expenses, at the begining
    def super_add(self, id, title, amount, created_at, tags):
        self.expenses.append(Expense(int(id), title, amount, created_at, tags))

    def list(self):
        for expense in self.expenses:
            self._print(expense)

    def _print(self, expense):
        print("*******************")
        print(expense.id)
        print(expense.title)
        print(expense.amount)
        print(expense.created_at)
        print(expense.tags)
        print("*******************")

    def get(self):  # itera sobre cada expense de self.expenses si title coincide regresa la impresion
        title = input("Ingresa el nombre del producto: ")
        for expense in self.expenses:
            if title == expense.title:
                self._print(expense)

    def edit(self):  # itera sobre cada expense i compara parametro id con self.expenses.id
        id = int(input("Ingresa el id del producto a editar: "))
        for i, expense in enumerate(self.expenses):  # enumerate regresa un entero desde 0 hasta n  sirve para sacar el index de expense que coinsidio
            if id == expense.id:  # si coincide
                title = input("producto: ")   # pregunta por datos para cambiar
                amount = float(input("precio: "))
                tags = input("Ingresa cateorias separadas por coma =  desayuno,lacteso...: ").split(",")
                self.expenses[i] = Expense(id, title, amount, expense.created_at, tags)
                # Remplaza  self.expenses[indice en base a i] id  y fecha queda igual

    def delete(self, id):
        id = int(input("Ingresa el id del producto a eliminar: "))
        for i, expense in enumerate(self.expenses):
            if id == expense.id:
                del self.expenses[i]  # lo elimina en base a i que es igual al index
                break  # break for

    def _save(self):  # Al salir del programa se tiene que guardar en db.txt   self.expenses -->db.txt
        with open('db.txt', 'w') as f:  # abre db.txt en modo write
            writer = csv.writer(f)
            writer.writerow(('id', "title", "amount", "created_at", "tags"))  # escribe en cabecera cada key
            for expense in self.expenses:  # iteara sobre cada expense y los añade cada expense en cada row
                writer.writerow((expense.id, expense.title, expense.amount, expense.created_at, expense.tags))

    def _test(self):  # Para hacer pruebas
        a = type(getattr(self.expenses[len(self.expenses) - 1], "id"))
        print(a)


def initiate_expense_tracker():
    expense_tracker = Expense_tracker()  # Crea objeto inical
    # Primer instruncion correra siempre al inicio y leera db.txt y lo guarda en mi class expense_tracker

    with open('db.txt', 'r', encoding="utf8") as f:  # alinicar programa lee db.txt y excribe en mi objeto
        reader = csv.reader(f)
        for idx, row in enumerate(reader):  # itera sbre cada linea de db.txt
            if idx == 0:  # si la linea esta vacia no hace nada
                continue
            if row == []:
                continue
            expense_tracker.super_add(row[0], row[1], row[2], row[3], row[4])
            # si tienen informacion añade cada row[n] es un elemento de 6,cacahuates,5.0,2020-12-03,['chatarra']
            """ id,title,amount,created_at,tags
                2,papas,12.2,2020-12-03,"['comida', 'snack']" """
    return expense_tracker

def run():
    expense_tracker = initiate_expense_tracker()

    while True:
        # MENU normal
        todo = input(""" ¿Que quieres hacer?
    1 - Add expense
    2 - list expenses
    3 - get expense
    4 - edit expense
    5 - delete expense
    0 - Salir
        """)
        match todo:
            case "1":  # add
                expense_tracker.add()

            case "2":  # list
                expense_tracker.list()

            case "3":  # get
                expense_tracker.get()

            case "4":  # edit
                expense_tracker.get()
                expense_tracker.edit()

            case "5":  # delete
                expense_tracker.get()
                expense_tracker.delete()

            case "0":
                print("**ADIOS**")
                break

            case "99":
                expense_tracker._test()  # para prueba
                
            case _:
                print("Comando Equivocado")

    # if progam ends everything is saved in deb.txt
    expense_tracker._save()


if __name__ == "__main__":
    run()
