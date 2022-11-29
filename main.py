import tkinter
from tkinter import ttk    #i use this for more and newer features
from tkinter import messagebox   #to add the error pop up
from tkinter import *


main = tkinter.Tk()

main.title("Btec Certificate")


#frame is a section inside a window and label/list frame is inside the frame

frame = tkinter.Frame(main)
frame.pack()

UX_frame = tkinter.LabelFrame(frame, text="Student Information")
UX_frame.grid(row=0, column=0, padx=20, pady=20)


fn_label = tkinter.Label(UX_frame, text="First Name")
fn_label.grid(row=0, column=0)
ln_label = tkinter.Label(UX_frame, text="Last Name")
ln_label.grid(row=0, column=1)

fn_entry = tkinter.Entry(UX_frame)
ln_entry = tkinter.Entry(UX_frame)
fn_entry.grid(row=1, column=0)
ln_entry.grid(row=1, column=1)

level = tkinter.Label(UX_frame, text="Btec Level")
level_drop = ttk.Combobox(UX_frame, values=["3", "4", "5"])
level.grid(row=0, column=2)
level_drop.grid(row=1, column=2)

# to even out space between the entries in the first layer

for widget in UX_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


units_frame = tkinter.LabelFrame(frame, text="Enter your mark for each unit")
units_frame.grid(row=1, column=0, sticky="news", padx=15, pady=15)


u1_label = tkinter.Label(units_frame, text="Information Technology Systems")
u1_label.grid(row=0, column=0)
u1_drop = ttk.Combobox(units_frame, values=["Distinction", "Merit", "Pass", "Fail"])
u1_drop.grid(row=0, column=1, padx=8, pady=8)


u3_label = tkinter.Label(units_frame, text="Social Media in Business")
u3_label.grid(row=1, column=0)
u3_drop = ttk.Combobox(units_frame, values=["Distinction", "Merit", "Pass", "Fail"])
u3_drop.grid(row=1, column=1, padx=8, pady=8)


u4_label = tkinter.Label(units_frame, text="Programming")
u4_label.grid(row=2, column=0)
u4_drop = ttk.Combobox(units_frame, values=["Distinction", "Merit", "Pass", "Fail"])
u4_drop.grid(row=2, column=1, padx=8, pady=8)


u6_label = tkinter.Label(units_frame, text="Website Development")
u6_label.grid(row=3, column=0)
u6_drop = ttk.Combobox(units_frame, values=["Distinction", "Merit", "Pass", "Fail"])
u6_drop.grid(row=3, column=1, padx=8, pady=8)


button = tkinter.Button(frame, text="submit", bg="white", command=lambda: display())
button.grid(row=3, column=0, sticky="news", padx=30, pady=30)


def display():

    certificate_window = Toplevel(main)
    certificate_window.geometry("500x500")
    certificate_window.title("Your Btec Certificate")








    Accepted = accept_var.get()

    if Accepted == "Accepted":

        print("Name:", fn_entry.get(), ln_entry.get())

        if fn_entry.get() and ln_entry.get() and level_drop.get() and u1_drop.get() and u3_drop.get() and u4_drop.get() and u6_drop.get():

            print("level:", level_drop.get())
            print("Your Score in Information Technology System:", u1_drop.get())
            print("Your Score in Social Media In Business:", u3_drop.get())
            print("Your Score in Programming:", u4_drop.get())
            print("Your Score in Website Development:", u6_drop.get())

            if u1_drop.get() == "Fail" or u3_drop.get() == "Fail" or u4_drop.get() == "Fail" or u6_drop.get() == "Fail":
                print(ln_entry.get() + " result is Fail")

            elif u1_drop.get() == "Pass" or u3_drop.get() == "Pass" or u4_drop.get() == "Pass" or u6_drop.get() == "Pass":
                print(ln_entry.get() + " result is Pass")

            elif u1_drop.get() == "Merit" or u3_drop.get() == "Merit" or u4_drop.get() == "Merit" or u6_drop.get() == "Merit":
                print(ln_entry.get() + " result is Merit")

            elif u1_drop.get() == "Distinction" and u3_drop.get() == "Distinction" and u4_drop.get() == "Distinction" and u6_drop.get() == "Distinction":
                print(ln_entry.get() + " result is Distinction")
        else:
            tkinter.messagebox.showwarning(title="Error", message="Please fill all the required fields")

    else:
        tkinter.messagebox.showwarning(title="Error", message="Please Accept the terms and conditions to move forward")




for widget in units_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


terms_frame = tkinter.LabelFrame(frame, text="Terms and Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=15, pady=15)

accept_var = tkinter.StringVar(value="Not Accepted")

terms_bx = tkinter.Checkbutton(terms_frame, text="I agree with the terms and conditions.",
                               variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_bx.grid(row=0, column=0)





""" This comment has the radio button version of the mark selection


rbad = tkinter.Radiobutton(units_frame, text="Distinction", variable=u1_label, value="d")
rbam = tkinter.Radiobutton(units_frame, text="Merit", variable=u1_label, value="m")
rbap = tkinter.Radiobutton(units_frame, text="Pass", variable=u1_label, value="p")
rbaf = tkinter.Radiobutton(units_frame, text="Fail", variable=u1_label, value="f")

rbad.grid(row=1, column=0)
rbam.grid(row=2, column=0)
rbap.grid(row=3, column=0)
rbaf.grid(row=4, column=0)


u3_label = tkinter.Label(units_frame, text="Social Media In Business")
u3_label.grid(row=0, column=1)

rbbd = tkinter.Radiobutton(units_frame, text="Distinction", variable=u3_label, value="d")
rbbm = tkinter.Radiobutton(units_frame, text="Merit", variable=u3_label, value="m")
rbbp = tkinter.Radiobutton(units_frame, text="Pass", variable=u3_label, value="p")
rbbf = tkinter.Radiobutton(units_frame, text="Fail", variable=u3_label, value="f")

rbbd.grid(row=1, column=1)
rbbm.grid(row=2, column=1)
rbbp.grid(row=3, column=1)
rbbf.grid(row=4, column=1)"""










main.mainloop()

