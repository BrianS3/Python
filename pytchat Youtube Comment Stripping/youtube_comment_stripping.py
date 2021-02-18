def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import pytchat
except:
    install(pytchat)
    import pytchat

try:
    import json
except:
    install(json)
    import json

videoId = input('Enter YouTube Video ID: ')

f = open(f'outputs/{videoId}.txt', 'w')
chat = pytchat.create(video_id=videoId)
while chat.is_alive():
    for c in chat.get().items:
        obj = c.json()
        obj2 = json.loads(obj)
        f.write(str("{} {}: {}".format(obj2['author']['name'], obj2['datetime'],obj2['message']).encode('utf8')))
        f.write("\n")
f.close()
