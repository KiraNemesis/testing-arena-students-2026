"""Starter tests for the weather module.

These tests deliberately cover only ordinary examples. They show how pytest works,
but they are not a sufficient test suite for the specification in SPECIFICATION.md.
"""
import pytest

from weather import (
    average_temperature,
    filter_by_temperature,
    hottest_measurement,
    parse_measurement,
    parse_time,
)


def test_parse_time_regular_time():
    assert parse_time("14:21") == 861


def test_parse_measurement_regular_line():
    assert parse_measurement("Köln;14:21;21.7") == ("Köln", 861, 21.7)


def test_filter_by_temperature_regular_values():
    measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 18.5),
        ("Bonn", 900, 25.0),
    ]

    assert filter_by_temperature(measurements, 15.0, 20.0) == [
        ("Düsseldorf", 720, 18.5)
    ]


def test_average_temperature_regular_values():
    measurements = [
        ("Köln", 600, 10.0),
        ("Köln", 720, 20.0),
    ]

    assert average_temperature(measurements, "Köln") == 15.0


def test_hottest_measurement_with_unique_maximum():
    measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 25.0),
        ("Bonn", 900, 20.0),
    ]

    assert hottest_measurement(measurements) == ("Düsseldorf", 720, 25.0)


def test_parse_time_limit():
    assert parse_time("23:00") == 1380


def test_parse_time_limit_round():
    assert parse_time("23:20") == 1400


def test_parse_time_incorrect_format():
    with pytest.raises(ValueError):
        parse_time("14_20")


def test_parse_time_incorrect_format_0():
    assert parse_time("04:20") == 260
    assert parse_time("4:20") == 260
    assert parse_time("4:2") == 242


def test_parse_time_non_numeric_input():
    with pytest.raises(ValueError):
        parse_time("14:2O")


def test_parse_measurement_non_string_input():
    with pytest.raises(ValueError):
        parse_measurement(["köln", "14:22", "21.7"])


def test_parse_measurement_more_semicolon_input():
    with pytest.raises(ValueError):
        parse_measurement("köln;14:22;21.7;90")


def test_parse_measurement_less_semicolon_input():
    with pytest.raises(ValueError):
        parse_measurement("köln;14:22")


def test_parse_measurement_wrong_order_input():
    with pytest.raises(ValueError):
        parse_measurement("14:22;Köln;21.7")


def test_parse_measurement_remove_empty_spaces_and_check_floats():
    assert parse_measurement("  Köln  ;14:22;21.7  ") == ("Köln", 862, 21.7)


def test_parse_measurement_temp_is_not_a_float():
    with pytest.raises(ValueError):
        parse_measurement("Köln;14:22;21,7")


def test_parse_measurement_plausibel_temp():
    assert parse_measurement("Köln;14:22;100") == ("Köln", 862, 100)


def test_filter_by_temp_boundary():
    assert filter_by_temperature([("Köln","14:22",20), ("Köln","14:22",100), ("Köln","14:22",30)], 20, 30) == [("Köln", "14:22", 20), ("Köln", "14:22", 30)]

def test_filter_by_temp_duplicates():
    assert filter_by_temperature([("Köln", "14:22", 20), ("Köln", "14:22", 20)], 20, 30) == [
        ("Köln", "14:22", 20), ("Köln", "14:22", 20)]

def test_filter_by_temp_lower_upper_error():
    with pytest.raises(ValueError):
        filter_by_temperature([("Köln", "14:22", 20), ("Köln", "14:22", 20)], 30, 20)