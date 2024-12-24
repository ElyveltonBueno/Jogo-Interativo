import pygame
import time
import random
from Chatbot import mensagemparaobot
from ChamaVideo import play_video
from pathlib import Path
from PIL import Image
from Função import ValidaNumero,ValidaNumeroLuta,ValidaText,mostrar_dialogo,exibir_texto_multilinha,Click_Next,digitacao,Escolha_de_Personagem,realizar_batalha

#video
Video1 = Path(__file__).parent / "assets" / "Abertura SEGA.mp4"
Video2 = Path(__file__).parent / "assets" / "Abertura -  Mundo Disney Personagens no Castelo.mp4"
Audio1 = Path(__file__).parent / "assets" / "Audio Abertura SEGA.mp3"
Audio2 = Path(__file__).parent / "assets" / "Audio Abertura -  Mundo Disney Personagens no Castelo.mp3"

largura = 900
altura = 600

pygame.init()
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("História Interativa")

fonte = pygame.font.SysFont("Arial", 23)
   
play_video(tela, Video1,Audio1)
play_video(tela, Video2,Audio2)
tela.fill((0, 0, 0))

text = ""  

# Loop principal'
jogando = True
parte = 0
Count = 0 
PersonagensAdversario = [0,1,2,3]
NumeroDOpersonagemPrincipal = 5

while jogando:  
    if parte == 0:
        mostrar_dialogo(tela,fonte,"Escolha o tema do jogo para criarmos os personagens:",20,20)        
        result = ValidaText(fonte)        
        tela.fill((0, 0, 0))
        mostrar_dialogo(tela,fonte,"Carregando, Por favor espere",20,20)
        Personagens = mensagemparaobot("Me diga apenas os nomes separado por virgula de 4 personagens de "+result)
        ListadePersonagens = Personagens.split(",")
        time.sleep(1)
        tela.fill((0, 0, 0))
        mostrar_dialogo(tela,fonte,"Escolha seu personagem: " ,20,20)
        mostrar_dialogo(tela,fonte,"0 - " +str(ListadePersonagens[0]) ,200,50)
        mostrar_dialogo(tela,fonte,"1 - " +str(ListadePersonagens[1]) ,200,70)
        mostrar_dialogo(tela,fonte,"2 - " +str(ListadePersonagens[2]) ,200,90)
        mostrar_dialogo(tela,fonte,"3 - " +str(ListadePersonagens[3]) ,200,110)
        
        NumeroDOpersonagemPrincipal =  int(ValidaNumero(fonte))
        
        tela.fill((0, 0, 0))
        mostrar_dialogo(tela,fonte,"Carregando os personagens... " ,20,20)
        PersonagensAdversario.remove(NumeroDOpersonagemPrincipal)
        random.shuffle(PersonagensAdversario)
        
        parte = parte+1
        time.sleep(3)
    
    elif parte == 1:
        chatgpt = "Me responda apenas a pergunta, crie a introdução de uma historia curta de heroi onde o " + ListadePersonagens[NumeroDOpersonagemPrincipal] + " o vilão é o " + ListadePersonagens[int(PersonagensAdversario[2])]
        tela.fill((0, 0, 0))
        retornochat = mensagemparaobot(chatgpt)
        exibir_texto_multilinha(fonte,retornochat, 20,20)
        Click_Next(fonte)
        digitacao(fonte)
        
        chatgpt = "Em busca do seu principal adversario , ele acaba encontrando " + ListadePersonagens[int(PersonagensAdversario[0])]+"."
        chatgpt2 = "Me responda apenas a pergunta,em uma historia onde o heroi é o " +  ListadePersonagens[NumeroDOpersonagemPrincipal] + " e ele precisa salvar o  mundo e ele acaba de encontrar seu primiero adversario o " + ListadePersonagens[int(PersonagensAdversario[0])]+ ", Crie um pequeno dialogo entre os dois antes de começar a luta"
        
        tela.fill((0, 0, 0))
        mostrar_dialogo(tela,fonte,chatgpt,20,20)
        result = mensagemparaobot(chatgpt2)
        pygame.time.delay(1000)
        Click_Next(fonte)
        digitacao(fonte)
        tela.fill((0, 0, 0))
        exibir_texto_multilinha(fonte,result, 20,20)
        
        Heroi = Escolha_de_Personagem("Heroi",0,ListadePersonagens[NumeroDOpersonagemPrincipal])
        Vilão = Escolha_de_Personagem("",0,ListadePersonagens[int(PersonagensAdversario[0])])
                
        parte = parte+1
        time.sleep(2)
       
    elif parte == 2:
        #Onde a luta começa
        Click_Next(fonte)
        digitacao(fonte)
        realizar_batalha(fonte,Heroi , Vilão)
        parte = parte+1
                
    elif parte == 3:            
        tela.fill((0, 0, 0))
        mostrar_dialogo(tela,fonte,"Você venceu seu primeiro adversario, daqui para frente tudo fica mais emocionante!!!!",20,20)            
        Heroi = Escolha_de_Personagem("Heroi",0,ListadePersonagens[NumeroDOpersonagemPrincipal])
        Vilão = Escolha_de_Personagem("",0,ListadePersonagens[int(PersonagensAdversario[1])])
        chatgpt = "Me responda apenas a pergunta,em uma historia onde o heroi é o " +  Heroi.nome + " e ele conseguil vencer o primeiro adversario o " + ListadePersonagens[int(PersonagensAdversario[0])]+ " mas agora vai precisar se esforçar mais para enfrentar um adversario mais forte o " + Vilão.nome + ", Crie um pequeno dialogo entre os dois antes de começar a luta"
        Click_Next(fonte)
        digitacao(fonte)
        tela.fill((0, 0, 0))
        mostrar_dialogo(tela,fonte,"Seguindo seu caminho até seu destino vc encontra "+Vilão.nome,20,20)
        pygame.time.delay(1400)
        tela.fill((0, 0, 0))
        exibir_texto_multilinha(fonte,mensagemparaobot(chatgpt), 20,20)
        pygame.time.delay(1400)
        Click_Next(fonte)
        digitacao(fonte)
        tela.fill((0, 0, 0))
        mostrar_dialogo(tela,fonte,"A luta Vai começar!!",20,20)
        time.sleep(2)
        realizar_batalha(fonte,Heroi,Vilão)
        parte = parte+1
    
    elif parte == 4:
    #terceira e ultima luta
        tela.fill((0, 0, 0))
        mostrar_dialogo(tela,fonte,"Você venceu seu segundo adversario, agora é tudo ou nada!!!!",20,20)            
        Heroi = Escolha_de_Personagem("Heroi",0,ListadePersonagens[NumeroDOpersonagemPrincipal])
        Vilão = Escolha_de_Personagem("",0,ListadePersonagens[int(PersonagensAdversario[2])])
        chatgpt = "Me responda apenas a pergunta, em uma historia onde o heroi é o " +  Heroi.nome + " e ele conseguil vencer o segundi adversario o " + ListadePersonagens[int(PersonagensAdversario[0])]+ " mas agora vai precisar enfrentar um adversario mais forte o " + Vilão.nome + "Crie um pequeno dialogo entre os dois antes de começar a luta"
        Click_Next(fonte)
        digitacao(fonte)
        tela.fill((0, 0, 0))
        exibir_texto_multilinha(fonte,mensagemparaobot(chatgpt), 20,20)
        Click_Next(fonte)
        digitacao(fonte)
        tela.fill((0, 0, 0))
        mostrar_dialogo(tela,fonte,"A luta Vai começar!!",20,20)
        time.sleep(3)
        realizar_batalha(fonte,Heroi,Vilão)
        parte = parte+1
                
    elif parte == 5:        
        chatgpt = "Me responda apenas a pergunta,em uma historia onde o heroi é o " +  Heroi.nome + " e ele conseguil venceu seu ultimo e maior adversario o "  + Vilão.nome + "Crie o final da historia contando o que vem agora depois que ele salvou o mundo"
        tela.fill((0, 0, 0))
        mostrar_dialogo(tela,fonte,"Gerando o final da Historia.",20,20)
        result = mensagemparaobot(chatgpt)
        tela.fill((0, 0, 0))
        exibir_texto_multilinha(fonte,result, 20,20)
        pygame.time.delay(2000)
        Click_Next(fonte)
        digitacao(fonte)
        tela.fill((0, 0, 0))
        mostrar_dialogo(tela,fonte,"Obrigado por jogar!!",20,20)
        time.sleep(3)
        mostrar_dialogo(tela,fonte,"Créditos:",20,40)
        time.sleep(3)
        mostrar_dialogo(tela,fonte,"Dev: Elyvelton Bueno",20,60)
        pygame.time.delay(2000)
        jogando = False

pygame.quit()
