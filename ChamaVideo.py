import pygame
import cv2
import sys
import os  # Importando para criar diretórios

def play_video(tela, video_path, audio_path):
        
    # Inicializar o OpenCV para ler o vídeo
    video_capture = cv2.VideoCapture(str(video_path))
        
    pygame.mixer.init()
    try:
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()
    except pygame.error as e:
        print(f"Erro ao carregar o áudio: {e}")
        return
    
    # Verificar se o vídeo foi carregado corretamente
    if not video_capture.isOpened():
        print(f"Erro ao abrir o vídeo: {video_path}")
        return

    # Obter largura e altura do vídeo
    width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))


    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                video_capture.release()
                pygame.quit()
                sys.exit()

        # Ler frame do vídeo
        ret, frame = video_capture.read()
        if not ret:
            break  # Fim do vídeo

        # Corrigir espelhamento horizontal (inversão horizontal)
        frame = cv2.flip(frame, 2)

        # Converter o frame de BGR para RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Redimensionar o frame para caber na tela do jogo
        frame = cv2.resize(frame, (tela.get_width(), tela.get_height()))

        # Converter o frame para Surface do Pygame
        frame_surface = pygame.surfarray.make_surface(frame)
        frame_surface = pygame.transform.rotate(frame_surface, -90)  # Ajustar orientação

        # Exibir o frame na tela do jogo
        tela.blit(frame_surface, (0, 0))
        pygame.display.update()

        # Controlar a velocidade para coincidir com o FPS do vídeo
        clock.tick(fps)

    video_capture.release()

