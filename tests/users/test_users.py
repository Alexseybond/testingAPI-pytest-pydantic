"""
Для запуска тестов с фикстурой добавить '-k dataAPI', '-k "not dataAPI"'...
"""

from src.baseclasses.response import Response
from src.pydantic_schemas.user import User
import pytest
from src.generators.player_localization import PlayerLocalization


# resp = requests.get(SERVICE_URL2)
# print(resp.__getstate__())        # Возвращает полностью ответ с ситемной инфой и другим


# def test_getting_user_list(get_user):
#     get_user.assert_status_code(200)
#     get_user.validate_json(User)


@pytest.mark.dataAPI
def test_getting_user_list(get_user):
    test_object = Response(get_user)
    test_object.assert_status_code(200)
    test_object.validate_json(User)


@pytest.mark.metaAPI
@pytest.mark.dataAPI
@pytest.mark.parametrize('code', [200, pytest.param(404, marks=pytest.mark.xfail)])
def test_for_stats_code(get_user, code):
    test_object = Response(get_user)
    test_object.assert_status_code(code)


@pytest.mark.parametrize('status', [
    "ACTIVE",
    "BANNED",
    "DELETED",
    "INACTIVE"
])
def test_something1(status, get_player_generator):
    print(get_player_generator.set_status(status).build())


@pytest.mark.parametrize('delete_key', [
    "account_status",
    "balance",
    "avatar",
    "localize"
])
def test_something2(delete_key, get_player_generator):
    testing_object = get_player_generator.build()
    del testing_object[delete_key]


def test_something3(get_player_generator):
    testing_object = get_player_generator.update_inner_generator(
        'localize', PlayerLocalization('fr_FR').set_number(99)
    ).build()
    print(testing_object)

