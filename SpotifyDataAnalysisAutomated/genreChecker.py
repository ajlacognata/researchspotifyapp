import json

n = 7



print("Input highest id num:") # in order to tell the program how many times to repeat
idinput = input()

idinput = int(idinput)


while n < idinput+1:
    with open('genres.json', encoding='utf-8') as file:
        data = json.load(file)
        f = open('dataArtists/data%s.txt' % n, 'r')
        w = open('indGenres/indGenres%s.txt' % n, 'w+')
        content = f.readlines()
        num = 0
        while num < 50:
            line = content[num]
            #print(line)
            lineFind = line.find('\'', 2)
            new = line[2:lineFind]
            #print(new)
            num += 1

            x = 0
            while x < 61:
                rocktest = False
                metaltest = False
                poptest = False
                kpoptest = False
                raptest = False
                rbtest = False
                alttest = False
                punktest = False
                indietest = False
                folktest = False
                countrytest = False
                comedytest = False
                latintest = False
                jazztest = False
                christiantest = False
                edmtest = False
                soundtracktest = False
                ambienttest = False


                rock = data['rock']
                rock = rock[x]
                metal = data['metal']
                metal = metal[x]
                pop = data['pop']
                pop = pop[x]
                kpop = data['k-pop']
                kpop = kpop[x]
                rap = data['rap']
                rap = rap[x]
                rb = data['r&b']
                rb = rb[x]
                alt = data['alternative']
                alt = alt[x]
                punk = data['punk']
                punk = punk[x]
                indie = data['indie']
                indie = indie[x]
                folk = data['folk']
                folk = folk[x]
                country = data['country']
                country = country[x]
                comedy = data['comedy']
                comedy = comedy[x]
                latin = data['latin']
                latin = latin[x]
                jazz = data['jazz']
                jazz = jazz[x]
                christian = data['christian']
                christian = christian[x]
                edm = data['electronic']
                edm = edm[x]
                soundtrack = data['soundtrack']
                soundtrack = soundtrack[x]
                ambient = data['ambient']
                ambient = ambient[x]

                if rock == new:
                    rocktest = True
                if metal == new:
                    metaltest = True
                elif pop == new:
                    poptest = True
                elif kpop == new:
                    kpoptest = True
                elif rap == new:
                    raptest = True
                elif rb == new:
                    rbtest = True
                elif alt == new:
                    alttest = True
                elif punk == new:
                    punktest = True
                elif indie == new:
                    indietest = True
                elif folk == new:
                    folktest = True
                elif country == new:
                    countrytest = True
                elif comedy == new:
                    comedytest = True
                elif latin == new:
                    latintest = True
                elif jazz == new:
                    jazztest = True
                elif christian == new:
                    christiantest = True
                elif edm == new:
                    edmtest = True
                elif soundtrack == new:
                    soundtracktest = True
                elif ambient == new:
                    ambienttest = True
                elif new == '':
                    w.write('indie')
                    w.write('\n')
                    x = 61
                elif x == 60: 
                    print("Please add %s to the list" % new)
                    #gap = input()
                
                x+=1

                if rocktest == True:
                    #print('rock')
                    w.write('rock')
                    w.write('\n')
                    x = 61
                if metaltest == True:
                    #print('metal')
                    w.write('metal')
                    w.write('\n')
                    x = 61
                elif poptest == True:
                    #print('pop')
                    w.write('pop')
                    w.write('\n')
                    x = 61
                elif kpoptest == True:
                    #print('kpop')
                    w.write('k-pop')
                    w.write('\n')
                    x = 61
                elif raptest == True:
                    #print('rap')
                    w.write('rap')
                    w.write('\n')
                    x = 61
                elif rbtest == True:
                    #print('r&b')
                    w.write('r&b')
                    w.write('\n')
                    x = 61
                elif alttest == True:
                    #print('alternative')
                    w.write('alternative')
                    w.write('\n')
                    x = 61
                elif punktest == True:
                    #print('punk')
                    w.write('punk')
                    w.write('\n')
                    x = 61
                elif indietest == True:
                    #print('indie')
                    w.write('indie')
                    w.write('\n')
                    x = 61
                elif folktest == True:
                    #print('folk')
                    w.write('folk')
                    w.write('\n')
                    x = 61
                elif countrytest == True:
                    #print('country')
                    w.write('country')
                    w.write('\n')
                    x = 61
                elif comedytest == True:
                    #print('comedy')
                    w.write('comedy')
                    w.write('\n')
                    x = 61
                elif latintest == True:
                    #print('latin')
                    w.write('latin')
                    w.write('\n')
                    x = 61
                elif jazztest == True:
                    #print('jazz')
                    w.write('jazz/soul')
                    w.write('\n')
                    x = 61
                elif christiantest == True:
                    #print('christian')
                    w.write('christian')
                    w.write('\n')
                    x = 61
                elif edmtest == True:
                    #print('edm')
                    w.write('electronic')
                    w.write('\n')
                    x = 61
                elif soundtracktest == True:
                    #print('soundtrack')
                    w.write('soundtrack')
                    w.write('\n')
                    x = 61
                elif ambienttest == True:
                    #print('ambient)
                    w.write('ambient')
                    w.write('\n')
                    x = 61

                
            

    n += 1