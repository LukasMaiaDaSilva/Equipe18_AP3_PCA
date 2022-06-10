import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

            #------------------ TELA - PLAYS ------------------
def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        #NOME - JOGO

        PLAY_NAME = get_font(30).render("QUESTÃO UM ", True, "white")
        PLAY_RECT = PLAY_NAME.get_rect(center=(645, 50))
        SCREEN.blit(PLAY_NAME, PLAY_RECT,)

        ##

        PLAY_QUESTION_ONE = Button(image=pygame.image.load("assets/Question Rect.png"), pos=(640, 150),
                                    text_input="Quais são as variantes do Sars-Cov-2 em circulação?", font=get_font(19), base_color="white", hovering_color="white")

        PLAY_ALTERNATIVA_ONE = Button(image=pygame.image.load("assets/Alternativa Rect.png"), pos=(540, 300),
                                    text_input="A - Alfa, Beta, Delta, Zeta e Ôminicron", font=get_font(10), base_color="white", hovering_color="lightblue")

        PLAY_ALTERNATIVA_TWO = Button(image=pygame.image.load("assets/Alternativa Rect.png"), pos=(540, 450),
                                      text_input="B - Celta, Mega, Fera, Nega e Pokémon", font=get_font(10),base_color="white", hovering_color="lightblue")

        PLAY_ALTERNATIVA_THREE = Button(image=pygame.image.load("assets/Alternativa Rect.png"), pos=(540, 600),
                                      text_input="C - Alfa, Beta, Gama, Delta, Ômicron", font=get_font(10),base_color="white", hovering_color="lightblue")

        for button in [PLAY_QUESTION_ONE, PLAY_ALTERNATIVA_ONE, PLAY_ALTERNATIVA_TWO, PLAY_ALTERNATIVA_THREE]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        PLAY_BACK = Button(image=None, pos=(1140, 660),
                           text_input="VOLTAR", font=get_font(15), base_color="white", hovering_color="lightblue")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if PLAY_ALTERNATIVA_ONE.checkForInput(PLAY_MOUSE_POS):
                    perdeu()
                if PLAY_ALTERNATIVA_TWO.checkForInput(PLAY_MOUSE_POS):
                    perdeu()
                if PLAY_ALTERNATIVA_THREE.checkForInput(PLAY_MOUSE_POS):
                    acertou()

        pygame.display.update()


def play_two():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        # NOME - JOGO

        PLAY_NAME = get_font(30).render("QUESTÃO DOIS ", True, "white")
        PLAY_RECT = PLAY_NAME.get_rect(center=(645, 50))
        SCREEN.blit(PLAY_NAME, PLAY_RECT,)

        PLAY_QUESTION_ONE = Button(image=pygame.image.load("assets/Question Rect.png"), pos=(640, 150),
                                   text_input="Quando foi o primeiro caso de covid-19 no Brasil?", font=get_font(19),
                                   base_color="white", hovering_color="white")

        PLAY_ALTERNATIVA_ONE = Button(image=pygame.image.load("assets/Alternativa Rect.png"), pos=(540, 300),
                                      text_input="A - 26 de fevereiro de 2020", font=get_font(10),
                                      base_color="white", hovering_color="lightblue")

        PLAY_ALTERNATIVA_TWO = Button(image=pygame.image.load("assets/Alternativa Rect.png"), pos=(540, 450),
                                      text_input="B - 27 de janeiro de 2019", font=get_font(10),
                                      base_color="white", hovering_color="lightblue")

        PLAY_ALTERNATIVA_THREE = Button(image=pygame.image.load("assets/Alternativa Rect.png"), pos=(540, 600),
                                        text_input="C - 28 de março de 2020", font=get_font(10),
                                        base_color="white", hovering_color="lightblue")

        for button in [PLAY_QUESTION_ONE, PLAY_ALTERNATIVA_ONE, PLAY_ALTERNATIVA_TWO, PLAY_ALTERNATIVA_THREE]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        PLAY_BACK = Button(image=None, pos=(1140, 660),
                           text_input="VOLTAR", font=get_font(15), base_color="white", hovering_color="lightblue")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if PLAY_ALTERNATIVA_ONE.checkForInput(PLAY_MOUSE_POS):
                    acertou_two()
                if PLAY_ALTERNATIVA_TWO.checkForInput(PLAY_MOUSE_POS):
                    perdeu()
                if PLAY_ALTERNATIVA_THREE.checkForInput(PLAY_MOUSE_POS):
                    perdeu()

        pygame.display.update()


def play_three():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        # NOME - JOGO

        PLAY_NAME = get_font(30).render("QUESTÃO TRÊS ", True, "white")
        PLAY_RECT = PLAY_NAME.get_rect(center=(645, 50))
        SCREEN.blit(PLAY_NAME, PLAY_RECT,)

        PLAY_QUESTION_ONE = Button(image=pygame.image.load("assets/Question Rect.png"), pos=(640, 150),
                                   text_input="Crianças podem ser infectadas pelo coronavírus?", font=get_font(19),
                                   base_color="white", hovering_color="white")

        PLAY_ALTERNATIVA_ONE = Button(image=pygame.image.load("assets/Alternativa Rect.png"), pos=(540, 300),
                                      text_input="A - Não, as crianças são autoimunes", font=get_font(10),
                                      base_color="white", hovering_color="lightblue")

        PLAY_ALTERNATIVA_TWO = Button(image=pygame.image.load("assets/Alternativa Rect.png"), pos=(540, 450),
                                      text_input="B - Sim, porém com menos chances que os adultos", font=get_font(10),
                                      base_color="white", hovering_color="lightblue")

        PLAY_ALTERNATIVA_THREE = Button(image=pygame.image.load("assets/Alternativa Rect.png"), pos=(540, 600),
                                        text_input="C - Sim. As crianças podem ser infectadas com coronavírus, mas os sintomas geralmente são leves", font=get_font(8),
                                        base_color="white", hovering_color="lightblue")

        for button in [PLAY_QUESTION_ONE, PLAY_ALTERNATIVA_ONE, PLAY_ALTERNATIVA_TWO, PLAY_ALTERNATIVA_THREE]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        PLAY_BACK = Button(image=None, pos=(1140, 660),
                           text_input="VOLTAR", font=get_font(15), base_color="white", hovering_color="lightblue")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if PLAY_ALTERNATIVA_ONE.checkForInput(PLAY_MOUSE_POS):
                    perdeu()
                if PLAY_ALTERNATIVA_TWO.checkForInput(PLAY_MOUSE_POS):
                    perdeu()
                if PLAY_ALTERNATIVA_THREE.checkForInput(PLAY_MOUSE_POS):
                    acertou_three()

        pygame.display.update()

def play_four():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        # NOME - JOGO

        PLAY_NAME = get_font(30).render("QUESTÃO QUATRO ", True, "white")
        PLAY_RECT = PLAY_NAME.get_rect(center=(645, 50))
        SCREEN.blit(PLAY_NAME, PLAY_RECT, )

        PLAY_QUESTION_ONE = Button(image=pygame.image.load("assets/Question Rect.png"), pos=(640, 150),
                                   text_input="Quanto tempo o coronavírus permanece ativo em diferentes superfícies?", font=get_font(14),
                                   base_color="white", hovering_color="white")

        PLAY_ALTERNATIVA_ONE = Button(image=pygame.image.load("assets/Alternativa Rect.png"), pos=(540, 300),
                                      text_input="A - O coronavírus não sobrevive à superfícies", font=get_font(10),
                                      base_color="white", hovering_color="lightblue")

        PLAY_ALTERNATIVA_TWO = Button(image=pygame.image.load("assets/Alternativa Rect.png"), pos=(540, 450),
                                      text_input="B - O novo coronavírus pode permanecer no ar por cerca de 40 minutos a até 2 horas e meia", font=get_font(8),
                                      base_color="white", hovering_color="lightblue")

        PLAY_ALTERNATIVA_THREE = Button(image=pygame.image.load("assets/Alternativa Rect.png"), pos=(540, 600),
                                        text_input="C - O coranavírus sobrevive no máximo 1 hora em superfícies",
                                        font=get_font(10),
                                        base_color="white", hovering_color="lightblue")

        for button in [PLAY_QUESTION_ONE, PLAY_ALTERNATIVA_ONE, PLAY_ALTERNATIVA_TWO, PLAY_ALTERNATIVA_THREE]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        PLAY_BACK = Button(image=None, pos=(1140, 660),
                           text_input="VOLTAR", font=get_font(15), base_color="white", hovering_color="lightblue")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if PLAY_ALTERNATIVA_ONE.checkForInput(PLAY_MOUSE_POS):
                    perdeu()
                if PLAY_ALTERNATIVA_TWO.checkForInput(PLAY_MOUSE_POS):
                    acertou_four()
                if PLAY_ALTERNATIVA_THREE.checkForInput(PLAY_MOUSE_POS):
                    perdeu()

        pygame.display.update()

def play_five():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        # NOME - JOGO

        PLAY_NAME = get_font(30).render("QUESTÃO CINCO", True, "white")
        PLAY_RECT = PLAY_NAME.get_rect(center=(645, 50))
        SCREEN.blit(PLAY_NAME, PLAY_RECT, )

        PLAY_QUESTION_ONE = Button(image=pygame.image.load("assets/Question Rect.png"), pos=(640, 150),
                                   text_input="O indivíduo pode ter algum problema no futuro por ter tomado a vacina contra a Covid-19?", font=get_font(10),
                                   base_color="white", hovering_color="white")

        PLAY_ALTERNATIVA_ONE = Button(image=pygame.image.load("assets/Alternativa Rect.png"), pos=(540, 300),
                                      text_input="A - Não há nenhum perigo de a vacina contra a Covid-19 causar problemas", font=get_font(10),
                                      base_color="white", hovering_color="lightblue")

        PLAY_ALTERNATIVA_TWO = Button(image=pygame.image.load("assets/Alternativa Rect.png"), pos=(540, 450),
                                      text_input="B - Sim, o indivíduo pode ter problemas graves", font=get_font(10),
                                      base_color="white", hovering_color="lightblue")

        PLAY_ALTERNATIVA_THREE = Button(image=pygame.image.load("assets/Alternativa Rect.png"), pos=(540, 600),
                                        text_input="C - Sim, o indivíduo pode ter problemas leves",
                                        font=get_font(10),
                                        base_color="white", hovering_color="lightblue")

        for button in [PLAY_QUESTION_ONE, PLAY_ALTERNATIVA_ONE, PLAY_ALTERNATIVA_TWO, PLAY_ALTERNATIVA_THREE]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        PLAY_BACK = Button(image=None, pos=(1140, 660),
                           text_input="VOLTAR", font=get_font(15), base_color="white", hovering_color="lightblue")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if PLAY_ALTERNATIVA_ONE.checkForInput(PLAY_MOUSE_POS):
                    you_win()
                if PLAY_ALTERNATIVA_TWO.checkForInput(PLAY_MOUSE_POS):
                    perdeu()
                if PLAY_ALTERNATIVA_THREE.checkForInput(PLAY_MOUSE_POS):
                    perdeu()

        pygame.display.update()





            # ------------------ TELA - ACERTOU -----------------


def acertou():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill('black')

        PLAY_LOSE = get_font(45).render("VOCÊ ACERTOU", True, "White")
        PLAY_RECT = PLAY_LOSE.get_rect(center=(645, 300))
        SCREEN.blit(PLAY_LOSE, PLAY_RECT, )

        PLAY_CONTINUAR = Button(image=None, pos=(1140, 660),
                           text_input="CONTINUAR", font=get_font(25), base_color="white", hovering_color="lightblue")

        PLAY_CONTINUAR.changeColor(PLAY_MOUSE_POS)
        PLAY_CONTINUAR.update(SCREEN)
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_CONTINUAR.checkForInput(PLAY_MOUSE_POS):
                    play_two()

        pygame.display.update()

def acertou_two():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill('black')

        PLAY_LOSE = get_font(45).render("VOCÊ ACERTOU", True, "White")
        PLAY_RECT = PLAY_LOSE.get_rect(center=(645, 300))
        SCREEN.blit(PLAY_LOSE, PLAY_RECT, )

        PLAY_CONTINUAR = Button(image=None, pos=(1140, 660),
                           text_input="CONTINUAR", font=get_font(25), base_color="white", hovering_color="lightblue")

        PLAY_CONTINUAR.changeColor(PLAY_MOUSE_POS)
        PLAY_CONTINUAR.update(SCREEN)
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_CONTINUAR.checkForInput(PLAY_MOUSE_POS):
                    play_three()

        pygame.display.update()

def acertou_three():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill('black')

        PLAY_LOSE = get_font(45).render("VOCÊ ACERTOU", True, "White")
        PLAY_RECT = PLAY_LOSE.get_rect(center=(645, 300))
        SCREEN.blit(PLAY_LOSE, PLAY_RECT, )

        PLAY_CONTINUAR = Button(image=None, pos=(1140, 660),
                                text_input="CONTINUAR", font=get_font(25), base_color="white",
                                hovering_color="lightblue")

        PLAY_CONTINUAR.changeColor(PLAY_MOUSE_POS)
        PLAY_CONTINUAR.update(SCREEN)
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_CONTINUAR.checkForInput(PLAY_MOUSE_POS):
                    play_four()

        pygame.display.update()


def acertou_four():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill('black')

        PLAY_LOSE = get_font(45).render("VOCÊ ACERTOU", True, "White")
        PLAY_RECT = PLAY_LOSE.get_rect(center=(645, 300))
        SCREEN.blit(PLAY_LOSE, PLAY_RECT, )

        PLAY_CONTINUAR = Button(image=None, pos=(1140, 660),
                                text_input="CONTINUAR", font=get_font(25), base_color="white",
                                hovering_color="lightblue")

        PLAY_CONTINUAR.changeColor(PLAY_MOUSE_POS)
        PLAY_CONTINUAR.update(SCREEN)
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_CONTINUAR.checkForInput(PLAY_MOUSE_POS):
                    play_five()

        pygame.display.update()


def you_win():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        PLAY_LOSE = get_font(30).render("PARABENS, VOCÊ VENCEU O JOGO!", True, "White")
        PLAY_RECT = PLAY_LOSE.get_rect(center=(645, 350))
        SCREEN.blit(PLAY_LOSE, PLAY_RECT,)

        PLAY_BACK = Button(image=None, pos=(140, 660),
                           text_input="VOLTAR", font=get_font(25), base_color="white", hovering_color="white")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

                # ------------------ TELA - PERDEU -----------------
def perdeu():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill('black')

        PLAY_LOSE = get_font(30).render("VOCÊ ERROU", True, "White")
        PLAY_RECT = PLAY_LOSE.get_rect(center=(645, 350))
        SCREEN.blit(PLAY_LOSE, PLAY_RECT,)

        PLAY_BACK = Button(image=None, pos=(140, 660),
                           text_input="VOLTAR", font=get_font(25), base_color="white", hovering_color="white")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(70).render("QUIZ VARIANTES", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 200))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 400),
                             text_input="JOGAR", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                             text_input="SAIR", font=get_font(45), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()