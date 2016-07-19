from flask import Flask, url_for, redirect
from .default_settings import Settings
from .models import db
from raven.contrib.flask import Sentry


def register_blueprints(app):
    from .numbers import numbers
    app.register_blueprint(
        numbers,
        url_prefix='/{}'.format(numbers.name),
    )


def create_app(conf_obj=Settings, conf_file='/etc/phoney.cfg',
               login_required=None):
    app = Flask(__name__)
    app.config.from_object(conf_obj)
    app.config.from_pyfile(conf_file, silent=True)

    if app.config['DB_SECRET_KEY'] == 'INSECURE_DEFAULT':
        if not (app.debug or app.testing):
            raise ValueError('Cannot use insecure key in PROD')

    db.init_app(app)
    register_blueprints(app)

    @app.route('/')
    def index():
        return redirect(url_for('numbers.index'))

    app.sentry = Sentry(app)

    return app
