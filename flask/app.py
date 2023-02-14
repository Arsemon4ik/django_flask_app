from flask import Flask, render_template
from flask import request, redirect
from utils import SCHEDULE, update

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'


@app.route('/', methods=['GET', 'POST'])
def index():
    """ index function is the main function which handles GET and POST requests and manage them
     Args:
     Returns:
     """
    if request.method == 'POST':
        id_list = request.form.getlist('subject')
        id_list = [int(id_) for id_ in id_list]
        update(id_list)

        return redirect('/')
    return render_template('schedule.html', subjects=SCHEDULE)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9999)
