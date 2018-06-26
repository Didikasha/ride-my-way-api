# ride-my-way-api
Ride-My-way is a carpooling application that provides drivers with the ability to create ride offers and passengers to join available ride offers

This repository contains Flask API endpoints and tests for the ride-my-way Application.

## Runnning Application
Clone Repo From GitHub
```
git clone https://github.com/didikasha/ride-my-way-api.git
```
Enter Directory
```
cd ride-my-way-api
```
Create Virtual Environment
```
virtualenv -p python3 venv
```
Start virtualenv
```
source rides/bin/activate
```
Install Dependencies
```
pip install -r requrements.txt
```
Run app
```
python run.py
```
## Available API Endpoints

| Endpoint | Description |
| --- | --- |
| POST /api/v1/rides | Adds a New ride
| GET /api/v1/books | Retrieves All Rides
| GET /api/v1/request/<string: rideId> | Get ride by id
| POST /api/v1/requests/<int: ride_Id> | request a ride
| POST /api/v1/user/register | Register a New User
| POST /api/v1/user/login | Logs in a registered User