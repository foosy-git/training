from flask import Flask, render_template, request
import pymysql.cursors

app = Flask(__name__)

# Set up a connection to your MySQL database
mydb = pymysql.connect(
    host='localhost',
    user='root',
    password='9137652j',
    db='project',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# Route for the web interface to enter SQL queries
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the user's SQL query
@app.route('/query', methods=['POST'])
def query():
    # Get the user's query from the form data
    user_query = request.form['query']

    # Sanitize the user's query to prevent SQL injection attacks
    sanitized_query = pymysql.escape_string(user_query)

    # Execute the user's query on your MySQL database
    with mydb.cursor() as cursor:
        cursor.execute(sanitized_query)
        results = cursor.fetchall()

    # Display the results of the user's query
    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run()