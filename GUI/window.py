import tkinter
import random
import sys



class GameBoard(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)

        self.food_exists = False
        self.snake_dir = "up"
        self.snake_parts = [None,None,None]
        

        self.init_bkg()
        
        self.init_canvas()
        self._canvas.pack()        

        if not self.food_exists:
           self.generate_food()
           pass
        
        self.create_snake()

        self.init_directions()

        self.move_snake()        


    def init_bkg(self):
        self.title("python snake")
        self.geometry("600x400")
        self.configure(background="black")
        self.resizable(width=False, height=False)


    def init_canvas(self):
        self._canvas = tkinter.Canvas(self, height= 400, width = 600, bg ="black", highlightthickness=0)


    def generate_food(self):
        self.food_x = 25*random.randint(0,23)
        self.food_y = 25*random.randint(0,15)

        '''
        while check_food_collision(self.food_x):
            self._canvas.food_x = 600 * random.random()

        while check_food_collision(self.food_y):
            self._canvas.food_y = 400 * random.random()
        '''
        self._canvas.create_rectangle(self.food_x, 
            self.food_y, (self.food_x+25), 
            (self.food_y+25), fill="light green")


        self.food_exists = True

        
    def init_directions(self):
        self.bind("w",self.turn_up)
        self.bind("s",self.turn_down)
        self.bind("d",self.turn_right)  
        self.bind("a",self.turn_left)
        self.bind("<Escape>", self.exit_game)
        
    def turn_up(self,event):
        if (self.snake_dir=="left" or self.snake_dir=="right"):
            self.snake_dir = "up"
            self.headY += 25
            print("pressed", repr(event.char))

        else: pass

    def turn_down(self,event):
        if (self.snake_dir=="left" or self.snake_dir=="right"):
            self.snake_dir = "down"
            self.headY -= 25
            print("pressed", repr(event.char))

        else: pass

    def turn_right(self,event):
        if (self.snake_dir=="up" or self.snake_dir=="down"):
            self.snake_dir = "right"
            self.headX += 25
            print("pressed", repr(event.char))

        else: pass
        
    def turn_left(self,event):
        if (self.snake_dir=="up" or self.snake_dir=="down"):
            self.snake_dir = "left"
            self.headX -= 25
            print("pressed", repr(event.char))

        else: pass
    
    def create_snake(self):

        self.headX = 15 * 25 
        self.headY = 8 * 25

        self.snake_coords = [[15*25,9*25],[15*25,10*25]]


        self.head = self._canvas.create_rectangle(self.headX, 
            self.headY, (self.headX+25), 
            (self.headY+25), fill="green")


        for i in range(len(self.snake_coords)):
            self.snake_parts[i] = self._canvas.create_rectangle(
                self.snake_coords[i][0], 
                self.snake_coords[i][1],
                self.snake_coords[i][0]+25,
                self.snake_coords[i][1]+25,
                fill= "green")

    def move_snake(self):
        for i in range(len(self.snake_parts)):
            if i == 0:
                self._canvas.move(self.snake_parts[i],
                    self.headX, self.headY)
            else:
                self._canvas.move(self.snake_parts[i],
                    self.snake_coords[i-1][0],
                    self.snake_coords[i-1][1])

        self._canvas.move(self.head, self.headX, self.headY)

    def grow_snake(self):
        pass

    def exit_game(self,event):
        self.destroy()
        sys.exit()

    def run_game(self):
        self.mainloop()
        
