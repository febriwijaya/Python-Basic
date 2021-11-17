import os
from datetime import datetime
from config import db
from models import Directors, Movies

# Data to initialize database with
DIRECTORS = [
    {
        "name": "James Cameron",
        "gender": "2",
        "uid" : "2710",
        "department" : "Directing",
        "movies": [
            ("Titanic", "200000000", "100", "1997-11-18", "1845034188", "Titanic", "7.5", "7562", "84 years later, a 101-year-old woman named Rose DeWitt Bukater tells the story to her granddaughter Lizzy Calvert, Brock Lovett, Lewis Bodine, Bobby Buell and Anatoly Mikailavich on the Keldysh about her life set in April 10th 1912, on a ship called Titanic when young Rose boards the departing ship with the upper-class passengers and her mother, Ruth DeWitt Bukater, and her fiancé, Caledon Hockley. Meanwhile, a drifter and artist named Jack Dawson and his best friend Fabrizio De Rossi win third-class tickets to the ship in a game. And she explains the whole story from departure until the death of Titanic on its first and last voyage April 15th, 1912 at 2:20 in the morning.", "Nothing on Earth could come between them.", "597"),
            ("Terminator 2: Judgment Day", "100000000", "101", "1991-07-01", "520000000", "Terminator 2: Judgment Day", "7.7", "4185", "Nearly 10 years have passed since Sarah Connor was targeted for termination by a cyborg from the future. Now her son, John, the future leader of the resistance, is the target for a newer, more deadly terminator. Once again, the resistance has managed to send a protector back to attempt to save John and his mother Sarah.", "It's nothing personal.", "280"),
            ("True Lies", "115000000", "38", "1994-07-14", "378882411", "True Lies", "6.8", "1116", "Harry Tasker is a secret agent for the United States Government. For years, he has kept his job from his wife, but is forced to reveal his identity and try to stop nuclear terrorists when he and his wife are kidnapped by them.", "When he said I do, he never said what he did.", "36955"),
            ("The Abyss", "70000000", "24", "1989-08-09", "90000098", "The Abyss", "7.1", "808", "A civilian oil rig crew is recruited to conduct a search and rescue effort when a nuclear submarine mysteriously sinks. One diver soon finds himself on a spectacular odyssey 25,000 feet below the ocean's surface where he confronts a mysterious force that has the power to change the world or destroy it.", "There's everything you've ever known about adventure, and then there's The Abyss.", "2756"),
            ("Aliens", "18500000", "67", "1986-07-18", "183316455", "Aliens", "7.7", "3220", "When Ripley's lifepod is found by a salvage crew over 50 years later, she finds that terra-formers are on the very planet they found the alien species. When the company sends a family of colonists out to investigate her story, all contact is lost with the planet and colonists. They enlist Ripley and the colonial marines to return and search for answers.", "This Time It's War", "679"),
            ("The Terminator", "6400000", "74", "1984-10-26", "78371200", "The Terminator", "7.3", "4128", "In the post-apocalyptic future, reigning tyrannical supercomputers teleport a cyborg assassin known as the Terminator back to 1984 to kill Sarah Connor, whose unborn son is destined to lead insurgents against 21st century mechanical hegemony. Meanwhile, the human-resistance movement dispatches a lone warrior to safeguard Sarah. Can he stop the virtually indestructible killing machine?", "Your future is in his hands.", "218")
        ],
    },
]

# Delete database file if it exists currently
if os.path.exists('final_proj.db'):
    os.remove('final_proj.db')

# Create the database
db.create_all()

# Iterate over the DIRECTORS structure and populate the database
for directors in DIRECTORS:
    p = Directors(name=directors.get("name"), gender=directors.get("gender"), uid=directors.get("uid"), department=directors.get("department"))

    # Add the moviess for the directors
    for movies in directors.get("movies"):
        original_title, budget, popularity, release_date, revenue, title, vote_average, vote_count, overview, tagline, uid = movies
        p.movies.append(
            Movies(
                original_title=original_title,
                budget=budget,
                popularity=popularity,
                release_date=release_date,
                revenue=revenue,
                title=title,
                vote_average=vote_average,
                vote_count=vote_count,
                overview=overview,
                tagline=tagline,
                uid=uid,
            )
        )
    db.session.add(p)

db.session.commit()