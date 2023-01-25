from flask import Flask,render_template,url_for,request
from forms import FeatureForm


app=Flask(__name__)

app.config['SECRET_KEY']='1c04928469c5e375cb8a123d94bd551a'
@app.route('/')
def home():
    form=FeatureForm()
    
    return render_template('home.html',form=form)


@app.route('/prediction',methods=['Post'])
def predict():
    form=FeatureForm()
    if form.validate_on_submit():

        Time=eval(form.time.data)
        Amount=eval(form.amount.data)
        V1=eval(form.v_first.data)
        V28=eval(form.v_last.data)
        rsult=Time+Amount+V1+V28

    msg=""
    # return render_template('predictions.html',time=Time,amount=Amount,v_fist=V1,v_last=V28,result=rsult)
    if rsult==0:
        msg="The Transaction is Not Fraudulent".title()
        return render_template("results.html",message=msg)

    msg=" Aew Aew Transaction is  Fraudulent".title()
    return render_template("results.html",message=msg)




if __name__=='__main__':
    app.run(debug=True)