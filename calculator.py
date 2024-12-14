# ---------------------setting up the environment------------------------------------
# import module
import tkinter as tk

# create app window
app = tk.Tk()
app.geometry("312x324")
app.resizable(0, 0)
app.title("Calculator")

# ------------ defining functions-----------------------------------------
input_value = ""
display_text = tk.StringVar()  # initializing string var

# function to contiuously update input display


def click_btn_action(item):
    global input_value
    input_value = input_value+str(item)
    display_text.set(input_value)

# function to clear the display


def clear_btn_action():
    global input_value
    input_value = ""
    display_text.set("")

# function to calculate input values


def equal_btn_action():
    global input_value
    result = str(eval(input_value))
    display_text.set(result)
    input_value = ""

# function to close app


def close_btn_action():
    app.destroy()


# -------------creating frames and widgets-----------------------------------
# creating frame for display
input_frame = tk.Frame(app, width=325, height=50, bd=0,
                       highlightbackground='black', highlightcolor='black', highlightthickness=2)
input_frame.pack(side=tk.TOP)

# creating entry widget inside diaplay frame
input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'),
                       textvariable=display_text, width=50, bg='#eee', justify=tk.RIGHT)
input_field.grid(row=0, column=0)
# ipady is for internal paddying to change the height of input field
input_field.pack(ipady=10)

# creating btns frame
btns_frame = tk.Frame(app, width=325, height=275, bg='grey')
btns_frame.pack()

# creating btns
# 1st row
clear_btn = tk.Button(btns_frame, text="C", fg='black', width=32, height=3, bd=0, bg='#eee', cursor='hand2',
                      command=lambda: clear_btn_action()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide_btn = tk.Button(btns_frame, text='/', fg='black', width=10, height=3, bd=0, bg='#eee',
                       cursor='hand2', command=lambda: click_btn_action("/")).grid(row=0, column=3, pady=1, padx=1)
# 2nd row
btn_7 = tk.Button(btns_frame, text='7', fg='black', width=10, height=3, bd=0, bg='#fff',
                  cursor='hand2', command=lambda: click_btn_action("7")).grid(row=1, column=0, pady=1, padx=1)
btn_8 = tk.Button(btns_frame, text='8', fg='black', width=10, height=3, bd=0, bg='#fff',
                  cursor='hand2', command=lambda: click_btn_action("8")).grid(row=1, column=1, pady=1, padx=1)
btn_9 = tk.Button(btns_frame, text='9', fg='black', width=10, height=3, bd=0, bg='#fff',
                  cursor='hand2', command=lambda: click_btn_action("9")).grid(row=1, column=2, pady=1, padx=1)
multiply_btn = tk.Button(btns_frame, text="*", fg='black', width=10, height=3, bd=0, bg='#fff',
                         cursor='hand2', command=lambda: click_btn_action("*")).grid(row=1, column=3, pady=1, padx=1)
# 3rd row
btn_4 = tk.Button(btns_frame, text='4', fg='black', width=10, height=3, bd=0, bg='#fff',
                  cursor='hand2', command=lambda: click_btn_action("4")).grid(row=2, column=0, pady=1, padx=1)
btn_5 = tk.Button(btns_frame, text='5', fg='black', width=10, height=3, bd=0, bg='#fff',
                  cursor='hand2', command=lambda: click_btn_action("5")).grid(row=2, column=1, pady=1, padx=1)
btn_6 = tk.Button(btns_frame, text='6', fg='black', width=10, height=3, bd=0, bg='#fff',
                  cursor='hand2', command=lambda: click_btn_action("6")).grid(row=2, column=2, pady=1, padx=1)
minus_btn = tk.Button(btns_frame, text="-", fg='black', width=10, height=3, bd=0, bg='#fff',
                      cursor='hand2', command=lambda: click_btn_action("-")).grid(row=2, column=3, pady=1, padx=1)
# 4th row
btn_1 = tk.Button(btns_frame, text='1', fg='black', width=10, height=3, bd=0, bg='#fff',
                  cursor='hand2', command=lambda: click_btn_action("1")).grid(row=3, column=0, pady=1, padx=1)
btn_2 = tk.Button(btns_frame, text='2', fg='black', width=10, height=3, bd=0, bg='#fff',
                  cursor='hand2', command=lambda: click_btn_action("2")).grid(row=3, column=1, pady=1, padx=1)
btn_3 = tk.Button(btns_frame, text='3', fg='black', width=10, height=3, bd=0, bg='#fff',
                  cursor='hand2', command=lambda: click_btn_action("3")).grid(row=3, column=2, pady=1, padx=1)
plus_btn = tk.Button(btns_frame, text="+", fg='black', width=10, height=3, bd=0, bg='#fff',
                     cursor='hand2', command=lambda: click_btn_action("+")).grid(row=3, column=3, pady=1, padx=1)
# 5th row
btn_0 = tk.Button(btns_frame, text='0', fg='black', width=10, height=3, bd=0, bg='#fff',
                  cursor='hand2', command=lambda: click_btn_action("0")).grid(row=4, column=0, pady=1, padx=1)
point_btn = tk.Button(btns_frame, text='.', fg='black', width=10, height=3, bd=0, bg='#fff',
                      cursor='hand2', command=lambda: click_btn_action(".")).grid(row=4, column=1, pady=1, padx=1)
equals_btn = tk.Button(btns_frame, text='=', fg='black', width=10, height=3, bd=0, bg='#fff',
                       cursor='hand2', command=lambda: equal_btn_action()).grid(row=4, column=2, pady=1, padx=1)
power_btn = tk.Button(btns_frame, text="CLOSE", fg='black', width=10, height=3, bd=0, bg='#fff',
                      cursor='hand2', command=lambda: close_btn_action()).grid(row=4, column=3, pady=1, padx=1)

# ---------------------------------------------------------run mainloop--------------------------------------------------------
app.mainloop()
