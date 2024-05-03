import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(paths, output):
    pdf_writer = PdfWriter()
    for path in paths:
        pdf_reader = PdfReader(path)
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)
    with open(output, 'wb') as out:
        pdf_writer.write(out)

def select_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    if len(file_paths) < 2:
        messagebox.showerror("错误", "请选择至少两个PDF文件进行合并！")
        return
    return file_paths

def on_merge_click():
    paths = select_files()
    if paths:
        output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if output_path:
            merge_pdfs(paths, output_path)
            messagebox.showinfo("完成", "PDF文件已成功合并到：" + output_path)
        else:
            messagebox.showinfo("取消", "合并操作已取消")
    else:
        messagebox.showinfo("取消", "合并操作已取消")

app = tk.Tk()
app.title("PDF合并工具")
app.geometry("300x150")

merge_button = tk.Button(app, text="合并PDF", command=on_merge_click, height=2, width=15)
merge_button.pack(pady=20)

app.mainloop()
