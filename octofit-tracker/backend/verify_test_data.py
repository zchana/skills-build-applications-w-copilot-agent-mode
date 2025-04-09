from pymongo import MongoClient

# Explicitly define database connection details
client = MongoClient('localhost', 27017)
db = client['octofit_db']

# Verify users collection
users = list(db.users.find())
print("Users:", users)

# Verify teams collection
teams = list(db.teams.find())
print("Teams:", teams)

# Verify activities collection
activities = list(db.activity.find())
print("Activities:", activities)

# Verify leaderboard collection
leaderboard = list(db.leaderboard.find())
print("Leaderboard:", leaderboard)

# Verify workouts collection
workouts = list(db.workouts.find())
print("Workouts:", workouts)
