# DS502-50 - Introduction to Computer Science
# Shobharani Polasa
# Average and Grade my_random, Chapter 5 - Calculate Average and Grade with Functions V2
# Extra credit

import random as r

def enter_scores(score):
    for x in range(5):
        s=int(input(f'Enter score [x+1]: '))
        score.append(s)
    return score


def calc_average(score):
    total=0
    for x in range(5):
        total+=score[x]
    avg = total/5
    return avg

def determine_grade(score):
        if score>=90 and score<=100:
            grade= 'A'
        elif score>=80 and score<90:
            grade= 'B' 
        elif score>=70 and score<80:
            grade= 'C'
        elif score>=60 and score<70:
            grade= 'D'
        elif score<60 and score>=0:
            grade= 'F'
        return grade


def main():
    question='yes'
    score=[]
    while question=='yes':
        for x in range(5):
            grade=r.randint(1,100)
            score.append(grade)
        print('Score', f'{"Numeric Grade   Letter Grade":>35}')
        print('---------------------------------------------------')
        for y in range(5):
            print(f'score {y}:  {score[y]:>15}',f'{determine_grade(score[y]):>7}')
        
        avg=calc_average(score)
        print(f'Average score: {avg:>10}', f'{determine_grade(avg):>7}')
        print()

        question=input('Enter "yes" if you would like to do another calculation: ')
    print()

main()

