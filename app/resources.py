
from flask import Blueprint, request, jsonify

resources_blueprint = Blueprint('resources', __name__)

@resources_blueprint.route('/suggest', methods=['POST'])
def suggest_resources():
    data = request.get_json()
    severity = data.get('severity')

    # This is a placeholder for the actual resource suggestion logic
    if severity == 'high':
        resources = ["Contact a therapist", "Call a helpline"]
    elif severity == 'medium':
        resources = ["Read self-help articles", "Practice mindfulness"]
    else:
        resources = ["Talk to a friend", "Get some exercise"]

    return jsonify({"resources": resources})
