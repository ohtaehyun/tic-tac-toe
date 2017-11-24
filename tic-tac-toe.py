from tkinter import *
def finish(player):
      return((list[0]['text']==list[1]['text']==list[2]['text']==player)or
             (list[3]['text']==list[4]['text']==list[5]['text']==player)or
             (list[6]['text']==list[7]['text']==list[8]['text']==player)or
             (list[0]['text']==list[3]['text']==list[6]['text']==player)or
             (list[1]['text']==list[4]['text']==list[7]['text']==player)or
             (list[2]['text']==list[5]['text']==list[8]['text']==player)or
             (list[0]['text']==list[4]['text']==list[8]['text']==player)or
             (list[2]['text']==list[4]['text']==list[6]['text']==player))

def checked(i) :
      global player
      button = list[i]

      if button["text"] != "     " :
            return
      button["text"] = player 
      button["bg"] = "yellow"

      if player == "X" :
            player = "O"
            button["bg"] = "yellow"
            if finish("X")==True:
                  print("X win")
                  window.destroy()
      else :
            player = "X"
            button["bg"] = "lightgreen"
            if finish("O")==True:
                  print("O win")
                  window.destroy()

window = Tk()
player = "X"
list= []

for i in range(9) :
      b = Button(window, text="     ", command=lambda k=i: checked(k))
      b.grid(row=i//3, column=i%3)
      list.append(b)

window.mainloop()


