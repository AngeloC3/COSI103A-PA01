'''
schedule maintains a list of courses with features for operating on that list
by filtering, mapping, printing, etc.
'''

import json

class Schedule():
    '''
    Schedule represent a list of Brandeis classes with operations for filtering
    '''
    def __init__(self,courses=()):
        ''' courses is a tuple of the courses being offered '''
        self.courses = courses

    def load_courses(self):
        ''' load_courses reads the course data from the courses.json file'''
        print('getting archived regdata from file')
        with open("courses20-21.json","r",encoding='utf-8') as jsonfile:
            courses = json.load(jsonfile)
        for course in courses:
            course['instructor'] = tuple(course['instructor'])
            course['coinstructors'] = [tuple(f) for f in course['coinstructors']]
        self.courses = tuple(courses)  # making it a tuple means it is immutable

    def lastname(self,names):
        ''' lastname returns the courses by a particular instructor last name'''
        return Schedule([course for course in self.courses if course['instructor'][1] in names])

    def email(self,emails):
        ''' email returns the courses by a particular instructor email'''
        return Schedule([course for course in self.courses if course['instructor'][2] in emails])

    def term(self,terms):
        ''' email returns the courses in a list of term'''
        return Schedule([course for course in self.courses if course['term'] in terms])

    def enrolled(self,vals):
        ''' enrolled filters for enrollment numbers in the list of vals'''
        return Schedule([course for course in self.courses if course['enrolled'] in vals])

    def subject(self,subjects):
        ''' subject filters the courses by subject '''
        return Schedule([course for course in self.courses if course['subject'] in subjects])

    def coursenum(self,subjects):
        ''' subject filters the courses by subject '''
        return Schedule([course for course in self.courses if course['coursenum'] in coursenums]) # wtf is codenums from
    
    def title(self, phrase):
        ''' filters courses by which ones have phrase in the title 
            case insensitive
            @author Angelo Cataldo
        '''
        return Schedule([course for course in self.courses if phrase.lower() in course['name'].lower()])
    
    def description(self, phrase):
        ''' filters courses by which ones have phrase in the description
            case insensitive
            @author Angelo Cataldo
        '''
        return Schedule([course for course in self.courses if phrase.lower() in course['description'].lower()])

    def independent_study_filter(self, boolean_val):
        ''' Filters courses by whether or not it is an independent study based on the passed boolean
            @author Angelo Cataldo
        '''
        return Schedule([course for course in self.courses if course['independent_study'] == boolean_val])
    def section(self, section, course_name):
        '''
            Filters courses by their name and section
            @author Su Lei Yadanar
        '''
        return Schedule([course for course in self.courses if course_name.lower() in course['name'].lower() and course['section']==section])
    
    def times(self, times):
        ''' filters courses by time period
            @author Andrew Chen
        '''
        return Schedule([course for course in self.courses if course['times'] == times])

    def sort(self,field):
        if field=='subject':
            return Schedule(sorted(self.courses, key= lambda course: course['subject']))
        else:
            print("can't sort by "+str(field)+" yet")
            return self
 
