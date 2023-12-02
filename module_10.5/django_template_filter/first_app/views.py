from django.shortcuts import render
import datetime

# Create your views here.


def home(request):
    data = {'name': 'Nirob',
                   'age': 25,
                   'addTemplate': 2000,
                   'addSlashTemplate': "I'm Nirob",
                   'capFirstTemplate': 'nirob',
                   'centerTemplate': 'Nirob',
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
                   'lowerTemplate': 'Nirob BARMAN',
                   'make_listTemplate': 123,
                   'make_listStringTemplate': 'Nirob BARMAN',
                   'randomTemplate': 'Nirob BARMAN',
                   #    'sliceTemplate': 'Nirob BARMAN',
                   'sliceTemplate': ['a', 'b', 'c', 'd', 'e'],
                   'slugifyTemplate': '    I am     Nirob BARMAN',
                   'timeTemplate': datetime.datetime.now(),
                   'timesinceTemplate': datetime.datetime.now() - datetime.timedelta(days=5),
                   'titleTemplate': 'i am nirob barman',
                   # 'unordered_listTemplate': ['a', 'b', 'c', 'd'],
                   'unordered_listTemplate': ['a', ['b', ['c', 'd']]],
                   'upperTemplate': 'nirob barman',
                   'wordcountTemplate': 'i am nirob barman',
                   'truncatecharsTemplate': 'i am nirob barman',
                   'truncatewordsTemplate': 'i am nirob barman',
                   #    'truncatewords_htmlTemplate': 'i am nirob barman',
                   'striptagsTemplate': '<b>I</b> <button>love</button> <span>dogs</span>',
                #    'pluralizeTemplate': 1,
                   }

    return render(request, 'index.html', data)