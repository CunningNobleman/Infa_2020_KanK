import pygame
from math import pi

pygame.init()

# Цвета
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
DARKGRAY =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
GRAY = (169, 169, 169)
DIMGRAY = (105,105,105)
SILVER = (192,192,192)
BROWN = (139,69,19)
ROSYBROWN = (255,228,196)
DARKGRAY = (169,169,169)
ROSYBROWN = (188,143,143)


screen = pygame.display.set_mode((1000, 700))


screen.fill(WHITE) # Зима, снег.
pygame.draw.rect(screen, SILVER, [0, 0, 1000, 300]) # Небо.



# Функция рисующая человека, xhum - x координата эллипса (его тела) в pygame. параметр s- его размер. 

def draw_human(xhum, yhum, s) :
    pygame.draw.arc(screen, BROWN,[xhum, yhum, 150 * s, 300 * s], 0, pi, 2) # дуга половины эллипса, 
    pygame.draw.rect(screen, BROWN, (xhum, (300 * s)/2 + yhum, 150 * s, 10 * s)) # прямоугольное основание к которому прикрепляются ножки
    pygame.draw.line(screen, ROSYBROWN, [xhum + 20 * s, yhum + (300 * s)/2 + 10], 
                    [xhum + 20, yhum + (300 * s)/2 + 10 + 40], 10)  # нога 1
    pygame.draw.line(screen, ROSYBROWN, [xhum + 130, yhum + 300/2 + 10], 
                    [xhum + 130, yhum + 300/2 + 10 + 40], 10)       # нога 2
    pygame.draw.circle(screen, ROSYBROWN, [xhum + int((150 * s)/2), yhum], (40 + 12) * s, 0)    # его лицо. 
    
    


draw_human(410, 275, 1) 


 # функция рисующая ДИКОГО ВОЛКА, параметры - его координаты.
def draw_WILD_WOLF (Xw, Yw) :
    pygame.draw.line(screen, DARKGRAY, [Xw + 20, Yw + 20 ], [Xw + 20, Yw + 50 + 20], 8)    # лапа 1, расстояние от левого туловища 20 
    pygame.draw.line(screen, DARKGRAY, [Xw + 80, Yw + 20], [Xw + 80, Yw + 50 + 20], 8)      # лапа 2
    pygame.draw.ellipse(screen, DARKGRAY, [Xw, Yw, 100, 50])    # туловище, размер 100 на 50
    pygame.draw.circle(screen, DARKGRAY, [Xw + (100) + 20 , Yw + int((50)/2)], 20, 0)    # морда
    
draw_WILD_WOLF (250,250)


 # рисует юрту. Параметры - координаты юрты. y - yurt
def draw_yurt (Xy, Yy, Sy) :
    pygame.draw.arc(screen, GRAY, [Xy, Yy, Sy, Sy], 0, pi, 4)   # Полуокружность. Xy,Yy координаты левой верхней точки квадрата огибающего эту окружность. Стороны Квадрата равны Sy
    pygame.draw.line(screen, GRAY, [Xy, Yy + Sy/2], [Xy + Sy, Yy + Sy/2], 4)  # Основание юрты
    pygame.draw.rect(screen, GRAY, [Xy + Sy/2, Yy + Sy/2 - 0.16 * Sy, Sy * 0.1, Sy * 0.16], 4)   # Дверь туда. Размер двери: 0.16 * Sy - высота, 0.1 * Sy ее ширина
draw_yurt (300, 500, 200)


pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()