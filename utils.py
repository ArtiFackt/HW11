import json

path = 'candidates.json'


def load_candidates_from_json():
    """возвращает список всех кандидатов
    """
    with open(path, 'r', encoding='utf8') as file:
        data = json.load(file)
    return data


def get_candidate(candidate_id):
    '''возвращает одного кандидата по его id
    '''
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    '''возвращает кандидатов по имени
    '''
    candidates = load_candidates_from_json()
    name_candidate = []
    name_lower = candidate_name.lower()

    for candidate in candidates:
        name = candidate['name'].lower().split(', ')
        if name_lower in name:
            name_candidate.append(candidate)
    return name_candidate


def get_candidates_by_skill(skill_name):
    '''возвращает кандидатов по навыку
    '''
    candidates = load_candidates_from_json()
    skill_candidate = []
    skill_lower = skill_name.lower()

    for candidate in candidates:
        candidate_skills = candidate['skills'].lower().split(', ')
        if skill_lower in candidate_skills:
            skill_candidate.append(candidate)
    return skill_candidate
