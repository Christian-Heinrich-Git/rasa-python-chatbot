# This is a Chatbot written with Rasa and Python

## Instructions to run the Bot

### NOTE: Chatbot is in German

1. Install python3.7
2. Install virtualenv: python3.7 -m pip install virtualenv
3. Create virtualenv: python3.7 -m virtualenv venv
4. Activate virtualenv: source venv/bin/activate
5. Install Rasa: python3.7 -m pip install rasa
6. Install dependencies for Rasa actions: python3.7 -m pip install urllib3
7. Train the Rasa model: rasa train
8. Start the Rasa actions: rasa run actions
9. Talk to the model: rasa shell
