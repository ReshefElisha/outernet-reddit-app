import json

date = "2015-05-15"
subReddit = "Science"
title = "Informative Shitpost"
content = "Informative shitpost content"

def generateJSON(date, subReddit, title, content):
    data = {}
    data['date'] = date
    data['subReddit'] = subReddit 
    data['title'] = title
    data['content'] = content
    json_data = json.dumps(data)
    print 'JSON: ', data

generateJSON(date, subReddit, title, content)












