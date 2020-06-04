import os, sys, time, random
from threading import Thread
import keyboard
class snake:
    def __init__(self, width=40, height=20, speed = 5, fps = 30):
        self.width = width
        self.height = height
        self.snake_len = 3
        self.speed = 1/speed
        self.fps = fps
        self.start_len = self.snake_len

    def start(self):
        self.pos = []
        self.game = []
        self.cur = "d"
        self.isover = False
        self.durum = True
        self.debug = False
        for y in range(self.height+2):
            self.game.append([])
            for x in range (self.width+2):
                if y == 0 or y == self.height+1:
                    self.game[y].append(["#"])
                else:
                    if x == 0 or x == self.width+1:
                        self.game[y].append(["#"])
                    else:
                        self.game[y].append([" "]) 
        self.pos.append([ int(self.width / 4), int(self.height / 2)])
        self.pos.append([ int(self.width / 4)+1, int(self.height / 2)])    
        self.pos.append([ int(self.width / 4)+2, int(self.height / 2)])
        while True:
            temp = [random.randint(2,self.width-1), random.randint(2,self.height-1)]
            if not temp in self.pos:
                self.apple = temp
                break
        Thread(target=self.update).start()
        Thread(target=self.draw).start()
        Thread(target=self.get_key).start()
        Thread(target=self.over).start()
    def over(self):
        while not self.isover:
            for i in range(self.snake_len-1):
                if self.pos[self.snake_len-1] == self.pos[i]:
                    self.isover = True
            time.sleep(self.speed/2)    
                 
    def update(self):
        while not self.isover:
            if not (self.pos[self.snake_len-1][0] >= self.width + 1 or self.pos[self.snake_len-1][0] <= 0 or self.pos[self.snake_len-1][1] >= self.height+1 or self.pos[self.snake_len-1][1] <= 0 )   :
                if self.cur == "d":
                    self.game[self.pos[0][1]][self.pos[0][0]][0] = " "
                    for i in range(self.snake_len-1):
                        self.pos[i] = self.pos[i+1] 
                    self.pos[self.snake_len-1] = [self.pos[self.snake_len-1][0]+1,self.pos[self.snake_len-1][1]]
                    if self.pos[self.snake_len-1] == self.apple:
                        self.pos.append([self.pos[self.snake_len-1][0]+1, self.pos[self.snake_len-1][1]])
                        self.snake_len= self.snake_len+ 1
                        while True:
                            temp = [random.randint(2,self.width-1), random.randint(2,self.height-1)]
                            if not temp in self.pos:
                                self.apple = temp
                                break
                        
                if self.cur == "a":
                    self.game[self.pos[0][1]][self.pos[0][0]][0] = " "
                    for i in range(self.snake_len-1):
                        self.pos[i] = self.pos[i+1] 
                    self.pos[self.snake_len-1] = [self.pos[self.snake_len-1][0]-1,self.pos[self.snake_len-1][1]]
                    if self.pos[self.snake_len-1] == self.apple:
                        self.pos.append([self.pos[self.snake_len-1][0]-1, self.pos[self.snake_len-1][1]])
                        self.snake_len= self.snake_len+ 1
                        while True:
                            temp = [random.randint(2,self.width-1), random.randint(2,self.height-1)]
                            if not temp in self.pos:
                                self.apple = temp
                                break
                if self.cur == "s":
                    self.game[self.pos[0][1]][self.pos[0][0]][0] = " "
                    for i in range(self.snake_len-1):
                        self.pos[i] = self.pos[i+1] 
                    self.pos[self.snake_len-1] = [self.pos[self.snake_len-1][0],self.pos[self.snake_len-1][1]+1] 
                    if self.pos[self.snake_len-1] == self.apple:
                        self.pos.append([self.pos[self.snake_len-1][0], self.pos[self.snake_len-1][1]+1])
                        self.snake_len= self.snake_len+ 1
                        while True:
                            temp = [random.randint(2,self.width-1), random.randint(2,self.height-1)]
                            if not temp in self.pos:
                                self.apple = temp
                                break
                if self.cur == "w" :
                    self.game[self.pos[0][1]][self.pos[0][0]][0] = " "
                    for i in range(self.snake_len-1):
                        self.pos[i] = self.pos[i+1] 
                    self.pos[self.snake_len-1] = [self.pos[self.snake_len-1][0],self.pos[self.snake_len-1][1]-1]
                    if self.pos[self.snake_len-1] == self.apple:
                        self.pos.append([self.pos[self.snake_len-1][0], self.pos[self.snake_len-1][1]-1])
                        self.snake_len= self.snake_len+ 1
                        while True:
                            temp = [random.randint(2,self.width-1), random.randint(2,self.height-1)]
                            if not temp in self.pos:
                                self.apple = temp
                                break
                for i in range(self.snake_len-1):
                    self.game[self.pos[i][1]][self.pos[i][0]][0] = "o"
                self.game[self.pos[self.snake_len-1][1]][self.pos[self.snake_len-1][0]][0] = "O"
                self.game[self.apple[1]][self.apple[0]][0] = "*"
                self.durum = True
               
                
            else:
                self.isover = True
            time.sleep(self.speed)
        os.system("cls")
        print("Game Over")
        print("Point: " + str(self.snake_len- self.start_len))
        os.system("pause")
    def draw(self):
        while not self.isover:
            os.system("cls")
            for y in range(self.height+2):
                temp = ""
                for x in range(self.width+2):
                    temp = temp + self.game[y][x][0]
                print(temp)
            print("Point: " + str(self.snake_len- self.start_len))
            if self.debug:
                print("FPS: " + str(self.fps))
                print("Genişlik: " + str(self.width))
                print("Yükseklik:" + str(self.height))
                print("Uzunluk: " + str(self.snake_len))
                print("Elma Konumu: " + str(self.apple[0]) + "," + str(self.apple[1]))
                print(self.pos)
            time.sleep(1/self.fps)
    def get_key(self):
        while not self.isover:
            if self.durum:
                temp = keyboard.read_key()
                if (temp == "w" or temp == "up") and (self.cur != "s" and self.cur != "w"):
                    self.cur = "w"
                    self.durum = False
                if (temp  ==  "a" or temp == "left") and (self.cur != "d" and self.cur != "a"):
                    self.cur = "a"
                    self.durum = False
                if (temp  == "s" or temp == "down") and (self.cur != "w" and self.cur != "s"):
                    self.cur = "s"
                    self.durum = False
                if (temp  ==  "d" or temp == "right") and (self.cur != "a" and self.cur != "d"):
                    self.cur = "d"   
                    self.durum = False
                if temp == "f3":
                    self.debug = True
                if temp == "f4":
                    self.debug = False
                if temp == "esc":
                    self.isover = True
                
if __name__ == "__main__":
    Settings = []
    try:
        if os.path.isfile("Settings.ini") and os.access("Settings.ini", os.R_OK):
            f = open("Settings.ini")
            Settings = f.readlines()
            f.close()
            for i in range(len(Settings)):
                Settings[i] = str(Settings[i]).rstrip()
        else:
            f = open("Settings.ini" , "w")
            f.writelines("40\n")
            f.writelines("20\n")
            f.writelines("5\n")
            f.writelines("30")
            f.close()
            f = open("Settings.ini")
            Settings = f.readlines()
            f.close()
            for i in range(len(Settings)):
                Settings[i] = str(Settings[i]).rstrip()
        
        s = snake(int(Settings[0]),int(Settings[1]),int(Settings[2]),int(Settings[3]))
        s.start()
    except:
        os.system("cls")
        print("Bir Sorun Oluştu Lütfen Ayarları Kontrol Edin!")
        os.system("pause")
