from flask import Flask
import database
import pretty_errors

app = Flask(__name__)
db = database.Database("res\\database.db")

db.create_tables()

@app.route('/add/<user_token>/<friend_token>')
def register_friendship(user_token, friend_token):
    db.cursor.execute("INSERT INTO users VALUES (?, ?)", (user_token, friend_token))
    db.connection.commit()
    return "200"

@app.route('/check/<user_token>')
def check_friendship(user_token):
    db.cursor.execute("SELECT * FROM users WHERE friend=?", (user_token,))
    return str(db.cursor.fetchall()[0][0])

@app.route('/debug/')
def debug():
    db.cursor.execute("SELECT * FROM users")
    db.connection.commit()
    for i in db.cursor.fetchall():
        print(i)
    return "check console bro"

if __name__ == "__main__":
    app.run(debug = True)
    db.close_connection()