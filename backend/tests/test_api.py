import json

import pytest


def _get_response_data_as_dict(response):
    return json.loads(response.data.decode('utf8'))


def test_app(app):
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
    assert response_dic['success'] == True

    # even
    response = c.get('/api/even')
    response_dic = _get_response_data_as_dict(response)
    assert response.status_code == 200
    assert response_dic['success'] == True
    assert response_dic.get('even') is not None

    # odd
    response = c.get('/api/odd')
    response_dic = _get_response_data_as_dict(response)
    assert response.status_code == 200
    assert response_dic['success'] == True
    assert response_dic.get('odd') is not None

    # greater
    response = c.get('/api/greater/5')
    response_dic = _get_response_data_as_dict(response)
    assert response.status_code == 200
    assert response_dic['success'] == True
    assert response_dic.get('greater') is not None

    # less
    response = c.get('/api/less/5')
    response_dic = _get_response_data_as_dict(response)
    assert response.status_code == 200
    assert response_dic['success'] == True
    assert response_dic.get('less') is not None

    # guess
    for i in range(minimum, maximum+2):
        response = c.get('/api/guess/{}'.format(i))
        response_dic = _get_response_data_as_dict(response)
        assert response.status_code == 200
        assert response_dic['success'] == True
        assert response_dic.get('guess') is not None
        if response_dic['guess']:
            break
    else:
        assert False, "This should never happen. We looped through all "\
                      "possible values and none was found!"
