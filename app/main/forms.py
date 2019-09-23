from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError, SelectField, RadioField
from wtforms.validators import Required,Email
from ..models import User

# class ReviewForm(FlaskForm):

#     title = StringField('Review title',validators=[Required()])
#     review = TextAreaField('Movie review', validators=[Required()])
#     submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    vote=RadioField('default field arguments', choices=[('1', 'UpVote'), ('1', 'DownVote')])
    submit = SubmitField('SUBMIT')  

class UpdateProfile(FlaskForm):
    bio = TextAreaField('we need your comment.',validators = [Required()])
    submit = SubmitField('Submit') 

class PitchForm(FlaskForm):
    category_id = SelectField('Select Category', choices=[('1', 'Story'), ('2', 'picking'), ('3', 'publicity'),('4','selling products')])
    content = TextAreaField('YOUR PITCH')
    submit = SubmitField('Create Pitch')

class UpvoteForm(FlaskForm):
    
    
    submit = SubmitField('Upvote')