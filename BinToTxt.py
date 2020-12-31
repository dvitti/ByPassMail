import os
import sys
from progress.bar import ChargingBar
import tkinter as tk
from tkinter import filedialog

#Initialize TKlib
root = tk.Tk()
root.withdraw()

#get filename to be converted in text
file_name = filedialog.askopenfilename(title='Select a file')

#Check if a file was selected
if (file_name != ""):

    file_stats = os.stat(file_name)
    file_save = filedialog.asksaveasfilename(title="Choose filename")

    with open(file_name, "rb") as f:
        with open(file_save, "w") as w:
            #Step of 2%
            progress_step = int(file_stats.st_size/50)
            bar = ChargingBar('Bytes Readining', max=50, suffix='%(percent)d%%')
            count_bytes_read = 0
            while (byte := f.read(1)):
                #Save as Binary
                #w.write(bin(int.from_bytes(byte, byteorder=sys.byteorder)))
                #Save as HEX
                w.write(byte.hex())

                #Progress Bar
                count_bytes_read= count_bytes_read + 1
                if (count_bytes_read % progress_step == 0):
                    bar.next()
            bar.next()   
    bar.finish()
else:
    print("None file selected!")

print ("Process complete")