import os.path

from src import utils
from config import ROOT_DIR


def test_load_operations():
    TEST_DATA_PATH = os.path.join(ROOT_DIR, 'tests', 'data_for_test.json')
    assert utils.load_operations(TEST_DATA_PATH) == [1, 2, 3]


def test_executed_operations():
    executed_operations = [
  {
    "id": 441945886,
    "state": "EXECUTED",
      },
  {
    "id": 41428829,
    "state": "EXECUTED",
      },
  {
    "id": 41428829,
    "state": "CANCELED",
    }]
    assert utils.executed_operations(executed_operations) == [
  {
    "id": 441945886,
    "state": "EXECUTED",
      },
  {
    "id": 41428829,
    "state": "EXECUTED",
      }]


def test_sorted_data():
    sorted_data = [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2020-07-03T18:35:29.512364",
      },
  {
    "id": 41428829,
    "state": "EXECUTED",
     "date": "2018-06-01T18:35:29.512364",
  }]
    assert utils.sorted_date(sorted_data) == [
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2020-07-03T18:35:29.512364"
    },
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041"
    },
  {
    "id": 41428829,
    "state": "EXECUTED",
     "date": "2018-06-01T18:35:29.512364",
  }]


def test_hidden_numbers():
  hidden_for_none = None
  hidden_for_card = "Maestro 1596837868705199"
  hidden_for_account = "Счет 64686473678894779589"
  assert utils.hidden_numbers(hidden_for_none) == "Нет данных"
  assert utils.hidden_numbers(hidden_for_card) == "Maestro 1596 83** **** 5199"
  assert utils.hidden_numbers(hidden_for_account) == "Счет **9589"


def test_formatted_operations():
  for_format = [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }]
  assert utils.formatted_operations(for_format) == "26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.\n"
