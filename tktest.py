import os, sys, time
import tkinter as tk

root = tk.Tk()

def pushed(b):
    b["text"] = "開始します"

#ウィンドウタイトル
root.title("Tkinter Window")

#ウィンドウサイズ
root.geometry("1280x720")


#ラベルを追加
label = tk.Label(root, text="Hello,World")

#表示
label.grid()

button =tk.Button(root, text="訓練開始", command= lambda : pushed(button))
button.grid()

    


#ウィンドウの表示
root.mainloop()