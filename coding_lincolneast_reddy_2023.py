from tkinter import * 
from tkinter import ttk
from tkinter.ttk import *
import random


global HELP_MENU_TEXT # Text that will be displayed in the help menu
HELP_MENU_TEXT = '''
INPUTTING STUDENTS
- The program is intended to be a miniature version/demo of a school reward system, so there is only space for 5 students.
- It is required that you enter 5 students. When entering a student into the system, it must be in the format "Name (Grade Number): Event, Event".
- You may list an event multiple times if the student attended that event multiple times (e.g. "Juan (9): Tennis Match, Tennis Match").
- You need to click "Update" after updating a student's info. This updates the text file and displays each student's points.

ACCEPTABLE VS. UNACCEPTABLE FORMATS
- You may only enter the available events listed below, and events must be typed exactly as they are written below.
- For example, an acceptable format would be "Juan (9): Tennis Match, Hour of Code, Swim Meet, Basketball Game, Track Meet". 
- An unacceptable format would be "Juan - 9 tennis match / Hour of Code" (Tennis Match written incorectly, and missing parentheses, semicolon, & commas). 
- Please make sure not to leave a space at the end of your input. For example, don't type "Juan (9): Tennis Match "
(there is a space after Tennis Match which may make formatting in certain parts of the program look odd).

GENERATE PRIZE REPORT BUTTON
- When clicked, the program will iterate through each student and check if the student has reached a point threshold
- If so, the student's information and their prize will be appended to string named "prize_report"
- This "prize_report" will be shown in a new window
- If no one has reached a point threshold, "prize_report" will simply say "No one has accumulated enough points to win a prize."

GENERATE RANDOM WINNDERS BUTTON
- When clicked, the program will sort each student into a list based on their grade
- A random student from each grade list will be chosen
- These students will be shown in a new window and will receive free attendance to 1 school event
- If a grade has no students, the new window will indicate that there were no students of that grade in the database

GENERATE TOP STUDENT BUTTON
- When clicked, the program will iterate through each student and find the student(s) with the most points
- The top student(s) will be shown in a new window
- If the top student(s) has/have 0 points, the new window will simply say "No one has accumulated any points."

GENERATE QUARTERLY REPORT BUTTON
- When clicked, the program will sort each student into a list based on their grade, and find the total points each grade has received
- The average points each grade has earned will be calculated by dividing the total grade points by the number of students in that grade
- This information will be displayed in a new window, along with details about each individual student in the full quarterly report
- If there are no students in a grade, then a placeholder element will be appended to that grade's list to avoid a divide by 0 error
'''


root = Tk() #Create main window
root.state('zoomed') #Make the main window full-screen
root.title("Student Reward Management") #Name the window

file = open("students.txt") #Open the text file with all of the students' information
content = file.readlines() #"content" is a list, where each element is a different line/student in the text file


"""
This function calculates and returns the points of the student it's called on
The function iterates through a student's information and adds points if they have attended an event
"index" indicates which line of "students.txt" the student is on
"""
def calculate_points(index):
    
    # The student's information is found and turned into a list, where each element is separated by a comma
    file = open("students.txt")
    content = file.readlines()
    points = 0 #Keeps track of student's points
    split_string = content[index].split(",")

    # For each element in "split_string", see which, if any, event was attended and add the corresponding points
    for element in split_string:
        if("Tennis Match" in element):
            points += 10
        if("Football Game" in element):
            points += 10
        if("Swim Meet" in element):
            points += 10
        if("Basketball Game" in element):
            points += 10
        if("Track Meet" in element):
            points += 10
        if("One-Act Play" in element):
            points += 15
        if("Musical" in element):
            points += 15
        if("Band Concert" in element):
            points += 5
        if("Hour of Code" in element):
            points += 20
        if("Science Fair" in element):
            points += 5
    
    file.close()
    return points


"""
This function updates all students' point labels
The function iterates finds all students' current points, then properly formats the strings
"""
def update():

    # Input Validation: If any student text boxes are left blank, users are asked to fill them in
    if(len(student1_text_box.get()) == 0 or len(student2_text_box.get()) == 0 or len(student3_text_box.get()) == 0 or len(student4_text_box.get()) == 0 or len(student5_text_box.get()) == 0):
        missing_fields = "Please fill out the following field(s):\n"
        if(len(student1_text_box.get()) == 0):
            missing_fields += "Text Box 1\n"
        if(len(student2_text_box.get()) == 0):
            missing_fields += "Text Box 2\n"
        if(len(student3_text_box.get()) == 0):
            missing_fields += "Text Box 3\n"
        if(len(student4_text_box.get()) == 0):
            missing_fields += "Text Box 4\n"
        if(len(student5_text_box.get()) == 0):
            missing_fields += "Text Box 5\n"
        fields_window = Toplevel(root)
        fields_window.title("Missing Fields")
        fields_window = Label(fields_window, text=missing_fields, font=('Sans Serif', 10)).pack(pady=15)
    
    # This part of the function runs if no text boxes are blank
    else:

        # Put the text in the text boxes in "students.txt"
        open('students.txt', 'w').close()
        file = open("students.txt", "a")
        file.write(student1_text_box.get() + "\n")
        file.write(student2_text_box.get() + "\n")
        file.write(student3_text_box.get() + "\n")
        file.write(student4_text_box.get() + "\n")
        file.write(student5_text_box.get())
        file.close()

        # Calculate the points for each student
        # The number indicates which line of the text file the student is on
        student1_points = calculate_points(0)
        student2_points = calculate_points(1)
        student3_points = calculate_points(2)
        student4_points = calculate_points(3)
        student5_points = calculate_points(4)

        # Properly format the string so that the point value always has 3 digits
        # For example, 9 --> 009, 90 --> 090, 900 --> 900
        # This helps other functions retrieve point values 
        if(student1_points >= 0 and student1_points < 10):
            student1_points_str = "00" + str(student1_points)
        elif(student1_points >= 10 and student1_points < 100):
            student1_points_str = "0" + str(student1_points)
        elif(student1_points >= 100 and student1_points < 1000):
            student1_points_str = str(student1_points)
        
        if(student2_points >= 0 and student2_points < 10):
            student2_points_str = "00" + str(student2_points)
        elif(student2_points >= 10 and student2_points < 100):
            student2_points_str = "0" + str(student2_points)
        elif(student2_points >= 100 and student2_points < 1000):
            student2_points_str = str(student2_points)
        
        if(student3_points >= 0 and student3_points < 10):
            student3_points_str = "00" + str(student3_points)
        elif(student3_points >= 10 and student3_points < 100):
            student3_points_str = "0" + str(student3_points)
        elif(student3_points >= 100 and student3_points < 1000):
            student3_points_str = str(student3_points)
        
        if(student4_points >= 0 and student4_points < 10):
            student4_points_str = "00" + str(student4_points)
        elif(student4_points >= 10 and student4_points < 100):
            student4_points_str = "0" + str(student4_points)
        elif(student4_points >= 100 and student4_points < 1000):
            student4_points_str = str(student4_points)
        
        if(student5_points >= 0 and student5_points < 10):
            student5_points_str = "00" + str(student5_points)
        elif(student5_points >= 10 and student5_points < 100):
            student5_points_str = "0" + str(student5_points)
        elif(student5_points >= 100 and student5_points < 1000):
            student5_points_str = str(student5_points)

        # Put the properly formatted student point values in "students.txt"
        open('students.txt', 'w').close()
        file = open("students.txt", "a")
        file.write(student1_text_box.get() + " - " + student1_points_str + "\n")
        file.write(student2_text_box.get() + " - " + student2_points_str + "\n")
        file.write(student3_text_box.get() + " - " + student3_points_str + "\n")
        file.write(student4_text_box.get() + " - " + student4_points_str + "\n")
        file.write(student5_text_box.get() + " - " + student5_points_str)
        file.close()

        # Update all of the labels
        student1_points_label.config(text=student1_points)
        student2_points_label.config(text=student2_points)
        student3_points_label.config(text=student3_points)
        student4_points_label.config(text=student4_points)
        student5_points_label.config(text=student5_points)


"""
This function iterate through each student and check if the student has reached a point threshold
If so, the student's information and their prize will be added to the prize report
"""
def generate_prize_report():
    
    prize_report = "" #Text that will be displayed in the prize report window
    file = open("students.txt")
    content = file.readlines()

    for i in range(len(content)): #For each student in "students.txt"
        points = calculate_points(i) #Calculate the student's points

        # Check which threshold the student has reached, then append the student and their prize to "prize_report"
        if(points >= 50 and points < 75):
            prize_report += "WINS FREE ATTENDANCE TO 1 SCHOOL EVENT --- " + content[i] + "\n"
        elif(points >= 75 and points < 100):
            prize_report += "WINS 2 SLICES OF FREE CHEESE PIZZA --- " + content[i] + "\n"
        elif(points >= 100):
            prize_report += "WINS 1 FREE SCHOOL SPIRIT T-SHIRT --- " + content[i] + "\n"

    if(prize_report == ""): #If no text is in the prize report after iterating through all students
        prize_report += "No one has accumulated enough points to win a prize."

    file.close()
    prize_window = Toplevel(root) #Create new window
    prize_window.title("Prize Report") #Name the window
    prize_label = Label(prize_window, text=prize_report, font=('Sans Serif', 10)).pack(pady=15) #Put the label with the "prize_report" text on the new window


"""
This function generates a random winner from each grade
The function sorts each student into their corresponding grade list, then randomly chooses a student from each grade list
"""
def generate_random_winners():
    
    # Grade lists
    grade_9 = []
    grade_10 = []
    grade_11 = []
    grade_12 = []
    
    file = open("students.txt")
    content = file.readlines()

    # For each student in "students.txt", check what their grade is and sort them into the correct grade list
    for i in range(len(content)):
        if("(9)" in content[i]):
            grade_9.append(content[i])
        elif("(10)" in content[i]):
            grade_10.append(content[i])
        elif("(11)" in content[i]):
            grade_11.append(content[i])
        elif("(12)" in content[i]):
            grade_12.append(content[i])
    
    # If any of the grade lists have no students, note that there are no students in that grade
    if(len(grade_9) == 0):
        grade_9.append("No 9th Graders in Database\n")
    if(len(grade_10) == 0):
        grade_10.append("No 10th Graders in Database\n")
    if(len(grade_11) == 0):
        grade_11.append("No 11th Graders in Database\n")
    if(len(grade_12) == 0):
        grade_12.append("No 12th Graders in Database\n")

    # Randomly select a student from each grade list
    grade_9_random_student = grade_9[random.randint(0, len(grade_9)-1)]
    grade_10_random_student = grade_10[random.randint(0, len(grade_10)-1)]
    grade_11_random_student = grade_11[random.randint(0, len(grade_11)-1)]
    grade_12_random_student = grade_12[random.randint(0, len(grade_12)-1)]

    file.close()
    random_window = Toplevel(root) #Create new window
    random_window.title("Random Winners") #Name the window
    random_winner_text = "The following students win free attendance to 1 school event!\n\n" #Create the text to be displayed
    random_winner_text += grade_9_random_student + "\n" + grade_10_random_student + "\n" + grade_11_random_student + "\n" + grade_12_random_student 
    random_window = Label(random_window, text=random_winner_text, font=('Sans Serif', 10)).pack(pady=15) #Put the label with the text to be displayed on the new window


# This function iterates through all students and finds the student with the most points
def generate_top_student():
    
    top_student = [] #Create top student list (it is a list instead of a string since there may be multiple students with the same highest point acculumation)
    top_student_points = 0 #Keeps track of what the highest point acculumation is
    file = open("students.txt")
    content = file.readlines()

    # For each student in "students.txt", calculate their points
    # If their points are higher than the current top student's points, make this student the new top student
    # If their points are equal to the current top student's points, append them to the "top_student" list
    for i in range(len(content)):
        points = calculate_points(i)
        if(points > top_student_points):
            top_student.clear()
            top_student.append(content[i])
            top_student_points = points
        elif(points == top_student_points):
            top_student.append(content[i])

    # Create the text that will display the top student(s)
    # If the top student has zero points, note that no one has accumulated any points
    # If there is more than 1 top student, note that there are multiple top students
    # Finally, for each student in the top student list, append their information to "top_student_text" to be displayed in the top student window
    top_student_text = ""
    if(top_student_points == 0):
        top_student_text += "No one has accumulated any points."
    else:
        if(len(top_student) > 1):
            top_student_text += "There is more than one student with the highest point accumulation.\n\n"
        for i in top_student:
            top_student_text += i + "\n"

    file.close()
    top_student_window = Toplevel(root) #Create new window
    top_student_window.title("Top Student(s)") #Name the window
    top_student_label = Label(top_student_window, text=top_student_text, font=('Sans Serif', 10)).pack(pady=15) #Put the label with the text to be displayed on the new window


# This function finds and displays the average points for each grade and each student's information
def generate_quarterly_report():
    
    # Create the text to be displayed, grade lists, and grade point trackers
    quarterly_report_text = ""
    grade_9 = []
    grade_9_points = 0
    grade_10 = []
    grade_10_points = 0
    grade_11 = []
    grade_11_points = 0
    grade_12 = []
    grade_12_points = 0

    file = open("students.txt")
    content = file.readlines()

    # For each student in "students.txt", sort them into the correct grade list and add their points to the correct grade point tracker
    for i in range(len(content)):
        if("(9)" in content[i]):
            grade_9.append(content[i])
            grade_9_points += calculate_points(i)
        elif("(10)" in content[i]):
            grade_10.append(content[i])
            grade_10_points += calculate_points(i)
        elif("(11)" in content[i]):
            grade_11.append(content[i])
            grade_11_points += calculate_points(i)
        elif("(12)" in content[i]):
            grade_12.append(content[i])
            grade_12_points += calculate_points(i)

    # Append a placeholder element to any grade lists with no students in order to avoid a divide by zero error later in the function
    if(len(grade_9) == 0):
        grade_9.append("")
    if(len(grade_10) == 0):
        grade_10.append("")
    if(len(grade_11) == 0):
        grade_11.append("")
    if(len(grade_12) == 0):
        grade_12.append("")

    # Find the average points for each grade by dividing the total points from all students in that grade by the number of students in that grade
    # Round to 2 decimal places
    avg_grade_9_points = str(round(grade_9_points / len(grade_9), 2))
    avg_grade_10_points = str(round(grade_10_points / len(grade_10), 2))
    avg_grade_11_points = str(round(grade_11_points / len(grade_11), 2))
    avg_grade_12_points = str(round(grade_12_points / len(grade_12), 2))
    
    # Append the average points for each grade to "quarterly_report_text"
    quarterly_report_text += "Average Number of Points Per 9th Grader: " + avg_grade_9_points + "\n"
    quarterly_report_text += "Average Number of Points Per 10th Grader: " + avg_grade_10_points + "\n"
    quarterly_report_text += "Average Number of Points Per 11th Grader: " + avg_grade_11_points + "\n"
    quarterly_report_text += "Average Number of Points Per 12th Grader: " + avg_grade_12_points + "\n\n"
    quarterly_report_text += "FULL QUARTERLY OUTPUT REPORT OF ALL STUDENTS:\n"

    # For each student in "students.txt", append their information to "quarterly_report_text"
    for i in range(len(content)):
        quarterly_report_text += content[i] + "\n"

    file.close()
    quarterly_report_window = Toplevel(root) #Create new window
    quarterly_report_window.title("Quarterly Output Report") #Name the window
    quarterly_report_label = Label(quarterly_report_window, text=quarterly_report_text, font=('Sans Serif', 10)).pack(pady=15) #Put the label on the new window


# This function opens the help menu
def help():
    global HELP_MENU_TEXT
    help_text = HELP_MENU_TEXT #The help menu includes the text in "HELP_MENU_TEXT" at the top of the program
    help_window = Toplevel(root) #Create new window
    help_window.title("Help Menu") #Name the window
    help_label = Label(help_window, text=help_text, font=('Sans Serif', 10)).pack(pady=15) #Put the label with the help menu text on the new window


# Create all of the student text boxes and labels
student1_text_box = Entry(root, width=70, justify=LEFT, font=('Sans Serif', 20,'bold')) #Create the text box
student1_text_box.delete(0, END) #Delete any text in the text box
student1_text_box.insert(0, content[0][:-7]) #Insert the student's information into the text box, excluding their point value
student1_points = calculate_points(0) #Calculate the student's points
student1_points_label = Label(root, text=student1_points, font=('Sans Serif', 20)) #Create the label and set the label's text to display the student's points

student2_text_box = Entry(root, width=70, justify=LEFT, font=('Sans Serif', 20,'bold'))
student2_text_box.delete(0, END)
student2_text_box.insert(0, content[1][:-7])
student2_points = calculate_points(1)
student2_points_label = Label(root, text=student2_points, font=('Sans Serif', 20))

student3_text_box = Entry(root, width=70, justify=LEFT, font=('Sans Serif', 20,'bold'))
student3_text_box.delete(0, END)
student3_text_box.insert(0, content[2][:-7])
student3_points = calculate_points(2)
student3_points_label = Label(root, text=student3_points, font=('Sans Serif', 20))

student4_text_box = Entry(root, width=70, justify=LEFT, font=('Sans Serif', 20,'bold'))
student4_text_box.delete(0, END)
student4_text_box.insert(0, content[3][:-7])
student4_points = calculate_points(3)
student4_points_label = Label(root, text=student4_points, font=('Sans Serif', 20))

student5_text_box = Entry(root, width=70, justify=LEFT, font=('Sans Serif', 20,'bold'))
student5_text_box.delete(0, END)
student5_text_box.insert(0, content[4][:-6])
student5_points = calculate_points(4)
student5_points_label = Label(root, text=student5_points, font=('Sans Serif', 20))


# Create the buttons, including their text and the function that will be run if the button is clicked
update_button = ttk.Button(root, text= "Update", command=update)
prize_button = ttk.Button(root, text= "Generate Prize Report", command=generate_prize_report)
random_button = ttk.Button(root, text= "Generate Random Winners", command=generate_random_winners)
top_student_button = ttk.Button(root, text= "Generate Top Student", command=generate_top_student)
quarterly_report_button = ttk.Button(root, text= "Generate Quarterly Report", command=generate_quarterly_report)
help_button = ttk.Button(root, text= "Help", command=help)


# Place all GUI elements in their appropriate position
student1_text_box.grid(row=0, column=0, pady=10, padx=10)
student1_points_label.grid(row=0, column=1, pady=10, padx=10)

student2_text_box.grid(row=1, column=0, pady=10, padx=10)
student2_points_label.grid(row=1, column=1, pady=10, padx=10)

student3_text_box.grid(row=2, column=0, pady=10, padx=10)
student3_points_label.grid(row=2, column=1, pady=10, padx=10)

student4_text_box.grid(row=3, column=0, pady=10, padx=10)
student4_points_label.grid(row=3, column=1, pady=10, padx=10)

student5_text_box.grid(row=4, column=0, pady=10, padx=10)
student5_points_label.grid(row=4, column=1, pady=10, padx=10)

update_button.grid(row=5, column=0, pady=10, padx=10)
prize_button.grid(row=5, column=1, pady=10, padx=10)
random_button.grid(row=6, column=1, pady=10, padx=10)
top_student_button.grid(row=7, column=1, pady=10, padx=10)
quarterly_report_button.grid(row=8, column=1, pady=10, padx=10)
help_button.grid(row=9, column=1, pady=10, padx=10)

file.close()
root.mainloop()   