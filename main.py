from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as sql
app = Flask(__name__)

connection = sql.connect(
    host="127.0.0.1",
    user="root",
    port=3306,
    database="crud"
)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form['bookname']
        author = request.form['authorname']
        publication = request.form['publicationname']
        availability = request.form['availability']
        try:
            cursor = connection.cursor() 
            cursor.execute("INSERT INTO books (book_name, authorname, publicationname, availability) VALUES (%s, %s, %s, %s)",
                        (name, author, publication, availability))
            connection.commit()   
            cursor.close()   

            return redirect(url_for('show_database'))
        except Exception as e:
            print("Registration error:", e)

    return render_template('index.html')


@app.route("/data")
def show_database():
    return render_template('data.html')


if __name__ == "__main__":
    app.run(debug=True)
