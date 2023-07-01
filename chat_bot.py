#first chatbot in python
""" 
chatbot
steps:
1.input/listen
2.process/decide
3.output/talkback
"""
greet_words=['hi','hello','yo']
bye_word=['bye','tata','hasta la vista']
bad_words=['dog','mf','fuck']

def listen():
    return input("Say something: ")

def decide(command):
    command=command.lower()
    #print command
    #print(command)
    broken_words=command.split(" ")
    #print broken words
    for word in broken_words:
        if word in greet_words:
            talkback("he said greetings")
            break
        elif word in bye_word:
            talkback("he said bye")
            break
        elif word in bad_words:
            talkback("You are a bad guy. Behave yourself")
            break
    

def talkback(response):
    print(response)
    
while(True):
    command=listen()
    decide(command)
