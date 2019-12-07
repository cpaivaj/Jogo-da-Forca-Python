# -*- coding: utf-8 -*-

# Jogo da Forca

import random

board = ['''
>>>>>>>>>>>>>>FORCA<<<<<<<<<<<<<<<

+----+
|    |
     |
     |
     |
     |
==============''', '''

+----+
|    |
0    |
     |
     |
     |
============== ''', '''

+----+
|    |
0    |
|    |
     |
     |
============== ''', '''

  +----+
  |    |
  0    |
 /|    |
       |
       |
============== ''', '''

  +----+
  |    |
  0    |
 /|\   |
       |
       |
============== ''', '''

  +----+
  |    |
  0    |
 /|\   |
 /     |
       |
============== ''', '''

  +----+
  |    |
  0    |
 /|\   |
 / \   |
       |
============== ''']


# Classe
class Hangman:

    # Construtor
    def __init__(self, word):
        self.word = word
        self.max_ammount_attempt = 6
        self.current_attempt = 0
        self.idx_discovered_words = []
        self.wrong_letters = []

    # Adivinha letra
    def guess(self, letter):

        right = False

        for indice, caracter in enumerate(self.word):
            if letter == caracter:
                self.idx_discovered_words.append(indice)
                right = True

        if not right:
            self.wrong_letters.append(letter)
            self.current_attempt += 1

    # Verifica se terminou
    def game_over(self):
        if self.max_ammount_attempt - self.current_attempt == 0:
            return True
        else:
            return False

    # Venceu
    def victory(self):

        # Se a quantidade de letras descobertas for igual a quantidade de letras da palavra, vitoria
        if len(self.idx_discovered_words) == len(self.word):
            return True
        else:
            return False

    # Nao mostra letra no board
    def hide_word(self):

        list_word_visible = list(self.word)

        for idx, carac in enumerate(self.word):
            if idx not in self.idx_discovered_words:
                list_word_visible[idx] = ' _ '
            else:
                list_word_visible[idx] = carac

        word_visible = ''

        for caract in list_word_visible:
            word_visible += caract

        print('Palavra: ' + str(word_visible))

    # Mostra o status do jogo
    def print_game_status(self):
        print('\nVoce possui ' + str(self.max_ammount_attempt - self.current_attempt) + ' tentativas!')


# Busca uma palavra aleatoria
# O strip() remove espacos em branco
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()

    return bank[random.randint(0, len(bank))].strip()


def main():
    # objeto
    game = Hangman(rand_word())

    print('\n******************************************************************')

    print('\nVoce pode errar ate ' + str(game.max_ammount_attempt) + ' vezes. Boa sorte!')

    # Enquanto o jogo nao tiver terminado, print status, solicita letra e le caractere
    while(not game.game_over() and not game.victory()):

        print('\n******************************************************************')

        if game.wrong_letters:
            print('Letras incorretas: ' + str(game.wrong_letters))

        print(board[game.current_attempt])

        game.hide_word()

        letter = input('\nDigite uma letra: ')

        game.guess(letter)

        print('\n******************************************************************')

        # Verifica status
        game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuario
    if game.victory():
        print('\n-----------------------------')
        print('Parabens, Voce venceu')
        print('-----------------------------')
    else:
        print('\n-----------------------------')
        print('Game Over. Voce perdeu')
        print('-----------------------------')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com voce! Agora va estudar!\n')


# Executa
if __name__ == "__main__":
    main()
