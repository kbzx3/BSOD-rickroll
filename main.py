import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Full-Screen Image Viewer")
root.attributes('-fullscreen', True)
root.config(cursor="none")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

img = Image.open("BSOD-rick.jpg")
img = img.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
img_tk = ImageTk.PhotoImage(img)

label = tk.Label(root, image=img_tk)
label.pack(fill="both", expand=True)

root.mainloop()
