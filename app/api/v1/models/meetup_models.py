from datetime import datetime

meetups = [
    {
    "createdOn": "Wed, 09 Jan 2019 07:44:28 GMT",
    "from_date": "Fri, 01 Feb 2019 08:00:00 GMT",
    "from_time": "Fri, 01 Feb 2019 17:00:00 GMT",
    "location": "Nairobi kenya",
    "meetup_id": 1,
    "organizer": "Andela",
    "tags": [
        "andela",
        "flutter"
    ],
    "title": "flutter study jam",
    "to_date": "Fri, 01 Feb 2019 17:00:00 GMT"
}
]


class MeetupModels():
    def __init__(self):
        self.db = meetups
        self.id = len(meetups) + 1
        self.now = datetime.now()

    def create_meetup(self, title, organizer, location, from_date, to_date, tags):
        """ method to add meetup """
        payload = {
            "meetup_id" : self.id,
            "title" : title,
            "organizer" : organizer,
            "createdOn" : self.now,
            "location" : location,
            "from_date" : datetime.strptime(from_date, '%m %d %Y %I:%M%p'),
            "to_date" :  datetime.strptime(to_date, '%m %d %Y %I:%M%p'),
            "from_time" :  datetime.strptime(to_date, '%m %d %Y %I:%M%p'),
            "tags" : tags
        }

        self.db.append(payload)
        return payload