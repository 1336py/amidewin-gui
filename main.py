# main.py

# stop skidding blud 

import customtkinter
import hPyT
import os
import time
import sys
import webbrowser
import random
import requests
import string
import win32api
import subprocess
import winreg as reg
import pywinstyles


root = customtkinter.CTk()
root.geometry("800x500")


# chatgpt code cus no wanna do 

def spoof_mac(new_mac):
    try:
        reg_path = r"SYSTEM\CurrentControlSet\Control\Class\{4D36E972-E325-11CE-BFC1-08002BE10318}"
        key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, reg_path)

        for i in range(100):
            try:
                subkey = reg.OpenKey(key, f"{i:04d}")
                name, _ = reg.QueryValueEx(subkey, "DriverDesc")

                try:
                    reg.QueryValueEx(subkey, "NetworkAddress")
                except FileNotFoundError:
                    reg.CloseKey(subkey)
                    continue

                reg.SetValueEx(subkey, "NetworkAddress", 0, reg.REG_SZ, new_mac)
                print(f"[+] MAC address for {name} changed to {new_mac}")

                reg.CloseKey(subkey)
                
                subprocess.call(f'netsh interface set interface "{name}" admin=disable', shell=True)
                time.sleep(2)
                subprocess.call(f'netsh interface set interface "{name}" admin=enable', shell=True)

            except Exception as e:
                print(f"[-] Error with {name}: {e}")
        
        reg.CloseKey(key)

    except Exception as e:
        print(f"common noob error! {e}")


def get_serial(command):
    try:
        result = subprocess.check_output(command, shell=True).decode().strip()
        return result
    except subprocess.CalledProcessError:
        return "N/A"

def get_cpu_serial():
    command = "wmic cpu get ProcessorId"
    return get_serial(command).split('\n')[1].strip()

def get_motherboard_serial():
    command = "wmic baseboard get serialnumber"
    return get_serial(command).split('\n')[1].strip()

def get_disk_serial():
    command = "wmic diskdrive get serialnumber"
    return get_serial(command).split('\n')[1].strip()

def get_system_uuid():
    command = "wmic csproduct get uuid"
    return get_serial(command).split('\n')[1].strip()

# chatgpt code stops here

def genSerials():
    serial = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(16))
    return serial

def permSpoof():
    win32api.MessageBox(0, "Permanently spoof. This CANNOT be undone. Procced?", "Confirm")
    if os.path.exists("AMIDEWINx64.EXE"):
        os.chdir("perm")
        spoof_cmds = [
            "/IVN \"AMI\"",
            "/SP \"System product name\"",
            "/SV \"System product name\"",
            "/SS \"" + genSerials() + "\"",
            "/SU AUTO",
            "/SK \"To Be Filled By O.E.M\"",
            "/BM \"AsRock\"",
            "/BP \"*8560M-C\"",
            "/BS \"" + genSerials() + "\"",
            "/BT \"Default String\"",
            "/BLC \"Default String\"",
            "/CM \"Default String\"",
            "/CV \"Default String\"",
            "/CS \"" + genSerials() + "\"",
            "/CA \"Default String\"",
            "/CSK \"SKU\"",
            "/PSN \"To Be Filled By O.E.M\"",
            "/PAT \"To Be Filled By O.E.M\""
        ]
        for cmd in spoof_cmds:
            os.system(f"AMIDEWINx64.EXE {cmd}")
        win32api.MessageBox(0, "Spoofing complete! Please vouch in the discord!", "Success")

    else:
        win32api.MessageBox(0, "AMIDEWINx64.EXE not found! Please reinstall the spoofer!", "Error")





tabview = customtkinter.CTkTabview(master=root, width=790, height=490)
tabview.pack(padx=20, pady=20)

tabview.add("Spoofer")  
tabview.add("Serials")  

perm_button = customtkinter.CTkButton(tabview.tab("Spoofer"), text="Spoof", command=permSpoof)
perm_button.pack(padx=20, pady=20)

mac_button = customtkinter.CTkButton(tabview.tab("Spoofer"), text="Mac Spoof (registry)", command=lambda: spoof_mac(genSerials()))
mac_button.pack(padx=20, pady=20)

motherboard_label = customtkinter.CTkLabel(tabview.tab("Serials"), text=f"Motherboard: {get_motherboard_serial()}")
motherboard_label.pack(padx=20, pady=20)

cpu_label = customtkinter.CTkLabel(tabview.tab("Serials"), text=f"CPU: {get_cpu_serial()}")
cpu_label.pack(padx=20, pady=20)

uuid_label = customtkinter.CTkLabel(tabview.tab("Serials"), text=f"UUID: {get_system_uuid()}")
uuid_label.pack(padx=20, pady=20)

disk_label = customtkinter.CTkLabel(tabview.tab("Serials"), text=f"Disk: {get_disk_serial()}")
disk_label.pack(padx=20, pady=20)

titles = ["Etherial Free Perm - https://discord.gg/tjen8MSj7F ", "Make sure to try the paid version ", "Orbital (#1 CS2 Cheats) - discord.gg/EaxTA6kQwr ", "Won't work on ASUS, Dell, Alienware, or HP sadly ", "Want YOUR ad here? Make a ticket to discuss pricing "] # last was a joke dont flame me lol
current_title_index = 0

def type_title(title, index=0):
    if index < len(title):
        root.title(title[:index + 1])
        root.after(75, lambda: type_title(title, index + 1))
    else:
        root.after(5000, switch_title)

def switch_title():
    global current_title_index
    current_title_index = random.choice(titles)
    type_title(current_title_index)

type_title(titles[current_title_index])


hPyT.rainbow_border.start(root, interval=4)
pywinstyles.apply_style(root, "transparent")
pywinstyles.apply_style(root, "inverse")
hPyT.maximize_minimize_button.hide(root) 

root.mainloop()
