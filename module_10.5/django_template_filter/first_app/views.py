from django.shortcuts import render
import datetime

# Create your views here.


def home(request):
    data = {       'name': 'Semon',
                   
                   'addTemplate': 1800,
                   'addSlashTemplate': "It adds slash after a apostrophe - It's Semon",
                   'capFirstTemplate': 'semon',
                   'centerTemplate': 'Semon',
                   'cutTemplate': 'string with whitespaces',
                   'dateTemplate': datetime.datetime.now(),
                   'defaultTemplate': "",
                   'dictsortTemplate': [
                       {'name': 'zed', 'age': 19},
                       {'name': 'amy', 'age': 22},
                       {'name': 'joe', 'age': 31},

                   ],
                   'divisiblebyTemplate': 21,
                   'escapeTemplate': "",
                   'filesizeformatTemplate': 123456789,
                   'firstTemplate': ['a', 'b', 'c', 'd'],
                   'joinTemplate': ['a', 'b', 'c', 'd'],
                   'lastTemplate': ['a', 'b', 'c', 'd'],
                   'lengthTemplate': 'string',
                   'linenumbersTemplate': "First Line\nSecond Line\nThird Line",
                   'lowerTemplate': 'Semon Islam',
                   'make_listTemplate': 123,
                   'make_listStringTemplate': 'Mohiminul Islam semon',
                   'randomTemplate': 'this is random',
                   
                   'sliceTemplate': ['a', 'b', 'c', 'd', 'e'],
                   'slugifyTemplate': '    I am     Semon ',
                   'timeTemplate': datetime.datetime.now(),
                   'timesinceTemplate': datetime.datetime.now() - datetime.timedelta(days=5),
                   'titleTemplate': 'i am mohiminul Islam',
              
                   'unordered_listTemplate': ['a', ['b', ['c', 'd']]],
                   'upperTemplate': 'semon ',
                   'wordcountTemplate': 'i am semon , my name is semon',
                   'truncatecharsTemplate': 'i am a graduate',
                   'truncatewordsTemplate': 'i am a student of class 15',
                  
                   'striptagsTemplate': '<b>I</b> <button>love</button> <span>dogs</span>',
               
                   }

    return render(request, 'index.html', data)