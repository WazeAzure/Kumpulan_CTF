import re from flask 
import Flask, render_template, request, render_template_string from subprocess 
import check_output, CalledProcessError, STDOUT

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home(): 
    cont = {} 
    if request.method == "POST": 
        if not "read" in request.form or not request.form["read"]: 
            return render_template("index.html", context=cont) 
        book = request.form["read"].lower()
        cont["book"] = book.title()
        if len(cont["book"]) > 10: 
            cont["content"] = "I don't think we would have any book with a name that long..."
            cont["status"] = "error" 
            return render_template("index.html", context=cont)
        try:
            cont["content"] = check_output(["sh", "-c", f"cat books/{book}.txt"], stderr=STDOUT).decode()
        except CalledProcessError as e: 
            cont["content"] = e.output.decode()
            cont["status"] = "error"
            return render_template("index.html", context=cont)
        cont["status"] = "success"
        return render_template("index.html", context=cont) 
    return render_template("index.html", context=cont) 

if __name__ == "__main__":
    app.run("0.0.0.0", port=1337)
