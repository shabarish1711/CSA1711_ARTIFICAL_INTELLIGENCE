% Student and Teacher Relationship Database

student(rahul, math).
student(priya, science).
student(arun, english).
student(kavin, math).

teacher(ravi, math).
teacher(suresh, science).
teacher(anitha, english).

% Function 1: Find the subject of a student
student_subject(Student, Subject) :-
    student(Student, Subject).

% Function 2: Find the teacher for a subject
subject_teacher(Subject, Teacher) :-
    teacher(Teacher, Subject).

% Function 3: Find the teacher of a student
student_teacher(Student, Teacher) :-
    student(Student, Subject),
    teacher(Teacher, Subject).

% Function 4: Check whether a teacher teaches a student
teaches(Teacher, Student) :-
    student(Student, Subject),
    teacher(Teacher, Subject).
