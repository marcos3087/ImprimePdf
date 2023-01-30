import sys, win32api 
from tkinter import messagebox
if(len(sys.argv)==1):
    messagebox.showwarning("Erro", "Nenhum nome de arquivo encontrado")
    
else:
    nombol = sys.argv[1]
    pdf_file = r'\\BOXSTER\Senior\temp\{}'

    final_text = pdf_file.format(nombol)
    #final_text = "//BOXSTER/Senior/temp/"+nombol

    try:
        x  =win32api.ShellExecute(0, "print", final_text, None, ".", 0)
        print(x)
        messagebox.showinfo("Imprimir", "Boleto enviado para a impressora.")

    except Exception as e:
        print(e)
        messagebox.showwarning("Erro", "Erro ao localizar o arquivo")


