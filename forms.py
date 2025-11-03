from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, RadioField, PasswordField, TextAreaField, IntegerField, SelectField
from wtforms.validators import InputRequired, DataRequired, Email, EqualTo, Length

class HomeForm(FlaskForm):
    project_name = StringField("Project Name:", validators=[InputRequired()])
    marketplace = RadioField("Marketplace:", validators=[InputRequired()])
    submit = SubmitField("Submit")
    
class RegisterForm(FlaskForm): 
    username = StringField("Username: ", validators=[InputRequired()])
    password = PasswordField("Password: ", validators=[InputRequired()])
    confirm_password = PasswordField("Confirm Password:", validators=[InputRequired()])
    submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')
    
class ReviewForm(FlaskForm):
    user = StringField('User', default='Anonymous')
    review = TextAreaField('Review', validators=[DataRequired()])
    submit = SubmitField('Submit')

class BizzarForm(FlaskForm):
    bizzar_id = IntegerField('Bizzar ID', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    reward_pledge_amount = IntegerField('Pledge Amount ($)', validators=[DataRequired()])
    objectives = SelectField('Objectives', choices=[
        ('1', 'To take over the word!'),
        ('2', 'To take care of six cats'),
        ('3', "To wash the dishes"),
        ('4', "To build wealth"),
        ('5', "To donate to charity")], validators=[DataRequired()])
    category = SelectField('Category',choices=[
        ('1', 'Art & Design'),
        ('2', 'Comics'),
        ('3', 'Crafts'),
        ('4', 'Dance'),
        ('5', 'Technology and Innovation'),
        ('6', 'Design'),
        ('7', 'Film and Video'),
        ('8', 'Culture and Society'),
        ('9', 'Theater'),
        ('10', 'Environment & Sustainability'),
        ('11', 'Education and Learning'),
        ('12', 'Entertainment and Media')], validators=[DataRequired()])
    traits = SelectField('Traits', choices=[
        ('1', 'social movements'),
        ('2', 'historical perspectives'),
        ('3', 'cultural differences'),
        ('4', 'ecological issues'),
        ('5', 'sustainable living'),
        ('6', 'green technology'),
        ('7', 'educational tools'),
        ('8', 'online courses'),
        ('9', 'music'),
        ('10', 'movies'),
        ('11', 'books'),
        ('12', 'video games'),
        ('13', 'color'),
        ('14', 'digital art'),
        ('15', 'sculpture'),
        ('16', 'design trends'),
        ('17', 'gadgets'),
        ('18', 'software development'),
        ('19', 'futuristic concepts')], validators=[DataRequired()])
    characteristics = SelectField('Characteristics', choices =[('1', 'confidence'),
        ('2', 'curious'),
        ('3', 'loyal'),
        ('4', 'creativity'),
        ('5', 'optimism'),
        ('6', 'disciplined'),
        ('7', 'honesty'),
        ('8', 'loyalty')],validators=[DataRequired()])
    
    submit = SubmitField('Submit')

class EditForm(FlaskForm):
    bizzar_id = IntegerField('Bizzar ID', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    reward_pledge_amount = IntegerField('Pledge Amount ($)', validators=[DataRequired()])
    objectives = SelectField('Objectives', choices=[
        ('1', 'To take over the world!'),
        ('2', 'To take care of six cats'),
        ('3', "To wash the dishes"),
        ('4', "To build wealth"),
        ('5', "To donate to charity")], validators=[DataRequired()])
    category = SelectField('Category',choices=[
        ('1', 'Art & Design'),
        ('2', 'Comics'),
        ('3', 'Crafts'),
        ('4', 'Dance'),
        ('5', 'Technology and Innovation'),
        ('6', 'Design'),
        ('7', 'Film and Video'),
        ('8', 'Culture and Society'),
        ('9', 'Theater'),
        ('10', 'Environment & Sustainability'),
        ('11', 'Education and Learning'),
        ('12', 'Entertainment and Media')], validators=[DataRequired()])
    traits = SelectField('Traits', choices=[
        ('1', 'social movements'),
        ('2', 'historical perspectives'),
        ('3', 'cultural differences'),
        ('4', 'ecological issues'),
        ('5', 'sustainable living'),
        ('6', 'green technology'),
        ('7', 'educational tools'),
        ('8', 'online courses'),
        ('9', 'music'),
        ('10', 'movies'),
        ('11', 'books'),
        ('12', 'video games'),
        ('13', 'color'),
        ('14', 'digital art'),
        ('15', 'sculpture'),
        ('16', 'design trends'),
        ('17', 'gadgets'),
        ('18', 'software development'),
        ('19', 'futuristic concepts')], validators=[DataRequired()])
    characteristics = SelectField('Characteristics', choices=[
        ('1', 'confidence'),
        ('2', 'curious'),
        ('3', 'loyal'),
        ('4', 'creativity'),
        ('5', 'optimism'),
        ('6', 'disciplined'),
        ('7', 'honesty'),
        ('8', 'loyalty')], validators=[DataRequired()])
    submit = SubmitField('Update')

class RecommendForm(FlaskForm): 
    criteria = SelectField('What beings you to Bizzar Bazzar today?', choices = [('I want to raise money for charity'), ('I am in a dire financial situation and I would like to do what is best in order to save myself'), ('I am interested in creating a startup and eating better')],validators=[DataRequired()])
    interest_level = RadioField('How interested are you in our products?', choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], default='medium')
    product_preference = SelectField('What kind of products are you interested in?', choices=[('tech', 'Technology'), ('books', 'Books'), ('clothes', 'Clothes'), ('art', 'Art')])
    comments = TextAreaField('Any comments or suggestions?')
    recommend = SubmitField('Recommend')
    submit = SubmitField('Submit')

class AdminRegisterForm(FlaskForm): 
    admin_username = StringField('Username', validators=[DataRequired()])
    admin_password = PasswordField('Password', validators=[DataRequired(), Length(min=5)])
    confirm_password = PasswordField("Confirm Password:", validators=[InputRequired()])
    submit = SubmitField('Log In')

class AdminLoginForm(FlaskForm):
    admin_username = StringField('Username', validators=[DataRequired()])
    admin_password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class ResetPasswordForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('New Password', validators=[DataRequired(), Length(min=5)])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), Length(min=5), EqualTo('password', message='Passwords must match.')]
    )
    submit = SubmitField('Reset Password')

class ResetAdminPasswordForm(FlaskForm): 
    admin_username = StringField('Username', validators=[DataRequired()])
    admin_password = PasswordField('New Password', validators=[DataRequired(), Length(min=5)])
    admin_password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), Length(min=5), EqualTo('admin_password', message='Passwords must match.')]
    )
    submit = SubmitField('Reset Password')



class InvestorForm(FlaskForm):
    investor = RadioField('Choose an investor', validators=[DataRequired()])
    submit = SubmitField('Submit')

class DeleteUserForm(FlaskForm):
    pass

