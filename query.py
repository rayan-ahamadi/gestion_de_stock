import mysql.connector
from tkinter import * 
from tkinter import messagebox
from tkinter.ttk import *
from produit import Produit

class Query:
    def __init__(self) -> None:
        self.__conn = mysql.connector.connect(host="127.0.0.1",
                               user="root", password="", 
                               database="boutique")
        
    def addOnTab(self,tab):
        cursor = self.__conn.cursor()
        sqlQuery = "SELECT * FROM produit;"
        cursor.execute(sqlQuery)
        resultat = cursor.fetchall()

        for enreg in resultat:
            tab.insert('', 'end', iid=enreg[0], values=(enreg[0],enreg[1], enreg[2], enreg[3],enreg[4],enreg[5]))

        cursor.reset()
        cursor.close()

            

    def deleteProduct(self):
        newWindow = Toplevel()

        def displayData(frame):
            cursor = self.__conn.cursor()
            sqlQuery = "SELECT id,nom FROM produit;"
            cursor.execute(sqlQuery)
            resultat = cursor.fetchall()

            row = 0
            for enreg in resultat:
                Label(frame,text="{}".format(enreg[0])).grid(row=row,column=0,padx=25)
                Label(frame,text="{}".format(enreg[1])).grid(row=row,column=1,padx=25)
                Button(frame,text="Delete",command=lambda id=id: self.__deleteData(int(enreg[0]),frame)).grid(row=row,column=2,padx=25)
                row+=1

        displayData(newWindow)

    def productList(self): 
        newScreen = Toplevel()
        Label(newScreen,text="Liste de produits").grid(row=0,column=0)

        tabColumn = ('id','nom','description','prix','quantité','idcatégorie')
        textTabColumn = ["ID","Nom","Description","Prix","Quantité","IDcatégorie"]
        dataTab = Treeview(newScreen,columns=('id','nom','description','prix','quantité','idcatégorie'))

        for head in tabColumn:
            dataTab.column(head,anchor=CENTER, stretch=NO, width=100)
            dataTab.heading(head, text=textTabColumn[tabColumn.index(head)])

        dataTab['show'] = 'headings'
        dataTab.grid(row=1,column=0,padx = 10, pady = (0, 10))
        self.addOnTab(dataTab)

        newScreen.mainloop()


    def addData(self):

        def commitNewData():            
            if ord(str(price.get())[0]) in range(48,57) and ord(str(quantity.get())[0]) in range(48,57) and ord(str(categ.current())[0]) in range(48,57):
                newProduct = Produit(str(nameProduct.get()),str(descri.get()),int(price.get()),int(quantity.get()),int(categ.current())+1)
                cursor = self.__conn.cursor()
                newProduct.addProduct(cursor) 
                self.__conn.commit()
                messagebox.showinfo("Succès","Données ajoutés avec succès")
                cursor.close()
            else : 
                messagebox.showerror("Erreur","Certains champs ne sont pas des valeurs numérique ou n'ont pas été rempli")
                return 0

        newWindow = Toplevel() 

        formulaire = Frame(newWindow)
        nameProduct = Entry(formulaire)
        descri = Entry(formulaire)
        price = Entry(formulaire)
        quantity = Entry(formulaire)
        categ = Combobox(formulaire)
        confirm = Button(newWindow,text="Ajout du produit",command=commitNewData)

        cursor = self.__conn.cursor()
        query = "SELECT * FROM categorie;"
        cursor.execute(query)
        list = cursor.fetchall()
        listCateg = []
        for elements in list : 
            listCateg.append(f"{elements[0]} - {elements[1]}")
        categ.config(values=listCateg)

        Label(newWindow,text="Nouveau produit").grid(row=0,column=0)
        
        Label(formulaire,text="Nom du produit :").grid(row=1,column=0,padx=10,pady=10)
        Label(formulaire,text="Description de Produit :").grid(row=2,column=0,padx=10,pady=10)
        Label(formulaire,text="Prix du produit :").grid(row=3,column=0,padx=10,pady=10)
        Label(formulaire,text="Quantité :").grid(row=4,column=0,padx=10,pady=10)
        Label(formulaire,text="Catégorie du produit :").grid(row=5,column=0,padx=10,pady=10)

        nameProduct.grid(row=1,column=1,padx=10,pady=10)
        descri.grid(row=2,column=1,padx=10,pady=10,ipady=25)
        price.grid(row=3,column=1,padx=10,pady=10)
        quantity.grid(row=4,column=1,padx=10,pady=10)
        categ.grid(row=5,column=1,padx=10,pady=10)
        confirm.grid(row=2,column=0,pady=5)
        formulaire.grid(row=1)


    def changeData(self):
        newWindow = Toplevel()
        

        def newForm(id,name,descr,prix,quant,id_cat):
            
            def commitChange():
                if ord(str(price.get())[0]) in range(48,57) and ord(str(quantity.get())[0]) in range(48,57) and ord(str(categ.current())[0]) in range(48,57):
                    newProduct = Produit(str(nameProduct.get()),str(descri.get()),int(price.get()),int(quantity.get()),int(categ.current())+1)
                    cursor = self.__conn.cursor()
                    newProduct.changeProduct(cursor,id) 
                    self.__conn.commit()
                    messagebox.showinfo("Succès","Données modifiés avec succès")
                    cursor.close()
                else : 
                    messagebox.showerror("Erreur","Certains champs ne sont pas des valeurs numérique ou n'ont pas été rempli")
                    return 0


            newWin = Toplevel()
            formulaire = Frame(newWin)

            nameProduct = Entry(formulaire)
            descri = Entry(formulaire)
            price = Entry(formulaire)
            quantity = Entry(formulaire)
            categ = Combobox(formulaire)

            confirm = Button(newWin,text="Ajout du produit",command= lambda : commitChange())

            nameProduct.insert(0,name)
            descri.insert(0,descr)
            price.insert(0,prix)
            quantity.insert(0,quant)

            cursor = self.__conn.cursor()
            query = "SELECT * FROM categorie;"
            cursor.execute(query)
            list = cursor.fetchall()
            listCateg = []
            for elements in list : 
                listCateg.append(f"{elements[0]} - {elements[1]}")
            categ.config(values=listCateg)
            categ.current(id_cat-1)
            cursor.close()

            Label(newWin,text="Modification du produit").grid(row=0,column=0)
            
            Label(formulaire,text="Nom du produit :").grid(row=1,column=0,padx=10,pady=10)
            Label(formulaire,text="Description de Produit :").grid(row=2,column=0,padx=10,pady=10)
            Label(formulaire,text="Prix du produit :").grid(row=3,column=0,padx=10,pady=10)
            Label(formulaire,text="Quantité :").grid(row=4,column=0,padx=10,pady=10)
            Label(formulaire,text="Catégorie du produit :").grid(row=5,column=0,padx=10,pady=10)

            nameProduct.grid(row=1,column=1,padx=10,pady=10)
            descri.grid(row=2,column=1,padx=10,pady=10,ipady=25)
            price.grid(row=3,column=1,padx=10,pady=10)
            quantity.grid(row=4,column=1,padx=10,pady=10)
            categ.grid(row=5,column=1,padx=10,pady=10)
            confirm.grid(row=2,column=0,pady=5)
            formulaire.grid(row=1)

        def displayData(frame):
            cursor = self.__conn.cursor()
            sqlQuery = "SELECT * FROM produit;"
            cursor.execute(sqlQuery)
            resultat = cursor.fetchall()

            row = 0
            for enreg in resultat:
                Label(frame,text="{}".format(enreg[0])).grid(row=row,column=0,padx=25)
                Label(frame,text="{}".format(enreg[1])).grid(row=row,column=1,padx=25)
                Button(frame,text="Modifier",command= lambda row=row: newForm(enreg[0],enreg[1],enreg[2],enreg[3],enreg[4],enreg[5])).grid(row=row,column=2,padx=25)
                row+=1

        displayData(newWindow)
         
        

    def __deleteData(self,id,frame):
        yes = messagebox.askyesnocancel(title="Attention",message="êtes-vous sûr de continuer")
        if yes : 
            deleteQuery = f"DELETE FROM produit WHERE id = {id};"
            cursor = self.__conn.cursor()
            cursor.execute(deleteQuery)
            self.__conn.commit()
            messagebox.showinfo(title="succès", message="Donnée supprimée avec succès")
            cursor.close()
            frame.destroy()
            self.deleteProduct()
            


    