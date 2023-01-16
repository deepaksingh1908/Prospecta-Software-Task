from flask import Flask, jsonify, request

app = Flask(_name_)

# Sample data
data = {
    "sno1": [
        {"title": "A", "description": "Description 1"},
        {"title": "B", "description": "Description 2"}
    ],
    "sno2": [
        {"title": "C", "description": "Description 3"},
        {"title": "D", "description": "Description 4"}
    ]
}

@app.route('/items', methods=['GET'])
def get_items():
    category = request.args.get('category')
    items = data.get(category, [])
    return jsonify(items)

if _name_ == '_main_':
    app.run(debug=True)