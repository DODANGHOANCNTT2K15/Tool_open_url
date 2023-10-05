import webbrowser
import csv
import tkinter as tk
from tkinter import messagebox,filedialog

filepath = ""
begin = 1
skip = 5
end = begin - 1 + skip
index = 0
check = True
root = tk.Tk()
root.geometry("400x200")
label = tk.Label(root, text="")
label.pack()

var1 = tk.StringVar()
var2 = tk.StringVar()

entry1 = tk.Entry(root, textvariable=var1)
entry1.pack()

entry2 = tk.Entry(root, textvariable=var2)
entry2.pack()

def get_info():
    global begin, skip, var1, var2, end
    if not var1.get() or not var2.get():
        messagebox.showwarning("Oh no", "Chưa nhập thông tin,Mặc định là 5 một lúc")
    else:
        begin = int(var1.get())
        skip = int(var2.get())
        end = begin - 1 + skip
        messagebox.showwarning("Okey", "Đã cập nhật thông tin")

button = tk.Button(root, text="Lấy thông tin", command=get_info)
button.pack()

def open_file():
    global filepath, label
    filepath = filedialog.askopenfilename()
    if not filepath:
        messagebox.showwarning("Chú ý", "Chưa có file !")
    else:
        messagebox.showwarning("Okey", f"Đã có file  {filepath}!")
        label.config(text=f"{filepath}")
        
def run_file():
    global filepath, begin, end, index
    if not filepath:
        print("no file")
    else:
        with open(filepath, 'r') as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if begin - 1 <= i < end:
                    webbrowser.open_new('https://www.tiktok.com/@' + row[0])
                    index += 1
                    if index >= skip:
                        begin += skip
                        end += skip
                        index = 0
                        break

def continue_file():
    run_file()

upfile_button = tk.Button(root, text="Chọn file", command=open_file)
run_button = tk.Button(root, text="Chạy", command=run_file)
continue_button = tk.Button(root, text="Tiếp tục", command=continue_file)

upfile_button.pack()
run_button.pack()
continue_button.pack()
root.mainloop()