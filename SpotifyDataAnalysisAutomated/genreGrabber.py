import json

n = 1

print("Input highest id number in Microsoft Forms:") # in order to tell the program how many times to repeat
idinput = input()

idinput = int(idinput)


while n < idinput+1:
    f = open('dataArtists/data%s.txt' % n, 'w+')

    num = 0
    while(num < 50): 
        with open('spotifyraw/artists/spotifyDataArtists_%s.json' % n, encoding='utf-8') as file:
            data = json.load(file)
            art = data[num]
            genresData = art["genres"]
            #print(genresData)
            f.write(str(genresData))
            f.write('\n')
            num+=1

    f.close()     
    
    n += 1
