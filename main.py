from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from model import Club

app = FastAPI()


@app.get("/clubs")
def get_clubs(db: Session = Depends(get_db)):
    clubs = db.query(Club).all()
    return [
        {
            "id": club.id,
            "name": club.name,
            "location": club.location,
            "capacity": club.capacity
        }
        for club in clubs
    ]
