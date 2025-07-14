#! /bin/bash

poetry run hypercorn runserver:app --workers 4 --bind 0.0.0.0:5000 --reload
