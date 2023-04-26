from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired
from scraper import Scraper


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class Request(FlaskForm):
    job_title = StringField("Job Title", validators=[DataRequired()], render_kw={"placeholder": "Python Developer"})
    job_location = StringField("Job location", validators=[DataRequired()],render_kw={"placeholder": "Kyiv, Ukraine"} )
    experience_level = SelectField("Experience level",choices=[('no_exp', 'No experience'), ('1y', '1 year'), ('2y', '2 years'),('3y', '3 years'),('5y', '5+ years')], validators=[DataRequired()],render_kw={"placeholder": "Middle"} )
    job_type = SelectMultipleField("Job Type",choices=[('office', 'full-time'), ('parttime', 'part-time'), ('remote', 'remote')], validators=[DataRequired()],render_kw={"placeholder": "Middle"} )
    salary_info =SelectField("Salary",choices=[('', 'Any'), ('1500', '$1500'), ('2500', '$2500'), ('3500', '$3500'),('5500', '$5500')], validators=[DataRequired()],render_kw={"placeholder": "Middle"} )


    submit = SubmitField("Submit")



@app.route('/',methods = ["GET", "POST"])
def home():
    form = Request()
    if form.validate_on_submit():
        title = form.job_title.data
        location = form.job_location.data
        experience = form.experience_level.data
        type = form.job_type.data
        salary = form.salary_info.data

        scraper = Scraper(title, location, experience, type, salary)
        result_djinni = scraper.get_info_djinni()
        result_dou = scraper.get_info_dou()
        result_linkedin = scraper.get_info_linkedin()


        return render_template('result.html', result_djinni = result_djinni, result_dou = result_dou, result_linkedin = result_linkedin)

    return render_template('index.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)