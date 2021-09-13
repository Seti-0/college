USE mydb2;

/*
	Task 1
*/

# 1) Count of students
SELECT count(*) FROM students;

# 2) Count of distinct second names
SELECT count(DISTINCT LastName) FROM students;

# 3) Average cost of courses
SELECT AVG(CourseCost) FROM courses;

# 4) Number of students that take EXL20
SELECT count(*) FROM student_courses
WHERE CourseCode = 'EXL20';

# 5) Courses ordered by cost
SELECT * FROM courses
ORDER BY CourseCost;

# 6) Name of courses whose code ends with 20
SELECT CourseName FROM courses
WHERE CourseCode LIKE "%20";

# 7) Average course cost for each student ID
SELECT StudentID, AVG(CourseCost) FROM student_courses
JOIN courses ON courses.CourseCode = student_courses.CourseCode
GROUP BY StudentID;
