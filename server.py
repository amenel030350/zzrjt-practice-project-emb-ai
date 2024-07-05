from flask import Flask, request, jsonify
from sentiment_analysis import sentiment_analyzer
import json

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    text_to_analyze = data.get('text', '')
    if not text_to_analyze:
        return jsonify({'error': 'No text provided'}), 400
    
    result = sentiment_analyzer(text_to_analyze)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
