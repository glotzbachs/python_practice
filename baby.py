from random import choice

questions = ['Why is the grass green?', 'Why is the sky blue?', 'Where do babies come from?', 'Where are the dinosaurs?']


answer = input(choice(questions)).strip().lower()

while answer != 'just because':
    answer = input('Why?').strip().lower()
    

print('oh')
