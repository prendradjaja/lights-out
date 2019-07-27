from collections import namedtuple
import random

Question = namedtuple('Question', 'question answer')

questions = [Question(*line.split()) for line in open('data', 'r')]

def main_loop():
    def format_status():
        if first_question:
            return 'Welcome! '
        elif last_correct:
            return ''
        else:
            return 'Incorrect. '

    def format_score():
        return '{}/{}'.format(num_correct, num_asked)

    num_correct = 0
    num_asked = 0
    first_question = True
    last_correct = None
    while True:
        if last_correct or first_question:
            q = random.choice(questions)
        if not first_question:
            print()
        print('? {question} ({status}{score})'.format(
                question=q.question,
                status=format_status(),
                score=format_score()))
        answer = input('> ')
        num_asked += 1
        if answer == q.answer:
            last_correct = True
            num_correct += 1
        else:
            last_correct = False
        first_question = False

if __name__ == '__main__':
    try:
        main_loop()
    except (EOFError, KeyboardInterrupt):
        print()
        exit()
