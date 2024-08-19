class Url:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/api'
    CREATE_USER_HANDLE = '/auth/register'
    DELETE_USER_HANDLE = '/auth/user'
    LOGIN_USER_HANDLE = '/auth/login'
    EDIT_USER_HANDLE = '/auth/user'
    ORDERS_HANDLE = '/orders'


class Message:
    USER_ALREADY_EXIST_403 = 'User already exists'
    REQUIRED_FIELD_EMPTY_403 = 'Email, password and name are required fields'
    EMAIL_OR_PASSWORD_INCORRECT_401 = 'email or password are incorrect'
    SHOULD_BE_AUTHORISED_401 = 'You should be authorised'
    EMAIL_ALREADY_EXIST_403 = 'User with such email already exists'
    INGREDIENTS_MUST_BE_PROVIDED_400 = 'Ingredient ids must be provided'


class TestData:
    INGREDIENT = '61c0c5a71d1f82001bdaaa70'