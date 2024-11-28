import tkinter as tk
from tkinter import messagebox
from tkinter import font
from PIL import Image, ImageTk
import json
import os

# Fișierul în care stocăm datele
fisier_date = "biblioteca.json"

# Încărcarea datelor din fișier
def incarca_date():
    if os.path.exists(fisier_date):
        with open(fisier_date, "r", encoding="utf-8") as f:  # Adaugă encoding="utf-8"
            return json.load(f)
    return []import tkinter as tk

def create_search_frame(parent):
    """Creates the search frame with a label, entry, and button."""
    frame_search = tk.Frame(parent, bg="#f0f0f0")
    frame_search.pack(pady=10)

    tk.Label(frame_search, text="Căutare:", font=("Helvetica", 12), bg="#f0f0f0").pack(side=tk.LEFT, padx=5)
    
    entry_search = tk.Entry(frame_search, **stil_entry)
    entry_search.pack(side=tk.LEFT, padx=5)

    search_button = tk.Button(frame_search, text="Caută", command=cauta_carte, **stil_buton)
    search_button.pack(side=tk.LEFT, padx=10)

    return entry_search  # Return the entry for further use if needed

def create_list_frame(parent):
    """Creates the list frame to display books."""
    frame_list = tk.Frame(parent)
    frame_list.pack(pady=10)

    list_books = tk.Listbox(frame_list, width=50, height=10, font=("Helvetica", 10))
    list_books.pack()

    return list_books  # Return the listbox for further use if needed

def create_button_frame(parent):
    """Creates the button frame with edit and delete buttons."""
    frame_buttons = tk.Frame(parent, bg="#f0f0f0")
    frame_buttons.pack(pady=20)

    edit_button = tk.Button(frame_buttons, text="Editează carte", command=editeaza_carte, **stil_buton)
    edit_button.pack(side=tk.LEFT, padx=10)

    delete_button = tk.Button(frame_buttons, text="Șterge carte", command=sterge_carte, **stil_buton)
    delete_button.pack(side=tk.LEFT, padx=10)

def main():
    """Main function to set up the application."""
    app = tk.Tk()
    app.title("Biblioteca")

    entry_cautare = create_search_frame(app)
    lista_carti = create_list_frame(app)
    create_button_frame(app)

    # Initialize the book list
    actualizeaza_lista()

    app.mainloop()

if __name__ == "__main__":
    main()import tkinter as tk

def create_search_frame(parent):
    """Creates the search frame with a label, entry, and button."""
    frame_search = tk.Frame(parent, bg="#f0f0f0")
    frame_search.pack(pady=10)

    tk.Label(frame_search, text="Căutare:", font=("Helvetica", 12), bg="#f0f0f0").pack(side=tk.LEFT, padx=5)
    
    entry_search = tk.Entry(frame_search, **stil_entry)
    entry_search.pack(side=tk.LEFT, padx=5)

    search_button = tk.Button(frame_search, text="Caută", command=cauta_carte, **stil_buton)
    search_button.pack(side=tk.LEFT, padx=10)

    return entry_search  # Return the entry for further use if needed

def create_list_frame(parent):
    """Creates the list frame to display books."""
    frame_list = tk.Frame(parent)
    frame_list.pack(pady=10)

    list_books = tk.Listbox(frame_list, width=50, height=10, font=("Helvetica", 10))
    list_books.pack()

    return list_books  # Return the listbox for further use if needed

def create_button_frame(parent):
    """Creates the button frame with edit and delete buttons."""
    frame_buttons = tk.Frame(parent, bg="#f0f0f0")
    frame_buttons.pack(pady=20)

    edit_button = tk.Button(frame_buttons, text="Editează carte", command=editeaza_carte, **stil_buton)
    edit_button.pack(side=tk.LEFT, padx=10)

    delete_button = tk.Button(frame_buttons, text="Șterge carte", command=sterge_carte, **stil_buton)
    delete_button.pack(side=tk.LEFT, padx=10)

def main():
    """Main function to set up the application."""
    app = tk.Tk()
    app.title("Biblioteca")

    entry_cautare = create_search_frame(app)
    lista_carti = create_list_frame(app)
    create_button_frame(app)

    # Initialize the book list
    actualizeaza_lista()

    app.mainloop()

if __name__ == "__main__":
    main()

# Salvarea datelor în fișier
def salveaza_date():
    with open(fisier_date, "w") as f:
        json.dump(biblioteca, f, indent=4)

# Inițializăm biblioteca cu datele încărcate
biblioteca = incarca_date()

# Funcții pentru gestionarea cărților
def adauga_carte():
    titlu = entry_titlu.get()
    autor = entry_autor.get()
    an_publicare = entry_an.get()
    sursa = entry_sursa.get()

    if not titlu or not autor or not an_publicare or not sursa:
        messagebox.showwarning("Eroare", "Toate câmpurile trebuie completate!")
        return
    
    if not an_publicare.isdigit():
        messagebox.showwarning("Eroare", "Anul publicării trebuie să fie un număr!")
        return

    biblioteca.append({"Titlu": titlu, "Autor": autor, "An Publicare": an_publicare, "Sursa": sursa})
    salveaza_date()
    messagebox.showinfo("Succes", f"Cartea '{titlu}' a fost adăugată!")
    entry_titlu.delete(0, tk.END)
    entry_autor.delete(0, tk.END)
    entry_an.delete(0, tk.END)
    entry_sursa.delete(0, tk.END)
    actualizeaza_lista()

def sterge_carte():
    try:
        selectia = lista_carti.curselection()
        index = selectia[0]
        carte = biblioteca.pop(index)
        salveaza_date()
        messagebox.showinfo("Succes", f"Cartea '{carte['Titlu']}' a fost ștearsă!")
        actualizeaza_lista()
    except IndexError:
        messagebox.showwarning("Eroare", "Selectați o carte pentru a șterge!")

def cauta_carte():
    cautare = entry_cautare.get().lower()
    lista_carti.delete(0, tk.END)
    for carte in biblioteca:
        if cautare in carte["Titlu"].lower() or cautare in carte["Autor"].lower():
            lista_carti.insert(tk.END, f"{carte['Titlu']} - {carte['Autor']} ({carte['An Publicare']}) - Sursa: {carte['Sursa']}")
    if lista_carti.size() == 0:
        lista_carti.insert(tk.END, "Nicio carte găsită.")

def editeaza_carte():
    try:
        selectia = lista_carti.curselection()
        index = selectia[0]
        carte = biblioteca[index]

        # Fereastră pentru editare
        def salveaza_editare():
            titlu_nou = entry_titlu_edit.get()
            autor_nou = entry_autor_edit.get()
            an_nou = entry_an_edit.get()
            sursa_noua = entry_sursa_edit.get()

            if not titlu_nou or not autor_nou or not an_nou or not sursa_noua:
                messagebox.showwarning("Eroare", "Toate câmpurile trebuie completate!")
                return
            
            if not an_nou.isdigit():
                messagebox.showwarning("Eroare", "Anul publicării trebuie să fie un număr!")
                return

            carte["Titlu"] = titlu_nou
            carte["Autor"] = autor_nou
            carte["An Publicare"] = an_nou
            carte["Sursa"] = sursa_noua
            salveaza_date()
            messagebox.showinfo("Succes", f"Cartea '{titlu_nou}' a fost actualizată!")
            actualizeaza_lista()
            fereastra_editare.destroy()

        fereastra_editare = tk.Toplevel(app)
        fereastra_editare.title("Editează carte")
        
        tk.Label(fereastra_editare, text="Titlu:", font=("Helvetica", 10)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        entry_titlu_edit = tk.Entry(fereastra_editare, width=30, font=("Helvetica", 10))
        entry_titlu_edit.grid(row=0, column=1, padx=5, pady=5)
        entry_titlu_edit.insert(0, carte["Titlu"])

        tk.Label(fereastra_editare, text="Autor:", font=("Helvetica", 10)).grid(row=1, column=0, padx=5, pady=5, sticky="e")
        entry_autor_edit = tk.Entry(fereastra_editare, width=30, font=("Helvetica", 10))
        entry_autor_edit.grid(row=1, column=1, padx=5, pady=5)
        entry_autor_edit.insert(0, carte["Autor"])

        tk.Label(fereastra_editare, text="An Publicare:", font=("Helvetica", 10)).grid(row=2, column=0, padx=5, pady=5, sticky="e")
        entry_an_edit = tk.Entry(fereastra_editare, width=30, font=("Helvetica", 10))
        entry_an_edit.grid(row=2, column=1, padx=5, pady=5)
        entry_an_edit.insert(0, carte["An Publicare"])

        tk.Label(fereastra_editare, text="Sursa:", font=("Helvetica", 10)).grid(row=3, column=0, padx=5, pady=5, sticky="e")
        entry_sursa_edit = tk.Entry(fereastra_editare, width=30, font=("Helvetica", 10))
        entry_sursa_edit.grid(row=3, column=1, padx=5, pady=5)
        entry_sursa_edit.insert(0, carte["Sursa"])

        tk.Button(fereastra_editare, text="Salvează", font=("Helvetica", 10), command=salveaza_editare).grid(row=4, column=0, columnspan=2, pady=10)
    except IndexError:
        messagebox.showwarning("Eroare", "Selectați o carte pentru a edita!")

def actualizeaza_lista():
    lista_carti.delete(0, tk.END)
    for carte in biblioteca:
        lista_carti.insert(tk.END, f"{carte['Titlu']} - {carte['Autor']} ({carte['An Publicare']}) - Sursa: {carte['Sursa']}")

# Interfața grafică
app = tk.Tk()
app.title("Gestionare Bibliotecă")
app.geometry("600x600")
app.config(bg="#f0f0f0")

# Adăugăm fundal
try:
    img_fundal = Image.open("fundal.jpg")  # Alege imaginea dorită
    img_fundal = img_fundal.resize((600, 600))  # Ajustează dimensiunile imaginii
    photo_fundal = ImageTk.PhotoImage(img_fundal)
    label_fundal = tk.Label(app, image=photo_fundal)
    label_fundal.place(relwidth=1, relheight=1)
except:
    print("Imaginea de fundal nu a fost găsită!")

# Stiluri
stil_buton = {"font": ("Helvetica", 12), "bg": "#4CAF50", "fg": "white", "relief": "flat", "width": 20, "height": 2}
stil_entry = {"font": ("Helvetica", 10), "width": 30}

# Secțiunea de introducere a datelor
frame_input = tk.Frame(app, bg="#f0f0f0")
frame_input.pack(pady=20)

tk.Label(frame_input, text="Titlu:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_titlu = tk.Entry(frame_input, **stil_entry)
entry_titlu.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Autor:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_autor = tk.Entry(frame_input, **stil_entry)
entry_autor.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_input, text="An Publicare:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_an = tk.Entry(frame_input, **stil_entry)
entry_an.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Sursa:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=3, column=0, padx=5, pady=5, sticky="e")
entry_sursa = tk.Entry(frame_input, **stil_entry)
entry_sursa.grid(row=3, column=1, padx=5, pady=5)

tk.Button(frame_input, text="Adaugă carte", command=adauga_carte, **stil_buton).grid(row=4, column=0, columnspan=2, pady=10)

# Secțiunea de căutare
frame_cautare = tk.Frame(app, bg="#f0f0f0")
frame_cautare.pack(pady=10)

tk.Label(frame_cautare, text="Căutare:", font=("Helvetica", 12), bg="#f0f0f0").pack(side=tk.LEFT, padx=5)
entry_cautare = tk.Entry(frame_cautare, **stil_entry)
entry_cautare.pack(side=tk.LEFT, padx=5)

tk.Button(frame_cautare, text="Caută", command=cauta_carte, **stil_buton).pack(side=tk.LEFT, padx=10)

# Secțiunea de listare a cărților
frame_lista = tk.Frame(app)
frame_lista.pack(pady=10)

lista_carti = tk.Listbox(frame_lista, width=50, height=10, font=("Helvetica", 10))
lista_carti.pack()

# Butoane pentru editare și ștergere
frame_butoane = tk.Frame(app, bg="#f0f0f0")
frame_butoane.pack(pady=20)

tk.Button(frame_butoane, text="Editează carte", command=editeaza_carte, **stil_buton).pack(side=tk.LEFT, padx=10)
tk.Button(frame_butoane, text="Șterge carte", command=sterge_carte, **stil_buton).pack(side=tk.LEFT, padx=10)

# Actualizează lista la început
actualizeaza_lista()

app.mainloop()
