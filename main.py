'''
This program is coded in python, it's a game called "Wordleee."
I took inspiration from the game "Wordle" which was originally published by The New York Times.
It takes and displays user input on the screen using the pygame package.
You can input/delete letters to make words. The goal is to guess the correct randomized word.
The program will show you which letters you got correct or partially correct.
'''

import pygame
import random
import time
from Storage.wordList import List as word_list

# Constants
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Game settings
BOX_COLORS = {
    "correct": (12, 200, 65),
    "partial": (246, 204, 65),
    "inactive": (121, 124, 128),
    "incorrect": (56, 53, 53)
}

# Creates a new box object with letter, color, and positional properties
class LetterBox:
    def __init__(self, letter, box_color, position_args):
        self.letter = letter
        self.box_color = box_color
        self.position_args = position_args
        
        self.setup_display(self.box_color)

    def draw_box(self):
        py_rect_value = pygame.Rect(self.position_args[0], self.position_args[1], 60, 60)
        pygame.draw.rect(screen, self.box_color, py_rect_value)
        pygame.draw.rect(screen, (0, 0, 0), py_rect_value, 2)
  
    def draw_text(self):
        letter = self.letter.upper()
        text = font.render(letter, True, (255, 255, 255))
        screen.blit(text, (self.position_args[0] + 18, self.position_args[1] + 16))
  
    def setup_display(self, color):
        self.box_color = color
        self.draw_box()
        self.draw_text()
        pygame.display.update()

    def get_letter(self):
        return self.letter

    def set_letter(self, new_letter):
        self.letter = new_letter

    def erase_box(self):
        self.box_color = BOX_COLORS["inactive"]
        self.draw_box()
        self.letter = ""
        pygame.display.update()

# Used when a new game starts. Clears the screen and sets up the game
class WordleeGame:
    def __init__(self):
        self.correct_word = random.choice(word_list)
        self.word_layout = []
        self.current_layout = 0

        self.setup_screen()
        self.input_detection()

    def setup_screen(self):
        # Reset Screen
        screen.fill((255, 255, 255))
        pygame.display.update()
        
        # Set up title
        text = pygame.font.Font('freesansbold.ttf', 65).render("Wordleee", True, (0, 0, 0))
        screen.blit(text, (330, 30))
        pygame.display.update()
    
        y = 150  # Starting y value
    
        for _index1 in range(5):
            x = 310  # Starting x value
            new_list = []
            for _index2 in range(5):
                time.sleep(.1)
                new_box = LetterBox("", BOX_COLORS["inactive"], (x, y))
                new_list.append(new_box)
                x += 70
            self.word_layout.append(new_list)
            y += 70

    def input_detection(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    key = pygame.key.name(event.key)
        
                    if key == "backspace":
                        for i in range(4, -1, -1):
                            value = self.word_layout[self.current_layout][i]
                            if value.get_letter() != "":
                                value.erase_box()
                                break
                        break
    
                    if key == "return":
                        correct = 0
                        count = 0
                        for _i, word_box in enumerate(self.word_layout[self.current_layout]):
                            if word_box.get_letter() != "":
                                count += 1
                        if count < 5:
                            continue
                        for i, word_box in enumerate(self.word_layout[self.current_layout]):
                            time.sleep(.1)
                            if self.correct_word[i] == word_box.get_letter():
                                word_box.setup_display(BOX_COLORS["correct"])
                                correct += 1
                            elif word_box.get_letter() in self.correct_word:
                                word_box.setup_display(BOX_COLORS["partial"])
                            else:
                                word_box.setup_display(BOX_COLORS["incorrect"])
                        if correct >= 5:
                            return
                        self.current_layout += 1
                        print(self.current_layout)
                        if self.current_layout >= 5:
                            return
              
                    if key not in ALPHABET:
                        continue
              
                    for _, word_box in enumerate(self.word_layout[self.current_layout]):
                        if word_box.get_letter() != "":
                            continue

                        word_box.set_letter(key)
                        word_box.setup_display(BOX_COLORS["inactive"])
                        break

def main():
    global screen, font
    
    # Set up pygame window
    pygame.init()
    screen = pygame.display.set_mode((1000, 600), pygame.NOFRAME)
    pygame.display.flip()
    font = pygame.font.Font('freesansbold.ttf', 32)
    
    # Game loop - Initializes a new game when the current game ends
    while True:
        the_game = WordleeGame()
        time.sleep(2)
        screen.fill((255, 255, 255))
        pygame.display.update()
        
        text = pygame.font.Font('freesansbold.ttf', 30).render("The correct word is " + the_game.correct_word, True, (0, 0, 0))
        screen.blit(text, (330, 300))
        pygame.display.update()
        time.sleep(3)
        
if __name__ == "__main__":
    main()
