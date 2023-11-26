# pumpkin-penguin

A Near-Smart System - ANSS, is a digital scheduler, that hopefully, can be fully or near-fully automated system, with as less human interaction as possible; and easy to command when required.

Aims to help radiotherapy specialists/doctors with the following problem:

> Oncologists, physicists, or generally speaking, "radiotherapy specialists" still have to plan out patients' treatment plans, which can spread out for a long period of time (up to 40 days even); using good-ol' pens and papers.

> This leads to hard to track available time slots of an accelerator, delays and huge backlogs deal to human-error or no real-time update on current usable accelerators (either by miss-planed, skipped, or rescheduled).
Which can cause stress, with work days lasting from 0630 to 2100; and unwanted wasted time to both sides: doctors and patients.

More information: [placeholder Junction project link]()

# Required python packages

pandas, numpy, faker, flask, flask-restful, flask-cors, flask-sqlalchemy, flask-marshmallow, sqlalchemy

# npm
```bash
# Go to the repo root directory
cd path/to/this/repo/

# Generated csv files
python3 ./scripts/data_generator.py

# Spin up the db
./scripts/start_server.sh

# On a separate terminal
# Add data from csv files to the db
python3 ./scripts/add_data.py

# Go to the frontend/ and start up npm
cd ./src/frontend/
npm install && npm run dev
```
