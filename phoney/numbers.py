from flask import Blueprint, render_template, request, redirect, url_for, abort
from .models import Number
from datetime import datetime
from sqlalchemy.sql import func
import sqlalchemy.orm.exc as orm_exc
import socket
import json

numbers = Blueprint('numbers', __name__)


@numbers.route('/')
def index():
    w = Number.query.filter(func.length(Number.number) > 6
                            ).order_by(Number.called.desc())
    return render_template('numbers/list.html', numbers=w)


@numbers.route('/h/<number>', methods=['GET'])
def hosting(number):
    w = None
    try:
        w = Number.query.filter_by(number=number).one()
    except orm_exc.NoResultFound:
        pass
    name = w.name if w and (w.name != number) else name
    postdata = {
        'name': 'Phonecall',
        'status': 0,
        'type': 'metric',
        'output': 'Call from %s (0%s)' % (name, number),
        'handlers': ['notify_ops'],
    }
    s = socket.create_connection(('127.0.0.1', 3030))
    s.send(json.dumps(postdata))
    s.close()


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
        from_.name = '0' + from_.number
    from_.called = datetime.utcnow()
    from_.save()
    return from_.name
