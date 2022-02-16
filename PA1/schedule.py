'''
schedule maintains a list of courses with features for operating on that list
by filtering, mapping, printing, etc.
'''
import json


class Schedule():
    '''
    Schedule represent a list of Brandeis classes with operations for filtering
    '''

    def __init__(self, courses=()):
        ''' courses is a tuple of the courses being offered '''
        self.courses = courses

    def load_courses(self):
        ''' load_courses reads the course data from the courses.json file'''
        print('getting archived regdata from file')
        with open("courses20-21.json", "r", encoding='utf-8') as jsonfile:
            courses = json.load(jsonfile)
        for course in courses:
            course['instructor'] = tuple(course['instructor'])
            course['coinstructors'] = [tuple(f)
                                       for f in course['coinstructors']]
        # making it a tuple means it is immutable
        self.courses = tuple(courses)

    def lastname(self, names):
        ''' lastname returns the courses by a particular instructor last name'''
        return Schedule([course for course in self.courses if course['instructor'][1] in names])

    def email(self, emails):
        ''' email returns the courses by a particular instructor email'''
        return Schedule([course for course in self.courses if course['instructor'][2] in emails])

    def instructor(self, instructors):
        '''
        combine the instructor last name and email seraches into one
        '''
        return Schedule([course for course in self.courses if instructors in course['instructor']])

    def term(self, terms):
        ''' email returns the courses in a list of term'''
        return Schedule([course for course in self.courses if course['term'] in terms])

    def enrolled(self, vals):
        ''' enrolled filters for enrollment numbers in the list of vals'''
        return Schedule([course for course in self.courses if course['enrolled'] in vals])

    def subject(self, subjects):
        ''' subject filters the courses by subject '''
        return Schedule([course for course in self.courses if course['subject'] in subjects])

    def coursenum(self, coursenums):
        ''' subject filters the courses by subject '''
        return Schedule([course for course in self.courses if course['coursenum'] in coursenums])
    
    def code(self, codeval):
        ''' filters by which courses match the code
            case sensitive
            @author Angelo Cataldo
        '''
        return Schedule([course for course in self.courses if codeval in course['code'] ])

    def title(self, phras):
        ''' filters courses by which ones have phrase in the title
            case insensitive
            @author Angelo Cataldo
        '''
        return Schedule([cours for cours in self.courses if phras in cours['name']])

    def description(self, phra):
        ''' filters courses by which ones have phrase in the description
            case insensitive
            @author Angelo Cataldo
        '''
        return Schedule([cou for cou in self.courses if phra in cou['description']])

    def independent_study_filter(self, bool_val):
        ''' Filters courses by whether or not it is an independent study based on the passed boolean
            @author Angelo Cataldo
        '''
        return Schedule([cours for cours in self.courses if cours['independent_study'] == bool_val])

    def limit(self, limit):
        '''
            Filters courses by their class size limit
            @author Su Lei Yadanar
        '''
        return Schedule([course for course in self.courses if course['limit'] == limit])

    def sort(self, field):
        '''
            Check if the filter method exists or not
            @author Joshua Liu
        '''
        if field == 'subject':
            return Schedule(sorted(self.courses, key=lambda course: course['subject']))
        print("can't sort by "+str(field)+" yet")
        return self
