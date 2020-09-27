from flask import Flask, render_template, request
import keys as keys
import boto3
from boto3.dynamodb.conditions import Key, Attr

app = Flask(__name__)
app.secret_key = 'mausam'

dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id=keys.aws_access_key_id,
                          aws_secret_access_key=keys.aws_secret_access_key,
                          aws_session_token=keys.aws_session_token
                          )


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['post'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        table = dynamodb.Table('users')

        table.put_item(
            Item={
                'name': name,
                'email': email,
                'password': password
            }
        )
        msg = "Registration Completed!"

        return render_template('login.html', msg=msg)
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/update', methods=['post', 'GET'])
def update():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        table = dynamodb.Table('users')

        table.update_item(
            key={
                'email': email
            },
            UpdateExpression='SET name = :val1',
            ExpressionAttributeValues={
                ':val1': name
            }
        )
        msg = "name updated"

        return render_template('login.html', msg=msg)
    return render_template('update.html')


@app.route('/check', methods=['post'])
def validate():
    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        table = dynamodb.Table('users')
        response = table.query(
            KeyConditionExpression=Key('email').eq(email)
        )
        items = response['Items']
        name = items[0]['name']
        print(items[0]['password'])
        if password == items[0]['password']:
            return render_template("home.html", name=name)
    return render_template("login.html")


@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
