import csv
import jinja2
from jinja2 import Template
from random import choice
from flask import Flask,render_template,request,redirect,url_for,Response

app = Flask(__name__, template_folder='template')

# function for movie recommendations
def recom(xa):
    csvFilePath = 'moviesdata.csv'
    comedy = {}
    animation = {}
    romance = {}
    family = {}
    biography = {}
    thriller = {}
    scifi = {}
    drama = {}
    horror = {}
    action = {}
    a = {"Funny":"Comedy", "Romantic":"Romance", "Feel good":"Family", "Thrilling":"Thriller", "Dramatic":"Drama","Heartwarming":"Animation", "Inspiring":"Biography","Smart":"Sci-Fi","Scary":"Horror","Action-packed":"Action"}
    if xa in a.keys():
        q = a[xa]
    x = ['Comedy','Animation','Romance','Family','Biography','Thriller','Action','Horror','Sci-Fi','Drama']
    if q in x:
        qi = x.index(q)
    y = [comedy,animation,romance,family,biography,thriller,action,horror,scifi,drama]
    with open(csvFilePath, encoding = "utf-8") as csvFile:
        csvReader = csv.DictReader(csvFile)
        for rows in csvReader:
           id = rows ['genre']
           if q in id:
            z = y[qi]
            z[id]  = rows
    random_element = choice(list(y[qi].items()))
    final = []
    dic = random_element[1]
    for keys in dic:
        final.append(dic[keys])
    return final

# routing of pages from page one to moods page to recom page
#routing of main pages
@app.route('/')
def xyz():
    return render_template("home.html")

@app.route('/try')
def index():
    return render_template ("try.html")

@app.route('/try1')
def index0():
    return render_template ("try1.html")

@app.route('/index4')
def index1():
    return render_template ("index4.html")

@app.route('/team')
def team():
    return render_template ("team.html")

#===========================================
#movie recommendations
@app.route('/mfunny')
def index10():
    a = recom('Funny')
    return render_template ("mfunny.html", a = a)

@app.route('/mdramatic')
def index11():
    a = recom('Dramatic')
    return render_template ("mdramatic.html", a = a)

@app.route('/mfeelgood')
def index12():
    a = recom('Feel good')
    return render_template ("mfeelgood.html" , a = a)

@app.route('/mscary')
def index13():
    a = recom('Scary')
    return render_template ("mscary.html", a = a)

@app.route('/msmart')
def index14():
    a = recom('Smart')
    return render_template ("msmart.html", a = a)

@app.route('/maction')
def index15():
    a = recom('Action-packed')
    return render_template ("maction.html",a = a)

@app.route('/minspi')
def index16():
    a = recom('Inspiring')
    return render_template ("minspi.html",a = a)

@app.route('/mthrill')
def index17():
    a = recom('Thrilling')
    return render_template ("mthrill.html",a = a)

@app.route('/mheartwarm')
def index18():
    a = recom('Heartwarming')
    return render_template ("mheartwarm.html",a = a)

@app.route('/mromantic')
def index19():
    a = recom('Romantic')
    return render_template ("mromantic.html",a = a)

#function for tv recommendations
def rect(ya):
    csvFilePath = 'series.csv'
    comedy = {}
    animation = {}
    romance = {}
    family = {}
    mystery = {}
    thriller = {}
    scifi = {}
    drama = {}
    horror = {}
    action = {}
    a = {"Funny":"Comedy", "Romantic":"Romance", "Feel good":"Family", "Thrilling":"Thriller", "Dramatic":"Drama","Heartwarming":"Animation", "Inspiring":"Sci-Fi","Smart":"Mystery","Scary":"Horror","Action-packed":"Action"}
    if ya in a.keys():
       q = a[ya]
    x = ['Comedy','Animation','Romance','Family','Mystery','Thriller','Action','Horror','Sci-Fi','Drama']
    if q in x:
       qi = x.index(q)
    y = [comedy,animation,romance,family,mystery,thriller,action,horror,scifi,drama]
    with open(csvFilePath, encoding = "utf-8") as csvFile:
        csvReader = csv.DictReader(csvFile)
        for rows in csvReader:
           id = rows ['Genre']
           if q in id:
               z = y[qi]
               z[id]  = rows
    random_element = choice(list(y[qi].items()))
    final = []
    dic = random_element[1]
    for keys in dic:
        final.append(dic[keys])
    return final

# =====================================
# T.V. recommendations
@app.route('/tfunny')
def index20():
    b = rect('Funny')
    return render_template ("tfunny.html",b=b)

@app.route('/tromantic')
def index21():
    b = rect('Romantic')
    return render_template ("tromantic.html",b=b)

@app.route('/theartwarm')
def index22():
    b = rect('Heartwarming')
    return render_template ("theartwarm.html",b=b)

@app.route('/tthrill')
def index23():
    b = rect('Thrilling')
    return render_template ("tthrill.html",b=b)

@app.route('/tfeelgood')
def index24():
    b = rect('Feel good')
    return render_template ("tfeelgood.html",b=b)

@app.route('/taction')
def index25():
    b = rect('Action-packed')
    return render_template ("taction.html",b=b)

@app.route('/tinspi')
def index26():
    b = rect('Inspiring')
    return render_template ("tinspi.html",b=b)

@app.route('/tsmart')
def index27():
    b = rect('Smart')
    return render_template ("tsmart.html",b=b)

@app.route('/tscary')
def index28():
    b = rect('Scary')
    return render_template ("tscary.html",b=b)

@app.route('/tdramatic')
def index29():
    b = rect('Dramatic')
    return render_template ("tdramatic.html",b=b)


#Music moods index
@app.route('/moe')
def moodeng():
    return render_template ("moe.html")

@app.route('/moh')
def moodhin():
    return render_template ("moh.html")

@app.route('/mom')
def moodmar():
    return render_template ("mom.html")

@app.route('/mot')
def moodtek():
    return render_template ("mot.html")

@app.route('/motam')
def moodtam():
    return render_template ("motam.html")

@app.route('/mop')
def moodpun():
    return render_template ("mop.html")

@app.route('/mog')
def moodguj():
    return render_template ("mog.html")

@app.route('/mob')
def moodben():
    return render_template ("mob.html")

@app.route('/mobp')
def moodbhoj():
    return render_template ("mobp.html")

@app.route('/mok')
def moodkan():
    return render_template ("mok.html")

#################################################################################
#ENGLISH
#chill
def chill(chill):
    csvFilePath = 'engdata.csv'
    final = []
    finall =[]
    y = ['dance','rap','chill','melodic']
    for i in range(4):
        l = []
        with open(csvFilePath, encoding = "utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'indie' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall

@app.route('/echill')
def echill():
    a = chill("chill")
    return render_template ("echill.html", a = a)

#dance
def dance(dance):
    csvFilePath = 'engdata.csv'
    final = []
    finall =[]
    y = ['dance','rap','chill','melodic']
    for i in range(4):
        l = []
        with open(csvFilePath, encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'dance' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall
    
@app.route('/edance')
def edance():
    a = dance("dance")
    return render_template ("edance.html", a = a)

#rap
def rap(rap):
    csvFilePath = 'engdata.csv'
    final = []
    finall =[]
    y = ['dance','rap','chill','melodic']
    for i in range(4):
        l = []
        with open(csvFilePath, encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'rap' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall
    
    
@app.route('/erap')
def erap():
    a = rap("rap")
    return render_template ("erap.html", a = a)

#melodic
def melodic(melodic):
    csvFilePath = 'engdata.csv'
    final = []
    finall =[]
    y = ['dance','rap','chill','melodic']
    for i in range(4):
        l = []
        with open(csvFilePath, encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'melodic' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall


@app.route('/emelod')
def emelod():
    a = melodic("melodic")
    return render_template ("emelod.html", a = a)

###################################################################################
#HINDI
#sad
def hsad(hsad):
    csvFilePath = 'hind.csv'
    final = []
    finall =[]
    y = ['Dance','Motivational','Romantic','Sad']
    for i in range(4):
        l = []
        with open(csvFilePath, encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Sad' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall

@app.route('/hsad')
def sadd():
    a = hsad("Sad")
    return render_template ("hsad.html", a = a)

#dance
def hdance(hdance):
    csvFilePath = 'hind.csv'
    final = []
    finall =[]
    y = ['Dance','Motivational','Romantic','Sad']
    for i in range(4):
        l = []
        with open(csvFilePath, encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Dance' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall

@app.route('/hdance')
def dancee():
    a = hdance("Dance")
    return render_template ("hdance.html", a = a)

#romance
def hromance(hromance):
    csvFilePath = 'hind.csv'
    final = []
    finall =[]
    y = ['Dance','Motivational','Romantic','Sad']
    for i in range(4):
        l = []
        with open(csvFilePath, encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Romantic' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall

@app.route('/hromance')
def rom():
    a = hromance("Romance")
    return render_template ("hromance.html", a = a)

#feelgood
def hfg(hfg):
    csvFilePath = 'hind.csv'
    final = []
    finall =[]
    y = ['Dance','Motivational','Romantic','Sad']
    for i in range(4):
        l = []
        with open(csvFilePath, encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Motivational' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall

@app.route('/hfg')
def fgg():
    a = hfg("Motivational")
    return render_template ("hfg.html", a = a)

###################################################################################
#TAMIL
#chill
def tamchill(chill):
    csvFilePath = 'Tamil.csv'
    final = []
    finall =[]
    y = ['Romantic','Party','Chill','Sad']
    for i in range(4):
        l = []
        with open(csvFilePath, encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Chill' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall
    
@app.route('/tamchill')
def tamchil():
    a = tamchill("Chill")
    return render_template ("tamchill.html", a = a)

#dance
def tamdance(dance):
    csvFilePath = 'Tamil.csv'
    final = []
    finall =[]
    y = ['Romantic','Party','Chill','Sad']
    for i in range(4):
        l = []
        with open(csvFilePath, encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Party' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall

@app.route('/tamdance')
def tamdanc():
    a = tamdance("Party")
    return render_template ("tamdance.html", a = a)

#sad
def tamsad(sad):
    csvFilePath = 'Tamil.csv'
    final = []
    finall =[]
    y = ['Romantic','Party','Chill','Sad']
    for i in range(4):
        l = []
        with open(csvFilePath, encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Sad' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall

@app.route('/tamsad')
def tamsa():
    a = tamsad("Sad")
    return render_template ("tamsad.html", a = a)

#romance
def tamromance(romance):
    csvFilePath = 'Tamil.csv'
    final = []
    finall =[]
    y = ['Romantic','Party','Chill','Sad']
    for i in range(4):
        l = []
        with open(csvFilePath, encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Romantic' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall

@app.route('/tamromance')
def tamromanc():
    a = tamromance("Sad")
    return render_template ("tamromance.html", a = a)

###################################################################################
#TELUGU
#chill
def telchill(chill):
    csvFilePath = 'telu.csv'
    final = []
    finall =[]
    y = ['Romantic','Party','Chill','Sad']
    for i in range(4):
        l = []
        with open(csvFilePath, encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Chill' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall


@app.route('/telchill')
def telchi():
    a = telchill("Chill")
    return render_template ("telchill.html", a = a)

#dance
def teldance(teldance):
    csvFilePath = 'telu.csv'
    final = []
    finall =[]
    y = ['Romantic','Party','Chill','Sad']
    for i in range(4):
        l = []
        with open(csvFilePath, encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Party' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall

@app.route('/teldance')
def teldan():
    a = telchill("Party")
    return render_template ("teldance.html", a = a)

#sad
def telsad(telsad):
    csvFilePath = 'telu.csv'
    final = []
    finall =[]
    y = ['Romantic','Party','Chill','Sad']
    for i in range(4):
        l = []
        with open(csvFilePath, encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Sad' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall

@app.route('/telsad')
def telsa():
    a = telsad("Sad")
    return render_template ("telsad.html", a = a)

#romance
def telromance(telrom):
    csvFilePath = 'telu.csv'
    final = []
    finall =[]
    y = ['Romantic','Party','Chill','Sad']
    for i in range(4):
        l = []
        with open(csvFilePath, encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Romantic' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall

@app.route('/telromance')
def telro():
    a = telsad("Romantic")
    return render_template ("telromance.html", a = a)

###################################################################################
#KANNADA
#chill
def kchill(kchill):
    csvFilePath = 'kanu.csv'
    final = []
    finall =[]
    y = ['Romantic','Rap','Devotional','Chill']
    for i in range(4):
        l = []
        with open(csvFilePath, encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Chill' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall

@app.route('/kchill')
def kchill():
    a = kchill("Chill")
    return render_template ("kchill.html", a = a)

#romance
def kromance(rom):
    csvFilePath = 'kanu.csv'
    final = []
    finall =[]
    y = ['Romantic','Rap','Devotional','Chill']
    for i in range(4):
        l = []
        with open(csvFilePath, encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Romantic' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall
    
@app.route('/kromance')
def kro():
    a = kromance("Chill")
    return render_template ("kromance.html", a = a)

#rap
def krap(rap):
    csvFilePath = 'kanu.csv'
    final = []
    finall =[]
    y = ['Romantic','Rap','Devotional','Chill']
    for i in range(4):
        l = []
        with open(csvFilePath, encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Rap' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall

@app.route('/krap')
def kra():
    a = krap("Rap")
    return render_template ("krap.html", a = a)

#devotional
def kdevo(kdevo):
    csvFilePath = 'kanu.csv'
    final = []
    finall =[]
    y = ['Romantic','Rap','Devotional','Chill']
    for i in range(4):
        l = []
        with open(csvFilePath, encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Devotional' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall

@app.route('/kdevo')
def kdev():
    a = krap("Devotional")
    return render_template ("kdevo.html", a = a)

###################################################################################
#MARATHI
#chill
def marchill(marchill):
    csvFilePath = 'maru.csv'
    final = []
    finall =[]
    y = ['Romantic','Party','Chill','Sad']
    for i in range(4):
        l = []
        with open(csvFilePath, encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Chill' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall

@app.route('/marchill')
def marchl():
    a = krap("Chill")
    return render_template ("marchill.html", a = a)

#Party
def marparty(marparty):
    csvFilePath = 'maru.csv'
    final = []
    finall =[]
    y = ['Romantic','Party','Chill','Sad']
    for i in range(4):
        l = []
        with open(csvFilePath, encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Party' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall

@app.route('/marparty')
def marpa():
    a = marparty("Party")
    return render_template ("marparty.html", a = a)

#Romance
def marromance(rom):
    csvFilePath = 'maru.csv'
    final = []
    finall =[]
    y = ['Romantic','Party','Chill','Sad']
    for i in range(4):
        l = []
        with open(csvFilePath, encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Romantic' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall

@app.route('/marromance')
def marom():
    a = marromance("Romance")
    return render_template ("marromance.html", a = a)

#Sad
def marsad(sa):
    csvFilePath = 'maru.csv'
    final = []
    finall =[]
    y = ['Romantic','Party','Chill','Sad']
    for i in range(4):
        l = []
        with open(csvFilePath, encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Sad' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall

@app.route('/marsad')
def masa():
    a = marsad("Sad")
    return render_template ("marsad.html", a = a)

#########################################################################################
#guj
#dance
def gdance(dan):
    csvFilePath = 'fafda.csv'
    final = []
    finall =[]
    y = ['Party','Sufi','Soothing','Romantic']
    for i in range(4):
        l = []
        with open(csvFilePath) as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Party' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall

@app.route('/gdance')
def gdan():
    a = gdance("Party")
    return render_template ("gdance.html", a = a)

#romance
def gromance(rom):
    csvFilePath = 'fafda.csv'
    final = []
    finall =[]
    y = ['Party','Sufi','Soothing','Romantic']
    for i in range(4):
        l = []
        with open(csvFilePath) as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Romantic' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall

@app.route('/gromance')
def grom():
    a = gromance("Romance")
    return render_template ("gromance.html", a = a)

#feelgood
def gfg(fg):
    csvFilePath = 'fafda.csv'
    final = []
    finall =[]
    y = ['Party','Sufi','Soothing','Romantic']
    for i in range(4):
        l = []
        with open(csvFilePath) as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Soothing' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall

@app.route('/gfg')
def gfff():
    a = gfg("Party")
    return render_template ("gfg.html", a = a)

#peaceful
def gpeace(peace):
    csvFilePath = 'fafda.csv'
    final = []
    finall =[]
    y = ['Party','Sufi','Soothing','Romantic']
    for i in range(4):
        l = []
        with open(csvFilePath) as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Sufi' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall

@app.route('/gpeaceful')
def gff():
    a = gpeace("Peaceful")
    return render_template ("gpeaceful.html", a = a)

########################################################################################
#Punjabi
#chill
def pchill(chill):
    csvFilePath = 'punju.csv'
    final = []
    finall =[]
    y = ['Romantic','Party','Chill','Sad']
    for i in range(4):
        l = []
        with open(csvFilePath, encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Chill' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall    
    
@app.route('/pchill')
def pchi():
    a = pchill("Chill")
    return render_template ("pchill.html", a = a)

#romance
def pro(rom):
    csvFilePath = 'punju.csv'
    final = []
    finall =[]
    y = ['Romantic','Party','Chill','Sad']
    for i in range(4):
        l = []
        with open(csvFilePath, encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Romantic' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall  

@app.route('/promance')
def prom():
    a = pro("Romantic")
    return render_template ("promance.html", a = a)

#dance
def pdance(dan):
    csvFilePath = 'punju.csv'
    final = []
    finall =[]
    y = ['Romantic','Party','Chill','Sad']
    for i in range(4):
        l = []
        with open(csvFilePath, encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Party' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall  

@app.route('/pdance')
def pdan():
    a = pdance("Party")
    return render_template ("pdance.html", a = a)

#sad
def psad(sad):
    csvFilePath = 'punju.csv'
    final = []
    finall =[]
    y = ['Romantic','Party','Chill','Sad']
    for i in range(4):
        l = []
        with open(csvFilePath, encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Sad' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall  

@app.route('/psad')
def psa():
    a = psad("Sad")
    return render_template ("psad.html", a = a)

########################################################################################
#Bengali
#party
def bdance(dan):
    csvFilePath = 'bengali.csv'
    final = []
    finall =[]
    y = ['Break-a-leg','Devotional','Emotional','Rap']
    for i in range(4):
        l = []
        with open(csvFilePath) as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Break-a-leg' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)

    return finall

@app.route('/bdance')
def bdan():
    a = bdance("Break-a-leg")
    return render_template ("bdance.html", a = a)

#emotional
def bemo(emo):
    csvFilePath = 'bengali.csv'
    final = []
    finall =[]
    y = ['Break-a-leg','Devotional','Emotional','Rap']
    for i in range(4):
        l = []
        with open(csvFilePath) as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Emotional' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall

@app.route('/bemo')
def bem():
    a = bemo("Emotional")
    return render_template ("bemo.html", a = a)

#devotional
def bdevo(devo):
    csvFilePath = 'bengali.csv'
    final = []
    finall =[]
    y = ['Break-a-leg','Devotional','Emotional','Rap']
    for i in range(4):
        l = []
        with open(csvFilePath) as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Devotional' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall

@app.route('/bdevo')
def bde():
    a = bdevo("Devotional")
    return render_template ("bdevo.html", a = a)

#Rap
def brap(rap):
    csvFilePath = 'bengali.csv'
    final = []
    finall =[]
    y = ['Break-a-leg','Devotional','Emotional','Rap']
    for i in range(4):
        l = []
        with open(csvFilePath) as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Devotional' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall

@app.route('/brap')
def bra():
    a = brap("Rap")
    return render_template ("brap.html", a = a)

########################################################################################
#Bhojpuri

#dance
def bpdance(dan):
    csvFilePath = 'Bhojpuri_dataset.csv'
    final = []
    finall =[]
    y = ['Party','Romance','Sufi','Sad']
    for i in range(4):
        l = []
        with open(csvFilePath, encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Party' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall

@app.route('/bpdance')
def bpdanc():
    a = bpdance("Party")
    return render_template ("bpdance.html", a = a)

#romance
def bpromance(rom):
    csvFilePath = 'Bhojpuri_dataset.csv'
    final = []
    finall =[]
    y = ['Party','Romance','Sufi','Sad']
    for i in range(4):
        l = []
        with open(csvFilePath, encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Romance' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall

@app.route('/bpromance')
def bprom():
    a = bpromance("Romance")
    return render_template ("bpromance.html", a = a)

#sad
def bpsad(sad):
    csvFilePath = 'Bhojpuri_dataset.csv'
    final = []
    finall =[]
    y = ['Party','Romance','Sufi','Sad']
    for i in range(4):
        l = []
        with open(csvFilePath, encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Sad' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall

@app.route('/bpsad')
def bpsa():
    a = bpsad("Sad")
    return render_template ("bpsad.html", a = a)

#peace
def bppeace(peace):
    csvFilePath = 'Bhojpuri_dataset.csv'
    final = []
    finall =[]
    y = ['Party','Romance','Sufi','Sad']
    for i in range(4):
        l = []
        with open(csvFilePath, encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows ['Genre']
                if 'Sufi' in id:
                    l.append(rows)
            random_element = choice(l)
            final.append(random_element)
    for i in final:
        df= []
        for keys in i:
            df.append(i[keys])
        for m in df:
            finall.append(m)
    return finall

@app.route('/bppeace')
def bppeac():
    a = bppeace("Sufi")
    return render_template ("bppeace.html", a = a)


if __name__ == '__main__':
    app.run(debug=True)