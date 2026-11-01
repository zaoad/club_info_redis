import json
import redis
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from model import Club

app = FastAPI()

redis_client = redis.Redis(host="localhost", port=6379, db=0)

CACHE_KEY = "clubs_list"
CACHE_EXPIRATION = 120


@app.get("/clubs")
def get_clubs(db: Session = Depends(get_db)):
    # Check if data exists in cache
    cached_data = redis_client.get(CACHE_KEY)

    if cached_data:
        return json.loads(cached_data)

    # If not in cache, query database
    clubs = db.query(Club).all()
    result = [
        {
            "id": club.id,
            "name": club.name,
            "location": club.location,
            "capacity": club.capacity
        }
        for club in clubs
    ]

    # Store in Redis with 120-second expiration
    redis_client.setex(CACHE_KEY, CACHE_EXPIRATION, json.dumps(result))

    return result
