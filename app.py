from flask import Flask, request, jsonify

app = Flask(__name__)

items = [
    {
        "name": "Juice",
        "rate": 46
    },
    {
        "name": "Pastry",
        "rate": 67
    }
]


@app.get('/get-items')
def get_items():
    return {"items": items}

@app.post('/add-item')
def add_item():
    request_items = request.get_json()
    if 'name' not in request_items or "rate" not in request_items:
        return {"message":"name and rate must be there"},404
    items.append(request_items)
    return {"message": "Item added successfully"}, 201

# Dynamic Url Type 1
@app.get('/get-item/<string:name>')
def get_item(name):
    for item in items:
        if name == item["name"]:
            return item
    return {"message":"Item not founded in the list"}

# Dynamic Url using parameter
@app.get('/get-itemp')
def get_itemp():
    name = request.args.get('name')
    for item in items:
        if name == item["name"]:
            return item
    return {"message":"Item not founded in the list"}

@app.put('/update-item')
def update_item():
    request_data = request.get_json()
    if 'name' not in request_data or "rate" not in request_data:
        return {"message":"name and rate must be there"},404
    for item in items:
        if request_data['name'] == item["name"]:
            item['rate'] = request_data['rate']
            return {'message':'Item Updated Successfully'}
    return {"message": "Item not Updated"}

@app.delete('/delete-item/<string:name>')
def delete_item(name):
    for item in items:
        if name == item["name"]:
            items.remove(item)
            return {'message':'Item Deleted Successfully'}
    return {"message": "Item not Deleted"}




if __name__ == "__main__":
    app.run(debug=True)
