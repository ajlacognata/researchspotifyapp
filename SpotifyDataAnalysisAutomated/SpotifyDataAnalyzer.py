import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Setup for interaction with the Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="d1092c6a474e44cc8f5b265910be71ec", client_secret="29c63f3edc73433fb13ec080d3ae94ef"))

print("Input highest ID num:") #to tell program how many times to run
idinput = input()
idinput = int(idinput)
n = 7
while n < idinput+1:
    # Initializes files for use
    f = open('dataTracks/data%s.txt' % n, 'r')
    datawrite = open('datacontent.json', 'w+')
    datawriteNew = open('datacontentFinal.json', 'w+')
    datawriteText = open('datacontent.txt', 'w+')


    # Attributes to be calculated later using averages data given (from Spotify) for all 50 tracks
    totalDanceability = 0
    totalEnergy = 0
    totalLoudness = 0
    totalSpeechiness = 0
    totalAcousticness = 0
    totalInstrumentalness = 0
    totalLiveness = 0
    totalValence = 0
    totalTempo = 0

    count = 0 # For counting number of lines in data.txt
    num = 0

    l = f.readlines() # For counting number of lines in data.txt
    for line in l:
        count += 1
        print("Line{}: {}".format(count, line.strip()))
        data = sp.audio_features(line.strip())
        #print(data) Debugging purposes
        json.dump(data, datawrite)
        datawrite.write("\n")

    datawrite.close() 


    # Converts datacontent.json to datacontent.txt (for later text replacement)
    filename = "datacontent.json"
    with open(filename, 'r') as fr:
        pre_ = fr.read()
        lines = pre_.split('\n')
        new_filename = filename.split('.')[0]+".txt" # To keep the same name except ext
        with open(new_filename, "a") as fw:
            fw.write("\n".join(lines))

    # Removes excess brackets
    with open('datacontent.txt') as file:
        dataread = file
        dataEdit = dataread.read().replace('[', '')
        dataEdit = dataEdit.replace(']', ',', 49)
        datawriteNew.write('[')
        datawriteNew.write(dataEdit)
        

    # Calculates attribute averages
    while (num < 50):
        with open('datacontentFinal.json') as file:
            dataAnalyzed = json.load(file)

            id = dataAnalyzed[num]

            danceability = id["danceability"]
            totalDanceability += danceability

            energy = id["energy"]
            totalEnergy += energy

            loudness = id["loudness"]
            totalLoudness += loudness

            speechiness = id["speechiness"]
            totalSpeechiness += speechiness

            acousticness = id["acousticness"]
            totalAcousticness += acousticness

            instrumentalness = id["instrumentalness"]
            totalInstrumentalness += instrumentalness

            liveness = id["liveness"]
            totalLiveness += liveness

            valence = id["valence"]
            totalValence += valence

            tempo = id["tempo"]
            totalTempo += tempo

            num += 1

    # Calculates average attribute values
    avgDanceability = totalDanceability/50
    avgEnergy = totalEnergy/50
    avgLoudness = totalLoudness/50
    avgSpeechiness = totalSpeechiness/50
    avgAcousticness = totalAcousticness/50
    avgInstrumentalness = totalInstrumentalness/50
    avgLiveness = totalLiveness/50
    avgValence = totalValence/50
    avgTempo = totalTempo/50

    # Prints attribute values
    print()
    print("Danceability:")
    print(totalDanceability)
    print(avgDanceability)
    print("Energy:")
    print(totalEnergy)
    print(avgEnergy)
    print("Loudness (dB):")
    print(totalLoudness)
    print(avgLoudness)
    print("Speechiness:")
    print(totalSpeechiness)
    print(avgSpeechiness)
    print("Acousticness:")
    print(totalAcousticness)
    print(avgAcousticness)
    print("Instrumentalness:")
    print(totalInstrumentalness)
    print(avgInstrumentalness)
    print("Liveness:")
    print(totalLiveness)
    print(avgLiveness)
    print("Valence:")
    print(totalValence)
    print(avgValence)
    print("Tempo:")
    print(totalTempo)
    print(avgTempo)
    print()

    # Array of attributes to be saved
    attributeArray = {"id": n, "Danceability": avgDanceability,"Energy": avgEnergy,"Loudness": avgLoudness,"Speechiness": avgSpeechiness,"Acousticness": avgAcousticness,"Instrumentalness": avgInstrumentalness,"Liveness": avgLiveness,"Valence": avgValence,"Tempo": avgTempo}

    # Saves each participant's attributes into their own json file
    attributeSave = open('indAtts/attributes_%s.json' % n, 'w+')
    json.dump(attributeArray, attributeSave)

    # Saves all participants' attributes into one file, that is easily readable by a human
    allAttributeSaveHuman = open('attributes_human.txt', 'a')
    allAttributeSaveHuman.write('ID %s :' % n)
    json.dump(attributeArray, allAttributeSaveHuman)
    allAttributeSaveHuman.write('\n')


    # Prepares for full attributes appending
    def write_json(data, filename='attributes.json'): 
        with open(filename,'w') as f: 
            json.dump(data, f, indent=2) 
        
        
    # Appends attributes.json, a file that contains a JSON array of all participants' attributes
    with open('attributes.json') as json_file: 
        data = json.load(json_file) 
        temp = data['id'] 
        # appending data to attributes.json[id]
        temp.append(attributeArray) 
    write_json(data)  # writes new data to attributes.json
    n += 1