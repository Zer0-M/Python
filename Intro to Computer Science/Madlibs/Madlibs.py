import random
#Word Banks(cite http://www.studentswriters.reikiflow.net/?p=995)
Names=['John F. Kennedy', 'Serena Williams', 'Thomas Edison', 'Arnold Schwarzenegger', 'Shadow Moon', 'Nikola Tesla', 'Samurai Jack', 'Timmy Turner', 'Bruce Wayne', 'Oswald Cobblepot', 'Clark Kent', 'Alfred Borden', 'Eleven', 'Chuck Norris']
Places=['Gotham City', 'Metropolis', 'Atlantis', 'Springfield', 'Hollywood', 'Castle Rock', 'Riverdale', 'Pandora', 'Tatooine']
Noun=['factory reset button', 'idiot', 'toaster', 'legend', 'death wish', 'therapy', 'french chef', 'antidepressant drug', 'candlestick maker', 'brethren', 'national security agency', 'useless brakes', 'international law enforcement agency', 'sound barrier', 'mad cow disease']
Verb=['surround', 'stab', 'return', 'medicate', 'blindside', 'boogie', 'flap', 'trip', 'swat', 'suck in', 'harasses', 'traps', 'snoops', 'explode', 'scatter', 'challenge', 'fight', 'bury', 'splatter', 'smacks']
Adjective=['dead', 'hairless', 'sadistic', 'metal', 'wild', 'domesticated', 'abnormal', 'medicated', 'cocky', 'vengeful', 'sinister', 'costumed', 'cowardly', 'haunting', 'startled', 'alcoholic', 'demanding', 'shivering', 'offensive']
print 'Welcome to Madlibs\nMade by Mohammed Jamil\n'
def extractText(file):
    source=open(file,'r')
    content=source.read()
    
    content+=' '
    content=content.replace('.',' .')
    content=content.replace(',',' ,')
    content=content.replace('?',' ?')
    content=content.replace('!',' !')
    return content


def extractBlanks(story):
    spacePos=story.find(' ')
    gatherer=[]
    while story != '':
        word=story[:spacePos]
        if word.count('*')==1:
            gatherer+=[word]
        story=story[spacePos+1:]
        spacePos=story.find(' ')
    return gatherer


def gatherWords(toBeReplaced):
    filledin=[]
    if raw_input('''do you want to input the words yourself?[Y/N]
if not the Madlib will be filled using a built in word database: ''')=='Y':
        for blank in toBeReplaced:
       
            if blank == 'noun*':
                filledin+=[raw_input('noun ')]
            elif blank == 'verb*':
                filledin+=[raw_input('verb ')]
            elif blank == 'adjective*':
                filledin+=[raw_input('adjective ')]
            elif blank == 'name*':
                filledin+=[raw_input('name ')]
            elif blank == 'place*':
                filledin+=[raw_input('place ')]
    else:
        for blank in toBeReplaced:
            if blank == 'noun*':
                filledin+=[random.choice(Noun)]
            elif blank == 'verb*':
                filledin+=[random.choice(Verb)]
            elif blank == 'adjective*':
                filledin+=[random.choice(Adjective)]
            elif blank == 'name*':
                filledin+=[random.choice(Names)]
            elif blank == 'place*':
                filledin+=[random.choice(Places)]
            
    return filledin
            

def fillBlanks(story,fillers):
    spacePos=story.find(' ')
    filledinstory=''
    pos=0
    while story != '':
        word=story[:spacePos]
        if word.count('*')==1:
            filledinstory+=fillers[pos] +' '
            pos+=1
        else:
            filledinstory+=word+' '
        story=story[spacePos+1:]
        spacePos=story.find(' ')
    return filledinstory
    


def outputstory(file, filledin):
    file=file.replace('.txt','')
    filledin=filledin.replace(' .','.')
    filledin=filledin.replace(' ,',',')
    filledin=filledin.replace(' ?','?')
    filledin=filledin.replace(' !','!')
    output=open(file+'_filled.txt','w',0)
    output.write(filledin+'\n')
    
def MadLibs(file):
    tofill=gatherWords(extractBlanks(extractText(file)))
    filledinstory=fillBlanks(extractText(file), tofill)
    outputstory(file,filledinstory)
    return filledinstory
def personalStory():
    filesToBeFilled=[]
    gatherer=''
    file='  '
    while file != '':
        file=raw_input(''' Do you want to use your own story? Type the filename(it has to be a text file) with extension. If you do not want to input press enter: ''')
        if file!= '':
            filesToBeFilled += [file]
    for files in filesToBeFilled:
        gatherer+=MadLibs(files)+'\n'
    return gatherer

print '\n'       
print personalStory()
print '\n'
def end():
    
    if raw_input('Do you want to do more Madlibs?[Y/N]: ')== 'Y':
        return raw_input('Then restart the program again: ')+'\n'
    else:
        return raw_input('Bye')
print end()
        
    

