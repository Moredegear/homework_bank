from src.processing import filter_by_state
from src.processing import sort_by_date
import pytest

@pytest.mark.parametrize("x,y,expected",[([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
                                          "EXECUTED",
                                        [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
                                         ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                           {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                           {'id': 615064591, 'state': 'CANCELED',
                                            'date': '2018-10-14T08:21:33.419441'}],
                                          "CANCELED",
                                        [{'id': 594226727,'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]),
                                         ([{'id': 41428829, 'date': '2019-07-03T18:35:29.512364'},
                                         {'id': 939719570, 'date': '2018-06-30T02:08:58.425572'},
                                         {'id': 594226727, 'date': '2018-09-12T21:27:25.241689'},
                                         {'id': 615064591, 'date': '2018-10-14T08:21:33.419441'}],
                                          "EXECUTED","В списке нет ключа 'state'"),([],"CANCELED","Список пусой")])
def test_filter_by_state(x,y,expected):
    assert filter_by_state(x,y) == expected


@pytest.mark.parametrize("x,y,expected",[([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
                                          True,
                                        [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
                                        ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
                                          False,
                                    [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                     {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]),
                                    ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                         {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                         {'id': 594226727, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
                                         {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}],
                                          True,
                                     [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                     {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                     {'id': 594226727, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
                                     {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}]),
                                        ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                     {'id': 939719570, 'state': 'EXECUTED', },
                                     {'id': 594226727, 'state': 'CANCELED', },
                                     {'id': 615064591, 'state': 'CANCELED', }],True,"В списке не указаны даты")])
def test_sort_by_date(x,y,expected):
    assert sort_by_date(x,y) == expected
