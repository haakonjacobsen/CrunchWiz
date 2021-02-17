# IT2901 CrunchWiz

CrunchWiz computes measurements from devices like tobi eyetrakers, Empatica E4 wristband and skeltal data from openPose.

## Dashboard

### Start dashboard

- `cd frontend && yarn start`

### Start websocket

- `cd backend/websocket && python3 websocket.py`

## CrunchWiz

- `cd backend && python3 app.py`

## Test
* backend test `pytest --cov=backend/` 
* frontend lint `yarn lint`
* backend lint `flake8`
* backend check import order `isort`

