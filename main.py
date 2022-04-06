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
    if not candidate:
        return 'Кандидат не найден!'
    return render_template('single.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def name_candidate(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    candidates_count = len(candidates)
    return render_template('search.html', candidates=candidates, candidates_count=candidates_count)


@app.route('/skill/<skill_name>')
def skill_name_candidate(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    candidates_count = len(candidates)
    return render_template('skill.html', candidates=candidates, candidates_count=candidates_count)

app.run()
