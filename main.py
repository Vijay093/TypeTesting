from tkinter import *
from data import easy_words
import random
# import time

started = False
cpm = 0
wpm = 0
secs = None

window = Tk()
window.title("Typing Speed Test")
window.config(padx=50, pady=50, background="#B1DDC6")

my_canvas = Canvas(height=526, width=800, bg="white")
first = my_canvas.create_text(400, 150, text="lets", font=("Arial", 60, 'bold'))
second = my_canvas.create_text(400, 253, text="type", font=("Arial", 40, 'bold'))
third = my_canvas.create_text(400, 353, text="test", font=("Arial", 20, 'bold'))
fourth = my_canvas.create_text(400, 453, text="ourselves", font=("Arial", 10, 'bold'))
timer = my_canvas.create_rectangle(700, 10, 780, 90, outline='black', fill='skyblue', width=2)
time_in_sec = my_canvas.create_text(740, 50, text='60', font=("Arial", 40, 'bold'))

text_entry = Entry(width=50, highlightthickness=10)
scorecard = Label(text=f"CPM:0\nWPM:0", width=50)
my_canvas.grid(row=0, column=0, columnspan=2, pady=20)
text_entry.grid(row=1, column=0, columnspan=2,  padx=100, pady=20)
scorecard.grid(row=2, column=0, columnspan=2, padx=100, pady=10)
text_entry.focus_set()


def draw(event=None):
    global started
    global cpm
    global wpm
    count = 0
    if started:
        word_to_type = my_canvas.itemcget(first, 'text')
        typed_word = text_entry.get()
        for i in range(len(word_to_type)):
            if typed_word[i] == word_to_type[i]:
                cpm += 1
                count += 1
            else:
                break

        my_canvas.itemconfig(first, text=my_canvas.itemcget(second, 'text'))
        my_canvas.itemconfig(second, text=my_canvas.itemcget(third, 'text'))
        my_canvas.itemconfig(third, text=my_canvas.itemcget(fourth, 'text'))
        my_canvas.itemconfig(fourth, text=random.choice(easy_words))
    else:
        started = True
        word_to_type = my_canvas.itemcget(first, 'text')
        typed_word = text_entry.get()
        for i in range(len(typed_word)):
            if typed_word[i] == word_to_type[i]:
                cpm += 1
                count += 1
            else:
                break

    if count == len(word_to_type):
        wpm += 1

    text_entry.delete(0, END)


def countdown(num):
    global timer
    global cpm
    global wpm
    global scorecard
    if scorecard:
        scorecard.destroy()

    my_canvas.itemconfig(time_in_sec, text=str(num))

    if num > 0:
        timer = window.after(1000, countdown, num-1)

    if num == 0:
        window.after_cancel(timer)
        my_canvas.itemconfig(time_in_sec, text='0')

        window.unbind('<space>')

        if wpm < 35:
            status = "Below Average"
        elif wpm < 45:
            status = "Average"
        elif wpm < 55:
            status = "Above Average"
        else:
            status = "Great Speed"
        scorecard = Label(text=f"CPM: {cpm}\nWPM:{wpm}\n{status}", width=50)
        scorecard.grid(row=2, column=0, columnspan=2, padx=100, pady=10)


def reset_timer():
    global timer
    global cpm
    global wpm
    window.after_cancel(timer)
    my_canvas.itemconfig(time_in_sec, text='60')
    window.unbind('<space>')
    cpm = 0
    wpm = 0
    my_canvas.itemconfig(first, text='lets')
    my_canvas.itemconfig(second, text='type')
    my_canvas.itemconfig(third, text='test')
    my_canvas.itemconfig(fourth, text='ourselves')


def start_timer():
    global started
    started = False
    draw()
    window.bind('<space>', draw)
    countdown(60)


start_button = Button(text="Start", highlightthickness=10, command=start_timer, background='pink')
reset_button = Button(text="Reset", highlightthickness=10, command=reset_timer, background='beige')
start_button.grid(row=4, column=0, pady=10)
reset_button.grid(row=4, column=1, pady=10)

# draw()
# window.bind('<space>', draw)

window.mainloop()

