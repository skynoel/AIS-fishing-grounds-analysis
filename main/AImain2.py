import tkinter as tk
from tkinter import filedialog
import AIS.mad
import AIS.patd
import AIS.chr_patd

def execute_mode():
    selected_mode = mode_var.get()
    selected_file = folder_var.get()
    save_filename = save_var.get()

    if selected_mode == "MAD":
        selected_year = year_var.get()
        selected_month = month_var.get()       
        file=AIS.mad.avperm(selected_file,save_filename,selected_year,selected_month)  #將經過時間碼標記的原始資料轉變為個小時每分鐘平均封包數的資料，並回傳檔名
        AIS.mad.graph(file)#利用該資料繪製成MAD
    elif selected_mode == "PATD":
        AIS.patd.chose(selected_file,save_filename)
    elif selected_mode == "CHR_PATD":
        AIS.chr_patd.chr(selected_file,save_filename)
        # Perform operations for CHR_PATD with selected_file
    elif selected_mode == "ASD":
        print("沒做出來")
        # Perform operations for ASD with selected_file
    elif selected_mode == "PFG":
        print("沒做出來")
        # Perform operations for PFG with selected_file

def browse_folder():
    folder_path = filedialog.askdirectory()
    folder_var.set(folder_path)

root = tk.Tk()
root.title("UI Interface")

# Mode selection
mode_var = tk.StringVar(root)
mode_var.set("MAD")  # Set default mode
mode_options = ["MAD", "PATD", "CHR_PATD", "ASD", "PFG"]
mode_dropdown = tk.OptionMenu(root, mode_var, *mode_options)
mode_dropdown.pack()

# Folder selection
folder_var = tk.StringVar(root)
folder_button = tk.Button(root, text="Browse", command=browse_folder)
folder_button.pack()
# Folder path display
folder_path_label = tk.Label(root, textvariable=folder_var)
folder_path_label.pack()
# Date selection for MAD

year_label = tk.Label(root, text="Enter year:")
year_label.pack()
year_var = tk.IntVar(root)  # Use IntVar to store integer value
year_entry = tk.Entry(root, textvariable=year_var)
year_entry.pack()

month_label = tk.Label(root, text="Enter month:")
month_label.pack()
month_var = tk.IntVar(root)  # Use IntVar to store integer value
month_entry = tk.Entry(root, textvariable=month_var)
month_entry.pack()

# Save filename input
save_label = tk.Label(root, text="Enter save filename:")
save_label.pack()
save_var = tk.StringVar(root)
save_entry = tk.Entry(root, textvariable=save_var)
save_entry.pack()


# Execute button
execute_button = tk.Button(root, text="Execute", command=execute_mode)
execute_button.pack()

root.geometry("500x500")

root.mainloop()