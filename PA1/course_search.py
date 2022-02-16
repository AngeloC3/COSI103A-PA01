'''
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
'''

from schedule import Schedule


SCHEDULE = Schedule()
SCHEDULE.load_courses()
# eliminate courses with no students
SCHEDULE = SCHEDULE.enrolled(range(5, 1000))

TOP_LEVEL_MENU = '''
quit
reset
term (filter by term)
course (filter by coursenum, e.g. COSI 103a)
instructor (filter by instructor)
subject (filter by subject, e.g. COSI, or LALS)
title (filter by phrase in title)
description (filter by phrase in description)
limit (filter by the class size limit)
timeofday (filter by day and time, e.g. meets at 11 on Wed)
independent (filter by whether or not a class is an independent study)
'''

# your team should add the following features to the course_search.py script
# course  -- filter by subject/coursenumber
# instructor -- filter by instructor email or lastname
# title -- filter by phrase in the title
# description -- filter by phrase in the description
# Create your own filter (each team member creates their own)

terms = {c['term'] for c in SCHEDULE.courses}


def topmenu():
    '''
    topmenu is the top level loop of the course search app
    '''
    global SCHEDULE
    while True:
        command = input(">> (h for help) ")
        if command == 'quit':
            return
        if command in ['t', 'term']:
            term = input("enter a term:"+str(terms)+":")
            SCHEDULE = SCHEDULE.term([term]).sort('subject')
        elif command in ['h', 'help']:
            print(TOP_LEVEL_MENU)
            print('-'*40+'\n\n')
            continue
        elif command in ['r', 'reset']:
            SCHEDULE.load_courses()
            SCHEDULE = SCHEDULE.enrolled(range(5, 1000))
            continue

        elif command in ['s', 'subject']:
            subject = input("enter a subject:")
            SCHEDULE = SCHEDULE.subject([subject])
        # Angelo's addition:
        elif command in ['independent', 'is', 'independent_study']:
            boolean_val = input("Enter True to see only independent studies or " +
                                "False to only see classes that are not independent studies: ")
            if str(boolean_val).lower() == "true":
                boolean_val = True
            elif str(boolean_val).lower() == "false":
                boolean_val = False
            else:
                print(
                    boolean_val + " is invalid. You must type true or false for this command.")
                continue
            SCHEDULE = SCHEDULE.independent_study_filter(boolean_val)
        # Josh's addition (Question 7) (Angelo wrote many of these functions, like a boss)
        # Filter by subject/coursenumber
        elif command in ['course']:
            code = input("enter a subject code or class number:")
            SCHEDULE = SCHEDULE.code([code])
        elif command in ['i', 'instructor']:
            # email OR lastname
            instructor = input("enter an instructor lastname or email:")
            SCHEDULE = SCHEDULE.instructor([instructor])
        elif command in ['ti', 'title', 'name', 'n']:
            title = input("enter a name:")
            SCHEDULE = SCHEDULE.title([title])
        elif command in ['d', 'description', 'desc']:
            desc = input("enter a name:")
            SCHEDULE = SCHEDULE.description([desc])
        # Su Lei's addition:
        elif command in ['l', 'limit']:
            limit = int(input("enter a class size limit:"))
            SCHEDULE = SCHEDULE.limit(limit)
        else:
            print('command', command, 'is not supported')
            continue

        print("courses has", len(SCHEDULE.courses), 'elements', end="\n\n")
        print('here are the first 10')
        for course in SCHEDULE.courses[:10]:
            print_course(course)
        print('\n'*3)


def print_course(course):
    '''print_course prints a brief description of the course'''
    print(course['subject'], course['coursenum'], course['section'],
          course['name'], course['term'], course['instructor'])


if __name__ == '__main__':
    topmenu()
