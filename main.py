import sys, random
import pygame
 
 
class Jeu:
   
 
    def __init__(self):
 
        self.ecran = pygame.display.set_mode((800, 600))
 
        pygame.display.set_caption('The Snake')
        self.jeu_encours = True
 
        self.serpent_position_x = 300
        self.serpent_position_y = 300
        self.serpent_direction_x = 0
        self.serpent_direction_y = 0
        self.serpent_corps = 10
 
 
    def fonction_principale(self):
       
 
        while self.jeu_encours:
 
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    sys.exit()
 
                if evenement.type == pygame.KEYDOWN:
 
                    if evenement.key == pygame.K_RIGHT:
                        self.serpent_direction_x = 0.5
                        self.serpent_direction_y = 0
 
                    if evenement.key == pygame.K_LEFT:
                        self.serpent_direction_x = -0.5
                        self.serpent_direction_y = 0
 
 
                    if evenement.key == pygame.K_UP:
                        self.serpent_direction_x = 0
                        self.serpent_direction_y = -0.5
 
 
                    if evenement.key == pygame.K_DOWN:
                        self.serpent_direction_x = 0
                        self.serpent_direction_y = 0.5
                       
 
           if self.serpent_position_x <= 100 or self.serpent_position_x >= 700 \
               or self.serpent_position_y <= 100 or self.serpent_position_y >= 600:
 
                   sys.exit()
 
            self.serpent_position_x += self.serpent_direction_x
            self.serpent_position_y += self.serpent_direction_y
 
            print(self.serpent_position_x,self.serpent_position_y)
 
 
 
            self.ecran.fill((0,0,0))
 
            self.creer_limites()
 
            pygame.draw.rect(self.ecran,(0,255,0),(self.serpent_position_x,self.serpent_position_y,self.serpent_corps,self.serpent_corps))
 
            pygame.display.flip()
 
    def creer_limites(self):
 
        pygame.draw.rect(self.ecran,(255,255,255),(100,100,600,500),3)
 
 
if __name__ == '__main__':
 
    pygame.init()
    Jeu().fonction_principale()
    pygame.quit()
