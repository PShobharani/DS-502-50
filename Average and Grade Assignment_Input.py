# DS502-50 - Introduction to Computer Science
# Shobharani Polasa
# Average and Grade
      
def calc_average (score1,score2,score3,score4,score5):
    return (score1+score2+score3+score4+score5) / 5.0

def determine_grade(score):
    if score >= 90 and score <= 100:
        return "A"
    elif score >= 80 and score <= 89:
        return "B"
    elif score >= 70 and score <= 79:
        return "C"
    elif score >= 60 and score <= 69:
        return "D"
    else:
        return "F"

def repeat ():
    print()
    answer = input("Enter 'yes' if you would like to do another calculation: ")
    if answer.lower() == 'yes':
        main()
    else:
        print('')

def main():
    score1 = float(input("Enter Score 1: "))
    score2 = float(input("Enter Score 2: "))
    score3 = float(input("Enter Score 3: "))
    score4 = float(input("Enter Score 4: "))
    score5 = float(input("Enter Score 5: "))
    print("\nScore " "    Numeric Grade " "   Letter Grade")
    print("-------------------------------------------")
    print("Score 1 :" , "\t",score1, "\t\t",determine_grade(score1))
    print("Score 2 :" , "\t",score2,  "\t\t",determine_grade(score2))
    print("Score 3 :" , "\t",score3,  "\t\t",determine_grade(score3))
    print("Score 4 :" , "\t",score4,  "\t\t",determine_grade(score4))
    print("Score 5 :" , "\t",score5, "\t\t",determine_grade(score5))
    average = calc_average(score1, score2, score3, score4, score5)
    print("Average score:  ",str(average), "\t\t",determine_grade(average))
    repeat()

main()
