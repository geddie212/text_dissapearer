from flask import Flask, render_template, jsonify, request
import keyboard
import time

app = Flask(__name__)

time_left = 10
timer_started = False
timer_clicked = False


def countdown():
    global time_left
    global timer_started
    if int(time_left) != 0 and timer_started:
        time.sleep(1)
        time_left = int(time_left) - 1
        print(f'time left: {time_left}')
        countdown()


@app.route('/show_result', methods=['POST'])
def show_result():
    global time_left
    global timer_started
    global timer_clicked
    time_left = 10
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
    time_left = 10
    countdown()
    return render_template('start.html')


@app.route('/')
def home():
    global time_left
    global timer_started
    global timer_clicked
    timer_clicked = False
    timer_started = False
    time_left = 10
    return render_template('index.html', time_left=time_left)


def on_press(key):
    global time_left
    time_left = 10


if __name__ == '__main__':
    keyboard.on_press(on_press)
    app.run(debug=True)

