# This is a Chatbot written with Rasa and Python

## Instructions to run the Bot

### NOTE: Chatbot is in German

1. Install python3.7
2. Install virtualenv: `python3.7 -m pip install virtualenv`
3. Create virtualenv: `python3.7 -m virtualenv venv`
4. Activate virtualenv: `source venv/bin/activate`
5. Install Rasa: `python3.7 -m pip install rasa`
6. Install dependencies for Rasa actions: `python3.7 -m pip install urllib3`
7. Train the Rasa model: `rasa train`
8. Start the Rasa actions: `rasa run actions`
9. Talk to the model: `rasa shell`

## If you want to use a browser widget

1. Run the index.html with python `python3.7 -m http.server`
2. Run the rasa chat with api enabled `rasa run --enable-api --cors="*"`

## To run the python actions successfully you have to install certificates

1. Go to your Application Folder
2. Go into Python 3.7
3. Run the `Install Certificates.command` file
