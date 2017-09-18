"""
Name: Kevin Li
UNI: krl2134
count_all_enrolled_students returns number of unique students in all classes
in a given dictionary, find_invalid_registrations returns a list of students
registered in course_code or lab_code but not both, notify_exam_conflicts 
returns a list of students who are in multiple of the courses specified,
and hold_workshop returns a list of all students who are not registered in
ENGI E1006

"""
def count_all_enrolled_students(d):
    #returns number of unique students in all classes in a given dictionary

    enrolled = []
    for value in d.values():
        for student in value:
            enrolled.append(student)
    
    enrolled = set(enrolled)
    total = len(enrolled)
    
    return total


def find_invalid_registrations(d, course_code, lab_code):
    #returns a list of students in course_code or lab_code but not both

    invalid = []
    for student in d[course_code]:
        if student not in d[lab_code]:
            invalid.append(student)
    
    for student in d[lab_code]:
        if student not in d[course_code]:
            invalid.append(student)

    return invalid
    

def notify_exam_conflict(d, course_codes):
    #returns list of students in multiple of the courses in course_codes

    students = []
    conflicts = []
    for course in course_codes:
        for student in d[course]:
            if student not in students:
                students.append(student)
            else:
                conflicts.append(student)

    return conflicts


def hold_workshop(d):
    #returns a list of all students who are not registered in ENGI E1006

    workshop = []
    for key in d.keys():
        for student in d[key]:
            if "ENGI E1006" in d.keys() and student not in d["ENGI E1006"]:
                workshop.append(student)
    workshop = list(set(workshop))

    return workshop

if __name__ == '__main__':

    d = {}
    d["ENGI E1006"] = ["Shreyas","Vidya","Kelsey","Caro"]
    d["COMS W3157"] = ["Ben","Kelsey","Caro","Yanlin"]
    d["COMS W3158"] = []

    print("Input Dictionary:", d)
    print("Your number of students:", count_all_enrolled_students(d))
    print("Expected number of students:", 6)

    print("Your invalid registrations:", find_invalid_registrations(d,\
"COMS W3157","COMS W3158"))
    print("Expected invalid registrations:", \
["Ben","Kelsey","Caro","Yanlin"])

    print("Your exam conflicts:", notify_exam_conflict(d, \
["COMS W3157","ENGI E1006"]))
    print("Expected exam conflicts:", ["Kelsey","Caro"])

    print("Your workshop participants:", hold_workshop(d))
    print("Expected workshop participants:", ["Ben","Yanlin"])
