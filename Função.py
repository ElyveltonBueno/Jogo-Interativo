import random
import pygame
import time
from PIL import Image
import os
from pathlib import Path

#Giff
PaxT = Path(__file__).parent / "assets" / "Papel x Tesoura.gif"
PaxPa = Path(__file__).parent / "assets" / "Papel x Papel.gif"
PaxPe = Path(__file__).parent / "assets" / "Papel x Pedra.gif"
TxPe = Path(__file__).parent / "assets" / "Tesoura x Pedra.gif"
TxT = Path(__file__).parent / "assets" / "Tesoura x Tesoura.gif"
TxPa = Path(__file__).parent / "assets" / "Tesoura x Papel.gif"
PexPe = Path(__file__).parent / "assets" / "Pedra x Pedra.gif"
PexT = Path(__file__).parent / "assets" / "Pedra x Tesoura.gif"
PexPa = Path(__file__).parent / "assets" / "Pedra x Papel.gif"

largura = 900
altura = 600
global frame_index 
frame_index = 0
global frame_delay 
frame_delay = 100  # Milissegundos entre os frames
FPS = 40
text_color = (255, 255, 255)
AtaqueFraco = random.choice([3,4,5,6])
ChancedeAcerto = random.choice([1,2,3])
tela = pygame.display.set_mode((largura, altura))
#fonte = pygame.font.SysFont("Arial", 23)
clock = pygame.time.Clock()

def GeraCaminho(imagem):
    raiz_do_projeto = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(raiz_do_projeto, "Giff", imagem)

def geargiff(Giff):
    gif = Image.open(Giff)
    frames = []
    try:
        while True:
            frames.append(pygame.image.fromstring(gif.tobytes(), gif.size, gif.mode))
            gif.seek(len(frames))  # Move para o próximo frame
    except EOFError:
        pass  # Fim do GIF
    
    # Mostra a animação
    running = True
    frame_index = 0
    start_time = time.time()
    while running and time.time() - start_time < 3:  # 5 segundos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               running = False
    
        tela.fill((255, 255, 255))
        tela.blit(frames[frame_index], (0, 0))
        pygame.display.update()
        frame_index = (frame_index + 1) % len(frames)
        pygame.time.delay(80)  # Ajuste o delay conforme necessário
    pygame.quit()
    
def ValidaNumeroLuta(fonte):
    numero = 8
    while numero not in ("1","2","3"):
        numero = str(digitacao(fonte))
        if  numero not in ("1","2","3"):
            mostrar_dialogo(tela,fonte,"Numero incorreto, Digite Novamente!",20,200)
    return numero

def ValidaNumero(fonte):
    numero = 8
    while numero not in ("0","1","2","3"):
        numero = str(digitacao(fonte))
        if  numero not in ("0","1","2","3"):
            mostrar_dialogo(tela,fonte,"Numero incorreto, Digite Novamente!",20,200)
    return numero
    
def ValidaText(fonte):
    text = ""
    while text == "":  
        text = digitacao(fonte)
        if text == "":
            mostrar_dialogo(tela,fonte,"O campo esta vazio, Digite Novamente!",20,200)            
    return text

def mostrar_dialogo(tela,fonte,dialogo, x,y):
    """Exibe um texto na tela como diálogo."""
    texto_surf = fonte.render(dialogo, True, (255, 255, 255))
    tela.blit(texto_surf, (x, y))
    pygame.display.update()
    pygame.time.delay(600) 

def digitacao(fonte):
    textdigitado = ""
    rodando = True
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Enter confirma a entrada
                    entrada = textdigitado
                    textdigitado = ""  # Limpa o texto para a próxima interação
                    return entrada
                elif event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                    textdigitado = textdigitado[:-1]  # Remove o último caractere
                else:
                    textdigitado += event.unicode  # Adiciona o caractere digitado

        # Renderiza o texto digitado
        texto_surf = fonte.render(textdigitado, True, (255, 255, 255))
        tela.blit(texto_surf, (20, 45))
        pygame.display.update()
        clock.tick(FPS)
        
def Click_Next(fonte):
    texto_surf = fonte.render("Clique para continuar", True, (255, 255, 255))
    tela.blit(texto_surf, (650, 500)),
    pygame.display.update() 

def realizar_batalha(fonte,heroi, vilao):
    """Realiza a lógica de combate entre dois personagens."""
    while heroi.vida > 0 and vilao.vida > 0:
        tela.fill((0, 0, 0))
        mostrar_dialogo(tela,fonte,"Escolha entre (1)Pedra,(2)Papel,(3)Tesoura : ",20,20)
        posição = ValidaNumeroLuta(fonte)
        posiçãoAdv = random.choice([1,2,3])
        heroi.atacarJokenPO(fonte,posição,posiçãoAdv, vilao)
        time.sleep(1)

        if vilao.vida <= 0:
            tela.fill((0, 0, 0))
            mostrar_dialogo(tela,fonte,f"{heroi.nome} venceu a batalha!", 20, 20)
            return True

        if heroi.vida <= 0:
            tela.fill((0, 0, 0))
            mostrar_dialogo(tela,fonte,f"{heroi.nome} perdeu a batalha! Game Over.", 20, 20)
            pygame.time.delay(3000)
            pygame.quit()
            exit()
 
def geargiff(Giff):
    gif = Image.open(Giff)
    frames = []
    try:
        while True:
            frames.append(pygame.image.fromstring(gif.tobytes(), gif.size, gif.mode))
            gif.seek(len(frames))  # Move para o próximo frame
    except EOFError:
        pass  # Fim do GIF
    
    # Defina o tamanho desejado para o GIF
    novo_tamanho = (500, 400)  # Exemplo: 200x200 pixels

    # Redimensiona os frames
    frames = [pygame.transform.scale(frame, novo_tamanho) for frame in frames]
    
    # Mostra a animação
    running = True
    frame_index = 0
    start_time = time.time()
    while running and time.time() - start_time < 3:  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               running = False
    
        tela.fill((255, 255, 255))
        largura_tela, altura_tela = tela.get_size()
        largura_frame, altura_frame = frames[frame_index].get_size()
        pos_x = (largura_tela - largura_frame) // 2
        pos_y = (altura_tela - altura_frame) // 2
        tela.blit(frames[frame_index], (pos_x, pos_y))
        
        pygame.display.update()
        frame_index = (frame_index + 1) % len(frames)
        pygame.time.delay(80)          

def ResultadoDaLuta(Numero):
     #(1)Pedra,(2)Papel,(3)Tesoura 
     match Numero:
        case "1,1":
            return PexPe
        case "1,2":
            return PexPa
        case "1,3":
            return PexT
        case "2,1":
            return PaxPe
        case "2,2":
            return PaxPa
        case "2,3":
            return PaxT
        case "3,1":
            return TxPe
        case "3,2":
            return TxPa
        case "3,3":
            return TxT

def ResultadoDaLutaValor(Result):
     #(1)Pedra,(2)Papel,(3)Tesoura 
     match Result:
        case "1,1":
            return "Empate"
        case "1,2":
            return "Derrota"
        case "1,3":
            return "Vitoria"
        case "2,1":
            return "Vitoria"
        case "2,2":
            return "Empate"
        case "2,3":
            return "Derrota"
        case "3,1":
            return "Derrota"
        case "3,2":
            return "Vitoria"
        case "3,3":
            return "Empate"

# Função para quebrar o texto
def exibir_texto_multilinha( fonte,texto, x, y):
    """Exibe texto quebrado em linhas na tela."""
    lines = wrap_text(fonte,texto)
    for line in lines:
        text_surface = fonte.render(line, True, text_color)
        tela.blit(text_surface, (x, y))
        y += text_surface.get_height() + 10

def wrap_text(fonte,text,  max_width = largura-50):
    words = text.split(' ')
    lines = []
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip()
        if fonte.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)
    return lines

def Escolha_de_Personagem(Tipo,x,xnome,):
    if Tipo == "Heroi":
        return Personagem(xnome, 30 , 4 , 4 )        
    match x:
        case 0:
            return Personagem(xnome, 30 , 3 , 3 )
        case 1:
            return Personagem(xnome, 30 , 4 , 3 )
        case 2:
            return Personagem(xnome, 30 , 4 , 4 )    

class Personagem:
    def __init__(self, nome,  vida, força , defesa ):
        self.nome = nome
        self.vida = vida
        self.força = força
        self.defesa = defesa
    
    def atacarFraco(self,fonte,posição ,Adversario):    
        test = ChancedeAcerto
        tela.fill((0, 0, 0))    
        
        if test != int(posição):
            mostrar_dialogo(tela,fonte,self.nome +" Errou o Ataque!!",20,20)
        else:
            Adversario.vida = Adversario.vida - ((self.força + int(AtaqueFraco)) - Adversario.defesa)
            mostrar_dialogo(tela,fonte,f"{self.nome} atacou {Adversario.nome}",20,20)
            mostrar_dialogo(tela,fonte,f"{Adversario.nome} agora tem {Adversario.vida}",20,40)
            
    def atacarJokenPO(self,fonte,posição,posiçãoAdv ,Adversario):    
        tela.fill((0, 0, 0))   
        result = str(posição)+","+str(posiçãoAdv)     
        imagem = ResultadoDaLuta(result)
        Retorno = ResultadoDaLutaValor(result)
        geargiff(imagem)
        pygame.time.delay(200)
        tela.fill((0, 0, 0))   
        if Retorno == "Empate":
            mostrar_dialogo(tela,fonte,"Empate",20,20)
        elif Retorno == "Vitoria":
            Adversario.vida = Adversario.vida - ((self.força + int(AtaqueFraco)) - Adversario.defesa)
            mostrar_dialogo(tela,fonte,f"{self.nome} atacou {Adversario.nome}",20,20)
            mostrar_dialogo(tela,fonte,f"{Adversario.nome} agora tem {Adversario.vida} de vida",20,40)
        elif Retorno == "Derrota":
            self.vida = self.vida - ((Adversario.força + int(AtaqueFraco)) - self.defesa)
            mostrar_dialogo(tela,fonte,f"{Adversario.nome} atacou {self.nome}",20,20)
            mostrar_dialogo(tela,fonte,f"{self.nome} agora tem {self.vida} de vida",20,40) 
