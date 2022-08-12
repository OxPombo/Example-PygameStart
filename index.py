import pygame, sys

# * Importamos as dependências necessárias.

class Jogo(): # * Criamos uma classe onde vamos colocar as definições gerais.

    def __init__(self):
        
        # * Setup Geral:

        pygame.init() # ! Importantíssimo, inicializa TODOS os módulos.

        self.screen = pygame.display.set_mode((1280, 720)) 
        pygame.display.set_caption('Hatey')

        self.clock = pygame.time.Clock()
        # ! Puxamos um objeto clock do pygame import:
        # * Serve para medir o tempo;
        # * Serve para controlar o framerate;

    def run(self):
        

        while True:

    # * Event loop
        # TODO: Event loop é um fluxo de controle de eventos, pode ser visto em várias linguagens de programação, um bom exemplo é o Event Loop do Node.js:
        # TODO -Em que o fluxo é formado por eventos ou alterações de State, chamando callbacks quando são enviados.
        # TODO: No pygame ele "ativa" o evento e chama a rotina (metódo) apropriado para lidar com ele.

            for event in pygame.event.get(): # * Geramos um evento.
            # ? Quando o evento acontece? 
                if event.type == pygame.QUIT: # * Especificamos o tipo de evento e definimos quando ele acontece.
                    pygame.quit() # * Resultado depois da ativação do seu método.
                    sys.exit()

            # TODO: Métodos são rotinas executados por objetos após receberem algo, eles determinam o comportamento dos objetos de uma classe X
            # TODO / Nesse caso o evento ativa o método quando clicamos no X da janela para fecharmos o jogo, executando o mesmo e determinando o comportamento a ser seguido.
            self.screen.fill('black')
            pygame.display.update()
            # *Atualiza a tela, semelhante ao pygame.flip, entretanto, uma versão melhorada já que podemos definir a área que será atualizada.
            # * Portanto, se nenhuma argumento for passado ele atualiza a área inteira, exatamente igual o pygame.flip.

            self.clock.tick(60)
            # * Definimos o limite de velocidade de execução do jogo.   

if __name__ == '__main__':  
    # ! Verificamos se este é o arquivo pai e caso seja...

    # TODO: Arquivo pai é o receptor de TODOS os códigos do projeto, podem existir outros arquivos pai, mas eles vão, no final, serem importados para este aqui!!
    # É mei confuso, eu sei, mas tem um código no meu github que explica bem, se precisarem só olhar lá: https://github.com/OxPombo/ghost
    jogo = Jogo()
    # * 1. Definimos uma igualdade de nome pra classe.
    jogo.run()
    # * 2. Executamos o novo "nome" da class da com o metódo run.