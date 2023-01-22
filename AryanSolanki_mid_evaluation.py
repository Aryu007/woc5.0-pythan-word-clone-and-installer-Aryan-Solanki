from tkinter import *
from tkinter import font

root = Tk()
root.title("Aryan Solanki")

def font_size_chooser(e):
	our_font.config(
		size=font_size_listbox.get(font_size_listbox.curselection()))
def font_style_chooser(e):
		style=font_style_listbox.get(font_style_listbox.curselection())
		if style == "bold":
			our_font.config(weight=style)
		if style == "regular":
			our_font.config(weight="normal",slant="roman",underline=0)
		if style == "italic":
			our_font.config(slant=style)
		if style == "underline":
			our_font.config(underline=1)
			
def font_chooser(e):
	our_font.config(
		family=my_listbox.get(my_listbox.curselection()))

our_font = font.Font(family="Helvetica",size="32")

my_frame = Frame(root,width=510,height=275)
my_frame.pack(pady=10)
my_frame.grid_propagate(False)
my_frame.columnconfigure(0,weight=10)

#Add text box
my_text=Text(my_frame,font=our_font)
my_text.grid(row=0,column=0)
my_text.grid_rowconfigure(0,weight=1)
my_text.grid_columnconfigure(0,weight=1)

bottom_frame = Frame(root)
bottom_frame.pack()

font_label = Label(bottom_frame,text="Choose Font",font=("Helvetica",14))
font_label.grid(row=0,column=0,padx=10)

size_label = Label(bottom_frame,text="Font size",font=("Helvetica",14))
size_label.grid(row=0,column=1)

style_label = Label(bottom_frame,text="Font style",font=("Helvetica",14))
style_label.grid(row=0,column=2,padx=10)
#add listbox
my_listbox = Listbox(bottom_frame,selectmode=SINGLE,width=80)
my_listbox.grid(row=1,column=0)
#size listbox
font_size_listbox=Listbox(bottom_frame,selectmode=SINGLE,width=80)
font_size_listbox.grid(row=1,column=1)
#style listbox
font_style_listbox=Listbox(bottom_frame,selectmode=SINGLE,width=80)
font_style_listbox.grid(row=1,column=2)

#Add font families to Listbox
for f in font.families():
	my_listbox.insert('end',f)

#Add sizes to size listbox	
font_sizes= [8,10,12,14,16,18,20,22,24]
for size in font_sizes:
	font_size_listbox.insert('end',size)

#Add styles to style listbox	
font_styles = ["regular","bold","italic","underline"]
for style in font_styles:
	font_style_listbox.insert('end',style)

#Blind the listbox
my_listbox.bind('<ButtonRelease-1>',font_chooser)
font_size_listbox.bind('<ButtonRelease-1>',font_size_chooser)
font_style_listbox.bind('<ButtonRelease-1>',font_style_chooser)





root.mainloop()