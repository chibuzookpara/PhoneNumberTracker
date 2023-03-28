import tkinter as tk
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
num = None


def get_location():
    global num
    num = entry.get()
    try:
        parsed_num = phonenumbers.parse(num)
        
        location = phonenumbers.geocoder.description_for_number(parsed_num, "en")
        result_label.config(text=f"Location: {location}")
        print(f"Location: {location}")  # print location to console
        root.destroy()  # close the window
    except phonenumbers.phonenumberutil.NumberParseException:
        result_label.config(text="Invalid phone number")
    
root = tk.Tk()

label = tk.Label(root, text="Enter a phone number:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Get Location", command=get_location)
button.pack()

result_label = tk.Label(root)
result_label.pack()

root.mainloop()

print(f"The phone number is: {num}")  # save the number after the window is closed
