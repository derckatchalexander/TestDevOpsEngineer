from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)


redis_host = os.getenv('REDIS_HOST', 'localhost')


redis_client = redis.Redis(host=redis_host, port=6379, db=0)

@app.route('/ping')
def ping():
    return jsonify({'status': 'ok'})

@app.route('/count')
def count():
   
    count = redis_client.incr('visits')
    return jsonify({'visits': count})

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5000) 