"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Competitive basketball team and practice",
        "schedule": "Mondays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": ["james@mergington.edu"]
    },
    "Tennis Club": {
        "description": "Learn tennis skills and play competitive matches",
        "schedule": "Wednesdays and Saturdays, 3:00 PM - 4:30 PM",
        "max_participants": 16,
        "participants": ["alex@mergington.edu", "noah@mergington.edu"]
    },
    "Drama Club": {
        "description": "Acting, theater productions, and performance art",
        "schedule": "Tuesdays, 4:00 PM - 5:30 PM",
        "max_participants": 25,
        "participants": ["isabella@mergington.edu", "mia@mergington.edu"]
    },
    "Digital Art Studio": {
        "description": "Digital painting, graphic design, and animation",
        "schedule": "Wednesdays and Fridays, 4:00 PM - 5:00 PM",
        "max_participants": 18,
        "participants": ["ava@mergington.edu"]
    },
    "Debate Team": {
        "description": "Competitive debate and public speaking skills",
        "schedule": "Mondays and Wednesdays, 3:45 PM - 5:00 PM",
        "max_participants": 20,
        "participants": ["lucas@mergington.edu", "elizabeth@mergington.edu"]
    },
    "Science Club": {
        "description": "Explore STEM topics through experiments and projects",
        "schedule": "Thursdays, 3:30 PM - 4:45 PM",
        "max_participants": 22,
        "participants": ["ryan@mergington.edu"]
    },
    "Volleyball Team": {
        "description": "Competitive volleyball team with practice and games",
        "schedule": "Tuesdays and Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 14,
        "participants": ["sarah@mergington.edu", "jessica@mergington.edu"]
    },
    "Swimming Team": {
        "description": "Competitive swimming and diving program",
        "schedule": "Mondays, Wednesdays, Fridays, 3:00 PM - 4:00 PM",
        "max_participants": 18,
        "participants": ["tyler@mergington.edu"]
    },
    "Music Ensemble": {
        "description": "Orchestra, band, and choir performances",
        "schedule": "Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 28,
        "participants": ["grace@mergington.edu", "connor@mergington.edu"]
    },
    "Photography Club": {
        "description": "Photography techniques, editing, and portfolio building",
        "schedule": "Saturdays, 10:00 AM - 12:00 PM",
        "max_participants": 15,
        "participants": ["maya@mergington.edu"]
    },
    "Robotics Club": {
        "description": "Build and program robots for competitions",
        "schedule": "Wednesdays and Saturdays, 3:30 PM - 5:30 PM",
        "max_participants": 16,
        "participants": ["david@mergington.edu", "nathan@mergington.edu"]
    },
    "Mathematics Olympiad": {
        "description": "Advanced problem-solving and mathematical competitions",
        "schedule": "Thursdays, 3:30 PM - 4:45 PM",
        "max_participants": 20,
        "participants": ["sophia@mergington.edu", "brandon@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Competitive soccer with training and matches",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": ["zachary@mergington.edu"]
    },
    "Track and Field": {
        "description": "Running, jumping, and athletic events",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 25,
        "participants": ["chloe@mergington.edu", "ethan@mergington.edu"]
    },
    "Ceramics Workshop": {
        "description": "Pottery, clay sculpting, and ceramic arts",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 12,
        "participants": ["lily@mergington.edu"]
    },
    "Creative Writing Club": {
        "description": "Fiction, poetry, and creative storytelling",
        "schedule": "Mondays, 3:30 PM - 4:45 PM",
        "max_participants": 16,
        "participants": ["harper@mergington.edu", "amelia@mergington.edu"]
    },
    "Model United Nations": {
        "description": "International diplomacy, debate, and advocacy",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 30,
        "participants": ["jackson@mergington.edu"]
    },
    "Computer Science Club": {
        "description": "Advanced programming, AI, and software development",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": ["madison@mergington.edu", "henry@mergington.edu"]
    },
    "Badminton Club": {
        "description": "Badminton skills, racquet techniques, and friendly competitions",
        "schedule": "Saturdays, 2:00 PM - 3:30 PM",
        "max_participants": 14,
        "participants": ["victoria@mergington.edu"]
    },
    "Cross Country Team": {
        "description": "Competitive long-distance running and trail racing",
        "schedule": "Mondays and Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": ["andrew@mergington.edu", "rachel@mergington.edu"]
    },
    "Dance Club": {
        "description": "Contemporary, hip-hop, and ballroom dance instruction",
        "schedule": "Tuesdays and Thursdays, 3:45 PM - 5:00 PM",
        "max_participants": 24,
        "participants": ["sophie@mergington.edu", "marcus@mergington.edu"]
    },
    "Painting Studio": {
        "description": "Oil, acrylic, and watercolor painting techniques",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 16,
        "participants": ["claire@mergington.edu"]
    },
    "Philosophy Club": {
        "description": "Discussion of ethics, logic, and philosophical ideas",
        "schedule": "Thursdays, 3:30 PM - 4:45 PM",
        "max_participants": 18,
        "participants": ["benjamin@mergington.edu", "olivia@mergington.edu"]
    },
    "Environmental Science Club": {
        "description": "Ecology, sustainability, and conservation projects",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": ["jessica@mergington.edu"]
    },
    "Golf Team": {
        "description": "Golf techniques, course management, and tournament play",
        "schedule": "Tuesdays and Thursdays, 3:00 PM - 4:30 PM",
        "max_participants": 12,
        "participants": ["christopher@mergington.edu"]
    },
    "Lacrosse Team": {
        "description": "Fast-paced team sport with emphasis on skill development",
        "schedule": "Mondays and Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 16,
        "participants": ["aiden@mergington.edu", "zoe@mergington.edu"]
    },
    "Sculpture Studio": {
        "description": "Stone, metal, and wood sculpture with hands-on projects",
        "schedule": "Wednesdays and Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 14,
        "participants": ["julia@mergington.edu"]
    },
    "Film Club": {
        "description": "Filmmaking, cinematography, and video production",
        "schedule": "Thursdays, 3:30 PM - 5:30 PM",
        "max_participants": 18,
        "participants": ["lucas@mergington.edu", "emma@mergington.edu"]
    },
    "Debate Competition Team": {
        "description": "Specialized training for competitive debate tournaments",
        "schedule": "Mondays and Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["michael@mergington.edu"]
    },
    "Engineering and Architecture Club": {
        "description": "Structural design, CAD modeling, and building projects",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["david@mergington.edu", "charlotte@mergington.edu"]
    }
}

@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]
    
    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student already signed up for this activity")
   
   # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
