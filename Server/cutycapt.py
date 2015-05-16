import subprocess
import cStringIO
import PIL.Image
import os

# assume data contains your decoded image


def cutyCapt(page, Rid):
    website = "--url="+page
    picture = "--out="+Rid+".png"
    subprocess.call(["cutycapt.exe", website, picture])
    with open(Rid+".png", "rb") as f:
        data = f.read()
    os.remove(Rid+".png")
    htmlstring = data.encode("base64").replace('\n','')
    return(htmlstring)
