#! /usr/bin/python
import csv
print 'content-type: text/html\n'
import cgitb
cgitb.enable()
import cgi

def generatehead(title):
    'Creates the tags that are at the top of a standards conforming html file'
    return '''<!DOCTYPE html>
<html>  
    <head>
        <style>
        body {text-align: center}
        </style>
        <meta charset="utf-8"/>
        <title>'''+title+'''</title>
    </head>
    <body>'''

def generatefoot():
    'Creates the tags that are at the end of a standards conforming html file'
    return '''  
    </body>
</html>'''

#------------------------------------- PYTHON 

#The following three functions extract,organize and compile data from the csv we are using
def compilefieldnames(csvfile):
    '''This function uses the DictReader method and creates dictionaries of all the records in the CSV.
       Then it uses the fieldnames method to make a list of fieldnames in the csv
    '''
    source=open( csvfile, 'rb')
    csvDictionary=csv.DictReader(source)
    return csvDictionary.fieldnames
    
fieldNames=compilefieldnames('recent-grads_relevant.csv') #Dictionaries of all the rows of data

def dictionaryOfCategories(csvfile):
    'Creates a dictionary using the major_categories from the CSV as keys and empty lists as placeholder values'
    source=open( csvfile, 'rb')
    index=fieldNames.index('Major Category')
    readerObject = csv.reader( source)
    categories={}
    for record in readerObject:
        categories[record[index]]=[]

    categories['All']=[]        
    return categories
categories=dictionaryOfCategories('recent-grads_relevant.csv')

def compileData(csvfile):
    '''This first creates lists for all records in the CSV using the reader method.
       Then these lists are compiled into the empty lists which were created by dictionaryOfCategories.
    '''
    source=open( csvfile, 'rb')
    csvAsLists=csv.reader(source)
    
    for record in csvAsLists:
        for category in categories:
            if category=='All' and record!=fieldNames:
                categories[category]+=[record]
            if category == record[fieldNames.index('Major Category')]:
                categories[category]+=[record]
    return categories

data=compileData('recent-grads_relevant.csv')

#The following two functions are used to create the html table

def createTableHeads(list):
    'This function uses fieldnames to create headers for the html table'
    tablerow='<tr>'
    for elements in list:
        tablerow+='<th>'+elements+'</th>\n'
        
    return tablerow+'</tr>'

fs=cgi.FieldStorage()    
def fieldStorageExtract(fieldstorage):
    '''This function uses the fieldstorage to find the category of data the user has asked for.
       It returns the list of majors under that category.
    '''
    for name in fieldstorage:
        if name=="category":
            category=fieldstorage[name].value
    for categories in data:
        if category==categories:
            majors=data[categories]
            break
    return majors

def MostEmployedInCateogory(fieldstorage):
    'This function finds the most employed in a certain category and produces a string containing that result'
    majors=fieldStorageExtract(fieldstorage)
    MostEmployed = 0
    majorName= ''
    for lists in majors:
        if int(lists[fieldNames.index('Employed')]) >= MostEmployed:
           MostEmployed = int(lists[fieldNames.index('Employed')])
           majorName= lists[fieldNames.index('Major')]
    MostEmployedAsString='The major with the most people employed, in the sample, in this category is: ' + majorName + ', with ' + str(MostEmployed) + ' people employed'
    return MostEmployedAsString   

def meanUnemployment(fieldstorage):
    'This function calculates the average unemployment rates in a certain category and produces a string containing that result in both floating point and percentage format'
    majors=fieldStorageExtract(fieldstorage)
    sumOfUnemploymentRate=0
    for lists in majors:
        if lists[fieldNames.index('Unemployment Rate')].isalpha():
            sumOfUnemploymentRate+=0
        else:
            sumOfUnemploymentRate+=float(lists[fieldNames.index('Unemployment Rate')])
    mean=sumOfUnemploymentRate/len(majors)
    meanPercent=mean*100
    meanAsString='The average unemployment rate in this category is '+str(mean)+' or '+str(meanPercent)+'%'
    return meanAsString
    
def percentFullTimeEmployed(fieldstorage):
    '''This function calculates what percent of the total number of people in each major in a certain category got a full-time year-round job 
       It uses the results to find which major has the highest percentage and displays it as a string.
    '''
    majors=fieldStorageExtract(fieldstorage)
    percent=0
    highestPercent=0
    majorName=''
    for lists in majors:
        ratio=float(lists[fieldNames.index('Full-time Year-round')])/float(lists[fieldNames.index('Total')])
        percent=ratio*100
        if percent >= highestPercent:
           highestPercent = percent
           majorName= lists[fieldNames.index('Major')]
    highestPercentAsString='The major with the highest percent of people employed full-time year-round is '+majorName+', with '+str(highestPercent)+'% employed full-time year-round'
    return highestPercentAsString
 
#FINAL ALL PUT TOGETHER FUNCTION
def createTableData(fieldstorage):
    '''
       This function iterates through the list that contains the records from the csv file for the given category(this data is in the form of a list).
       The data from the records contained in those lists is used to create a string for the tabledatum.
    '''
    # The two for loops below are used to find the majors associated with the category python got from field storage
    majors=fieldStorageExtract(fieldstorage)
    tabledatum=''
    for lists in majors:
        tabledatum+='<tr>\n'
        for dat in lists:
            tabledatum+='    <td>'+dat+'</td>'+'\n'
        tabledatum+='</tr>\n'
    return tabledatum
    
TopString = '<h3>You picked: <em>'+ fs['category'].value+ '</em>.' + '</h3><strong>Some useful statistics about this category</strong><br>'
print generatehead('Results')+ TopString+MostEmployedInCateogory(fs) + '<br>'+percentFullTimeEmployed(fs)+'<br>'+meanUnemployment(fs) +'<br><br>'+ '\n<table style="margin-left:auto;margin-right:auto" border="1">\n<caption> <strong>Here is the data on the majors in this category</strong></caption>\n'+createTableHeads(fieldNames)+createTableData(fs)+'\n</table>'+generatefoot()
