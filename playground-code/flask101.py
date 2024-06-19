from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        assert username, "Missing `username` form"
        assert password, "Missing `password` form"
        
        print(username, password)
        user = db.execute(f"SELECT rowid, * FROM users WHERE username = ? AND password = ?", (username, password)).fetchone()
        print(user)
        #assert user, "Invalid `username` or `password`"

        #return redirect(request.path, user=int(user["rowid"]))

    if "user" in request.args:
        user_id = int(request.args["user"])
        user = db.execute("SELECT * FROM users WHERE rowid = ?", (user_id,)).fetchone()
        if user:
            username = user["username"]
            if username == "flag":
                return f"{flag}\n"
            return f"Hello, {username}!\n"
    
    return 'hihihih'
if __name__ == '__main__':
    app.run
