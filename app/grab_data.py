import requests
import re
import time
from pymongo import MongoClient
from collections import defaultdict

start = time.clock()

def grab_data(seed_verse):
#Connect to database and initialize links_table
    client = MongoClient('localhost', 27017)
    db = client.sefaria
    links_table = db.links

    #regex for filtering out Biblical verses from other text types

    regex = "^((I){1,2} )?[a-zA-Z]* [0-9]+:[0-9]+$|^Song of Songs [0-9]+:[0-9]+$"

    #seed_verse =  str(book) + " " + str(chapter) + ":" + str(verse) #"Exodus 20:2"

    links = []
    verses = []

    result = links_table.find({"refs": seed_verse})
    for link in result:
        refs = link['refs']
        if refs[0] == seed_verse:
            links.append(refs[1])
        else:
            links.append(refs[0])

    for link in links:
        results = links_table.find({"refs": link})
        for result in results:
            if result['refs'][0] == link:
                ref = result['refs'][1]
            else:
                ref = result['refs'][0]
            if ref != seed_verse and re.search(regex, ref):
                verses.append((ref, link))

    verse_connections_dict = defaultdict(list)
    for verse in set(verses):
        if verse_connections_dict[verse[0]]:
            verse_connections_dict[verse[0]].append(verse[1])
        else:
            verse_connections_dict[verse[0]] = [verse[1]]

    # for node in verse_connections_dict:
    #     print node + " " + str(verse_connections_dict[node])

    end = time.clock()
    return verse_connections_dict
    #print end - start
