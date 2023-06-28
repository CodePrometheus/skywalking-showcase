from fastapi import FastAPI
from faker import Faker

app = FastAPI()
fake = Faker()

@app.get("/api/v{apiVersion}/artists/{artist}/moments/{postid}/comments/{commentid}")
async def handle_request(apiVersion: int, artist: str, postid: int, commentid: int):

    comment_details = {
        "commentId": commentid,
        "commentBody": fake.sentence(),
        "likes": fake.random_int(min=0, max=99999),
        "userId": fake.random_number(digits=6)
    }
    
    return comment_details
