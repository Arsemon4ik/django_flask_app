from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

SCHEDULE = [
    {
        "id": 1,
        "schedule_name": "Django лабораторна 1",
        "is_passed": False
    },
    {
        "id": 2,
        "schedule_name": "Flask лабораторна 3",
        "is_passed": False
    },
    {
        "id": 3,
        "schedule_name": "Вища математика тест 2",
        "is_passed": False
    },

]

STATE = set()


def update(list) -> None:
    """ Update function takes list and toggle the value of is_passed
    Args:
        list: [List of checked ids]
    Returns:
    """
    global STATE
    if list:
        # check if values are removed from list and remain in STATE
        for id in sorted(STATE, key=int):
            if id not in list:
                for subject in SCHEDULE:
                    if subject["id"] == int(id):
                        subject['is_passed'] = 0
                        STATE.remove(int(id))
    else:
        reset()
        STATE = set()

    # add new values to STATE
    for id in list:
        for subject in SCHEDULE:
            if subject["id"] == int(id):
                subject['is_passed'] = 1
                STATE.add(int(id))


def reset():
    """ reset function reset all the values of DB
     Args:
     Returns:
     """
    for subject in SCHEDULE:
        subject['is_passed'] = False


@app.route('/', methods=['GET', 'POST'])
def index():
    """ index function is the main function which handles GET and POST requests and manage them
     Args:
     Returns:
     """
    if request.method == 'POST':
        id_list = request.form.getlist('subject')
        id_list = [int(id) for id in id_list]
        update(id_list)

        return redirect('/')
    return render_template('schedule.html', subjects=SCHEDULE)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9999)
