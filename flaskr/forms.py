from wtforms import Form, StringField, TextAreaField, PasswordField, validators


class RegistrationForm(Form):
    username = StringField('Username', [
        validators.Length(message="Username must be between 4 and 25 characters", min=4, max=25)
    ])
    email = StringField('Email Address', [
        validators.Email(message="Must be valid email", check_deliverability=True)
    ])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.Length(message="Passwords must be at least 8 characters", min=8),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')


class LoginForm(Form):
    username = StringField('Username', [])
    password = PasswordField('Password', [])


class CreatePostForm(Form):
    title = StringField('Title', [
        validators.DataRequired(message="Title is required"),
        validators.Length(message="Title must be less than 32 characters", max=32)
    ])
    body = TextAreaField('Body', [
        validators.DataRequired(message="Post must not be empty"),
        validators.Length(message="Post must be less than 1024 characters", max=1024)
    ])