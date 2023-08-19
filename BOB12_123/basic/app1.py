from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route('/')

def index():
    
    # GET parameter 처리하는 방법 
    user_name = request.args.get('name')
    print(user_name)
    

    users = [
        {'name': 'Alice', 'age': 25, 'phone': '123-456-7890'},
        {'name': 'Bob', 'age': 30, 'phone': '987-654-3210'},
        {'name': 'Charlie', 'age': 35, 'phone': '555-123-4567'}
    ]
    
    if user_name:
        search_user = []
        for u in users:
            if u['name'] == user_name:
                search_user.append(u)
        
    
    return render_template('user.html',users=users)


if __name__ == "__main__":
    
    app.run(debug=True)


