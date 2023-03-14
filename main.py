import customtkinter
import os
import plotly.graph_objects as go
import networkx as nx
import matplotlib.pyplot as plt

def scan_event():
    #scan device with nmap using the ip address output txt file
    #TODO: Check for empty ip field
    if ip_field.get() == "":
        print("Error: IP Address field is empty")
        return

    #Check for valid IP format for subnet scanning or individual IP
    if "/" in ip_field.get():
        if ip_field.get().count(".") != 3:
            print("Error: Invalid IP Address")
            return
    #Check for valid IP format for individual IP
    else:
        if ip_field.get().count(".") != 3:
            print("Error: Invalid IP Address")
            return
        else:
            for i in ip_field.get().split("."):
                if int(i) > 255:
                    print("Error: Invalid IP Address")
                    return


    ip = ip_field.get()
    file = file_field.get()

    if file == "":
        file = "scan"

    print("Starting Scan...")
    
    #use nmap to scan the ip address
    os.system("nmap " + ip + " > " + "output\\"+ file + ".txt")
    print("Scan Complete")

    #Error checking
    if os.path.exists("output\\" + file + ".txt") == False:
        print()
        print()
        print()
        print("Error: Scan Image File not found, recreating...")
        os.mkdir("output")
        print()
        print()
        print()
        print("Restarting Scan...")

        #create the folder if it doesn't exist
        os.system("nmap " + ip + " > " + "output\\"+ file + ".txt")
        print("Scan Complete")

    #create a network graph for every report line starting with "Nmap scan report for"
    print("Creating Graph...")
    G = nx.Graph()
    with open("output\\" + file + ".txt", "r") as f:
        for line in f:
            if "Nmap scan report for" in line:
                G.add_node(line.split(" ")[4])

    print("Graph Created")

    #if multiple nodes, add edges between them
    if len(G.nodes) > 1:
        print("Adding Edges...")
        with open("output\\" + file + ".txt", "r") as f:
            for line in f:
                if "Nmap scan report for" in line:
                    ip1 = line.split(" ")[4]
                elif "Host is up" in line:
                    ip2 = line.split(" ")[4]
                    G.add_edge(ip1, ip2)
    
    print("Edges Added")

    #draw the graph
    print("Drawing Graph...")
    #draw the graph with #212121 background, light blue nodes, and white text
    plt.figure(figsize=(20, 20))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="#1e90ff", edge_color="#1e90ff", font_color="white", font_size=10, node_size=1000, width=2, alpha=0.8, background_color="#212121")

    print("Graph Drawn")

    plt.savefig("output\\" + file + "-results" + ".png", format="PNG")
    

    return


    #image_results = customtkinter.CTkImage(master=frame2, image="images/output.png", width=1000, height=500)

    #TODO: Open the file and get the results (common ports, # of devices pinged, etc.)


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.iconbitmap("images/capto.ico")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(2, weight=1)
root.title("Capto: Network Scanner")
root.geometry("1280x720")

#Frames
frame1 = customtkinter.CTkFrame(master=root)
frame1.grid(row=0, column=0, padx=10, pady=10, sticky="ns")


frame2 = customtkinter.CTkFrame(master=root)
frame2.grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky="news")


#Capto Input Widget
capto_label = customtkinter.CTkLabel(master=frame1, text="Capto", font=("Lato", 32), width=140, height=20).grid(row=0, column=0, padx=10, pady=20)

ip_field = customtkinter.CTkEntry(master=frame1, font=("Lato", 12), width=180, height=40, placeholder_text="IP Address or Range")
ip_field.grid(row=1, column=0, padx=30, pady=10)

file_field = customtkinter.CTkEntry(master=frame1, font=("Lato", 12), width=180, height=40, placeholder_text="Output File Name")
file_field.grid(row=2, column=0, padx=10, pady=10)

label = customtkinter.CTkButton(master=frame1, text="Scan", font=("Lato", 20), width=140, height=35, command=lambda: scan_event()).grid(row=3, column=0, padx=10, pady=10)


#Capto Output Widget (Results)
capto_label = customtkinter.CTkLabel(master=frame2, text="Results", font=("Lato", 32), width=140, height=20).grid(row=0, column=0, padx=20, pady=15, sticky="n")

















root.mainloop()
