import pygame #Blibliotaca com diversas funcionalidades como a de reproduzir audio 

print("==ABRINDO E REPRODUZINDO O ÁUDIO MP3==")

pygame.init() #Inicializador da bibliotaca  
pygame.mixer_music.load("") #Coloca o nome do arquivo que você quer reproduzir para ele carregar o arquivo 
pygame.mixer.music.play() #Da play na musica 
pygame.event.wait() #Espera o envento (a musica) terminar para encerrar o programa 

#NÃO FIZ O TESTE DO PROGRAMA PQ NÃO QUIS BAIXAR ARQUIVO DE MUSICA POIS ESTAVA NO PC DA EMPRESA #