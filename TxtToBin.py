import os
import sys
import tkinter as tk
from tkinter import filedialog
from progress.bar import ChargingBar

root = tk.Tk()
root.withdraw()

#get filename to be converted in other format
file_name = filedialog.askopenfilename(title='Select a file')

print(file_name)

#Check if a file was selected
if (file_name != ""):

    file_stats = os.stat(file_name)
    file_save = filedialog.asksaveasfilename(title="Choose filename")

    with open(file_name, "r") as f:
        with open(file_save, "wb") as w:
            #Step of 2%
            progress_step = int(len(f.read())/(2*50))
            bar = ChargingBar('Bytes Readining', max=50, suffix='%(percent)d%%')
            count_bytes_read = 0
            #reset reading
            f.seek(0)
            while (hexa := f.read(2)):
                #Para salvar em binário
                #w.write(bin(int.from_bytes(byte, byteorder=sys.byteorder)))
                #Para salvar em hex
                w.write(bytes.fromhex(hexa))
                
                #Progress Bar
                count_bytes_read= count_bytes_read + 1
                if (count_bytes_read % progress_step == 0):
                    bar.next()
            bar.next()
        bar.finish()
else:
    print("None file selected!")

print ("Process complete")