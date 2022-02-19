from src.enums.global_enums import GlobalErrorMessages


class Response:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status_code = response.status_code

    def validate_json(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.parse_obj(item)
        else:
            schema.parse_obj(self.response_json)

    def assert_status_code(self, status_code: (int, list)):
        """
        Проверка на нужный статус код.
        :param status_code: ...
        """
        if isinstance(status_code, list):
            assert self.response_status_code in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status_code == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value

    def assert_len_json(self, count):
        assert len(self.response_json) == count, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value

