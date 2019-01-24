import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from os.path  import basename
import os


def crowler(url):
    page=requests.get(url).text
    list_urls=[]
    soup=BeautifulSoup(page,'lxml')
    
    images=soup.find_all('img')
    for img_url in images:
         #checks the images in following format or filter image urls
         if img_url.get('src') is not None:
             if img_url.get('src').endswith(('.png', '.jpg', '.jpeg','.gif')):
                 
                 # working with relative links 
                 imageurl=img_url.get('src')
                 #print(imageurl)

                 if url_validator(img_url.get('src'))==False:
                     
                 #Try to make it valid (or create a valid url)
                     imageurl=url+"/"+img_url.get('src')
                     print(url+"/"+img_url.get('src'))
                     list_urls.append(imageurl)
             else:
                 print("Invalid Url Founds")

    return list_urls
             

    
def url_validator(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc, result.path])
    except:
        return False


def downloadImages(image_urls):
    for image in image_urls:
        imageName=basename(image)
        
        if not os.path.isfile("images/"):
            os.makedirs("images/", exist_ok=True)
            with open("images/"+imageName,'wb') as f: 
                 f.write(requests.get(image).content) 


def main(url):
    print("Program started successfully.......")
    list_images=crowler(url)
    downloadImages(list_images)
    print("Program ended successfully.......")

    
# Main entry point to invoke program

if __name__ == "__main__": 
    # pass the images scrapping url

    main("")

