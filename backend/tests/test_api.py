import json


def _get_response_data_as_dict(response):
    return json.loads(response.data.decode('utf8'))


def test_app_won(app):
    '''
    This tests all the possible requests to the API
    '''

    c = app.test_client()
    minimum = 1
    maximum = 2

    # Start
    response = c.get('/api/start/{}/{}'.format(minimum, maximum))
    response_dic = _get_response_data_as_dict(response)
    assert response.status_code == 200
    assert response_dic['success']

    # even
    response = c.get('/api/even')
    response_dic = _get_response_data_as_dict(response)
    assert response.status_code == 200
    assert response_dic['success']
    assert response_dic.get('even') is not None
    assert type(response_dic['even']) == bool

    # odd
    response = c.get('/api/odd')
    response_dic = _get_response_data_as_dict(response)
    assert response.status_code == 200
    assert response_dic['success']
    assert response_dic.get('odd') is not None
    assert type(response_dic['odd']) == bool

    # greater
    response = c.get('/api/greater/5')
    response_dic = _get_response_data_as_dict(response)
    assert response.status_code == 200
    assert response_dic['success']
    assert response_dic.get('greater') is not None
    assert type(response_dic['greater']) == bool

    # less
    response = c.get('/api/less/5')
    response_dic = _get_response_data_as_dict(response)
    assert response.status_code == 200
    assert response_dic['success']
    assert response_dic.get('less') is not None
    assert type(response_dic['less']) == bool

    # guess
    with c.session_transaction() as session:
        value = session['guess']
        response = c.get('/api/guess/{}'.format(value))
        response_dic = _get_response_data_as_dict(response)
        assert response.status_code == 200
        assert response_dic['success']
        assert response_dic['message'] == 'You won!'
    # we need to query the session again. looks like its cached
    with c.session_transaction() as session:
        assert session.get('guess') is None

    # Check if the session['guess'] was deleted
    response = c.get('/api/even')
    response_dic = _get_response_data_as_dict(response)
    assert response.status_code == 200
    assert not response_dic['success']
    assert response_dic.get('message') is None


def test_app_lost(app):
    '''
    Test a simple: "you lost"
    '''

    c = app.test_client()
    minimum = 1
    maximum = 10

    # Start
    response = c.get('/api/start/{}/{}'.format(minimum, maximum))
    response_dic = _get_response_data_as_dict(response)
    assert response.status_code == 200
    assert response_dic['success']

    # guess
    with c.session_transaction() as session:
        value = session['guess']
        response = c.get('/api/guess/{}'.format(value+1))
        response_dic = _get_response_data_as_dict(response)
        assert response.status_code == 200
        assert response_dic['success']
        assert response_dic['message'] == 'You lost!'
    with c.session_transaction() as session:
        assert session.get('guess') is None


def test_app_failure(app):
    '''
    No game is created (e.g. the `guess` is not stored in the session)
    All methods should return {'success': 'false'}
    '''

    c = app.test_client()

    # even
    response = c.get('/api/even')
    response_dic = _get_response_data_as_dict(response)
    assert response.status_code == 200
    assert not response_dic['success']
    assert response_dic.get('even') is None

    # odd
    response = c.get('/api/odd')
    response_dic = _get_response_data_as_dict(response)
    assert response.status_code == 200
    assert not response_dic['success']
    assert response_dic.get('even') is None

    # greater
    response = c.get('/api/greater/5')
    response_dic = _get_response_data_as_dict(response)
    assert response.status_code == 200
    assert not response_dic['success']
    assert response_dic.get('even') is None

    # less
    response = c.get('/api/less/5')
    response_dic = _get_response_data_as_dict(response)
    assert response.status_code == 200
    assert not response_dic['success']
    assert response_dic.get('even') is None

    # guess
    response = c.get('/api/guess/123')
    response_dic = _get_response_data_as_dict(response)
    assert response.status_code == 200
    assert not response_dic['success']
    assert response_dic.get('message') is None
