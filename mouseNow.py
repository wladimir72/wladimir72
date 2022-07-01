#! python

# mouseNow.py - Exibe a posição atual do cursos na tela e padrão RGB do pixel.

import  pyautogui

print('\nPressione CTRL-C para interromper\n')
# Obtém e exibe as coordenadas do mouse.
try:
    while True:
        # Obtem as coordenadas do mouse
        x,y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)     # Cria uma variável string formatada para exibição da coordenada.
        pixelColor = pyautogui.screenshot().getpixel((x,y))                  # Coleta o padrão RGB da imagem que o cursor está.
        positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
        positionStr += ', ' + str(pixelColor[1]).rjust(3)
        positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'

        print(positionStr, end='')
        '''
        Utilize repetição de string para gerar uma string com a
        quantidade de caracteres \b igual ao tamanho da string armazenada em
        positionStr, o que terá o efeito de apagar a string "positionStr" exibida
        previamente.
        '''
        print('\b' * len(positionStr), end='', flush=True)
        '''
        Sempre passe "flush=True" às chamadas a print() que exibam caracteres \b de backspace.
        Caso cotrário, o texto na tela poderá não ser atualizado conforme desejado.
        '''
except KeyboardInterrupt:
    print('\nFinalizado!')
    
        
