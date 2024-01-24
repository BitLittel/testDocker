#!/bin/bash

alembic upgrade head
hypercorn --bind 0.0.0.0:8000 -w 4 --reload main:main
