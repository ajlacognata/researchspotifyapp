import json
n = 1 # First ID num in Microsoft Forms

print("Input highest id number from Microsoft Forms:") # in order to tell the program how many times to repeat
idinput = input()

idinput = int(idinput)

while n < idinput+1:
    # Opens data.txt to prepare to write to it
    f = open("dataTracks/data%s.txt" % n,"w+")

    num = 0 # used to count for each of the 50 tracks on the top 50
    while (num < 50): # Extracts the track id from each track
        with open('spotifyraw/spotifyDataTracks_%s.json' % n, encoding='utf-8') as file:
            data = json.load(file)
            num0 = data[num]
            id0 = num0["id"]
            print(id0)
            num+=1
            f.write(id0)
            f.write("\n")
    n += 1
    print()
