from datetime import date
import datetime

#Greetings function to greet at the time of entry 
def Greetings(name):
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print('Good Morning!',name)
    
    elif hour>=12 and hour<18:
        print('Good Afternoon!',name)

    else:
        print('Good Evening!',name)
# Greetings func end
             
today = date.today()
format_date = today.strftime('%B %d, %Y')
hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute

print('Hello I am Phoenix. Welcome to Harsh GPT 1.0 !!!')
print()
name = input('Please tell me your name !!! : ')
Greetings(name)
Query = ''

print('Ask me your query and I will try to give solution to it.')
while True:
    print(name," : ",end="")
    Query = input()
    if 'bye' in Query.lower():
        print('Phoenix : Thank you for using me. Am always here to assist you')
        break

    elif 'exit' in Query.lower():
        print('Phoenix : Thank you for using me. Am always here to assist you')
        break

    elif 'see you' in Query.lower():
        print('Phoenix : Thank you for using me. Am always here to assist you')
        break

    elif 'time' in Query.lower():
        print('Phoenix : The time is',hour,'hour ',end='')
        print('and',minute,'minutes')
        print()

    elif 'weather today' in Query.lower():
        print('Phoenix : Weather today is quite good and overall the day will be good not too sunny !')
        print()
    
    elif 'date' in Query.lower():
        print('Today\'s date is ',format_date)
        print()

    elif 'pm of india' in Query.lower():
        print('Phoenix : The Prime minister of India is : Shree Narendra Modi')
        morepm = input('do you want to know more about him ?(y/n) : ')
        if morepm == 'Y' or morepm == 'y':
            print('Phoenix : Narendra Modi was born in Gujarat and he became the prime minister of India in 2014. He did many good things for the betterment of the society...')
            print()

    elif 'joke' in Query.lower():
        print('Phoenix : What did one Ocean said to another ?')
        print('      nothing it just waved ',chr(128515))
        print()

    elif 'html' in Query.lower():
        print('Phoenix : Html stands for Hyper Text Markup Language.')
        morehtml = input('      Do you want to know more about html?(y/n) : ')
        if morehtml == 'y' or morehtml == 'Y':
            print('Phoenix : Html is used to create web pages which can be displayed using web browsers. Html have tags to classify elements further Css and Js are used to make it more interactive...')
            print()
    
    elif 'css' in Query.lower():
        print('Phoenix : Css stands for Cascading Style Sheets. ')
        morecss = input('Want to know more about Css? (y/n) : ')
        if morecss == 'y' or morecss == 'Y':
            print('Phoenix : Css is used to style a webpage created by Html. This helps the developer make the webpage more attractive and beautiful. There are properties in Css to make things work properly')
            print()

    elif 'c language' in Query.lower():
        print('Phoenix : C Language is one of the oldest computer languages made by Dennis Ritchie at Bell laboratories')
        morec = input(' do you want to know more about C ? (y/n) : ')
        if morec == 'y' or morec == 'Y':
            print('Phoenix : The C language is also known as the mother of all languages as it becomes easy to learn any other language if we know C language.')
            print()

    elif 'python' in Query.lower():
        print('Phoenix : Python was made by Guido Van Rossum at Centrum Wiskunde & Informatica (CWI)')
        morepy = input(' Do you want to know more about python ?(y/n) : ')
        if morepy == 'y' or morepy == 'Y':
            print('Phoenix : While you may know python as a large snake , the name of python programming language comes from an old BBC television comedy sketch series called "Monty Python\'s flying circus"')
            print()

    elif 'c++' in Query.lower():
        print('Phoenix : C++ was developed by Danish computer scientist Bjarne Stroustrap as an extension to C language at the Bell laboratories')
        morecpp = input('do you want to know more about C++ ?(y/n) : ')
        if morecpp == 'y' or morecpp == 'Y':
            print('Phoenix : C++ is a general purpouse programming language (GPL) that is used to build software. C++ is an object oriented programming language, which means it emphasizes using data fiels with unique attributes (objects) rather than logic or functions.')
            print()

    elif 'java' in Query.lower():
        print('Phoenix : Java was developed by James Gosling at Sun microsystems .')
        morejava = input('do you want to know more about Java ?(y/n)')
        if morejava == 'y' or morejava == 'Y':
            print("Phoenix : Java is a class based , object oriented programming language designed to have as few implementation dependencies as possible. ")
            print()

    else:
        print('Phoenix : I don\'t have answer for that but it can be covered in my future versions !')
        print('          I am extremely sorry')