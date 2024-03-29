from tkinter import *
import sqlite3
from PIL import ImageTk, Image
import settings

global my_selection_question


def new_rank(prize,total_time,mo,my_score):
    toplevel_rank = Toplevel()
    toplevel_rank.geometry("400x400")
    toplevel_rank.title("My rank")
    toplevel_rank.resizable(False, False)

    my_canvas = Canvas(toplevel_rank, width=400, height=400)

    img = Image.open('assets\millioner_logo.jpg').resize((400, 400))

    transparency = 40
    img_transparent = img.copy()
    img_transparent.putalpha(int(255 * (transparency / 100)))

    img = ImageTk.PhotoImage(img_transparent)

    toplevel_rank.resizable(False, False)
    my_canvas.pack(fill="both", expand=True)
    my_canvas.create_image(0, 0, image=img, anchor="nw")

    def close():
        settings.open_window = 0
        toplevel_rank.destroy()

    toplevel_rank.protocol("WM_DELETE_WINDOW", close)

    def submit(name, my_score,prize,total_time,mo):
        conn = sqlite3.connect('millionerdb.db')
        c = conn.cursor()
        c.execute(f"INSERT INTO rank_table (name,score,amount,totaltime,mo) VALUES ('{name}','{my_score}','{prize}','{total_time}','{mo}')")
        conn.commit()
        conn.close()
        close()

    my_canvas.create_text(50, 20, text=f"Game over!!!", anchor='nw', fill='black',
                                        font=("Arial", 40, 'bold'))
    my_canvas.create_text(70, 80, text=f"Your score is {my_score}", anchor='nw', fill='black',
                                        font=("Arial", 30, 'bold'))
    my_canvas.create_text(80, 165, text=f"Name:  ", anchor='nw', fill='black', font=("Arial", 25, 'bold'))

    e = Entry(my_canvas)
    e.insert(0, "")
    btn_submit = Button(my_canvas, text="Submit", command=lambda: submit(e.get(), my_score, prize, total_time, mo), width=25,
                        font=("Arial", 12))
    my_canvas.create_window(190, 180, anchor="nw", window=e)
    my_canvas.create_window(80, 205, anchor="nw", window=btn_submit)

    toplevel_rank.mainloop()
