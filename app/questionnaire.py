
from flask import Blueprint, request, jsonify

questionnaire_blueprint = Blueprint('questionnaire', __name__)

@questionnaire_blueprint.route('/questions', methods=['GET'])
def get_questions():
    # This is a placeholder for the actual questions
    questions = {
        "phq9": [
            "Little interest or pleasure in doing things",
            "Feeling down, depressed, or hopeless",
            "Trouble falling or staying asleep, or sleeping too much",
            "Feeling tired or having little energy",
            "Poor appetite or overeating",
            "Feeling bad about yourself - or that you are a failure or have let yourself or your family down",
            "Trouble concentrating on things, such as reading the newspaper or watching television",
            "Moving or speaking so slowly that other people could have noticed. Or the opposite - being so fidgety or restless that you have been moving around a lot more than usual",
            "Thoughts that you would be better off dead, or of hurting yourself in some way"
        ],
        "gad7": [
            "Feeling nervous, anxious, or on edge",
            "Not being able to stop or control worrying",
            "Worrying too much about different things",
            "Trouble relaxing",
            "Being so restless that it is hard to sit still",
            "Becoming easily annoyed or irritable",
            "Feeling afraid as if something awful might happen"
        ]
    }
    return jsonify(questions)

@questionnaire_blueprint.route('/submit', methods=['POST'])
def submit_answers():
    data = request.get_json()
    # Here you would process the answers and run the ML model
    # For now, we'll just return a confirmation message
    return jsonify({"msg": "Answers submitted successfully"})
