import os
import zlib
import tkinter as tk
from tkinter import filedialog, messagebox

def get_file_size(file_path):
    return os.path.getsize(file_path) if os.path.exists(file_path) else 0

def compress_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    
    output_path = file_path + ".compressed"
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
            compressed_data = zlib.compress(data)
        
        with open(output_path, 'wb') as f:
            f.write(compressed_data)
        
        original_size = get_file_size(file_path)
        compressed_size = get_file_size(output_path)
        messagebox.showinfo("Compression Successful", f"Original Size: {original_size} bytes\nCompressed Size: {compressed_size} bytes\nSaved as {output_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def decompress_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    
    if not file_path.endswith(".compressed"):
        messagebox.showwarning("Warning", "Please select a valid compressed file")
        return
    
    output_path = file_path.replace(".compressed", ".decompressed")
    try:
        with open(file_path, 'rb') as f:
            compressed_data = f.read()
            data = zlib.decompress(compressed_data)
        
        with open(output_path, 'wb') as f:
            f.write(data)
        
        compressed_size = get_file_size(file_path)
        decompressed_size = get_file_size(output_path)
        messagebox.showinfo("Decompression Successful", f"Compressed Size: {compressed_size} bytes\nDecompressed Size: {decompressed_size} bytes\nSaved as {output_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create UI
root = tk.Tk()
root.title("File Compression/Decompression System")
root.geometry("400x200")

tk.Label(root, text="Select an option:", font=("Arial", 12)).pack(pady=10)

tk.Button(root, text="Compress File", command=compress_file, font=("Arial", 10)).pack(pady=5)
tk.Button(root, text="Decompress File", command=decompress_file, font=("Arial", 10)).pack(pady=5)

tk.Button(root, text="Exit", command=root.quit, font=("Arial", 10)).pack(pady=10)

root.mainloop()
