import pytest

import helpers


@pytest.fixture(scope='function')
def user():
    user = helpers.register_new_user_and_return_user_data()
    yield user
    helpers.delete_user(user['json']['accessToken'])
    return user