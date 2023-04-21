from tkinter import *
from tkinterdnd2 import *
from PIL import Image, ImageTk

width = -1
height = -1

def drop(event):
    global display_image, canvas
    canvas.delete("image")
    img = Image.open(event.data)
    print(f"img.width: {img.width}, img.height: {img.height}")
    ratio = min(width / img.width, height / img.height)
    print(f"ratio: {ratio}")
    new_size = (int(img.width * ratio), int(img.height * ratio))
    print(f"new_size: {new_size[0]}, {new_size[1]}")
    img = img.resize(new_size)
    display_image = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, image = display_image, anchor = "nw")
    return event.action

# メインウィンドウの生成
display_image = None
root = TkinterDnD.Tk()
root.geometry("650x500")
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
width, height = 650, 500
print(f"width: {width}, height: {height}")
root.title('Canvasにドラッグアンドドロップ機能追加')
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)
# Canvasウィジェットの生成
canvas = Canvas(root, width=640, height=480)
# ウィジェットの配置
canvas.pack()

root.mainloop()