from src.baseclasses.response import Response
from src.pydantic_schemas.user import User
import pytest

# resp = requests.get(SERVICE_URL2)
# print(resp.__getstate__())        # Возвращает полность ответ с ситемной инфой и другим
# print(resp.url)


# def test_getting_user_list(get_user):
#     get_user.assert_status_code(200)
#     get_user.validate_json(User)


def test_getting_user_list(get_user):
    test_object = Response(get_user)
    test_object.assert_status_code(200)
    test_object.validate_json(User)


@pytest.mark.parametrize('code', ['200', '404'])
def test_for_stats_code(get_user, code):
    test_object = Response(get_user)
    test_object.assert_status_code(code)

