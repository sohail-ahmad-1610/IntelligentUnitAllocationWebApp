from flask import Flask, render_template, redirect, url_for, request, session
from flask_paginate import Pagination, get_page_args

app = Flask(__name__)
app.template_folder = 'templates'
users = list(range(100))


def get_users(offset=0, per_page=10):
    return users[offset: offset + per_page]


def getAllDefaultExperties():
    expertiesDict = {}
    expertiesDict['C100'] = 'C'
    expertiesDict['C101'] = 'C++'
    expertiesDict['C102'] = 'Java'
    expertiesDict['C103'] = 'Python'
    return expertiesDict

# Route for handling the login page logic
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin' or request.form['loginUserRole'] != 'ADMIN':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['loggedInUser'] = request.form['username']

            if request.form['loginUserRole'] == "ADMIN":
                return redirect(url_for('index'))
    return render_template('login1.html', error=error)


@app.route('/logout')
def logout():
    if session:
        session.clear()
    return redirect(url_for('login'))


@app.route('/index')
def index():
    if session.get('loggedInUser') is None:
        return redirect(url_for('login'))
    else:
        page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
        total = len(users)
        pagination_users = get_users(offset=offset, per_page=per_page)
        pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
        return render_template('index.html',
                           users=pagination_users,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )
    return render_template('index.html')


@app.route('/lecturers', methods=['POST','GET'])
def getLecturersList():
    if session.get('loggedInUser') is None:
        return redirect(url_for('login'))
    else:
        page, per_page, offset = get_page_args(page_parameter='page',
                                               per_page_parameter='per_page')
        total = len(users)
        pagination_users = get_users(offset=offset, per_page=per_page)
        pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
        return render_template('lecturersCRUD.html',users=pagination_users,page=page,per_page=per_page,pagination=pagination,
                               expertiesDict = getAllDefaultExperties())
    return render_template('login1.html')


@app.route('/addLecturer', methods=['POST'])
def addLecturer():
    if session.get('loggedInUser') is None:
        return redirect(url_for('login'))
    else:
        error = None
        if request.method == 'POST':
            lecturerName = request.form['lecturerName']
            lecturerType = request.form['lecturerType']
            lecturerExperties = request.form.getlist('lecturerExperties')

            '''Getting Class Routines of Lecturer...'''
            mondayStartTime = request.form['mondayStartTime']
            mondayEndTime = ''
            if mondayStartTime != '':
                mondayEndTime = request.form['mondayEndTime']

            tuesdayStartTime = request.form['tuesdayStartTime']
            tuesdayEndTime = ''
            if tuesdayStartTime != '':
                tuesdayEndTime = request.form['tuesdayEndTime']

            wednesdayStartTime = request.form['wednesdayStartTime']
            wednesdayEndTime = ''
            if wednesdayStartTime != '':
                wednesdayEndTime = request.form['wednesdayEndTime']

            thursdayStartTime = request.form['thursdayStartTime']
            thursdayEndTime = ''
            if thursdayStartTime != '':
                thursdayEndTime = request.form['thursdayEndTime']

            fridayStartTime = request.form['fridayStartTime']
            fridayEndTime = ''
            if fridayStartTime != '':
                fridayEndTime = request.form['fridayEndTime']

            teachingHours = request.form['teachingHours']

            print("Lecturer Class Routine: ",(mondayStartTime,mondayEndTime),(tuesdayStartTime,tuesdayEndTime),
                  (wednesdayStartTime,wednesdayEndTime),(thursdayStartTime,thursdayEndTime),(fridayStartTime,fridayEndTime))

            print(lecturerName,lecturerType,lecturerExperties,teachingHours)
        page, per_page, offset = get_page_args(page_parameter='page',
                                               per_page_parameter='per_page')
        total = len(users)
        pagination_users = get_users(offset=offset, per_page=per_page)
        pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
        return render_template('lecturersCRUD.html',users=pagination_users,page=page,per_page=per_page,pagination=pagination,
                               expertiesDict = getAllDefaultExperties())


@app.route('/tutors', methods=['POST','GET'])
def getTutorsList():
    if session.get('loggedInUser') is None:
        return redirect(url_for('login'))
    else:
        page, per_page, offset = get_page_args(page_parameter='page',
                                               per_page_parameter='per_page')
        total = len(users)
        pagination_users = get_users(offset=offset, per_page=per_page)
        pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
        return render_template('tutorsCRUD.html',
                           users=pagination_users,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,expertiesDict = getAllDefaultExperties(),)
    return render_template('login1.html')


@app.route('/addTutor', methods=['POST'])
def addTutor():
    if session.get('loggedInUser') is None:
        return redirect(url_for('login'))
    else:
        error = None
        if request.method == 'POST':
            tutorName = request.form['tutorName']
            tutorType = request.form['tutorType']
            tutorExperties = request.form.getlist('tutorExperties')

            '''Getting Class Routines of Tutor...'''
            mondayStartTime = request.form['mondayStartTime']
            mondayEndTime = ''
            if mondayStartTime != '':
                mondayEndTime = request.form['mondayEndTime']

            tuesdayStartTime = request.form['tuesdayStartTime']
            tuesdayEndTime = ''
            if tuesdayStartTime != '':
                tuesdayEndTime = request.form['tuesdayEndTime']

            wednesdayStartTime = request.form['wednesdayStartTime']
            wednesdayEndTime = ''
            if wednesdayStartTime != '':
                wednesdayEndTime = request.form['wednesdayEndTime']

            thursdayStartTime = request.form['thursdayStartTime']
            thursdayEndTime = ''
            if thursdayStartTime != '':
                thursdayEndTime = request.form['thursdayEndTime']

            fridayStartTime = request.form['fridayStartTime']
            fridayEndTime = ''
            if fridayStartTime != '':
                fridayEndTime = request.form['fridayEndTime']

            teachingHours = request.form['teachingHours']

            print("Tutor Class Routine: ",(mondayStartTime,mondayEndTime),(tuesdayStartTime,tuesdayEndTime),
                  (wednesdayStartTime,wednesdayEndTime),(thursdayStartTime,thursdayEndTime),(fridayStartTime,fridayEndTime))

            print(tutorName,tutorType,tutorExperties,teachingHours)
        page, per_page, offset = get_page_args(page_parameter='page',
                                               per_page_parameter='per_page')
        total = len(users)
        pagination_users = get_users(offset=offset, per_page=per_page)
        pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
        return render_template('tutorsCRUD.html',users=pagination_users,page=page,per_page=per_page,pagination=pagination,
                               expertiesDict = getAllDefaultExperties())


@app.route('/units')
def getUnitsList():
    if session.get('loggedInUser') is None:
        return redirect(url_for('login'))
    else:
        page, per_page, offset = get_page_args(page_parameter='page',
                                               per_page_parameter='per_page')
        total = len(users)
        pagination_users = get_users(offset=offset, per_page=per_page)
        pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
        return render_template('unitsCRUD.html',
                           users=pagination_users,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )
    return render_template('login1.html')


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)
