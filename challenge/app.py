# app.py

import os
from flask import Flask
import redis

app = Flask(__name__)

@app.route('/')
def homepage():
    return '''
    <html>
      <head>
        <style>
          body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: lightblue;
          }
          .container {
            text-align: center;
          }
          h1 {
            color: white;
            font-weight: bold;
          }
          button {
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            background-color: white;
            color: #007BFF;
            transition: background-color 0.3s ease, transform 0.2s ease;
          }
          button:hover {
            background-color: #e6f0ff;
            transform: scale(1.05);
          }
        </style>
      </head>
      <body>
        <div class="container">
          <h1>Welcome to my Flask app</h1>
          <form action="/count">
            <button type="submit">Go to Counter</button>
          </form>
        </div>
      </body>
    </html>
    '''

@app.route('/count')
def count():
    r = redis.Redis(
        host=os.environ.get('REDIS_HOST', 'mydb'),
        port=int(os.environ.get('REDIS_PORT', 6379))
    )
    count = r.incr('counter')
    return f'''
    <html>
      <head>
        <style>
          body {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: lightblue;
          }}
          .container {{
            text-align: center;
          }}
          h1 {{
            color: white;
            font-weight: bold;
          }}
          a {{
            display: inline-block;
            margin-top: 20px;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 8px;
            text-decoration: none;
            background-color: white;
            color: #007BFF;
            transition: background-color 0.3s ease, transform 0.2s ease;
          }}
          a:hover {{
            background-color: #e6f0ff;
            transform: scale(1.05);
          }}
        </style>
      </head>
      <body>
        <div class="container">
          <h1>Counter: {count}</h1>
          <a href="/">Back to Home</a>
        </div>
      </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
