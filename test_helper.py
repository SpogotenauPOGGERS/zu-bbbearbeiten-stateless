import pytest
import helper
import datetime


def test_add():
    # Given: I want to add a to-do with a date
    text = "Lorem ipsum"
    date = "2023-09-02"

    # When: I add the item
    helper.add(text, datetime.datetime.strptime(date, '%Y-%m-%d'))
    

    # Then: The most recently added to-do should have a date
    item = helper.todos[-1]
    assert isinstance(item.date, datetime.date)
