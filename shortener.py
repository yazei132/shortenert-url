import tkinter as tk
from tkinter import messagebox
import pyshorteners


# criando função para encurtar
def encurtar_url():
    url_longa = entry_url.get()
    if not url_longa:
        messagebox.showwarning("Aviso", "Por favor, cole uma URL.")
        return
    
    try:
        type_tiny = pyshorteners.Shortener()
        url_curta = type_tiny.tinyurl.short(url_longa)
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, url_curta)
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível encurtar a URL.\nErro: {e}")

# Cria janela principal
root = tk.Tk()
root.title("Encurtador de URL")
root.geometry("400x150")
root.resizable(False, False)

# input para URL longa
label_url = tk.Label(root, text="Cole a URL longa:")
label_url.pack(pady=(10, 0))

entry_url = tk.Entry(root, width=50)
entry_url.pack(pady=5)

# Botão para encurtar
btn_encurtar = tk.Button(root, text="Encurtar URL", command=encurtar_url)
btn_encurtar.pack(pady=5)

# output para mostrar URL curta
label_resultado = tk.Label(root, text="URL curta:")
label_resultado.pack()

entry_resultado = tk.Entry(root, width=50)
entry_resultado.pack(pady=5)

root.mainloop()
