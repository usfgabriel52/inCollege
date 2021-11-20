import sqlite3
from OutputApis import MyCollegeTraining_WriteOut


# updates an entry in the Training table
def CompleteTraining(username, course_id):
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    query = """UPDATE Training SET Status = 'Complete' WHERE username = ? AND course_id = ?"""
    c.execute(query, [username, course_id])

    conn.commit()
    conn.close()

    MyCollegeTraining_WriteOut()

    return 0


# returns the title and status of all the Courses in the database given a username
def checkTraining(username):
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()
    query = """SELECT title, status FROM Training T INNER JOIN Courses C ON T.course_id = C.id WHERE username = ?"""
    userTraining = c.execute(query, [username]).fetchall()
    conn.close()
    return userTraining


# adds a Course to the database
def addCourse(title):
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    query = "INSERT INTO Courses(title) VALUES (?);"
    c.execute(query, [title])

    conn.commit()
    conn.close()
    return True


# finds a Course in the database
def findCourse(title):
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    query = "SELECT * FROM Courses WHERE title = ?"
    result = c.execute(query, [title]).fetchone()

    conn.close()

    # if the Course is already in the database, return True. Otherwise, return False
    if result is None:
        return False
    else:
        return True


# get all the Courses in the database
def getAllCourses():
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    query = "SELECT * FROM Courses"
    result = c.execute(query).fetchall()

    conn.close()

    return result


# adds a row to the Training table
def addTrainingEntry(username, course_id):
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    query = "INSERT INTO Training(username, course_id, status) VALUES (?,?,?);"
    c.execute(query, [username, course_id, "Incomplete"])

    conn.commit()
    conn.close()


# looks for a specific course in the Training table
def findCourseInTrainingByTitle(title):
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    result = c.execute("SELECT * FROM Training T INNER JOIN Courses C ON T.course_id = C.id WHERE title = ?", [title]).fetchall()
    conn.close()

    if result == None:
        return False
    else:
        return True
