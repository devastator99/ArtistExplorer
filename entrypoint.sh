# Example entrypoint.sh script
python manage.py migrate --no-input
python manage.py collectstatic --no-input

# Set up a superuser if needed

# Start Gunicorn with the correct binding
gunicorn crudproject.wsgi:application --bind 0.0.0.0:$PORT
