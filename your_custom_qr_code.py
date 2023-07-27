import tkinter as tk

import qrcode


def generate_qrcode():
    input_text = entry.get("1.0", tk.END).strip()
    qr_code_name = qrCodeName.get()
    generated_document = qrcode.make(input_text)
    file_name = qr_code_name + ".jpg"
    generated_document.save(file_name)
    open_qrcode(file_name)
    entry.delete("1.0", tk.END)
    qrCodeName.delete(0, tk.END)


def open_qrcode(file_name):
    import os
    os.system(f'start {file_name}')


root = tk.Tk()
root.title("QR Code Generator")
root.geometry("800x400")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_entry = tk.Label(frame, text="Enter your QR Code content:")
label_entry.pack()

entry = tk.Text(frame, width=50, height=10, bg="#ffffe0")
entry.pack(pady=5)

label_qr_code_name = tk.Label(frame, text="File name for the QR Code:")
label_qr_code_name.pack()

qrCodeName = tk.Entry(frame, width=50, bg="#ffffe0")
qrCodeName.pack(pady=5)

btn_generate_qr_code = tk.Button(
    frame, text="Generate QR Code", command=generate_qrcode)
btn_generate_qr_code.pack(pady=10)

root.mainloop()
