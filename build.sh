#!/usr/bin/env bash
set -o errexit

echo "===== build.sh: installing dependencies ====="
pip install -r requirements.txt

echo "===== build.sh: showing pip list (should include gunicorn) ====="
pip list

echo "===== build.sh: checking which gunicorn ====="
which gunicorn || echo "gunicorn not found in PATH"

echo "===== build.sh: collecting static files ====="
python manage.py collectstatic --noinput

echo "===== build.sh: applying migrations ====="
python manage.py migrate

echo "===== build.sh: build.sh completed ====="

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
