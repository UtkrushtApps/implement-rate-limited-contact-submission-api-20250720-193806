from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory notifications store
# Format: {username: [notification dicts, ...]}
notifications_store = {}

class Notification(BaseModel):
    username: str
    message: str
    timestamp: str

@app.post("/notifications/", status_code=201)
def create_notification(notification: Notification):
    user = notification.username
    notif_dict = notification.dict()
    if user not in notifications_store:
        notifications_store[user] = []
    notifications_store[user].append(notif_dict)
    return {"success": True}

@app.get("/notifications/{username}", response_model=List[Notification])
def get_notifications(username: str):
    return notifications_store.get(username, [])
