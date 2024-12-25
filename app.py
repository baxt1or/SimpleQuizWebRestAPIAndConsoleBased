from db import get_db_connection
from flask import Flask, request, jsonify, session

app = Flask(__name__)
app.secret_key = 'hellokotlar'

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    """Quiz API."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    
    cursor.execute('SELECT * FROM questions')
    questions = cursor.fetchall()
    conn.close()

    if request.method == 'POST':
        
        user_answers = request.json
        score = 0

    
        for question in questions:
            question_id = str(question['id'])
            if question_id in user_answers and user_answers[question_id] == question['correct_option']:
                score += 1

        
        response = {
            'score': score,
            'total': len(questions),
            'message': 'Quiz submitted successfully'
        }
        return jsonify(response), 200

   
    response = {
        'questions': [
            {
                'id': question['id'],
                'question': question['question'],
                'options': {
                    'a': question['option_a'],
                    'b': question['option_b'],
                    'c': question['option_c'],
                    'd': question['option_d']
                }
            } for question in questions
        ]
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
