import os
import random
from datetime import datetime

class Guard:

    def __init__(self):
        self.file_data = []
        self.dict_guard = {}

        self.intro = '\nThis is your mid-season attendance update.'

        self.grade_intro = '\nAssuming you grade started at an A (100%), with you attendance factored in, you grade would be a(n) '

        self.unexcused_message = '\nYou have unexcused absences, for each of those your grade is docked 10%.  Please check MBATT and submit the appropriate absence form.\n'
        self.makeup_message = '\nYou have minutes to make up, if you are concerned about making up the time, please come talk to me and we can discuss a plan for you to make up the time.' \
                                '\n\nThe table below describes how your minutes to make up affect your grade, for your reference.'\
                                '\n90 minutes remaining or less = up to one letter grade reduction;'\
                                '\n91­180 minutes = up to two letter grade reduction;'\
                                '\n181-270 minutes = up to three letter grade reduction;'\
                                '\nover 270 minutes remaining = up to four letter grade reduction. '\

        self.message_end = '\n\n\nThanks,\n Julie \n\n GILB'


    def read_file(self):


        filename = "Abscences.csv"

        for line in open(filename, 'r').readlines()[1:]:

            member_x500 = line.split(',')[3]
            dict_member_info = {'name': line.split(',')[0],
                                'minutes missed': float(line.split(',')[1]),
                                'minutes to make up': float(line.split(',')[2]),
                                'x500': line.split(',')[3],
                                'unexcused': int(line.split(',')[4]),
                                'grade': int(100),
                                'grade_letter':'A',
                                'message': ''}

            self.dict_guard[member_x500] = dict_member_info


    def message(self):
        for key in self.dict_guard:
            self.grade(self.dict_guard.get(key))
            un = (str(self.dict_guard.get(key).get('unexcused')))
            min = str(self.dict_guard.get(key).get('minutes to make up'))
            miss = str(self.dict_guard.get(key).get('minutes missed'))
            g = str(self.dict_guard.get(key).get('grade'))
            main_message = 'Hello ' + self.dict_guard.get(key).get('name') + "," + self.intro +\
                            '\n\tMinutes missed: ' + miss+\
                            '\n\tMinutes to make up: ' + min +\
                            '\n\tUnexcused Absences: ' + un +\
                            self.grade_intro + self.dict_guard.get(key).get('grade_letter') + '(' + g + '%)\n'

            if (self.dict_guard.get(key).get('unexcused')):
                main_message = main_message + self.unexcused_message
            elif(self.dict_guard.get(key).get('minutes to make up') > 0):
                main_message = main_message + self.makeup_message
            else:
                main_message = main_message+ '\nYou have no unexcused absences and no minutes to make up, awesome!'
            main_message = main_message + self.message_end


            self.dict_guard.get(key)['message'] = main_message
            print(main_message)



    def grade(self, dict):
        neg = 0
        unexcused = dict.get('unexcused')
        unexcused = unexcused * 10

        mins = dict.get('minutes to make up')

        if (mins <=0):
            neg = unexcused
        elif (mins < 91):
            neg = unexcused + 10
        elif (mins <181):
            neg = unexcused + 20
        elif (mins <271):
            neg = unexcused + 30
        else:
            neg = unexcused + 40

        dict['grade'] = dict.get('grade') - neg

        g = dict.get('grade')
        if (g>=90):
            dict['grade_letter']= 'A'
        elif (g>=80):
            dict['grade_letter'] = 'B'
        elif (g>=70):
            dict['grade_letter'] = 'C'
        elif(g>=60):
            dict['grade_letter'] = 'D'
        else:
            dict['grade_letter'] = 'F'



x = Guard()
x.read_file()
x.message()
