# Cipher the AI assistant

To install the required modules, run: `pip install -r requirements`

It is recommended to create a virtual environment for this assistant. You can search `how to create virtual environment in python`

You need to install one more module after this which when we try to install using pip, gives use error and that module is PyAudio.

To install it, run: `pywin install pyaudio`

After the installation is complete without any error, your AI assistant is ready to take your commands.

To start cipher, run: `python assistant.py`

## Extra features

To use features such as receiving latest news and weather report, you need to set their corresponding api keys and other related parameters.

### Latest news

We will use Times of India for this. Obtain Times of India API key. You can obtain the API key from [here](https://newsapi.org/register). Now run the following command in the terminal.
`set news_api=<API KEY>`

### Weather Report

We will use Google Open Weather service. Obatin the API key from their official website and run the following command in the terminal.  
`set weather_api=<API KEY>`