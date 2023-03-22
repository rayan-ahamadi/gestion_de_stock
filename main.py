from tkinter import * 
from tkinter.ttk import *
from query import *


mainWindow = Tk()
mainWindow.title("Gestion de stock")
mainWindow.geometry("625x350")
    
SelectFrom = Query()

Label(mainWindow,text="Gestion des stocks",font=("arial",20)).grid(row=0,column=0,pady = 50)
frameButton = Frame(mainWindow)
addProductButton = Button(frameButton,text="Ajouter un produit",command=SelectFrom.addData)
deleteProductButton = Button(frameButton,text="Supprimer un produit",command= SelectFrom.deleteProduct)
modifyProductButton = Button(frameButton,text="Modifier un produit",command=SelectFrom.changeData)
#L'affichage de la liste des produits se met à jour seulement au lancement du programme
# je n'arrive pas à faire un tableau qui se met à jour en temps réel
listProduct = Button(frameButton,text="Afficher la liste des produits",command=SelectFrom.productList)

frameButton.grid(row=1,column=0)
listProduct.grid(row=1,column=0,padx = 20,pady = 25,ipady=20)
addProductButton.grid(row=1,column=1,padx = 10,pady = 25,ipady=20)
deleteProductButton.grid(row=1,column=2,padx = 10,pady = 25,ipady=20)
modifyProductButton.grid(row=1,column=3,padx = 10,pady = 25,ipady=20)



mainWindow.mainloop()
    
    