import json, jsonpickle
import random



def main():
    print('loading default intents')

    myIntents = {'patterns':
                     {'Hello! How are you': {'sentences': {'hi how are you', 'how are you', 'how are you doing',
                                                           'greetings', 'ello', 'hello', 'hi'},
                                             'words': {'hi': 0, 'are': 0, 'you': 0, 'how': 0, 'doing': 0,
                                                       'greetings': 0, 'ello': 0, 'hello': 0},
                                             'times_called': 0},

                      'Have a good night!': {'sentences': {'goodbye', 'bye', 'good night',
                                                           'see you', 'later'},
                                             'words': {'bye': 0, 'goodbye': 0, 'good': 0, 'you': 0, 'see': 0,
                                                       'later': 0, 'night': 0},
                                             'times_called': 0
                                             }
                      },

                 'times_called': 0
                 }
    dumpIntents = jsonpickle.encode(myIntents)
    with open(r'tagguessing\DMintents.json', 'w') as file:
        json.dump(dumpIntents, file)
