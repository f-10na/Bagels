import tkinter as tk
from tkinter import PhotoImage
from PIL import Image,ImageTk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Bagels")

fermi_count = 0
pico_count = 0
tries_left = 10

#GUI components
original_image = Image.open("bagel.png")
resized_image = original_image.resize((60,50))
bagel_image = ImageTk.PhotoImage(resized_image)

bagel_label = tk.Label(root, text="BaGelS!", compound="left",image=bagel_image,bg="white", fg="pink", font=("Times New Roman", 40, "bold"))
entry_label = tk.Label(root, text="Guess the 3 digit number: ",fg="pink", bg="white", font=("Times New Roman",))
fermi_label = tk.Label(root, text=f"Fermi: {fermi_count}", fg="pink",bg="white", font=("Times New Roman",))
pico_label = tk.Label(root, text=f"Pico: {pico_count}", fg="pink",bg="white", font=("Times New Roman",))
tries_label = tk.Label(root, text=f"Tries left: {tries_left}",fg="pink", bg="white", font=("Times New Roman",))
entry = tk.Entry(root, width=40, bg="white", fg="pink", font=("Times New Roman",), highlightbackground="white")

def generate_random_number():
    return random.randint(100, 999)
    
def update_labels():
    fermi_label.config(text=f"Fermi: {fermi_count}")
    pico_label.config(text=f"Pico: {pico_count}")
    tries_label.config(text=f"Tries left: {tries_left}")

def show_result_message(result):
    messagebox.showinfo("Game Result", result)
    #root.after(100, reload_page)
    
answer = generate_random_number()
print(answer)

def check_number():
    global tries_left, fermi_count, pico_count,answer
    entered = entry.get()
    print(type(entered))
    answer_list = list(str(answer))
    #print(answer_list)
    entry_list = list(entered)
    if (len(entry_list)==3):
        common_elements = set(answer_list) & set(entry_list)
        
        fermi_count = sum(a == b for a,b in zip(answer_list,entry_list))
        
        pico_count = len(common_elements)- fermi_count
        
        update_labels()  # update labels after each iteration
        tries_left -= 1
        print(f"Fermi: {fermi_count}")
        print(f"Pico: {pico_count}")
        print(f"Tries left: {tries_left}")

        if fermi_count == 3:
            show_result_message("Congratulations! You guessed the correct number.")
        elif tries_left == 0:
            show_result_message(f"Out of tries. The correct number was: {answer}")
    else:
        show_result_message("Incorrect input either empty or not 3 digits")
        
        

enter_button = tk.Button(root, text="ENTER", width=8, height=3,fg="pink",
                         bg="white",font=("Times New Roman", 20), highlightbackground="pink",command=check_number)

bagel_label.pack(pady=20)
entry_label.pack()
entry.pack()
enter_button.pack()
pico_label.pack()
fermi_label.pack()
tries_label.pack()

root.minsize(400, 300)
root.maxsize(500, 400)
root.configure(bg="white")
root.mainloop()
