from lib.L298N import L298N
from pyfirmata import Arduino
from flask import Flask, jsonify, request
app = Flask(__name__)

FALSE = 0
TRUE = 1

DELAY = 0.5

board = Arduino('/dev/ttyACM0')
# Initial pin
ena = 11
enb = 10
in1 = 7
in2 = 6
in3 = 5
in4 = 4
motor = L298N(board, ena, in1, in2, in3, in4, enb)


@app.route('/')
def home():
    return 'What you look on here!!!'


@app.route('/forward')
def forward():
    speed = float(request.args.get('speed'))
    # if not speed.digit():
    #     return jsonify({'status': FALSE, 'message': 'Speed must digit'})
    motor.forward(speed, DELAY)
    return jsonify({'status': TRUE})

@app.route('/backward')
def backward():
    speed = float(request.args.get('speed'))
    # if not speed.digit():
    #     return jsonify({'status': FALSE, 'message': 'Speed must digit'})
    motor.backward(speed, DELAY)
    return jsonify({'status': TRUE})

@app.route('/left')
def left():
    speed = float(request.args.get('speed'))
    # if not speed.digit():
    #     return jsonify({'status': FALSE, 'message': 'Speed must digit'})
    motor.turn_left(speed, DELAY)
    return jsonify({'status': TRUE})

@app.route('/right')
def right():
    speed = float(request.args.get('speed'))
    # if not speed.digit():
    #     return jsonify({'status': FALSE, 'message': 'Speed must digit'})
    motor.turn_right(speed, DELAY)
    return jsonify({'status': TRUE})

@app.route('/stop')
def stop():
    motor.full_stop(DELAY)
    return jsonify({'status': DELAY})
