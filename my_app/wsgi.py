# Flask does not have a WSGI HTTP Server, so for this tutorial, we will use the most common library Gunicorn. For this, we will create a new wsgi.py file.
# You can now run wsgi.py locally and see the outcomes.

from my_app.app import app

if __name__ == "__main__":
    app.run()