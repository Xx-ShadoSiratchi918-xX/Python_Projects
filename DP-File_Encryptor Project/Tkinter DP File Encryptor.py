# Importem els mòduls "*", "filedialog", "messagebox" per utilitzar-los més tard.
from tkinter import *
from tkinter import filedialog, messagebox

# Creem la finestra principal per crear una interfície i configurar el contingut dins la finestra.
root = Tk()
root.geometry('600x500')
root.title("Encriptador d`Arxius DP")
root.iconbitmap("Graphicloads-Flat-Finance-Lock.ico")

# Crear els marcs para las páginas
page1 = Frame(root, bg="cyan", borderwidth=10)
page2 = Frame(root, bg="cyan", borderwidth=10)
page3 = Frame(root, bg="cyan", borderwidth=10)
page4 = Frame(root, bg="cyan", borderwidth=10)
page5 = Frame(root, bg="cyan", borderwidth=10)

numbers_of_encriptation = 0
numbers_of_change_method = 1

# Define una funció per mostrar la página 1
def show_page1():
    page2.pack_forget()
    page3.pack_forget()
    page4.pack_forget()
    page5.pack_forget()
    page1.pack(fill='both', expand=True)


# Define una funció per mostrar la página 2
def show_page2():
    page1.pack_forget()
    page3.pack_forget()
    page4.pack_forget()
    page5.pack_forget()
    page2.pack(fill='both', expand=True)


# Define una funció pera mostrar la página 3
def show_page3():
    page1.pack_forget()
    page2.pack_forget()
    page4.pack_forget()
    page5.pack_forget()
    page3.pack(fill='both', expand=True)


# Define una funció per mostrar la página 4
def show_page4():
    page1.pack_forget()
    page2.pack_forget()
    page3.pack_forget()
    page5.pack_forget()
    page4.pack(fill='both', expand=True)


# Define una funció per mostrar la página 5
def show_page5():
    page1.pack_forget()
    page2.pack_forget()
    page3.pack_forget()
    page4.pack_forget()
    page5.pack(fill='both', expand=True)


# Afagir contingut a la página 1
title_label = Label(page1, text='🔒 Benvingut a l`Encriptador d`Arxius DP 🔓', font="Verdana 15 bold", bg="darkcyan", fg="white")
title_label.pack(pady=50)

# Crea los botones para canviar entre páginas
button1 = Button(page1, text='  Encriptar 🔏 ', font="Verdana 13", command=show_page2, bg="lightblue", fg="white")
button2 = Button(page1, text='  Desxifrar 🔐 ', font="Verdana 13", command=show_page3, bg="lightblue", fg="white")
button3 = Button(page1, text='  Configuració ⚙ ', font="Verdana 13", command=show_page4, bg="lightblue", fg="white")
button4 = Button(page1, text='  Ajuda ❔  ', font="Verdana 13", command=show_page5, bg="lightblue", fg="white")

button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)
button4.pack(pady=10)

# Crea los botónes de "retornada" a la página de inici
back_button1 = Button(page2, text='   ❮—   ', command=show_page1, bg="darkcyan", fg="white")
back_button2 = Button(page3, text='   ❮—   ', command=show_page1, bg="darkcyan", fg="white")
back_button3 = Button(page4, text='   ❮—   ', command=show_page1, bg="darkcyan", fg="white")
back_button4 = Button(page5, text='   ❮—   ', command=show_page1, bg="darkcyan", fg="white")

back_button1.pack(side="top", pady=10, anchor=W)
back_button2.pack(side="top", pady=10, anchor=W)
back_button3.pack(side="top", pady=10, anchor=W)
back_button4.pack(side="top", pady=10, anchor=W)

# Define las funcions de la página 2

# Aquesta funció desa l'entrada de caràcters escrits per l'usuari a "display_entry2".
def get_entry2_path():
    get_path = display_entry2.get()
    return get_path

# Aquesta funció desa el mètode d'encriptació i el guarda a la variable de cadena de text "finale_text".
offset = StringVar()
number_changed = offset.get()

offset.set("1")

def change_method_dialog():
    response = messagebox.askokcancel("Canvi de mètode", "Esteu segur de canviar el mètode?")
    if response == True:
        global number_changed
        number_changed = int(offset.get())
        messagebox.showinfo("Mètode canviat correctament", "S'ha canviat el mètode amb èxit")

def encrypt(text):
    final_text = ''
    if offset.get() != "1":
        change_method_dialog()
    for letter in text:
        ascii = ord(letter)
        ascii += (numbers_of_change_method, int(offset.get()))
        final_text += chr(ascii)
    return final_text


# Aquesta funció declara una funció global, llegeix el fitxer, el reescriu per encriptar-lo,
# explica les vegades que ha encriptat el fitxer i mostra un diàleg que el fitxer es va encriptar amb èxit
def encrypt_file():
    global numbers_of_encriptation
    path_file = get_entry2_path()
    file = open(path_file, 'r')
    text = file.read()
    file.close()
    encrypted_text = encrypt(text)

    file = open(path_file, 'w')
    file.write(encrypted_text)
    file.close()

    numbers_of_encriptation += 1
    encriptention_numbers.config(text=f'numeros de veces encrpitacion: {str(numbers_of_encriptation)}')
    desncriptention_numbers.config(text=f'numeros de veces a desencrpitar: {str(numbers_of_encriptation)}')
    messagebox.showinfo("L'operació s'ha realitzat amb èxit", "El fitxer s'ha encriptat correctament")
    return numbers_of_encriptation

# Aquesta funció és l'alternativa per a l'encriptació manual,
# fa que surti un quadre de diàleg per seleccionar el fitxer i no cal fer-ho a mà
def select_to_encrypt():
    path_file = filedialog.askopenfilename()
    display_entry2.insert(0, path_file)

# Afagir contingut a la página 2

insert_pathfile = Label(page2, text='Introduïu la ruta absoluta del fitxer: ', font="Verdana 13 bold", bg="lightblue", fg="white")
encriptention_numbers = Label(page2, text=f'Numero de veces encriptado: {str(numbers_of_encriptation)}', font="Verdana 13 bold", bg="lightblue", fg="white")
# Creem una entrada de text per introduir la ruta absoluta del fitxer.
display_entry2 = Entry(page2, font='Verdana 15', bg="lightgrey")

# Cridem a les etiquetes i l'entrada de text per mostrar-ho a la pàgina 2 de la finestra.
insert_pathfile.pack(pady=10)
encriptention_numbers.pack(pady=10)
display_entry2.pack(pady=10)

# Guardem en una variable una imatge per cridar més tard a la finestra.
select_file_image = PhotoImage(file="carpeta-de-archivos-azul-con-los-documentos-34337927 (1).png")

# botons per encriptar els fitxers.
encrypt_alternative_button = Button(page2, text=" Selccionar un arxiu ", font="Verdana 9 bold", compound="left", bg="white", fg="darkcyan", command=select_to_encrypt, image=select_file_image)
encrypt_Button = Button(page2, text="Encriptar arxiu", font="Verdana 13 bold", bg="darkcyan", fg="white", command=encrypt_file)

encrypt_alternative_button.pack(padx=10)
encrypt_Button.pack(pady=10)

# Definir funciones de la página 3

# Aquesta funció desa l'entrada de caràcters escrits per l'usuari a "display_entry3".
def get_entry3_path():
    get_path = display_entry3.get()
    return get_path

# Aquesta funció desa el mètode d'encriptació i el guarda a la variable de cadena de text "finale_text".
def decrypt(text):
    finale_text = ''
    for letter in text:
        ascii = ord(letter)
        ascii -= numbers_of_change_method
        finale_text += chr(ascii)
    return finale_text

# Aquesta funció declara una funció global, llegeix el fitxer, el reescriu per desxifrar-lo,
# explica les vegades que falta per desxifrar el fitxer i mostra un diàleg que el fitxer s'ha desxifrat amb èxit
def decrypt_file():
    global numbers_of_encriptation
    path_file = get_entry3_path()
    file = open(path_file, 'r')
    text = file.read()
    file.close()
    decrypted_text = decrypt(text)

    file = open(path_file, 'w')
    file.write(decrypted_text)
    file.close()
    print(numbers_of_encriptation)
    numbers_of_encriptation -= 1
    encriptention_numbers.config(text=f'numeros de veces encrpitacion: {str(numbers_of_encriptation)}')
    desncriptention_numbers.config(text=f'numeros de veces a desencrpitar: {str(numbers_of_encriptation)}')
    messagebox.showinfo("L'operació s'ha realitzat amb èxit", "El fitxer s'ha desxifrat correctament")

# Aquesta funció és l'alternativa per a l'encriptació manual,
# fa que surti un quadre de diàleg per seleccionar el fitxer i no cal fer-ho a mà
def select_to_encrypt2():
    path_file = filedialog.askopenfilename()
    display_entry3.insert(0, path_file)

# Creem les vegades que compta el mètode d'encriptació i
# el desa com a íntegre en variable "change_method_of_encriptation".
def change_method_of_encriptation():
    global numbers_of_change_method
    print(numbers_of_change_method)
    numbers_of_change_method = int(change_methode_user.get())
    print(numbers_of_change_method)



# Afagir el contigut a la página 3

insert_pathfile2 = Label(page3, text='Introduïu la ruta absoluta del fitxer: ', font="Verdana 13 bold", bg="lightblue", fg="white")
desncriptention_numbers = Label(page3, text=f'numeros de veces a desencrpitar: {str(numbers_of_encriptation)}', font="Verdana 13 bold", bg="lightblue", fg="white")
display_entry3 = Entry(page3, font='Verdana 15', bg="lightgrey")

insert_pathfile2.pack(pady=10)
desncriptention_numbers.pack(pady=10)
display_entry3.pack(pady=10)

# botones per desxifrar el fitxers

encrypt_alternative_button2 = Button(page3, text=" Selccionar un arxiu ", font="Verdana 9 bold", compound="left", bg="white", fg="darkcyan", command=select_to_encrypt2, image=select_file_image)
Desencrypt_Button = Button(page3, text=" Desxifrar arxiu", font="Verdana 13 bold", bg="darkcyan", fg="white", command=decrypt_file)

encrypt_alternative_button2.pack(padx=10)
Desencrypt_Button.pack(pady=10)

# Afagir el contigut a la página 4

configruation_label = Label(page4, text='Configuració', font="Verdana 15 bold", bg="lightblue", fg="white")
change_methode_user = Entry(page4, font='Verdana 15', bg="lightgrey",textvariable=offset)
methode_changes = Button(page4, text="Canviar Metode", font="Verdana 13 bold", bg="lightcyan", command=change_method_dialog)

# Cridem perque es mostre en totes els widgets en la pagina 4

configruation_label.pack(pady=10)
change_methode_user.pack(pady=10)
methode_changes.pack(pady=10)


# Añadir contenido a la página 5

# En aquesta apartat es mostra una pagina que serveix com ajuda per utilitzar el encriptador de arxius.

help_text = '''
Com utilitzar l'Encriptador d'Arxius DP:

1. Selecciona la pàgina "Encriptar" o "Desxifrar", depenent de si vols encriptar o desencriptar un fitxer.
2. Selecciona el fitxer que vols encriptar o desencriptar.
3. Espera a que l'operació s'acabi i apareixerà un missatge indicant que s'ha realitzat amb èxit.
4. Si vols, pots anar a la pàgina "Configuració" per si vols configurar el metode de encriptació.
'''

help_label = Text(page5, font="Verdana 7 bold", bg="darkcyan", fg="white", wrap="word", width=60, height=10)
help_label.insert('end', help_text)
help_label.config(state='disabled')

scrollbar = Scrollbar(page5, command=help_label.yview)
help_label.config(yscrollcommand=scrollbar.set)

example_pathfile = Label(page5, text="Exemple de com es una ruta absoluta del arxiu:", font="Verdana 13 bold", bg="lightblue", fg="white")
pathfile_route = Label(page5, text="\n C:/Users/<Usuari>/OneDrive(Opcional)/Documents/<Domcument de prova> \n", font="Verdana 10 italic bold", bg="white", wraplength=500)
alternative_pathfile_example = Label(page5, text="Un altre exemple: ", font="Verdana 13 bold", bg="lightblue", fg="white")

example_pathfile.pack(pady=10)
pathfile_route.pack(pady=10)
alternative_pathfile_example.pack(pady=10)

example_image = PhotoImage(file="2023-05-05 10_06_48-Encriptador dArxius DP.png")
alternative_example = Label(page5, image=example_image)
example2_image = PhotoImage(file="2023-05-05 10_05_01-Python_Projects.py – Tkinter DP File Encryptor.py.png")
alternative_example2 = Label(page5, image=example2_image)

scrollbar.pack(side='right', fill='y')
help_label.pack(pady=20, padx=5)
alternative_example.pack()
alternative_example2.pack()


# Mostrar la página de inici
show_page1()

# Mostrar la ventana principal
root.mainloop()
