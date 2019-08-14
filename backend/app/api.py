import logging
import random

from flask import Blueprint, jsonify, session

logger = logging.getLogger(__name__)
api = Blueprint('api', 'api', url_prefix='/api')


@api.route('/start/<int:minimum>/<int:maximum>')
def start(minimum, maximum):
    session['guess'] = random.randint(minimum, maximum)
    logger.debug("Set session with = {}".format(session['guess']))
    return jsonify(success=True)


@api.route('/even')
def even():
    value = session.get('guess', None)
    if value is not None:
        even = value % 2 == 0
        return jsonify(success=True, even=even)
    else:
        return jsonify(success=False)


@api.route('/odd')
def odd():
    value = session.get('guess', None)
    if value is not None:
        odd = value % 2 == 1
        return jsonify(success=True, odd=odd)
    else:
        return jsonify(success=False)


@api.route('/greater/<int:number>')
def greater(number):
    value = session.get('guess', None)
    if value is not None:
        greater = value > number
        return jsonify(success=True, greater=greater)
    else:
        return jsonify(success=False)


@api.route('/less/<int:number>')
def less(number):
    value = session.get('guess', None)
    if value is not None:
        less = value < number
        return jsonify(success=True, less=less)
    else:
        return jsonify(success=False)

@api.route('/guess/<int:number>')
def guess(number):
    ''' Try to see if it is a guess '''
    value = session.get('guess', None)
    if value is not None:
        guess = value == number
        return jsonify(success=True, guess=guess)
    else:
        return jsonify(success=False)