import requests

def get_last_release():
    
    try:
        url = 'https://github.com/wrwrabbit/Partisan-Telegram-Android/releases/latest'
        r = requests.get(url)
        version = r.url.split('/')[-1]
        return version
    
    except:
        print("Error while making the GET request to the specified URL")

 
print(get_last_release())
