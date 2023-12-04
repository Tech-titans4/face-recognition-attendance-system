import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendance-43e2a-default-rtdb.firebaseio.com/"
})

ref=db.reference('Students')

data={
    "01":
        {
            "name":"Mukesh Ambani",
            "major":"Reliance",
            "starting_year":1957,
            "total attendance":8,
            "standing":"A",
            "year":66,
            "last_attendance_time":"2023-11-27 08:30:50"
        },
    "02":
        {
            "name": "Ratan Tata",
            "major": "Tata",
            "starting_year":1937,
            "total attendance":7,
            "standing": "A",
            "year": 85,
            "last_attendance_time": "2023-11-27 08:37:50"
        },
    "03":
        {
            "name": "Sundar Pichai",
            "major": "Google",
            "starting_year":1972,
            "total attendance": 8,
            "standing": "A",
            "year": 51,
            "last_attendance_time": "2023-11-27 08:25:56"
        },
    "04":
        {
            "name": "Sachin Tendulkar",
            "major": "Cricket",
            "starting_year": 1973,
            "total attendance": 8,
            "standing": "A",
            "year": 50,
            "last_attendance_time": "2023-11-27 08:25:56"
        }
}

for key,value in data.items():
    ref.child(key).set(value)