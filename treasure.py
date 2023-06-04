import random

def generate_sequence():
    sequence = []
    for i in range(10):
        count = random.randint(1, 20)
        sequence.extend (str(i) * count)
    sequence.extend ('TREASURE')
    sequence.extend([ count *str(i) for i in range(9, -1, -1)])
    return sequence

def create_file(file):
    sequence = generate_sequence()
    with open(file, 'w') as file:
        file.write(''.join((sequence)))

def play_game(filename):
    with open(filename, 'r') as file:
        sequence = file.read()

    start_of_TREASURE = sequence.index('TREASURE')
    end_of_TREASURE = start_of_TREASURE + len('TREASURE')
    turns = 0
    index = 0
    Treasure_not_Found = True 
    print (start_of_TREASURE) 
    while Treasure_not_Found == True:
        move= input ("Where you want to move? [1- forward 2-backwards]")
        turns += 1
        steps = int(input(("How many steps? ")))
        if move == '1':
            index += steps
            if start_of_TREASURE <= index & index <= end_of_TREASURE:
                print("Congratulations! You found the treasure!")
                print("Total turns taken:", turns)
                print("Current character:", sequence[index])
                Treasure_not_Found = False
        elif move == '2':
            index -= steps
            if start_of_TREASURE <= index & index <= end_of_TREASURE:
                print("Congratulations! You found the treasure!")
                print("Total turns taken:", turns)
                print("Current character:", sequence[index])
                Treasure_not_Found = False
        

filename = 'treasure_file.txt'
create_file(filename)
print("The treasure file has been created.")

play_game(filename)    

