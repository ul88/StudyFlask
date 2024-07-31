from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import UserCreateForm, UserLoginForm
from pybo.models import User

bp = Blueprint('auth',__name__,url_prefix="/auth")

@bp.route("/signup", methods=["GET","POST"])
def signup():
    form = UserCreateForm()
    if request.method == "POST" and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            user = User(username = form.username.data,
                        password = generate_password_hash(form.password1.data),
                        email = form.email.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("main.index"))
        else:
            flash('이미 존재하는 사용자입니다.')
    return render_template('auth/signup.html', form=form)

@bp.route('/login', methods=["GET","POST"])
def login():
    form = UserLoginForm()
    if request.method == "POST" and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user.password, form.password.data):
            error = "비밀번호가 올바르지 않습니다."
        
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('main.index'))
        flash(error)
    return render_template('auth/login.html', form=form)

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("main.index"))

@bp.before_app_request # 모든 라우팅 함수보다 항상 먼저 실행된다.
def load_logged_in_user():
    '''
    g는 플라스크의 컨텍스트 변수이다. 이 변수는 request 변수와 마찬가지로
    [요청 -> 응답] 과정에서 유효하다.
    코드에서 보듯 session변수에 user_id값이 있으면 데이터베이스에서 사용자 정보를 조회하여 g.user에 저장한다.
    이렇게 하면 이후 사용자 로그인 검사를 할 때, session을 조사할 필요가 없다. g.user에 값이 있는지만 확인하면 된다.
    g.user에는 User 객체가 저장되어 있으므로 여러가지 사용자 정보(username, email등)를 추가로 얻어내는 이점이 있다.
    '''
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)