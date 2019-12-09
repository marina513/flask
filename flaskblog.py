from flask import Flask, render_template, url_for, flash , redirect
from forms import RegistrationForm , LoginForm
  #import flask class
  #url_for btgeeb el css
										  # btst5dm l load mn bra

#The configuration files are organized into sections, and 
#each section can contain name-value pairs for configuration data
# tre2a ezae bngen el rkm eltoeel
# python  import secrets  secrets.token_hex(3dd bits el rkm 16 msln)  exit()



app = Flask(__name__)     #create object of flask 
app.config['SECRET_KEY'] = '7367e30d624d196c037260aae7a5e120'

#el klam nfso betnada t7t fe return home
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")  #decorator--->which URL should call 
                 #associated fn,,lma URL da etft7 de fn 
                 #ele httnfz


@app.route("/home")
def home():
    return render_template('home.html', posts=posts)



@app.route("/about")
def about():
    return render_template('about.html',title= 'About')


# methods=['GET', 'POST'] ---> de el 7agat ele hae3mlha , get e3ne hae
# Both GET and POST method is used to transfer data from client to server in 
#HTTP protocol but Main difference between POST and GET method is that GET 
#carries request parameter appended in URL string while POST carries request 
#parameter in message body which makes it 
#more secure way of transferring data from client to server in http protocol.

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()  # instance of Reg.Form
    
    #3shan el user et2kd eno 3aml submit
    #flash e3ne alert w "seccess" da no3 el alert
    # f e3ne feh variable haet7t
    # hnrg3o tane ll home lma e5ls
    # lazm nzhr el msg fe layout 3shan aked msh htb2a f hao
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    
    return render_template('register.html', title='Register', form=form)



@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
     
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
 
    return render_template('login.html', title='Login', form=form)








if __name__ == '__main__':  # we run script with python directlt 
                            # t2rebn m3nah eno mtosl bl command prompt
    app.run(debug=True)    #ze hna bdl mnktbha 3la prompt ktbnaha hna 3ade 