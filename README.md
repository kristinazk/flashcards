# flashcards
## Desctiption
The benefits of flashcards include improving language skills, increasing the ability to compose stories, memorizing, analyzing a problem, and enriching vocabulary. The program has lots of commands, which are explained below. Also, it reads user input from the command-line terminal, and does corresponding actions.
### Usage

#### Python Console commands
* **add** - saves the card to the memory with the mentioned term and the definition.
* **remove** - removes the card from the memory.
* **import** - imports the contents of a specified file.
* **export** - exports the cards saved in the computer memory to a specified file.
* **ask** - asks the definitions for the terms of the cards added to the memory.
* **hardest card** - the program counts all the errors and defines the card you have made most mistakes on.
* **reset stats** - resets all the errors which were made.

#### Command-line terminal commands
* **--import_from**=FILENAME - write the command before running the actual script with the file name which should be present in the directory (JSON format).
* **--export_to**=FILENAME - write the command before running the **exit** command. The program will export all the saved cards into the file you specify and keep it in the directory. You will be able to import it whenever you want.
