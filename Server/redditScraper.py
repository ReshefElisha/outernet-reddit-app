import praw
from StringIO import StringIO
from PIL import Image
from urllib import urlopen
import base64, datetime
import json

def generateJSON(date, subReddit, title, content, id):
    data = {}
    data['date'] = date
    data['subReddit'] = subReddit
    data['title'] = title
    data['content'] = content
    data['id'] = id
    json_data = json.dumps(data)
    return data

reddit = praw.Reddit('OuternetRedditApp')
reddit.login('outernet-project','outernet')
front_page = reddit.get_front_page()
for submission in front_page:
    if submission.url.lower().endswith(('.png','.jpg')):
        title = str(submission.title)
        print title
        subreddit = str(submission.subreddit)
        date = datetime.datetime.fromtimestamp(int(submission.created_utc)).strftime('%Y-%m-%d %H:%M:%S')
        image = Image.open(StringIO(urlopen(submission.url).read()))
        jpeg_image_buffer = StringIO()
        image.save(jpeg_image_buffer, format="JPEG")
        img_str = base64.b64encode(jpeg_image_buffer.getvalue())
        print date
        jsonObj = generateJSON(date, subreddit, title, img_str, str(submission.id))
        jsonFile = open('jsonObj/' + submission.id + ".json", 'a')
        jsonFile.write(str(jsonObj))
        print 'Printed File'













