import json
import os.path
import argparse
from random import choice


class Flashcards:
    parser = argparse.ArgumentParser()
    parser.add_argument('--import_from')
    parser.add_argument('--export_to')

    def __init__(self):
        self.actions = '(add, remove, import, export, ask, exit, hardest card, reset stats):'
        self.cards = {}
        self.hardest = {}
        self.arguments = self.parser.parse_args()

    @staticmethod
    def welcome_printer():
        print('Welcome to Flashcards!')

    def term_in_card(self, term):
        if term in self.cards.keys():
            term_2 = input(f'The term "{term}" already exists. Try again:\n')
            return self.term_in_card(term_2)
        return term

    def definition_in_card(self, definition):
        if definition in self.cards.values():
            definition_2 = input(f'The definition "{definition}" already exists. Try again:\n')
            return self.definition_in_card(definition_2)
        return definition

    def card_remover(self, term_name):
        if term_name in self.cards.keys():
            self.cards.pop(term_name)
            print('The card has been removed.')
        else:
            print(f'''Can't remove "{term_name}": there is no such card.''')

    def card_loader(self, file):
        with open(file, 'r') as f:
            python_dict = json.load(f)
        self.cards.update(python_dict)
        print(f'{len(python_dict)} card{"s" if len(python_dict) > 1 else ""} ha{"s" if len(python_dict) == 1 else "ve"} been loaded.')

    def card_saver(self, file):
        json_dict = json.dumps(self.cards)
        with open(file, 'a') as f:
            f.write(json_dict)
        print(f'{len(self.cards)} card{"s" if len(self.cards) > 1 else ""} ha{"s" if len(self.cards) == 1 else "ve"} been saved.')

    def start_importer(self):
        import_file = self.arguments.import_from
        if import_file:
            self.card_loader(import_file)

    def end_exporter(self):
        export_file = self.arguments.export_to
        if export_file:
            self.card_saver(export_file)

    def run(self):
        self.start_importer()
        while True:
            action = input(f'Input the action {self.actions}\n').strip()
            if action == 'exit':
                print('Bye bye!')
                self.end_exporter()
                break

            if action == 'add':
                term = self.term_in_card(input('The card:\n'))
                definition = self.definition_in_card(input('The definition of the card:\n'))
                self.cards[term] = definition
                print(f'The pair ("{term}":"{definition}") has been added.')

            elif action == 'remove':
                remove_card = input('Which card?\n')
                self.card_remover(remove_card)

            elif action == 'ask':
                number_of_cards = int(input('How many times to ask?\n'))
                i = 0
                while i < number_of_cards:
                    i += 1
                    term = choice(list(self.cards.keys()))
                    answer = input(f'Print the definition of "{term}":\n')
                    if answer == self.cards[term]:
                        print('Correct!')
                    elif answer in self.cards.values():
                        self.hardest.setdefault(term, 0)
                        self.hardest[term] += 1
                        print(
                            f'Wrong. The right answer is {self.cards[term]}, but your definition is correct for "{[el for el in self.cards.keys() if self.cards[el] == answer][0]}".')
                    else:
                        self.hardest.setdefault(term, 0)
                        self.hardest[term] += 1
                        print(f'Wrong. The right answer is "{self.cards[term]}".')

            elif action == 'export':
                file_name = input('File name:\n')
                self.card_saver(file_name)

            elif action == 'import':
                file_name = input('File name:\n')
                if os.path.isfile(file_name):
                    self.card_loader(file_name)
                else:
                    print('File not found.')

            elif action == 'hardest card':
                if len(self.hardest) == 0:
                    print('There are no cards with errors.')
                elif list(self.hardest.values()).count(max(list(self.hardest.values()))) == 1:
                    max_value = max(list(self.hardest.values()))
                    print(f'The hardest card is "{[el for el in self.hardest.keys() if self.hardest[el] == max_value][0]}. You have {max_value} errors answering it."')
                else:
                    output = 'The hardest cards are'
                    for key in self.hardest.keys():
                        if self.hardest[key] == max(list(self.hardest.values())):
                            output += f' "{key}",'
                    print(output[:-1])

            elif action == 'reset stats':
                self.hardest = {}
                print('Card statistics have been reset.')

            else:
                print('Invalid action. Try again.')
                return self.run()


flashcard = Flashcards()
flashcard.welcome_printer()
flashcard.run()
