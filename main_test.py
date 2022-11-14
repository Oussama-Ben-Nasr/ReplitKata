import pytest
from main import isValid


@pytest.mark.unit
def test_sample_valid_skip_delete():
  assert isValid(
    'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
    'Repl.it uses operational transformations.',
    '[{"op": "skip", "count": 40}, {"op": "delete", "count": 47}]')


@pytest.mark.unit
def test_sample_invalid_delete_past_end_of_string():
  assert not isValid(
    'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
    'Repl.it uses operational transformations.',
    '[{"op": "skip", "count": 45}, {"op": "delete", "count": 47}]')


@pytest.mark.unit
def test_sample_invalid_skip_past_end_of_string():
  assert not isValid(
    'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
    'Repl.it uses operational transformations.',
    '[{"op": "skip", "count": 40}, {"op": "delete", "count": 47}, {"op": "skip", "count": 2}]'
  )


@pytest.mark.unit
def test_sample_valid_delete_insert_skip_delete():
  assert isValid(
    'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
    'We use operational transformations to keep everyone in a multiplayer repl in sync.',
    '[{"op": "delete", "count": 7}, {"op": "insert", "chars": "We"}, {"op": "skip", "count": 4}, {"op": "delete", "count": 1}]'
  )


@pytest.mark.unit
def test_sample_invalid_delete_past_end_of_string_after_valid_delete_insert_skip(
):
  assert not isValid(
    'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
    'We can use operational transformations to keep everyone in a multiplayer repl in sync.',
    '[{"op": "delete", "count": 7}, {"op": "insert", "chars": "We"}, {"op": "skip", "count": 4}, {"op": "delete", "count": 1}]'
  )


@pytest.mark.unit
def test_no_operations():
  assert isValid(
    'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
    'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
    '[]')


@pytest.mark.unit
def test_start_empty_string():
  assert isValid('', 'Repl.it rocks!',
                 '[{"op": "insert", "chars": "Repl.it rocks!"}]')


@pytest.mark.unit
def test_start_empty_string_ends_empty():
  assert isValid(
    '', '',
    '[{"op": "insert", "chars": "Repl.it rocks!"}, {"op": "seek", "pos": 0}, {"op": "delete", "count": 14}]'
  )


@pytest.mark.unit
def test_delete_from_empty_string():
  assert not isValid('', '', '[{"op": "delete", "count": 1}]')


@pytest.mark.unit
def test_insert_empty_string():
  assert isValid('', '', '[{"op": "insert", "chars": ""}]')


@pytest.mark.unit
def test_start_empty_string_ends_one_char():
  assert isValid(
    '', '!',
    '[{"op": "insert", "chars": "Repl.it rocks!"}, {"op": "seek", "pos": 0}, {"op": "delete", "count": 13}]'
  )
