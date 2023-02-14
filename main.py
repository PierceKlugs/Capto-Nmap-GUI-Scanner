import customtkinter
import os



def scan_event():
    #scan device with nmap using the ip address output txt file
    #TODO: Check for empty ip field

    #TODO: Check for valid IP format

    ip = ip_field.get()
    file = file_field.get()

    if file == "":
        file = "scan"

    print("Starting Scan...")
    
    #use nmap to scan the ip address
    os.system("nmap " + ip + " > " + file + ".txt")
    print("Scan Complete")





customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.iconbitmap("images/capto.ico")
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure((0, 2), weight=1)
root.title("Capto: Network Scanner")
root.geometry("500x500")


frame1 = customtkinter.CTkFrame(master=root)
frame1.pack(pady=20, padx=60, fill="both", expand=True)


#Add a label to the frame1 with the Title Capto
capto_label = customtkinter.CTkLabel(master=frame1, text="Capto", font=("Lato", 32), width=140, height=20)
capto_label.pack(pady=30, padx=30, fill="both", expand=False)

#Add a field for the IP range or address
ip_field = customtkinter.CTkEntry(master=frame1, font=("Lato", 12), width=140, height=40, placeholder_text="IP Address or Range")
ip_field.pack(pady=20, padx=60, fill="both", expand=False)

#Add a field for output file name and/or location
file_field = customtkinter.CTkEntry(master=frame1, font=("Lato", 12), width=140, height=40, placeholder_text="Output File Name")
file_field.pack(pady=20, padx=60, fill="both", expand=False)

#Scan Button
label = customtkinter.CTkButton(master=frame1, text="Scan", font=("Lato", 20), width=140, height=40, command=lambda: scan_event())
label.pack(pady=20, padx=60, fill="both", expand=False)




















root.mainloop()
