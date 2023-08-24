from tkinter import Tk, Canvas, CENTER


def fill_heart(x, y, shape):
    for i in range(len(shape)):
        for j in range(len(shape[i])):

            if shape[i][j] == 1:
                canvas.create_text(x + 7 * j, y + 7 * i, text="*",
                                   fill="#FF2400")
            else:
                canvas.create_text(x + 7 * j, y + 7 * i, text="",
                                   fill="#004D40")


def change_heart(x, y, shape):
    if shape[x][y] == 0:
        shape[x][y] = 1
        change_heart(x + 1, y, shape)
        change_heart(x - 1, y, shape)
        change_heart(x, y + 1, shape)
        change_heart(x, y - 1, shape)
    return shape


heart = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

root = Tk()
root.title("Love")
root.geometry("170x300+500+200")

canvas = Canvas(bg="white", width=130, height=220)
canvas.pack(anchor=CENTER, expand=1)

fill_heart(20, 20, heart)
x = len(heart[0]) // 2
y = len(heart) // 2
fill_heart(20, 120, change_heart(x, y, heart))

root.mainloop()
