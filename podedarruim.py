import customtkinter as ctk
import pandas as pd
import pygame
from pygame.locals import *
import time
import math
import random
import requests
import io
from urllib.request import urlopen
from PIL import Image, ImageTk



azul_claro = '#99bed9'
laranja = '#c5721a'
azul2 = '#3f78b4'
amareloclaro = '#e38e74'
vermelho = '#b91728'
cinza = '#a5b2c3'
roxo ='#8c778e'
verde = '#858154'
azul_escuro = '#27355a'

# Básicos
janela = ctk.CTk()
ctk.set_appearance_mode("dark")
janela.title("Pokémon")
janela.geometry("3000x2000")


# Variável para armazenar o nome
nome = ctk.StringVar()

def imagem():
    pikachu = ctk.CTkImage(light_image=Image.open("assets/imgjogo.jpeg"), dark_image=Image.open("assets/imgjogo.jpeg"), size=(740, 800))

    # Cria um label dentro do frame e adiciona a imagem a ele
    image_label = ctk.CTkLabel(master=frame_direita, image=pikachu, text="")
    image_label.place(relx=0.5, rely=0.5, anchor='center')  # Centraliza o label

def limpar_frame(frame):
    for widget in frame.winfo_children():
        widget.place_forget()

def limpar_frame_2(frame):
    for widget in frame.winfo_children():
        widget.pack_forget()

# Função para mostrar a pergunta sobre o gênero
def mostrar_genero():
    limpar_frame(framee2)
    nome_usuario = nome_entry.get()
    print(f"Nome do usuário: {nome_usuario}")  # Armazena o nome do usuário na variável
    # genero_label.place(x=70,y=70)
    genero_label.pack(padx=20,pady=20)
    masculino.place(x=176, y= 70)
    feminino.place(x=176, y= 110)
    

# Função para mostrar a mensagem final para gênero masculino
def selecionar_masculino():
    nome_usuario = nome_entry.get()
    genero_label.pack_forget()
    frase_final.configure(text=f"Ótimo, então você é o {nome_usuario}!")
    frase_final.pack(pady=20)
    masculino.place_forget()
    feminino.place_forget()
    janela.after(2000, mostrar_opcoes)

# Função para mostrar a mensagem final para gênero feminino
def selecionar_feminino():
    nome_usuario = nome_entry.get()
    genero_label.pack_forget()
    masculino.place_forget()
    feminino.place_forget()
    frase_final.configure(text=f"Ótimo, então você é a {nome_usuario}!")
    frase_final.pack(pady=20)
    janela.after(2000, mostrar_opcoes)

# Função para mostrar as opções após a frase final desaparecer
def mostrar_opcoes():
    nome_usuario = nome_entry.get()
    frase_final.pack_forget()
    opcao_label.configure(text=f"{nome_usuario}, escolha como deseja prosseguir:")
    #opcao_label.place(x=50, y=75)
    opcao_label.pack(padx=20,pady=20)
    batalhar.pack(pady=10)
    listar_pokemons.pack(pady=10)

def listar_pokémon():
    limpar_frame_2(framee2)
    ger1.pack(pady=10)
    ger2.pack(pady=10)
    ger3.pack(pady=10)
    ger4.pack(pady=10)
    ger5.pack(pady=10)
    ger6.pack(pady=10)
    botao_voltar.pack(pady=10)
    #data = pd.read_csv('Pokemon.csv')
    # def listar_pokemons_por_geracao(geracao):
    # # Filtrar os Pokémon pela geração selecionada
    #     pokemons_geracao = data[data['Generation'] == geracao]

    # # Criar a lista em formato bullet list
    #     bullet_list = "\n".join([f"- {row['Name']}" for index, row in pokemons_geracao.iterrows()])

    #     return bullet_list

    # # Exemplo de uso
    #     geracao = 1  # O usuário escolhe a geração
    #     lista_pokemons = listar_pokemons_por_geracao(geracao)
    #     print(f"Pokémons da geração {geracao}:\n{lista_pokemons}")

def botão_batalhar():
    listar_pokemons.pack_forget()
    batalhar.pack_forget()
    
def geração_1():
    limpar_frame(frame_direita)
    data = pd.read_csv('Pokemon.csv')

    rolar.pack()
    


    def listar_pokemons_por_geracao(geracao):
        # Filtrar os Pokémon pela geração selecionada
        pokemons_geracao = data[data['Generation'] == geracao]

        # Criar a lista em formato bullet list
        bullet_list = "\n".join([f"• {row['Name']}" for index, row in pokemons_geracao.iterrows()])

        return bullet_list

    # Exemplo de uso
    geracao = 1  # O usuário escolhe a geração
    lista_pokemons = listar_pokemons_por_geracao(geracao)
    #print(f"Pokémons da geração {geracao}:\n{lista_pokemons}")
    mostrar_g_1.configure(text=f"Pokémons da geração {geracao}: \n{lista_pokemons}")
    mostrar_g_1.pack(pady=20)
    

def geração_2():
    limpar_frame(frame_direita)
    data = pd.read_csv('Pokemon.csv')

    def listar_pokemons_por_geracao(geracao):
        # Filtrar os Pokémon pela geração selecionada
        pokemons_geracao = data[data['Generation'] == geracao]

        # Criar a lista em formato bullet list
        bullet_list = "\n".join([f"• {row['Name']}" for index, row in pokemons_geracao.iterrows()])

        return bullet_list

    # Exemplo de uso
    geracao = 2  # O usuário escolhe a geração
    lista_pokemons = listar_pokemons_por_geracao(geracao)
    #print(f"Pokémons da geração {geracao}:\n{lista_pokemons}")
    mostrar_g_1.configure(text=f"Pokémons da geração {geracao}: \n{lista_pokemons}")
    mostrar_g_1.pack(pady=20)

def geração_3():
    limpar_frame(frame_direita)
    data = pd.read_csv('Pokemon.csv')

    def listar_pokemons_por_geracao(geracao):
        # Filtrar os Pokémon pela geração selecionada
        pokemons_geracao = data[data['Generation'] == geracao]

        # Criar a lista em formato bullet list
        bullet_list = "\n".join([f"• {row['Name']}" for index, row in pokemons_geracao.iterrows()])

        return bullet_list

    # Exemplo de uso
    geracao = 3  # O usuário escolhe a geração
    lista_pokemons = listar_pokemons_por_geracao(geracao)
    #print(f"Pokémons da geração {geracao}:\n{lista_pokemons}")
    mostrar_g_1.configure(text=f"Pokémons da geração {geracao}: \n{lista_pokemons}")
    mostrar_g_1.pack(pady=20)

def geração_4():
    limpar_frame(frame_direita)
    data = pd.read_csv('Pokemon.csv')

    def listar_pokemons_por_geracao(geracao):
        # Filtrar os Pokémon pela geração selecionada
        pokemons_geracao = data[data['Generation'] == geracao]

        # Criar a lista em formato bullet list
        bullet_list = "\n".join([f"• {row['Name']}" for index, row in pokemons_geracao.iterrows()])

        return bullet_list

    # Exemplo de uso
    geracao = 4  # O usuário escolhe a geração
    lista_pokemons = listar_pokemons_por_geracao(geracao)
    #print(f"Pokémons da geração {geracao}:\n{lista_pokemons}")
    mostrar_g_1.configure(text=f"Pokémons da geração {geracao}: \n{lista_pokemons}")
    mostrar_g_1.pack(pady=20)

def geração_5():
    limpar_frame(frame_direita)
    data = pd.read_csv('Pokemon.csv')

    def listar_pokemons_por_geracao(geracao):
        # Filtrar os Pokémon pela geração selecionada
        pokemons_geracao = data[data['Generation'] == geracao]

        # Criar a lista em formato bullet list
        bullet_list = "\n".join([f"• {row['Name']}" for index, row in pokemons_geracao.iterrows()])

        return bullet_list

    # Exemplo de uso
    geracao = 5  # O usuário escolhe a geração
    lista_pokemons = listar_pokemons_por_geracao(geracao)
    #print(f"Pokémons da geração {geracao}:\n{lista_pokemons}")
    mostrar_g_1.configure(text=f"Pokémons da geração {geracao}: \n{lista_pokemons}")
    mostrar_g_1.pack(pady=20)

def geração_6():
    limpar_frame(frame_direita)
    data = pd.read_csv('Pokemon.csv')

    def listar_pokemons_por_geracao(geracao):
        # Filtrar os Pokémon pela geração selecionada
        pokemons_geracao = data[data['Generation'] == geracao]

        # Criar a lista em formato bullet list
        bullet_list = "\n".join([f"• {row['Name']}" for index, row in pokemons_geracao.iterrows()])

        return bullet_list

    # Exemplo de uso
    geracao = 6  # O usuário escolhe a geração
    lista_pokemons = listar_pokemons_por_geracao(geracao)
    #print(f"Pokémons da geração {geracao}:\n{lista_pokemons}")
    mostrar_g_1.configure(text=f"Pokémons da geração {geracao}: \n{lista_pokemons}")
    mostrar_g_1.pack(pady=20)

def voltar():
    ger1.pack_forget()
    ger2.pack_forget()
    ger3.pack_forget()
    ger4.pack_forget()
    ger5.pack_forget()
    ger6.pack_forget()
    mostrar_g_1.pack_forget()
    botao_voltar.pack_forget()
    mostrar_opcoes()
    imagem()

def batalha():
    pygame.init()

    #Cria a janela do jogo
    game_width = 500
    game_height = 500
    size = (game_width, game_height)
    game = pygame.display.set_mode(size)
    pygame.display.set_caption("Batalha Pokémon")

    #fundo
    bg = pygame.image.load("bg.jpg").convert_alpha()

    def draw_background():
        scaled_backgound = pygame.transform.scale(bg, (500, 500))
        game.blit(scaled_backgound, (0, 0))



    #escolhendo as cores
    black = (0, 0, 0)
    gold = (218, 165, 32)
    grey = (200, 200, 200)
    green = (0, 200, 00)
    red = (200, 0, 0)
    white = (255, 255, 255)
    dark_green = (124, 227, 25)

    #URL da API

    base_url = "https://pokeapi.co/api/v2"

    class Move():
        
        def __init__(self, url):
            
            #chama a API de movimentos
            
            req = requests.get(url)
            self.json = req.json()
            
            self.name = self.json["name"]
            self.power = self.json["power"]
            self.type = self.json["type"]["name"]
            
            
            


    class Pokemon(pygame.sprite.Sprite):
        
        
        def __init__(self, name, level, x, y ):
            
            pygame.sprite.Sprite.__init__(self)

            #chamar a API pokémon
            req = requests.get(f"{base_url}/pokemon/{name.lower()}")
            self.json = req.json()
            
            #Contar as vitórias do pokemons
            
            
            #definindo o nome e o nível do pokémon
            self.name = name
            self.level =level
            
            #definindo a posição dos sprites na tela
            self.x = x
            self.y = y
            
            #numero de poções restantes
            self.num_potions = 3
            
            self.win = 0
            
            #pega os status dos pokemons da API
            stats = self.json["stats"]
            
            for stat in stats:
                if stat["stat"]["name"] == "hp":
                    self.current_hp  = stat["base_stat"] + self.level
                    self.max_hp = stat["base_stat"] + self.level    
                elif stat["stat"]["name"] == "attack":
                    self.attack = stat["base_stat"]     
                elif stat["stat"]["name"] == "defense":
                    self.defense = stat["base_stat"]
                elif stat["stat"]["name"] == "speed":
                    self.speed = stat["base_stat"]
            
            #definindo o tipo do pokémon
            
            self.types = []
            for i in range(len(self.json["types"])):
                type = self.json["types"][i]
                self.types.append(type["type"]["name"])
                
            #definindo o tamanho dos sprites
            self.size = 150
            
            self.set_sprite("front_default")
            
        def perform_attack(self, other, move):
            
            display_message(f"{self.name} usou {move.name}")
            
            #pausa por dois segundos
            time.sleep(2)
            
            #calcula o dano do ataque
            damage = (2 * self.level + 10) / 250 * self.attack / other.defense * move.power
            
            #Ataque do mesmo tipo bonus
            if move.type in self.types:
                damage *= 1.5
                
            #hit critico (6.75% de chance)
            random_num = random.randint(1, 10000)
            if random_num <= 625:
                damage *= 1.5
                
            #arrendonda o dano para o número inteiro mais próximo
            damage = math.floor(damage)
            
            other.take_damage(damage)
            
            
        def take_damage(self, damage):
            
            self.current_hp -= damage
            
            #o hp não pode ficar abaixo de 0
            
            if self.current_hp < 0:
                self.current_hp = 0
            
            
            
            
        def use_potion(self):
            
            #verifica se exixtem poções restantes
            if self.num_potions > 0:
                
                #adciona 30 de hp mas nao aumenta a vida
                self.current_hp += 50
                if self.current_hp > self.max_hp:
                    self.current_hp = self.max_hp
                    
                #dimnui o número de poções 
                self.num_potions -= 1
                
                
            
        def set_sprite(self, side):
            
            #definir o sprite dos pokémons
            image = self.json["sprites"][side]
            image_stream = urlopen(image).read()
            image_file = io.BytesIO(image_stream)
            self.image = pygame.image.load(image_file).convert_alpha()
            
            #escalar a imagem 
            scale = self.size / self.image.get_width()
            new_width = self.image.get_width() * scale
            new_height = self.image.get_height() * scale
            self.image = pygame.transform.scale(self.image, (new_width, new_height))
            
            
        def set_moves(self):
            
            self.moves = []
            
            #percorre toda a API do movimentos
            for i in range(len(self.json["moves"])):
                
                #pega os movimentos para o jogo
                versions = self.json["moves"][i]["version_group_details"]
                for j in range(len(versions)):
                    version = versions[j]
                    
                    #pega os movimentos apenas da geração 1
                    
                    if version["version_group"]["name"] != "red-blue":
                        continue
                    
                    learn_method = version["move_learn_method"]["name"]
                    if learn_method != "level-up":
                        continue
                    
                    #adiciona movimento se o nívle do pokemon for alto o suficiente
                    level_learned = version["level_learned_at"]
                    if self.level >= level_learned:
                        move = Move(self.json["moves"][i]["move"]["url"])
                        
                        #adicionar apenas movimentos de ataque
                        if move.power is not None:
                            self.moves.append(move)
                            
            #seleciona 4 movimentos aleatórios
            if len(self.moves) > 4:
                self.moves = random.sample(self.moves, 4)
                        
                
            
            
        def draw(self, alpha = 255):
            
            sprite = self.image.copy()
            transparency = (255, 255, 255, alpha)
            sprite.fill(transparency, None, pygame.BLEND_RGBA_MULT)
            game.blit(sprite, (self.x, self. y))
            
        def draw_hp(self):
            
            #mostra a barra de vida
            bar_scale = 200 // self.max_hp
            for i in range(self.max_hp):
                bar = (self.hp_x + bar_scale * i, self.hp_y, bar_scale, 20) 
                pygame.draw.rect(game, red, bar)
                
            for i in range(self.current_hp):
                bar = (self.hp_x + bar_scale * i, self.hp_y, bar_scale, 20)
                pygame.draw.rect(game,green,bar)
                
            #Mostra o número da vida
            font = pygame.font.Font(pygame.font.get_default_font(), 16)
            text = font.render(f"HP: {self.current_hp} / {self.max_hp}", True, black)
            text_rect = text.get_rect()
            text_rect.x = self.hp_x
            text_rect.y = self.hp_y + 30
            game.blit(text, text_rect)
                
            
        def get_rect(self):
            
            return Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        def get_win(self):
            if self.current_hp > 0:
                self.win += 1
                
        
        
    def display_message(message):
        
        #desena uma caixa branca com borda preta
        pygame.draw.rect(game, white, (10, 350, 480, 140 ))
        pygame.draw.rect(game, black, (10, 350, 480, 140), 3)
        
        #exibe a mensagem
        font = pygame.font.Font(pygame.font.get_default_font(), 20)
        text = font.render(message, True, black)
        text_rect = text.get_rect()
        text_rect.x = 30
        text_rect.y = 410
        game.blit(text, text_rect)
        
        pygame.display.update()
        
    def create_button(width, height, left, top, text_cx, text_cy, label):
        
        #posição do cursor do mouse
        mouse_cursor = pygame.mouse.get_pos()
        
        button = Rect(left, top, width, height)
        
        #marca o botão caso o  mouse esteja em cima do botão
        if button.collidepoint(mouse_cursor):
            pygame.draw.rect(game,gold, button)
        else:
            pygame.draw.rect(game, white, button)
            
        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text = font.render(f"{label}", True, black)
        text_rect = text.get_rect(center = (text_cx, text_cy))
        game.blit(text, text_rect)
        
        return button
        
        

            
    #cria os pokémons iniciais
    level = 50
    bulbasaur = Pokemon("Bulbasaur", level, 25, 150)
    charmander = Pokemon("Charmander", level, 175, 150)
    squirtle = Pokemon("Squirtle", level, 325, 150)
    eevee =  Pokemon("Eevee", level,25, 0 )
    pikachu = Pokemon("Pikachu", level, 175, 0 )
    seel = Pokemon("Seel", level, 325, 0)
    ponyta = Pokemon("Ponyta", level, 25, 300)
    poliwag = Pokemon("Poliwag", level, 175, 300)
    pidgeotto = Pokemon("Pidgeotto", level, 325, 300)
    mewtwo = Pokemon("Mewtwo", 70, 325, 470 )
    pokemons = [bulbasaur, charmander, squirtle, eevee, pikachu, seel, ponyta, poliwag, pidgeotto, mewtwo]

    #Pokémon escolhido pelo rival
    player_pokemon = None
    rivel_pokemon = None


    #Loop do jogo
    game_status = "select pokemon"
    while game_status != "quit":

        for event in pygame.event.get():
            if event.type == QUIT:
                game_status = "quit"
                
            #Detecta a tecla pressionada
            if event.type == KEYDOWN:
                
                #jogar de novo
                if event.key == K_s:
                    cont = 0
                    bulbasaur = Pokemon("Bulbasaur", level, 25, 150)
                    charmander = Pokemon("Charmander", level, 175, 150)
                    squirtle = Pokemon("Squirtle", level, 325, 150)
                    eevee =  Pokemon("Eevee", level,25, 0 )
                    pikachu = Pokemon("Pikachu", level, 175, 0 )
                    seel = Pokemon("Seel", level, 325, 0)
                    ponyta = Pokemon("Ponyta", level, 25, 300)
                    poliwag = Pokemon("Poliwag", level, 175, 300)
                    pidgeotto = Pokemon("Pidgeotto", level, 325, 300)
                    mewtwo = Pokemon("Mewtwo", 70, 325, 470 )
                    pokemons = [bulbasaur, charmander, squirtle, eevee, pikachu, seel, ponyta, poliwag, pidgeotto, mewtwo]
                    game_status = "select pokemon"
                
                #sair
                elif event.key == K_n:
                    game_status = "quit"
                    
                
            #dectecta o clique do mouse
            if event.type == MOUSEBUTTONDOWN:
                
                #Cordenadas do clique do mouse
                mouse_click = event.pos
                
                #para selecionar o pokémon
                
                if game_status == "select pokemon":
                    cont = 0
                    #checar qual pokemon foi escolhido
                    
                    for i in range (len(pokemons)):
                        
                        if pokemons[i].get_rect().collidepoint(mouse_click):
                            
                            
                            #seleciona o pokemon do jogador e do rival
                            player_pokemon = pokemons[i]
                            num = random.randint(0,len(pokemons) - 1)
                            rival_pokemon = pokemons[num]
                            while cont < 1:
                                if player_pokemon == rival_pokemon or rival_pokemon.name == "Mewtwo":
                                    num = random.randint(0,len(pokemons))
                                    rival_pokemon = pokemons[num]
                                elif player_pokemon != rival_pokemon and rival_pokemon.name != "Mewtwo":
                                    cont += 1
                            
                            
                            #diminui o nivel do pokemon do rival para deixar o jogo mais facil
                            
                            rival_pokemon.level = int(rival_pokemon.level)
                            
                            #define as coordenadas da barra de vida
                            player_pokemon.hp_x = 275
                            player_pokemon.hp_y = 250
                            
                            rival_pokemon.hp_x = 50
                            rival_pokemon.hp_y = 50
                            
                            game_status = "prebattle"
                            
                            
                elif game_status == "player turn":
                    
                    #verifica se o botão de luta foi clicado
                    if fight_button.collidepoint(mouse_click):
                        game_status = "player move"
                        
                    #verifica se o botão de poção foi clicado
                    if potion_button.collidepoint(mouse_click):
                        
                        if player_pokemon.num_potions == 0:
                            display_message("Não há mais poções restantes!")
                            time.sleep(2)
                            game_status = "player move"
                        
                        else:
                            player_pokemon.use_potion()
                            display_message(f"{player_pokemon.name} usou uma poção!")
                            time.sleep(2)
                            game_status = "rival turn"   
                                            
                                            
                                            
                #selecionar um movimento
                elif game_status == "player move":
                    
                    #verifica qual botão foi clicado
                    for i in range(len(move_buttons)):
                        button = move_buttons[i]
                        
                        if button.collidepoint(mouse_click):
                            move = player_pokemon.moves[i] ###estudar###
                            player_pokemon.perform_attack(rival_pokemon, move)
                            
                            
                            #verifica se o pokémon inimigo foi atordoado
                            if rival_pokemon.current_hp == 0:
                                game_status = "fainted"
                            else:
                                game_status = "rival turn"
            
        #tela para selecionar pokemon
        
        if game_status == "select pokemon":
            
            game.fill(white)
            
            #desenhar os inicias
            for pokemon in pokemons:
                pokemon.draw()
            #desenhar a caixa ao redor do pokémon
            
            mouse_cursor = pygame.mouse.get_pos()
            for pokemon in pokemons:
                
                if pokemon.get_rect().collidepoint(mouse_cursor):
                    pygame.draw.rect(game, black, pokemon.get_rect(), 2)
            
            pygame.display.update()
            
        #pega os movimentos da API e reposiciona os pokémons
        if game_status == "prebattle":
            
            #desenha o pokémon selecionado
            game.fill(white)
            player_pokemon.draw()
            pygame.display.update()
            
            player_pokemon.set_moves()
            rival_pokemon.set_moves()
            
            #reposiciona os pokémons
            player_pokemon.x = -50
            player_pokemon.y = 100
            rival_pokemon.x = 250
            rival_pokemon.y = -50
            
            #muda o tamanho dos sprites
            player_pokemon.size = 300
            rival_pokemon.size = 300
            player_pokemon.set_sprite("back_default")
            rival_pokemon.set_sprite("front_default")
            
            game_status = "start battle"
            
        #começa luta
        if game_status == "start battle":
            
            #rival lança o seu pokemon
            alpha = 0
            
            while alpha < 255:
                
                draw_background()
                rival_pokemon.draw(alpha)
                display_message(f"O Rival mandou {rival_pokemon.name}!")
                
                alpha += 0.2
                
                pygame.display.update()
            
            #pausa por um segundo
            time.sleep(1)
            
            #jogador lançã o seu pokémons
            alpha = 0
            
            while alpha < 255:
                draw_background()
                rival_pokemon.draw()
                player_pokemon.draw(alpha)
                display_message(f"Vai {player_pokemon.name}!")
                alpha += 0.2
                
                pygame.display.update()
                
            #desenha a barra de vida
            player_pokemon.draw_hp()
            rival_pokemon.draw_hp()
            
            #determina quem joga primeiro
            if rival_pokemon.speed > player_pokemon.speed:
                game_status = "rival turn"
            else:
                game_status = "player turn"
            
            pygame.display.update()
            
            #Pausa por um segundo
            
            time.sleep(1)
            
        #Mostra o botão de luta e de usar poção
        if game_status == "player turn":

            draw_background()
            player_pokemon.draw()
            rival_pokemon.draw()
            player_pokemon.draw_hp()
            rival_pokemon.draw_hp()
            
            #cria o botao de luta e de poção
            fight_button = create_button(240, 140, 10, 350, 130, 412, "Lutar")
            potion_button = create_button(240, 140, 250, 350, 370, 412, f"Use uma poção ({player_pokemon.num_potions})")

            #desenha a borda preta
            pygame.draw.rect(game, black, (10, 350, 480, 140), 3)
            
            pygame.display.update()
            
            
        #mostra os botões de ataque
        if game_status == "player move":
            draw_background()
            player_pokemon.draw()
            rival_pokemon.draw()
            player_pokemon.draw_hp()
            rival_pokemon.draw_hp()
            
            move_buttons = []
            for i in range(len(player_pokemon.moves)):
                move = player_pokemon.moves[i]
                button_width = 240
                button_height = 70
                left = 10 + i % 2 * button_width
                top = 350 + i // 2 * button_height 
                text_center_x = left + 120
                text_center_y = top + 35
                button = create_button(button_width, button_height, left, top, text_center_x, text_center_y, move.name.capitalize())
                move_buttons.append(button)
                
            #desenha a borda preta
            pygame.draw.rect(game, black, (10, 350, 480, 140), 3)
            
            pygame.display.update()
            
        #O rival seleciona um movimento aleatório para usar
        if game_status == "rival turn":
            
            draw_background()
            player_pokemon.draw()
            rival_pokemon.draw()
            player_pokemon.draw_hp()
            rival_pokemon.draw_hp()
            
            display_message("")
            time.sleep(2)
            
            #Seleciona um movimento aleatório
            move = random.choice(rival_pokemon.moves)
            rival_pokemon.perform_attack(player_pokemon, move)
            
            #verifica se o pokémon foi derrotado
            if player_pokemon.current_hp == 0:
                game_status = "fainted"
            else:
                game_status = "player turn"
                
            pygame.display.update()
            
        #um dos pokémons foi derrotado
        if game_status == "fainted":
            
            alpha = 255
            while alpha > 0:
                
                draw_background()
                player_pokemon.draw_hp()
                rival_pokemon.draw_hp()
                
                #verifica qual pokémon foi derrotado
                if rival_pokemon.current_hp == 0:
                    player_pokemon.draw()
                    rival_pokemon.draw(alpha)
                    display_message(f"{rival_pokemon.name} foi derrotado!")
                else:
                    
                    player_pokemon.draw(alpha)
                    rival_pokemon.draw()
                    display_message(f"Seu {player_pokemon.name} foi derrotado!")
                alpha -= 4
                
                pygame.display.update()
            
            player_pokemon.get_win()
            rival_pokemon.get_win()
                
            game_status = "gameover"
            
        #tela de game over
        if game_status == "gameover":
            for pokemon in pokemons:
                pokemon.win
                print(f"{pokemon.name} teve: {pokemon.win} vitóras")
            display_message("Jogar de novo (S/N)?")
            
                
    pygame.quit()


# Criando frame da esquerda
frame_esquerda = ctk.CTkFrame(master=janela, width=770, height=2000, fg_color='black')
frame_esquerda.pack_propagate(False)
frame_esquerda.pack(side='left')

frame_direita = ctk.CTkFrame(master=janela, width=770, height=2000, fg_color='black')
frame_direita.pack_propagate(False)
frame_direita.pack(side='right')

framee2 = ctk.CTkFrame(master=frame_esquerda, width=500, height=500, fg_color='black')
framee2.pack_propagate(False)
framee2.place(relx=0.5, rely=0.5, anchor="center")
imagem()

rolar = ctk.CTkScrollableFrame(master=frame_direita,orientation='vertical',height=800, width=400)

# Frase inicial
inicial = ctk.CTkLabel(master=framee2,
                    text="Olá! Eu sou o professor Carvalho!", 
                    wraplength=400, 
                    text_color=azul_claro,
                    font=("Cambria", 25,'bold'),)
inicial.place(x=13,y=35)
#inicial.place(x=315,y=480)
inicial2 = ctk.CTkLabel(master=framee2,
                    text="Antes de começarmos nossa jornada, me diga qual é o seu nome:", 
                    wraplength=500, 
                    text_color=azul2,
                    font=("Verdana", 13),)
inicial2.place(x=13,y=65)

# Caixa de texto para o nome
nome_entry = ctk.CTkEntry(master=framee2, textvariable=nome, placeholder_text="Nome",width=200)
nome_entry.place(x=15,y=120)

# Gênero
genero_label = ctk.CTkLabel(master=framee2, text="Selecione o gênero:",  font=("Cambria", 25),wraplength=300, text_color='#f0be00')
masculino = ctk.CTkButton(master=framee2, text="Masculino", command=selecionar_masculino,fg_color='black',
                      hover_color=laranja,
                      font=("Verdana", 15),
                      border_color=azul_claro,
                      border_width=1)
feminino = ctk.CTkButton(master=framee2, text="Feminino", command=selecionar_feminino,fg_color='black',
                      hover_color=laranja,
                      font=("Verdana", 15),
                      border_color=azul_claro,
                      border_width=1)

# Botão que chama a função para mostrar a pergunta sobre o gênero
botao = ctk.CTkButton(master=framee2, 
                      text="Enviar", 
                      fg_color='black',
                      hover_color=azul2,
                      command=mostrar_genero,
                      font=("Verdana", 15),
                      border_color=azul_claro,
                      border_width=1)
botao.place(x=13,y=170)
#botao.pack(pady=20)

# Frase final que será exibida após selecionar o gênero
frase_final = ctk.CTkLabel(master=framee2, text="", wraplength=450,font=("Cambria", 25),text_color='#f0be00' )
#frase_final.pack(padx=20,pady=20)

# Label para mostrar as opções após a frase final
opcao_label = ctk.CTkLabel(master=framee2, text="", wraplength=450, font=("Cambria",25), text_color=cinza)

# Botões para as opções
batalhar = ctk.CTkButton(master=framee2, text="Batalhar", command=batalha, fg_color='black',border_color='white',border_width=1, hover_color=roxo, font=('Verdana', 13))
listar_pokemons = ctk.CTkButton(master=framee2, text="Listar Pokémon", command=listar_pokémon,fg_color='black',border_color='white',border_width=1, hover_color=roxo, font=('Verdana', 13))



# image_path = "assets/pikachu.png"  # Altere para o caminho da sua imagem
# image = Image.open(image_path)
# image = image.resize((500, 500))  # Redimensiona a imagem, se necessário
# photo = ImageTk.PhotoImage(image)

# # Cria um label dentro do frame e adiciona a imagem a ele
# image_label = ctk.CTkImage(master=frame_direita, image=photo)
# #image_label.pack(pady=20, padx=20)
# image_label.place(relx=0.5, rely=0.5, anchor='center')

#selecionar geração
ger1 = ctk.CTkButton(master=framee2, text="Geração 1", command=geração_1, fg_color='black', hover_color=verde,border_color='white',border_width=1,font=('Verdana', 15))
ger2 = ctk.CTkButton(master=framee2, text="Geração 2", command=geração_2, fg_color='black', hover_color=azul_escuro,border_color='white',border_width=1,font=('Verdana', 15))
ger3 = ctk.CTkButton(master=framee2, text="Geração 3", command=geração_3, fg_color='black', hover_color=roxo,border_color='white',border_width=1,font=('Verdana', 15))
ger4 = ctk.CTkButton(master=framee2, text="Geração 4", command=geração_4, fg_color='black', hover_color=vermelho,border_color='white',border_width=1,font=('Verdana', 15))
ger5 = ctk.CTkButton(master=framee2, text="Geração 5", command=geração_5, fg_color='black', hover_color=azul_claro,border_color='white',border_width=1,font=('Verdana', 15))
ger6 = ctk.CTkButton(master=framee2, text="Geração 6", command=geração_6, fg_color='black', hover_color=laranja,border_color='white',border_width=1,font=('Verdana', 15))

botao_voltar = ctk.CTkButton(master=framee2, text="Voltar", command=voltar, fg_color='black', hover_color=amareloclaro,border_color='white',border_width=1,font=('Verdana', 15))

mostrar_g_1 = ctk.CTkLabel(master=rolar, text="", wraplength=300, font=('Cambria', 18))
# mostrar_g_2 = ctk.CTkLabel(master=frame_direita, text="", wraplength=300)
# mostrar_g_3 = ctk.CTkLabel(master=frame_direita, text="", wraplength=300)
# mostrar_g_4 = ctk.CTkLabel(master=frame_direita, text="", wraplength=300)
# mostrar_g_5 = ctk.CTkLabel(master=frame_direita, text="", wraplength=300)
# mostrar_g_6 = ctk.CTkLabel(master=frame_direita, text="", wraplength=300)


# Definir cor de fundo


janela.configure(fg_color='black')

janela.mainloop()
