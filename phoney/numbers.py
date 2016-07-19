from flask import Blueprint, render_template, request, redirect, url_for, abort
from .models import Number
from datetime import datetime
from sqlalchemy.sql import func
import sqlalchemy.orm.exc as orm_exc

numbers = Blueprint('numbers', __name__)


@numbers.route('/')
def index():
    w = Number.query.filter(func.length(Number.number) > 6
                            ).order_by(Number.called.desc())
    return render_template('numbers/list.html', numbers=w)


@numbers.route('/n/<number>', methods=['GET'])
def detail(number):
    try:
        w = Number.query.filter_by(number=number).one()
    except orm_exc.NoResultFound:
        abort(404)
    return w.name


@numbers.route('/n/<number>', methods=['POST'])
def update(number):
    try:
        w = Number.query.filter_by(number=number).one()
        name = request.form['name']
        if not name:
            abort(404)
        w.name = name
        w.save()
        return redirect(url_for('.index'))
    except orm_exc.NoResultFound:
        abort(404)


@numbers.route('/c/<number>', methods=['POST'])
def called(number):
    to_, _ = Number.get_or_create(number=number)
    from_, _ = Number.get_or_create(number=request.form['from'])
    if from_.name == 'Unknown':
        from_.name = from_.number
    from_.called = datetime.utcnow()
    from_.save()
    return from_.name
