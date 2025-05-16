
import tkinter as tk
from tkinter import messagebox
from connection import get_connection

# Συνάρτηση για εισαγωγή αυτοκινήτου
from connection import get_connection

def insert_car(model, year, color):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO cars (model, year, color) VALUES (%s, %s, %s)"
    values = (model, year, color)
    cursor.execute(sql, values)
    connection.commit()
    print("Car added.")
    cursor.close()
    connection.close()
    return True
except Exception as e:
print("Σφάλμα:", e)
return False


# Συνάρτηση για χειρισμό του κουμπιού
def submit_car():
    model = model_title.get()
    year = entry_year.get()
    color = entry_color.get()

    if not (model and year and color):
        messagebox.showwarning("Σφάλμα", "Συμπλήρωσε όλα τα πεδία!")
        return

    try:
        year = int(year)
    except ValueError:
        messagebox.showerror("Σφάλμα", "Το έτος πρέπει να είναι αριθμός!")
        return

    if insert_car(model, year, color):
        messagebox.showinfo("Επιτυχία", "Το αυτοκίνητο προστέθηκε επιτυχώς!")
        entry_model.delete(0, tk.END)
        entry_year.delete(0, tk.END)
        entry_color.delete(0, tk.END)
    else:
        messagebox.showerror("Αποτυχία", "Αποτυχία εισαγωγής αυτοκινήτου.")

# Δημιουργία παραθύρου
window = tk.Tk()
window.title("Εισαγωγή Αυτοκινήτου")
window.geometry("400x300")

# Ετικέτες και πεδία
tk.Label(window, text="Μοντέλο:").pack(pady=5)
entry_model = tk.Entry(window, width=40)
entry_model.pack()

tk.Label(window, text="Χρονολογία:").pack(pady=5)
entry_year = tk.Entry(window, width=40)
entry_year.pack()

tk.Label(window, text="Χρώμα:").pack(pady=5)
entry_color = tk.Entry(window, width=40)
entry_color.pack()

# Κουμπί καταχώρησης
submit_button = tk.Button(window, text="Καταχώρηση Αυτοκινήτου", command=submit_book)
submit_button.pack(pady=20)

# Εκκίνηση εφαρμογής
window.mainloop()
