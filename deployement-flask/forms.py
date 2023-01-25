from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Length



class FeatureForm(FlaskForm):
    time=StringField('Time',
            validators=[DataRequired(),Length(min=2,max=20)])

    amount=StringField('Amount',
            validators=[DataRequired()])  

    v_first= StringField('V1',validators=[DataRequired()]) 

    v_last= StringField('V1',validators=[DataRequired()]) 

   

    submit=SubmitField('Sign Up')  
    