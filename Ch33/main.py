import pygame

pygame.mixer.init()

# sound = pygame.mixer.Sound('14.wav')
# sound.play(1)
# print(sound.get_volume())
# pygame.time.delay(30000)
# sound.play(2)
pygame.mixer.music.load('bubble.mp3')
pygame.mixer.music.play(-1)
pygame.time.delay(10000)