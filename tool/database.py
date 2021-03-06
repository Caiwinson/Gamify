from firebase_admin import credentials, db, initialize_app
from tool.config import config
cred=credentials.Certificate(config["Firebase"]["location"])
initialize_app(cred, {"databaseURL": config["database"]["databaseURL"]})

cached={}
def get(id):
    id=str(id)
    if id not in cached:
        ref=db.reference("data").child(id)
        data=ref.get()
        cached[id]=data
    if cached[id] is not None and "member" not in cached[id]:
        cached[id]["member"]=[]
    return cached[id]

def post(id, data):
    id=str(id)
    ref=db.reference("data").child(id)
    ref.update(data)
    if id not in cached or cached[id] is None:
        cached[id]={}
    for i in list(data.keys()):
        if data[i]==[] or data[i] is None:
            del cached[id][i]
        else:
            cached[id][i]=data[i]
        
