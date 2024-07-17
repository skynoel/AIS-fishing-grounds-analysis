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

def browse_file():
    file_path = filedialog.askopenfilename()
    folder_var.set(file_path)

root = tk.Tk()
root.title("UI Interface")
root.option_add("*Font", "Helvetica 18")
# Mode selection
mode_var = tk.StringVar(root)
mode_var.set("MAD")  # Set default mode
mode_options = ["MAD", "PATD", "CHR_PATD", "ASD", "PFG"]
mode_dropdown = tk.OptionMenu(root, mode_var, *mode_options)
mode_dropdown.pack()

# Folder selection
folder_var = tk.StringVar(root)
folder_frame = tk.Frame(root)
folder_frame.pack()

folder_button = tk.Button(folder_frame, text="folder", command=browse_folder)
folder_button.pack(side="left")

file_button = tk.Button(folder_frame, text="file", command=browse_file)
file_button.pack(side="left")
# Folder path display
folder_path_label = tk.Label(root, textvariable=folder_var)
folder_path_label.pack()
# Date selection for MAD
year_frame = tk.Frame(root)
year_frame.pack()

year_label = tk.Label(year_frame, text="Enter year:")
year_label.pack(side="left")
year_var = tk.IntVar(root)  # Use IntVar to store integer value
year_entry = tk.Entry(year_frame, textvariable=year_var)
year_entry.pack(side="left")

month_frame = tk.Frame(root)
month_frame.pack()
month_label = tk.Label(month_frame, text="Enter month:")
month_label.pack(side="left")
month_var = tk.IntVar(root)  # Use IntVar to store integer value
month_entry = tk.Entry(month_frame, textvariable=month_var)
month_entry.pack(side="left")

# Save filename input
filename_frame = tk.Frame(root)
filename_frame.pack()
save_label = tk.Label(filename_frame, text="Enter save filename:")
save_label.pack(side="left")
save_var = tk.StringVar(root)
save_entry = tk.Entry(filename_frame, textvariable=save_var)
save_entry.pack(side="left")


# Execute button
execute_button = tk.Button(root, text="Execute", command=execute_mode)
execute_button.pack()

root.geometry("600x450")



root.mainloop()