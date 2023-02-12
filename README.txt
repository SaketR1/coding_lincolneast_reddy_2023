FBLA Coding and Programming 2023
School Reward Management System

RUNNING
- To run the program, click on the "dist" folder.
- Then, click on the file named "coding_lincolneast_reddy_2023". It is an application (.exe).
- Data is stored in the text file named "students" (.txt). This does not need to be opened, and should not be edited or moved by the user.
- The folder "build" also does not need to be opened, and should not be edited or moved.
- The program was made using Python Tkinter.

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

AVAILABLE SPORTING EVENTS
Tennis Match
Football Game
Swim Meet
Basketball Game
Track Meet

AVAILABLE NON-SPORTING EVENTS
One-Act Play
Musical
Band Concert
Hour of Code
Science Fair

POINT VALUES FOR EACH EVENT
Tennis Match (10)
Football Game (10)
Swim Meet (10)
Basketball Game (10)
Track Meet (10)
One-Act Play (15)
Musical (15)
Band Concert (5)
Hour of Code (20)
Science Fair (5)

EXAMPLES
The following is a list of example students you may enter so you get a feel for how the program works. You can also create your own.
Juan (9): Tennis Match, Hour of Code, Swim Meet, Basketball Game, Track Meet
Louise (10): Basketball Game, Track Meet, Hour of Code, Science Fair
Satoru (10): Tennis Match, Swim Meet, Basketball Game, Track Meet, Hour of Code, Science Fair, One-Act Play, Musical
Maya (11): Basketball Game, Swim Meet
Omar (12): Track Meet

PRIZES
50 points - Free Attendance to 1 School Event
75 points - 2 Slices of Free Cheese Pizza
100 points - 1 Free School Spirit T-Shirt

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