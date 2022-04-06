from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route('/')
def page_index():
    candidates = load_candidates_from_json()

    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:id>')
def view_candidate(id):
    candidate = get_candidate(id)
    return render_template('candidate.html', candidate=candidate)


app.run(debug=True)
