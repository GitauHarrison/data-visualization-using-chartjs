from crypt import methods
from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.forms import LoginForm, RegistrationForm, MeanScore
from app.models import User, Meanscore
from flask_login import current_user, login_user, logout_user, login_required


@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    teacher = User.query.filter_by(email=current_user.email).first()
    form = MeanScore()
    if form.validate_on_submit():
        meanscore = Meanscore(
            term=form.term.data,
            math=form.math.data,
            english=form.english.data,
            science=form.science.data,
            ict=form.ict.data,
            history=form.history.data,
            author=current_user)
        db.session.add(meanscore)
        db.session.commit()
        flash('Your mean score has been recorded.')
        return redirect(url_for('index'))

    term_meanscore = teacher.meanscores.all()
    terms = []
    math = []
    english = []
    science = []
    ict = []
    history = []
    for term in term_meanscore:
        terms.append(term.term)
        math.append(term.math)
        english.append(term.english)
        science.append(term.science)
        ict.append(term.ict)
        history.append(term.history)
    print(terms)
    print(math)
    return render_template(
        'index.html',
        form=form,
        title='Home',
        teacher=teacher,
        terms=terms,
        math=math,
        english=english,
        science=science,
        ict=ict,
        history=history)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        flash('Welcome back!')
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Successfully registered! You can now log in.')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
