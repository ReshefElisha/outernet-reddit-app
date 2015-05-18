import subprocess
import cStringIO
import PIL.Image
import os
import praw
from StringIO import StringIO
from PIL import Image
from urllib import urlopen
import base64, datetime
import json

# assume data contains your decoded image

def generateJSON(date, subReddit, title, content, id):
    data = {}
    data['date'] = date
    data['subReddit'] = subReddit
    data['title'] = title
    data['content'] = content
    data['id'] = id
    json_data = json.dumps(data)
    return data

def cutyCapt(page, Rid):
    website = "--url="+page
    picture = "--out="+Rid+".png"
    subprocess.call(["cutycapt.exe", website, picture])
    try:
        with open(Rid+".png", "rb") as f:
            data = f.read()
        os.remove(Rid+".png")
        htmlstring = data.encode("base64").replace('\n','')
    except IOError as e:
        return None
    return(htmlstring)

reddit = praw.Reddit('OuternetRedditApp')
reddit.login('outernet-project','outernet')
front_page = reddit.get_front_page()
for submission in front_page:
    err = 0
    try:
        title = str(submission.title)
        print title
        subreddit = str(submission.subreddit)
        date = datetime.datetime.fromtimestamp(int(submission.created_utc)).strftime('%Y-%m-%d %H:%M:%S')
    except UnicodeEncodeError as e:
        err = None
    if err != None:
        if submission.url.lower().endswith(('.png','.jpg')):
            image = Image.open(StringIO(urlopen(submission.url).read()))
            jpeg_image_buffer = StringIO()
            image.save(jpeg_image_buffer, format="JPEG")
            img_str = base64.b64encode(jpeg_image_buffer.getvalue())
            print date
            jsonObj = generateJSON(date, subreddit, title, img_str, str(submission.id))
            jsonFile = open('jsonObj/' + submission.id + ".json", 'a')
            jsonFile.write(str(jsonObj))
            print 'Printed File'
        else:
            img_str = cutyCapt(submission.url, str(submission.id))
            if img_str != None:
                jsonObj = generateJSON(date, subreddit, title, img_str, str(submission.id))
                jsonFile = open('jsonObj/' + str(submission.id) + ".json", 'a')
                jsonFile.write(str(jsonObj))
                print 'Printed File'
            else:
                print 'Failed to print File'
    else:
        print 'Failed to print File'
        
        
