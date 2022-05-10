import pygame
from pygame.locals import *
import random
from random import randint

# variáveis que definem a largura e altura da tela do jogo.
LARGURA = 1200
ALTURA = 600

def inicializa(): #função para inicializar a tela, áudio, textos, e dicionários de variáveis utilizadas no jogo.

    pygame.init() #código para inicializar o pygame
    pygame.mixer.init() #código para inicialiar o audio utilizado no jogo
    #criando a tela do jogo e definindo a altura e largura da tela.
    tela = pygame.display.set_mode((LARGURA, ALTURA), vsync=True, flags=pygame.SCALED)
    #definição do nome da tela do jogo.
    pygame.display.set_caption("INSPER NINJA")
    pygame.key.set_repeat(50)

    default_font_name = pygame.font.get_default_font()
    def_font = pygame.font.Font(default_font_name, 40)

    state = {
        #definição da posição de cada objeto do jogo
        'asteroide_pos1': [random.randint(50, 1100), random.randint(-1500, -100)],
        'asteroide_pos2': [random.randint(50, 1100), random.randint(-1500, -100)],
        'asteroide_pos3': [random.randint(50, 1100), random.randint(-1500, -100)],
        'asteroide_pos4': [random.randint(50, 1100), random.randint(-1500, -100)],
        'asteroide_pos5': [random.randint(50, 1100), random.randint(-1500, -100)],

        'escudo_pos1': [random.randint(50, 1100), random.randint(-1500, -100)],
        'escudo_pos2': [random.randint(50, 1100), random.randint(-1500, -100)],
        'escudo_pos3': [random.randint(50, 1100), random.randint(-1500, -100)],
        'escudo_pos4': [random.randint(50, 1100), random.randint(-1500, -100)],
        'escudo_pos5': [random.randint(50, 1100), random.randint(-1500, -100)],

        'laptop_pos1': [random.randint(50, 1100), random.randint(-1500, -100)],
        'laptop_pos2': [random.randint(50, 1100), random.randint(-1500, -100)],
        'laptop_pos3': [random.randint(50, 1100), random.randint(-1500, -100)],
        'laptop_pos4': [random.randint(50, 1100), random.randint(-1500, -100)],
        'laptop_pos5': [random.randint(50, 1100), random.randint(-1500, -100)],

        'nave_pos1': [random.randint(50, 1100), random.randint(-1500, -100)],
        'nave_pos2': [random.randint(50, 1100), random.randint(-1500, -100)],
        'nave_pos3': [random.randint(50, 1100), random.randint(-1500, -100)],
        'nave_pos4': [random.randint(50, 1100), random.randint(-1500, -100)],
        'nave_pos5': [random.randint(50, 1100), random.randint(-1500, -100)],

        'tempo_inicio': 0,

        'tempo_real': 0,

        #definição dos pontos que o jogador obterá ao destruir os objetos
        'pontos' : 0,

        #definição da vida do jogador no momento da gameplay
        'vida' : 0,

        #definição da velocidade dos objetos do jogo.
        'velocidade': 0 ,

        #definição da variável de tempo para poder alterar a velocidade dos objetos.
        'last_updated': 0,

        #definição da variável para verificar se houve clique na tela e então desenhar as respectivas telas dependendo do valor da variável
        'true': False
    }
    assets = {

        #botão 'play again' que aparece quando o usuário perde (vida <= 0).
        'play_again': pygame.transform.scale(pygame.image.load("playagain.png"),(250,100)),

        #botão 'game over' que aparece quando o usuário perde (vida <= 0).
        'game_over': pygame.transform.scale(pygame.image.load("PLAY AGAIN (1) - cópia.png"),(600,300)),

        #variável para carregar a fonte utilizada nos textos do jogo
        'font': def_font,

        #variaveis das telas de fundo do jogo
        'background1' : pygame.transform.scale(pygame.image.load("SERGINHO.png"), (LARGURA, ALTURA)),
        'background2' : pygame.transform.scale(pygame.image.load("cenario1.png"), (LARGURA, ALTURA)),
        'background3' : pygame.transform.scale(pygame.image.load("cenario2.2.webp"), (LARGURA, ALTURA)),
        'background4' : pygame.transform.scale(pygame.image.load("cenario3.webp"), (LARGURA, ALTURA)),
        'background5' : pygame.transform.scale(pygame.image.load("background4.png"), (LARGURA, ALTURA)),

        #variáveis dos objetos dos jogos .
        'asteroide1': pygame.transform.scale(pygame.image.load("asteroidepygame.png"), (60,60)),
        'asteroide2': pygame.transform.scale(pygame.image.load("asteroidepygame.png"), (60,60)),
        'asteroide3': pygame.transform.scale(pygame.image.load("asteroidepygame.png"), (60,60)),
        'asteroide4': pygame.transform.scale(pygame.image.load("asteroidepygame.png"), (60,60)),
        'asteroide5': pygame.transform.scale(pygame.image.load("asteroidepygame.png"), (60,60)),

        'escudo1' : pygame.transform.scale(pygame.image.load("escudopygame-removebg-preview.png"), (60,60)),
        'escudo2' : pygame.transform.scale(pygame.image.load("escudopygame-removebg-preview.png"), (60,60)), 
        'escudo3' : pygame.transform.scale(pygame.image.load("escudopygame-removebg-preview.png"), (60,60)), 
        'escudo4' : pygame.transform.scale(pygame.image.load("escudopygame-removebg-preview.png"), (60,60)), 
        'escudo5' : pygame.transform.scale(pygame.image.load("escudopygame-removebg-preview.png"), (60,60)),

        'laptop1' : pygame.transform.scale(pygame.image.load("laptop-removebg-preview.png"), (60,60)),
        'laptop2' : pygame.transform.scale(pygame.image.load("laptop-removebg-preview.png"), (60,60)),
        'laptop3' : pygame.transform.scale(pygame.image.load("laptop-removebg-preview.png"), (60,60)),
        'laptop4' : pygame.transform.scale(pygame.image.load("laptop-removebg-preview.png"), (60,60)),
        'laptop5' : pygame.transform.scale(pygame.image.load("laptop-removebg-preview.png"), (60,60)),

        'nave1' : pygame.transform.scale(pygame.image.load("spaceship.png"), (60,60)),
        'nave2' : pygame.transform.scale(pygame.image.load("spaceship.png"), (60,60)),
        'nave3' : pygame.transform.scale(pygame.image.load("spaceship.png"), (60,60)),
        'nave4' : pygame.transform.scale(pygame.image.load("spaceship.png"), (60,60)),
        'nave5' : pygame.transform.scale(pygame.image.load("spaceship.png"), (60,60)),


    }


    return tela, assets, state


def finaliza(): #função para finalizar o game.
    pygame.quit()


def desenha(tela: pygame.Surface, assets, state): # função para desenhar telas ou objetos na tela dependendo de certas condições.
    
    #condições para definir qual tela será desenhada e quais objetos serão desenhados caso o usuário clique em alguma tecla ou dependendo do tempo decorrido do jogo.
    if not state["true"]:
        tela.blit(assets['background1'], (0, 0))
        state["vida"] = 25
        state["pontos"] = 0
        state["tempo_inicio"] = pygame.time.get_ticks()
    else:
        if state["tempo_real"] >= 0 and state["tempo_real"]< 15000:
            tela.blit(assets['background2'], (0, 0))
            state["velocidade"] = 200
            tela.blit(assets["asteroide1"], state["asteroide_pos1"])
            tela.blit(assets["asteroide2"], state["asteroide_pos2"])
            tela.blit(assets["asteroide3"], state["asteroide_pos3"])
            tela.blit(assets["asteroide4"], state["asteroide_pos4"])
            tela.blit(assets["asteroide5"], state["asteroide_pos5"])

        elif state["tempo_real"] >= 15000 and state["tempo_real"] < 30000:

            tela.blit(assets['background3'], (0, 0))
            state["velocidade"] = 280
            tela.blit(assets["escudo1"], state["escudo_pos1"])
            tela.blit(assets["escudo2"], state["escudo_pos2"])
            tela.blit(assets["escudo3"], state["escudo_pos3"])
            tela.blit(assets["escudo4"], state["escudo_pos4"])
            tela.blit(assets["escudo5"], state["escudo_pos5"])


        elif state["tempo_real"] >= 30000 and  state["tempo_real"] < 45000:
            tela.blit(assets['background4'], (0, 0))
            state["velocidade"] = 310
            tela.blit(assets["laptop1"], state["laptop_pos1"])
            tela.blit(assets["laptop2"], state["laptop_pos2"])
            tela.blit(assets["laptop3"], state["laptop_pos3"])
            tela.blit(assets["laptop4"], state["laptop_pos4"])
            tela.blit(assets["laptop5"], state["laptop_pos5"])

        elif state["tempo_real"] >= 45000 :
            tela.blit(assets['background5'], (0, 0))
            state["velocidade"] = 380
            tela.blit(assets["nave1"], state["nave_pos1"])
            tela.blit(assets["nave2"], state["nave_pos2"])
            tela.blit(assets["nave3"], state["nave_pos3"])
            tela.blit(assets["nave4"], state["nave_pos4"])
            tela.blit(assets["nave5"], state["nave_pos5"])

    #desenhando os quadrados que estarão escritos os pontos e a vida do jogador.
    pygame.draw.rect(tela,(0, 0, 0), pygame.Rect(1000,15,180,50))
    pygame.draw.rect(tela,(0, 0, 0), pygame.Rect(15,15,260,50))

    #inserindo a contagem da vida do jogador.
    ms = assets['font'].render(f'VIDA: {state["vida"]}', True, (255, 255, 255))
    tela.blit(ms, (1010, 25))

    #inserindo a contagem dos pontos do jogador.
    ms = assets['font'].render(f'PONTOS: {state["pontos"]}', True, (255, 255, 255))
    tela.blit(ms, (25, 25))

    #condição que caso o usuário perca, desenhe na tela os botoes de 'game over'e 'play again' e a velocidade dos objetos tenha valor 0.
    if state["vida"] <= 0 :
        tela.blit(assets["game_over"],(300,100))
        tela.blit(assets["play_again"],(475,450))
        state["velocidade"] = 0
        # state["last_updated"] = -59000

    pygame.display.update()

def colidiu(rect, mouse): # função para verificar se houve colisão entre o clique do mouse e outro objeto.
    return  rect.collidepoint(mouse[0], mouse[1]) 

def atualiza_estado(state):

    #variável para coletar a posição do clique do mouse.
    pos = pygame.mouse.get_pos() 

    #variável para coletar a contagem de tempo do jogo.
    valor = pygame.time.get_ticks()
    delta_t = (valor - state['last_updated'])/1000 

    #condições para alterar a velocidade do objetos dependendo do tempo passado no jogo.
    if state["tempo_real"] >= 0 and state["tempo_real"] < 15000:
        state['asteroide_pos1'][1] = state['asteroide_pos1'][1] + state['velocidade'] * delta_t
        state['asteroide_pos2'][1] = state['asteroide_pos2'][1] + state['velocidade'] * delta_t
        state['asteroide_pos3'][1] = state['asteroide_pos3'][1] + state['velocidade'] * delta_t
        state['asteroide_pos4'][1] = state['asteroide_pos4'][1] + state['velocidade'] * delta_t
        state['asteroide_pos5'][1] = state['asteroide_pos5'][1] + state['velocidade'] * delta_t
    elif state["tempo_real"] >= 15000 and state["tempo_real"] < 30000:
        state['escudo_pos1'][1] = state['escudo_pos1'][1] + state['velocidade'] * delta_t
        state['escudo_pos2'][1] = state['escudo_pos2'][1] + state['velocidade'] * delta_t
        state['escudo_pos3'][1] = state['escudo_pos3'][1] + state['velocidade'] * delta_t
        state['escudo_pos4'][1] = state['escudo_pos4'][1] + state['velocidade'] * delta_t
        state['escudo_pos5'][1] = state['escudo_pos5'][1] + state['velocidade'] * delta_t
    elif state["tempo_real"] >= 30000 and  state["tempo_real"] < 45000:
        state['laptop_pos1'][1] = state['laptop_pos1'][1] + state['velocidade'] * delta_t
        state['laptop_pos2'][1] = state['laptop_pos2'][1] + state['velocidade'] * delta_t
        state['laptop_pos3'][1] = state['laptop_pos3'][1] + state['velocidade'] * delta_t
        state['laptop_pos4'][1] = state['laptop_pos4'][1] + state['velocidade'] * delta_t
        state['laptop_pos5'][1] = state['laptop_pos5'][1] + state['velocidade'] * delta_t
    elif state["tempo_real"] >= 45000 :
        state['nave_pos1'][1] = state['nave_pos1'][1] + state['velocidade'] * delta_t
        state['nave_pos2'][1] = state['nave_pos2'][1] + state['velocidade'] * delta_t
        state['nave_pos3'][1] = state['nave_pos3'][1] + state['velocidade'] * delta_t
        state['nave_pos4'][1] = state['nave_pos4'][1] + state['velocidade'] * delta_t
        state['nave_pos5'][1] = state['nave_pos5'][1] + state['velocidade'] * delta_t

    #condições que, caso um objeto ultrapasse o limite da tela, ele retorna à uma certa coordenada da tela, para que ele possa retornar ao jogo de maneira coerente, e a vida do usuário é abaixada em uma unidade. 
    if state['asteroide_pos1'][1] >= 650 :
        state['asteroide_pos1'][0] = random.randint(60,1140)
        state['asteroide_pos1'][1] = random.randint(-1500, -100)
        state["vida"] -= 1
    elif state['asteroide_pos2'][1] >= 650 :
        state['asteroide_pos2'][0] = random.randint(60,1140)
        state['asteroide_pos2'][1] = random.randint(-1500, -100)
        state["vida"] -= 1
    elif state['asteroide_pos3'][1] >= 650 :
        state['asteroide_pos3'][0] = random.randint(60,1140)
        state['asteroide_pos3'][1] = random.randint(-1500, -100)
        state["vida"] -= 1
    elif state['asteroide_pos4'][1] >= 650 :
        state['asteroide_pos4'][0] = random.randint(60,1140)
        state['asteroide_pos4'][1] = random.randint(-1500, -100)
        state["vida"] -= 1
    elif state['asteroide_pos5'][1] >= 650 :
        state['asteroide_pos5'][0] = random.randint(60,1140)
        state['asteroide_pos5'][1] = random.randint(-1500, -100)
        state["vida"] -= 1

    elif state['laptop_pos1'][1] >= 650:
        state['laptop_pos1'][0] = random.randint(60,1140)
        state['laptop_pos1'][1] = random.randint(-1500, -100)
        state["vida"] -= 1
    elif state['laptop_pos2'][1] >= 650:
        state['laptop_pos2'][0] = random.randint(60,1140)
        state['laptop_pos2'][1] = random.randint(-1500, -100)
        state["vida"] -= 1
    elif state['laptop_pos3'][1] >= 650:
        state['laptop_pos3'][0] = random.randint(60,1140)
        state['laptop_pos3'][1] = random.randint(-1500, -100)
        state["vida"] -= 1
    elif state['laptop_pos4'][1] >= 650:
        state['laptop_pos4'][0] = random.randint(60,1140)
        state['laptop_pos4'][1] = random.randint(-1500, -100)
        state["vida"] -= 1
    elif state['laptop_pos5'][1] >= 650:
        state['laptop_pos5'][0] = random.randint(60,1140)
        state['laptop_pos5'][1] = random.randint(-1500, -100)
        state["vida"] -= 1

    elif state['nave_pos1'][1] >= 650:
        state['nave_pos1'][0] = random.randint(60,1140)
        state['nave_pos1'][1] = random.randint(-1500, -100)
        state["vida"] -= 1
    elif state['nave_pos2'][1] >= 650:
        state['nave_pos2'][0] = random.randint(60,1140)
        state['nave_pos2'][1] = random.randint(-1500, -100)
        state["vida"] -= 1
    elif state['nave_pos3'][1] >= 650:
        state['nave_pos3'][0] = random.randint(60,1140)
        state['nave_pos3'][1] = random.randint(-1500, -100)
        state["vida"] -= 1
    elif state['nave_pos4'][1] >= 650:
        state['nave_pos4'][0] = random.randint(60,1140)
        state['nave_pos4'][1] = random.randint(-1500, -100)
        state["vida"] -= 1
    elif state['nave_pos5'][1] >= 650:
        state['nave_pos5'][0] = random.randint(60,1140)
        state['nave_pos5'][1] = random.randint(-1500, -100)
        state["vida"] -= 1

    elif state['escudo_pos1'][1] >= 650:
        state['escudo_pos1'][0] = random.randint(60,1140)
        state['escudo_pos1'][1] = random.randint(-1500, -100)
        state["vida"] -= 1
    elif state['escudo_pos2'][1] >= 650:
        state['escudo_pos2'][0] = random.randint(60,1140)
        state['escudo_pos2'][1] = random.randint(-1500, -100)
        state["vida"] -= 1
    elif state['escudo_pos3'][1] >= 650:
        state['escudo_pos3'][0] = random.randint(60,1140)
        state['escudo_pos3'][1] = random.randint(-1500, -100)
        state["vida"] -= 1
    elif state['escudo_pos4'][1] >= 650:
        state['escudo_pos4'][0] = random.randint(60,1140)
        state['escudo_pos4'][1] = random.randint(-1500, -100)
        state["vida"] -= 1
    elif state['escudo_pos5'][1] >= 650:
        state['escudo_pos5'][0] = random.randint(60,1140)
        state['escudo_pos5'][1] = random.randint(-1500, -100)
        state["vida"] -= 1
    
    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

        #condição para alterar o valor de uma variável caso o usuário clique em qualquer tecla.    
        elif ev.type == pygame.KEYDOWN: 
            state["true"] = True

        elif ev.type == pygame.MOUSEBUTTONDOWN :

            #condição para verificar se o usuário clicou no botão 'play again' e então reiniciar o jogo. 
            if state["vida"] <= 0 and colidiu(pygame.Rect((475,450),(250,100)), pos):
                state["true"] = False
                
            #condições para verificar se houve colisão entre o clique do mouse e um objeto, se sim, o objeto retorna à um ponto coerente, o ponto é acrescido em uma unidade e um efeito sonoro é tocado.
            if colidiu(pygame.Rect(state["asteroide_pos1"][0],state["asteroide_pos1"][1],60,60), pos):
                state['asteroide_pos1'][0] = random.randint(60,1140)
                state["asteroide_pos1"][1] = random.randint(-1500, -100)
                state["pontos"] += 1
                efeito = pygame.mixer.Sound("retro_sound_1_0.wav")
                pygame.mixer.Sound.play(efeito)
            elif colidiu(pygame.Rect(state["asteroide_pos2"][0],state["asteroide_pos2"][1],60,60), pos):
                state['asteroide_pos2'][0] = random.randint(60,1140)
                state["asteroide_pos2"][1] = random.randint(-1500, -100)
                state["pontos"] += 1
                efeito = pygame.mixer.Sound("retro_sound_1_0.wav")
                pygame.mixer.Sound.play(efeito)
            elif colidiu(pygame.Rect(state["asteroide_pos3"][0],state["asteroide_pos3"][1],60,60), pos):
                state['asteroide_pos3'][0] = random.randint(60,1140)
                state["asteroide_pos3"][1] = random.randint(-1500, -100)
                state["pontos"] += 1
                efeito = pygame.mixer.Sound("retro_sound_1_0.wav")
                pygame.mixer.Sound.play(efeito)
            elif colidiu(pygame.Rect(state["asteroide_pos4"][0],state["asteroide_pos4"][1],60,60), pos):
                state['asteroide_pos4'][0] = random.randint(60,1140)
                state["asteroide_pos4"][1] = random.randint(-1500, -100)
                state["pontos"] += 1
                efeito = pygame.mixer.Sound("retro_sound_1_0.wav")
                pygame.mixer.Sound.play(efeito)
            elif colidiu(pygame.Rect(state["asteroide_pos5"][0],state["asteroide_pos5"][1],60,60), pos):
                state['asteroide_pos5'][0] = random.randint(60,1140)
                state["asteroide_pos5"][1] = random.randint(-1500, -100)
                state["pontos"] += 1
                efeito = pygame.mixer.Sound("retro_sound_1_0.wav")
                pygame.mixer.Sound.play(efeito)

            elif colidiu(pygame.Rect(state["escudo_pos1"][0],state["escudo_pos1"][1],60,60), pos):
                state["escudo_pos1"][0] = random.randint(60,1140)
                state["escudo_pos1"][1] = random.randint(-1500, -100)
                state["pontos"] += 1
                efeito = pygame.mixer.Sound("retro_sound_1_0.wav")
                pygame.mixer.Sound.play(efeito)
            elif colidiu(pygame.Rect(state["escudo_pos2"][0],state["escudo_pos2"][1],60,60), pos):
                state["escudo_pos2"][0] = random.randint(60,1140)
                state["escudo_pos2"][1] = random.randint(-1500, -100)
                state["pontos"] += 1
                efeito = pygame.mixer.Sound("retro_sound_1_0.wav")
                efeito.play()
            elif colidiu(pygame.Rect(state["escudo_pos3"][0],state["escudo_pos3"][1],60,60), pos):
                state["escudo_pos3"][0] = random.randint(60,1140)
                state["escudo_pos3"][1] = random.randint(-1500, -100)
                state["pontos"] += 1
                efeito = pygame.mixer.Sound("retro_sound_1_0.wav")
                pygame.mixer.Sound.play(efeito)
            elif colidiu(pygame.Rect(state["escudo_pos4"][0],state["escudo_pos4"][1],60,60), pos):
                state["escudo_pos4"][0] = random.randint(60,1140)
                state["escudo_pos4"][1] = random.randint(-1500, -100)
                state["pontos"] += 1
                efeito = pygame.mixer.Sound("retro_sound_1_0.wav")
                pygame.mixer.Sound.play(efeito)
            elif colidiu(pygame.Rect(state["escudo_pos5"][0],state["escudo_pos5"][1],60,60), pos):
                state["escudo_pos5"][0] = random.randint(60,1140)
                state["escudo_pos5"][1] = random.randint(-1500, -100)
                state["pontos"] += 1
                efeito = pygame.mixer.Sound("retro_sound_1_0.wav")
                pygame.mixer.Sound.play(efeito)

            elif colidiu(pygame.Rect(state["laptop_pos1"][0],state["laptop_pos1"][1],60,60), pos):
                state["laptop_pos1"][0] = random.randint(60,1140)
                state["laptop_pos1"][1] = random.randint(-1500, -100)
                state["pontos"] += 1
                efeito = pygame.mixer.Sound("retro_sound_1_0.wav")
                pygame.mixer.Sound.play(efeito)
            elif colidiu(pygame.Rect(state["laptop_pos2"][0],state["laptop_pos2"][1],60,60), pos):
                state["laptop_pos2"][0] = random.randint(60,1140)
                state["laptop_pos2"][1] = random.randint(-1500, -100)
                state["pontos"] += 1
                efeito = pygame.mixer.Sound("retro_sound_1_0.wav")
                pygame.mixer.Sound.play(efeito)
            elif colidiu(pygame.Rect(state["laptop_pos3"][0],state["laptop_pos3"][1],60,60), pos):
                state["laptop_pos3"][0] = random.randint(60,1140)
                state["laptop_pos3"][1] = random.randint(-1500, -100)
                state["pontos"] += 1
                efeito = pygame.mixer.Sound("retro_sound_1_0.wav")
                pygame.mixer.Sound.play(efeito)
            elif colidiu(pygame.Rect(state["laptop_pos4"][0],state["laptop_pos4"][1],60,60), pos):
                state["laptop_pos4"][0] = random.randint(60,1140)
                state["laptop_pos4"][1] = random.randint(-1500, -100)
                state["pontos"] += 1
                efeito = pygame.mixer.Sound("retro_sound_1_0.wav")
                pygame.mixer.Sound.play(efeito)
            elif colidiu(pygame.Rect(state["laptop_pos5"][0],state["laptop_pos5"][1],60,60), pos):
                state["laptop_pos5"][0] = random.randint(60,1140)
                state["laptop_pos5"][1] = random.randint(-1500, -100)
                state["pontos"] += 1
                efeito = pygame.mixer.Sound("retro_sound_1_0.wav")
                pygame.mixer.Sound.play(efeito)

            elif colidiu(pygame.Rect(state["nave_pos1"][0],state["nave_pos1"][1],60,60), pos):
                state["nave_pos1"][0] = random.randint(60,1140)
                state["nave_pos1"][1] = random.randint(-1500, -100)
                state["pontos"] += 1
                efeito = pygame.mixer.Sound("retro_sound_1_0.wav")
                pygame.mixer.Sound.play(efeito)
            elif colidiu(pygame.Rect(state["nave_pos2"][0],state["nave_pos2"][1],60,60), pos):
                state["nave_pos2"][0] = random.randint(60,1140)
                state["nave_pos2"][1] = random.randint(-1500, -100)
                state["pontos"] += 1
                efeito = pygame.mixer.Sound("retro_sound_1_0.wav")
                pygame.mixer.Sound.play(efeito)
            elif colidiu(pygame.Rect(state["nave_pos3"][0],state["nave_pos3"][1],60,60), pos):
                state["nave_pos3"][0] = random.randint(60,1140)
                state["nave_pos3"][1] = random.randint(-1500, -100)
                state["pontos"] += 1
                efeito = pygame.mixer.Sound("retro_sound_1_0.wav")
                pygame.mixer.Sound.play(efeito)
            elif colidiu(pygame.Rect(state["nave_pos4"][0],state["nave_pos4"][1],60,60), pos):
                state["nave_pos4"][0] = random.randint(60,1140)
                state["nave_pos4"][1] = random.randint(-1500, -100)
                state["pontos"] += 1
                efeito = pygame.mixer.Sound("retro_sound_1_0.wav")
                pygame.mixer.Sound.play(efeito)
            elif colidiu(pygame.Rect(state["nave_pos5"][0],state["nave_pos5"][1],60,60), pos):
                state["nave_pos5"][0] = random.randint(60,1140)
                state["nave_pos5"][1] = random.randint(-1500, -100)
                state["pontos"] += 1
                efeito = pygame.mixer.Sound("retro_sound_1_0.wav")
                pygame.mixer.Sound.play(efeito)

    state['last_updated'] = valor 
    state["tempo_real"] = state['last_updated'] - state["tempo_inicio"]
    return True

def gameloop(tela, assets, state):
    while atualiza_estado(state):
        desenha(tela, assets, state)

if __name__ == '__main__':
    tela, assets, state = inicializa()
    gameloop(tela, assets, state)
    finaliza()
