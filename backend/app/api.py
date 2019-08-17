import logging
import random

from flask import Blueprint, jsonify, session

'''
Main file with the server routines for the guessing game
'''

logger = logging.getLogger(__name__)
api = Blueprint('api', 'api', url_prefix='/api')


@api.route('/start/<int:minimum>/<int:maximum>')
def start(minimum, maximum):
    """Starts a new game.
    generates a random number between `minimum` and `maximum`
    and stores it in the session as `guess`
    """
    session['guess'] = random.randint(minimum, maximum)
    logger.debug("Set session with = {}".format(session['guess']))
    return jsonify(success=True)


@api.route('/even')
def even():
    ''' Checks if the guess number stored in the session is even '''
    value = session.get('guess', None)
    if value is not None:
        even = value % 2 == 0
        return jsonify(success=True, even=even)
    else:
        return jsonify(success=False)


@api.route('/odd')
def odd():
    ''' Checks if the guess number stored in the session is odd '''
    value = session.get('guess', None)
    if value is not None:
        odd = value % 2 == 1
        return jsonify(success=True, odd=odd)
    else:
        return jsonify(success=False)


@api.route('/greater/<int:number>')
def greater(number):
    ''' Checks if the guess number stored in the session is greather than the
    `number` argument '''
    value = session.get('guess', None)
    if value is not None:
        greater = value > number
        return jsonify(success=True, greater=greater)
    else:
        return jsonify(success=False)


@api.route('/less/<int:number>')
def less(number):
    ''' Checks if the guess number stored in the session is less than the
    `number` argument '''
    value = session.get('guess', None)
    if value is not None:
        less = value < number
        return jsonify(success=True, less=less)
    else:
        return jsonify(success=False)


@api.route('/guess/<int:number>')
def guess(number):
    ''' Matches the `number` argument with the `guess` stored in the session
    (set by the function `start`). Returns a different message depending on
    wether or nor the `number` is equal to session `guess`. Cleans the
    session `guess` value.'''
    value = session.get('guess', None)
    if value is not None:
        guess = value == number
        session.pop('guess')
        if guess:
            return jsonify(success=True, message="You won!")
        else:
            return jsonify(success=True, message="You lost!")
    else:
        return jsonify(success=False)
