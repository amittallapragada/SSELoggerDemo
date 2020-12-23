## Realtime Log Streaming with FastAPI and Server-Sent Events

![Demo](/imgs/app_demo.gif?raw=true "Optional Title")


### Setup

#### Prerequisites
To run this program you will need python 3 (I used 3.8). Then run the following commands:
- python3 -m venv py38
- source py38/bin/activate
- pip install -r requirements.txt

#### Running the code
- python server/program.py (runs the app that generates logs)
- python server/server.py (runs the web server that sends SSE)
- open client/client.html in a browser to view the events