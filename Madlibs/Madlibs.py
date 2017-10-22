import random
#Word Banks(cite http://www.studentswriters.reikiflow.net/?p=995)
Names=['John F. Kennedy', 'Serena Williams', 'Thomas Edison', 'Arnold Schwarzenegger', 'Shadow Moon', 'Nikola Tesla', 'Samurai Jack', 'Timmy Turner', 'Bruce Wayne', 'Oswald Cobblepot', 'Clark Kent', 'Alfred Borden', 'Eleven', 'Chuck Norris']
Places=['Gotham City', 'Metropolis', 'Atlantis', 'Springfield', 'Hollywood', 'Castle Rock', 'Riverdale', 'Pandora', 'Tatooine']
Noun=['factory reset button', 'idiot', 'toaster', 'legend', 'death wish', 'therapy', 'french chef', 'antidepressant drug', 'candlestick maker', 'brethren', 'national security agency', 'useless brakes', 'international law enforcement agency', 'sound barrier', 'mad cow disease']
Verb=['surround', 'stab', 'return', 'medicate', 'blindside', 'boogie', 'flap', 'trip', 'swat', 'suck in', 'harasses', 'traps', 'snoops', 'explode', 'scatter', 'challenge', 'fight', 'bury', 'splatter', 'smacks']
Adjective=['dead', 'hairless', 'sadistic', 'metal', 'wild', 'domesticated', 'abnormal', 'medicated', 'cocky', 'vengeful', 'sinister', 'costumed', 'cowardly', 'haunting', 'startled', 'alcoholic', 'demanding', 'shivering', 'offensive']

def extractText(file):
    source=open(file,'r')
    content=source.read()
    
    content+=' '
    content=content.replace('.',' .')
    content=content.replace(',',' ,')
    content=content.replace('?',' ?')
    content=content.replace('!',' !')
    return content
print extractText('story0.txt')

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

print extractBlanks(extractText('story0.txt'))

def gatherWords(toBeReplaced):
    filledin=[]
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
            
print gatherWords(extractBlanks(extractText('story0.txt')))
print gatherWords(extractBlanks(extractText('story1.txt')))

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
    
#print fillBlanks(extractText('story0.txt'), tofill)

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
    
print MadLibs('story0.txt')
print MadLibs('story1.txt')
