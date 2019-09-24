from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def validation():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    username_errors = validate_username(username)
    password_errors = validate_password(password, verify)
    verify_errors = validate_verify(verify)
    email_errors = validate_email(email)
    if not username_errors and not password_errors and not verify_errors and not email_errors:
        return render_template('welcome.html', username=username)

    return render_template('index.html', username=username, username_errors=username_errors, password=password,
                               password_errors=password_errors, verify=verify, verify_errors=verify_errors, email=email,
                               email_errors=email_errors)

def validate_username(username):
    if not username:
        return 'Please enter a username'
    if len(username) < 3 or len(username) > 20:
        return 'Invalid username length'
    if ' ' in username:
        return 'Invalid username please remove spaces'
    return ''

def validate_password(password, verify):
    if not password:
        return 'Please enter a password'
    if len(password) < 3 or len(password) > 20:
        return 'Invalid password length'
    if ' ' in password:
        return 'Invalid password please remove spaces'
    if password != verify:
        return 'Password and verification do not match'
    return ''

def validate_verify(verify):
    if not verify:
        return 'Please enter a verification password'
    return ''


def validate_email(email):
    if email:
        if len(email) < 3 or len(email) > 20:
            return 'Please enter a valid email'
        if count_character('.',email) != 1:
            return 'Please enter a valid email'
        if count_character('@',email) != 1:
            return 'Please enter a valid email'
        if ' ' in email:
            return 'Please enter a valid email'
    return ''

def count_character(character, string):
    count = 0
    for i in string:
        if i == character:
            count = count+1
    return count


if __name__ == '__main__':
    app.run()
