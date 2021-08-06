import sys
# This code calculate ccgpa of student
# AREA TO FURTHER BETTER THIS CODE
# 1 A way of printing all courses their unit, scores and  total
# 2 " Your total unit is --- and total score --- is and you GPA is ---"
# 3 A way of accepting both Grade or score
# wriiting and completed on 4 of Aug 2021


def cgpacal():
    try:             # The try block to catch any value error in this code
        totalscore = 0
        gradegot = 0
        print(" WEARNING ANY INCORRECT VALUE WILL CAUSE THIS CODE TO STOP  \n -----------------------------------")

        print(' Let me calculate your CGPA for you \n ************************')
        # Enter the total number of courses taken
        number_of_courses = int(
            input(' How many Courses did you take this semester ? : '))
        print('========================================================')
        # loop to enter the courses one took
        for x in range(number_of_courses):
            class_number = x + 1  # This allow us to see the number of individual course taken
            course1 = input(f"Enter course code number {class_number} : ")
            unit = int(input("Enter course unit : "))
            score = int(input('What did you score : '))
            Grade_A = f'Your score is {score} which is A'
            Grade_B = f'Your score is {score} which is B'
            Grade_C = f'Your score is {score} which is C'
            Grade_D = f'Your score is {score} which is D'
            Grade_F = f'Your score is {score} which is F'

            print('=======================================================')
            # total score obtainable based on course unit
            totalscore += unit*5  # we multiply by 5 because this CGPA work with a 5.0 scale, it can be
            # removed and this code wont be affected, we only need to adjust line 63
            ''' grade range (70 - 100 = 5 points, 60 - 69 = 4 points,
            50 - 59 = 3 points, 45 - 49 = 2 points, lesser than 44 = o points)

            '''
            if score >= 70:
                print(Grade_A)
                print('---------------------------------------------------')
                grade = 5
            elif score < 70 and score >= 60:
                print(Grade_B)
                print('---------------------------------------------------')
                grade = 4
            elif score < 60 and score >= 50:
                print(Grade_C)
                print('---------------------------------------------------')
                grade = 3
            elif score < 50 and score >= 45:
                print(Grade_D)
                print('---------------------------------------------------')
                grade = 2
            else:
                print(Grade_F)
                print('---------------------------------------------------')
                grade = 0

            gradegot += unit*grade
        cgpa = float(gradegot/totalscore * 5)
        # this  * 5 can be removed if the one up is removed to balance the code
        print("Your CGPA is : " + str(cgpa))
    except ValueError:
        print("Invalid we expect a number and got something else")
        print("please Re-run again")
        sys.exit


cgpacal()
