import pytest
import requests_mock

from load_balancer.app.helpers import decode_string, get_meta_data
from ..consts import METADATA_API_URI


@pytest.mark.parametrize(
    'input_data, output_data', [('abc', 'abc'), (b'abc', 'abc')])
def test_decode_string(input_data, output_data):
    assert decode_string(input_data) == output_data


# @pytest.mark.parametrize(
#     "finish_meta_data, intermediate_meta_data", [
#         pytest.param(
#             {"path": "first_path", "value": "first_value"},
#             [{"path": "first_path", "value": "first_value"}]
#         ),
#         pytest.param(
#             {"path": "first_path",
#              "value": {"first_path__second_path": "second_value"}
#              }, [
#                 {"path": "first_path",
#                  "value": "first_path__second_path/"},
#                 {"path": "first_path/first_path__second_path",
#                  "value": "second_value"}
#             ]
#         ),
#     ]
# )
# def test_get_meta_data(finish_meta_data, intermediate_meta_data):
#     if not intermediate_meta_data:
#         intermediate_meta_data = []
#     with requests_mock.Mocker() as mock_request:
#         for intermediate_data in intermediate_meta_data:
#             intermediate_url = "{0}{1}".format(
#                 METADATA_API_URI, intermediate_data["path"]
#             )
#             mock_request.get(intermediate_url, text=intermediate_data["value"])
#
#         finish_path = finish_meta_data["path"]
#         finish_value = finish_meta_data["value"]
#         assert get_meta_data([finish_path]) == {finish_path: finish_value}
#
#         # second_path = "path2/"
#         # second_url = "{0}{1}".format(METADATA_API_URI, second_path)
#         #
#         # second_path_first_value = "path2_path1"
#         # mock_request.get('{0}{1}'.format(second_url, second_path_first_value),
#         #                  text="path2_path1_value")
#         #
#         # second_path_second_value = "path2_path2"
#         # mock_request.get('{0}{1}'.format(second_url, second_path_second_value),
#         #                  text="path2_path2_value")
#         #
#         # second_path_third_value = "path2_path3/"
#         #
#         # second_path_third_value_value = "path2_path3_path1"
#         # mock_request.get('{0}{1}'.format(second_url, second_path_third_value),
#         #                  text=second_path_third_value_value)
#         # mock_request.get('{0}{1}{2}'.format(second_url, second_path_third_value,
#         #                                     second_path_third_value_value),
#         #                  text="path2_path3_path1__value")
#         #
#         # second_path_value = "{0}\n{1}\n{2}".format(
#         #     second_path_first_value,
#         #     second_path_second_value,
#         #     second_path_third_value
#         # )
#         # mock_request.get(second_url, text=second_path_value)
#         #
#         # third_url = "{0}/{1}".format(second_url, second_path_third_value)
#         # mock_request.get(third_url, text=second_path_third_value_value)
#         #
#         # path_info = get_meta_data([second_path])
#         # assert 1 == 1
