import json
import requests
import webbrowser


api_base_url = "https://itunes.apple.com/search?"

def get_info(): 
    api_url = '{0}term=afternooninparadisum'.format(api_base_url)
    print(api_url)
    
    response = requests.get(api_url)

    if response.status_code == 200:
        return json.loads(response.content)
    else:
        print(response.status_code)
        return None


info = get_info()


#track_url = ""



if info is not None:
    print("Here's your info:")
    data = json.dumps(info, indent=2)
    with open("TestFile.txt","w") as f:
        f.write(data)
    print(json.dumps(info, indent=2))
