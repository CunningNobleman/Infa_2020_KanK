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
DEEPTAUPE = (101, 83, 79)
TUSCANY = (192,153,153)
SADDLEBROWN = (139,69,19)


screen = pygame.display.set_mode((1000, 700))


screen.fill(WHITE) # Зима, снег.
pygame.draw.rect(screen, SILVER, [0, 0, 1000, 300]) # Небо.

# Используется для рисования носов.
def draw_pyramid (x, y, h, w) :
    '''
    x: x coordinate of the bottom-left base edge
    y: y coordinate of the bottom-left base edge
    h: height of the pyramid
    w: base width
    '''
    dy = 0.001
    dx = w / (2 * (h/dy - 1))
    N = int(h/dy)
    for i in range (1, N):
        pygame.draw.rect(screen, BLACK,[x + dx * (i - 1), 
                         y + h - dy * i, w - 2 * (i-1)*dx, dy])

def draw_face (xface, yface, headsize):
    '''
    xface - x coordinate of centre of the face which is represented by circle.
    yface - x coordinate of centre of the face which is represented by circle.
    headsize - radius of the face circumference.
    '''
    pygame.draw.line(screen, BLACK, [xface + 0.65 * (headsize) , 
                                             yface - 0.65 * (headsize)], 
                                             [xface + 0.35 * (headsize) , 
                                             yface  - 0.35 * (headsize)], 2)
        
    pygame.draw.line(screen, BLACK, [xface - 0.65 * (headsize) , 
                                             yface - 0.65 * (headsize)], 
                                             [xface - 0.35 * (headsize) , 
                                             yface  - 0.35 * (headsize)], 2)
    draw_pyramid(xface - 2, yface + 2, 4, 4)
    pygame.draw.line(screen, BLACK, [xface - 0.2 * (headsize), 
                                    yface + 0.6 * (headsize)],
                                    [xface + 0.2 * (headsize), 
                                    yface + 0.6 * (headsize)]
                                    )
 

def draw_human(xhum, yhum, Hh) :
    '''
    xhum: x coordinate of the body rectangle.
    yhum: y coordinate of the body rectangle.
    Hh: human's height (from bottom of the legs to upper point of the head)
    
    '''
    Hw = 0.4 * Hh
    body_height = Hh * 0.6
    leg_length = Hh * 0.25
    
    head_radius = Hh - body_height - leg_length
    
    head_coordinates = [xhum + int(Hw / 2), yhum]
    
    human_head_size = head_radius * 0.6
    
    pygame.draw.ellipse(screen, DEEPTAUPE, [xhum, yhum, Hw, 2 * body_height])# Тело
    pygame.draw.rect(screen, WHITE, [xhum, yhum + body_height, Hw, body_height])# Магический квадрат
    pygame.draw.line(screen, ROSYBROWN, [xhum + 0.3 * Hw, yhum + body_height], 
                                        [xhum + 0.3 * Hw, yhum + leg_length + body_height], 10 )# Левая нога
    pygame.draw.line(screen, ROSYBROWN, [xhum + 0.7 * Hw, yhum + body_height], 
                                        [xhum + 0.7 * Hw, yhum + leg_length + body_height], 10 )  # Правая нога
    pygame.draw.circle(screen, DIMGRAY, [xhum + int(Hw / 2), yhum], int(head_radius), 0) # Капюшон пальто
    pygame.draw.circle(screen, ROSYBROWN, [xhum + int(Hw / 2), yhum], int(human_head_size), 0) # голова
    
    draw_face(xhum, yhum, human_head_size)
 
 
 
 
 # функция рисующая дикого волка, параметры - его координаты.
def draw_WILD_WOLF (Xw, Yw) :
    '''
    Xw: x coordinate of the top left corner of the recangle in which body (ellipse) is insribed.
    Yw: y coordinate of the top left corner of the recangle in which body (ellipse) is insribed.
    '''
    pygame.draw.line(screen, DARKGRAY, [Xw + 20, Yw + 20 ], [Xw + 20, Yw + 50 + 20], 8)    # лапа 1, расстояние от левого туловища 20 
    pygame.draw.line(screen, DARKGRAY, [Xw + 80, Yw + 20], [Xw + 80, Yw + 50 + 20], 8)      # лапа 2
    pygame.draw.ellipse(screen, DARKGRAY, [Xw, Yw, 100, 50])    # туловище, размер 100 на 50
    pygame.draw.circle(screen, DARKGRAY, [Xw + (100) + 20 , Yw + int((50)/2)], 20, 0)    # морда
    draw_face (Xw + (100) + 20, Yw + int((50)/2), 20) # характеристики лица

def draw_yurt (Xy, Yy, Base) :
    '''
    Xy - x coordinate of the top left corner of rectangle 
    in which semicircle (yurt) is inscribed.
    
    Yy - y coordinate of the top left corner of rectangle 
    in which semicircle (yurt) is inscribed.
    
    Base - diameter of yurt. 
    '''
    pygame.draw.arc(screen, BLACK, [Xy, Yy, Base, Base], 0, pi + 0.01, 4)   # Полуокружность. Xy,Yy координаты левой верхней точки квадрата огибающего эту окружность. Стороны Квадрата равны Base
    pygame.draw.line(screen, BLACK, [Xy, Yy + Base/2], [Xy + Base, Yy + Base/2], 4)  # Основание юрты
    pygame.draw.rect(screen, BLACK, [Xy + Base/2, Yy + Base/2 - 0.16 * Base, Base * 0.1, Base * 0.16], 4)   # Дверь туда. Размер двери: 0.16 * Base - высота, 0.1 * Base ее ширина

draw_yurt (100, 400, 300)

    
draw_WILD_WOLF (350,350)
draw_human (600, 300, 200)





pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()