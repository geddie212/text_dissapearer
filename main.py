from flask import Flask, render_template, jsonify, request
import keyboard
import time
import os

app = Flask(__name__)

time_left = os.environ.get('TIMER')
timer_started = False
timer_clicked = False


def countdown():
    global time_left
    global timer_started
    if time_left != 0 and timer_started:
        time.sleep(1)
        time_left -= 1
        countdown()


@app.route('/show_result', methods=['POST'])
def show_result():
    global time_left
    global timer_started
    global timer_clicked
    time_left = os.environ.get('TIMER')
    timer_started = False
    text = request.form['text-box']
    return render_template('result.html', text=text, timer_clicked=timer_clicked)


@app.route('/progress')
def progress():
    global time_left
    return jsonify(result=str(time_left))


@app.route('/start')
def start():
    global time_left
    global timer_started
    global timer_clicked
    timer_clicked = True
    timer_started = True
    time_left = os.environ.get('TIMER')
    countdown()
    return render_template('start.html')


@app.route('/')
def home():
    global time_left
    global timer_started
    global timer_clicked
    timer_clicked = False
    timer_started = False
    time_left = os.environ.get('TIMER')
    return render_template('index.html', time_left=time_left)


def on_press(key):
    global time_left
    time_left = os.environ.get('TIMER')


if __name__ == '__main__':
    keyboard.on_press(on_press)
    app.run(debug=True)

