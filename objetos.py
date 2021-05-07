import pygame

class Objetos:

    def __init__(self, image, x, y):

        self.group = pygame.sprite.Group()
        self.personagens = pygame.sprite.Sprite(self.group)
        self.personagens.image = pygame.image.load(image)
        self.personagens.rect = self.personagens.image.get_rect()
        self.personagens.rect[0] = x
        self.personagens.rect[1] = y
        self.movimento_cima = False
        self.movimento_baixo = False
        self.movimento_esquerda = False
        self.movimento_direita = False
        self.teclaenter = False
        self.tiro = False
        self.quadros = 1
        self.marcacao = 0

    def draw(self, janela):
        self.group.draw(janela)

    def animacoes(self, imagem, marcacao, quadros):
        self.marcacao += 1
        if self.marcacao == marcacao:
            self.marcacao = 0
            self.quadros += 1
        if self.quadros > quadros:
            self.quadros = 1
        self.personagens.image = pygame.image.load("arquivos/" + imagem + str(self.quadros) + ".png")

class Nave(Objetos):

    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.contagem_armadura = 5
        self.contagem_discernimento = 0
        self.contagem_resiliencia = 0
        self.contagem_enter = 0

    def movimentacao_nave(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_w:
                self.movimento_cima = True
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_w:
                self.movimento_cima = False
        if self.movimento_cima:
            self.personagens.rect[1]-=10
        else:
            self.personagens.rect[1]+=0

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_s:
                self.movimento_baixo = True
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_s:
                self.movimento_baixo = False
        if self.movimento_baixo:
            self.personagens.rect[1]+=10
        else:
            self.personagens.rect[1]+=0

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:
                self.movimento_esquerda = True
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_a:
                self.movimento_esquerda = False
        if self.movimento_esquerda:
            self.personagens.rect[0]-=10
        else:
            self.personagens.rect[0]+=0

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_d:
                self.movimento_direita = True
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_d:
                self.movimento_direita = False
        if self.movimento_direita:
            self.personagens.rect[0]+=10
        else:
            self.personagens.rect[0]+=0

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                self.teclaenter = True
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_RETURN:
                self.teclaenter = False
        if self.teclaenter:
            self.contagem_enter += 1
        else:
            pass

    def colisao_planetas(self, group, nome):
        nome = nome
        colisao_planetas = pygame.sprite.spritecollide(self.personagens, group, True)
        if nome == "planetainimigos" and colisao_planetas:
            self.contagem_armadura -= 1
            pygame.mixer.init()
            self.som = pygame.mixer.Sound("arquivos/explosao.flac")
            self.som.play()
        if nome == "planetaaliados" and colisao_planetas:
            self.contagem_discernimento += 1
            pygame.mixer.init()
            self.som = pygame.mixer.Sound("arquivos/ponto.wav")
            self.som.play()
        if nome == "aste1" and colisao_planetas:
            self.contagem_armadura -= 1
            pygame.mixer.init()
            self.som = pygame.mixer.Sound("arquivos/explosao.flac")
            self.som.play()
        if nome == "aste2" and colisao_planetas:
            self.contagem_armadura -= 1
            pygame.mixer.init()
            self.som = pygame.mixer.Sound("arquivos/explosao.flac")
            self.som.play()
        if nome == "aste3" and colisao_planetas:
            self.contagem_armadura -= 1
            pygame.mixer.init()
            self.som = pygame.mixer.Sound("arquivos/explosao.flac")
            self.som.play()

    def colisao_asteroides(self, group, name):
        name = name
        colisao_asteroides = pygame.sprite.spritecollide(self.personagens, group, True)
        if (name == "gggg" or name == "ggg" or name == "gg" or name == "g") and colisao_asteroides:
            self.contagem_armadura -= 1
            pygame.mixer.init()
            self.som = pygame.mixer.Sound("arquivos/explosao.flac")
            self.som.play()
        if name == "r" and colisao_asteroides:
            self.contagem_resiliencia += 1
            pygame.mixer.init()
            self.som = pygame.mixer.Sound("arquivos/ponto.wav")
            self.som.play()

class Tiro(Objetos):

    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.ok = False

    def disparo(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_e:
                self.tiro = True
                pygame.mixer.init()
                pygame.mixer.music.set_volume(0.2)
                self.som_tiro = pygame.mixer.Sound("arquivos/tiro.ogg")
                self.som_tiro.play()
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_e:
                self.tiro = False
        if self.tiro:
            print("Tiro",self.tiro)
        else:
            pass

    def colisao_tiro(self, group, nomee):
        nomee = nomee
        colisao_tiro = pygame.sprite.spritecollide(self.personagens, group, False)
        if nomee == "planetainimigos" and colisao_tiro:
            self.personagens.kill()
        if nomee == "planetaaliados" and colisao_tiro:
            self.personagens.kill()

    def colisao_tiroo(self, group, nomee):
        nomee = nomee
        colisao_tiroo = pygame.sprite.spritecollide(self.personagens, group, True)
        if nomee == "gggg" and colisao_tiroo:
            self.personagens.kill()
        if nomee == "ggg" and colisao_tiroo:
            self.personagens.kill()
        if nomee == "gg" and colisao_tiroo:
            self.personagens.kill()
        if nomee == "g" and colisao_tiroo:
            self.personagens.kill()