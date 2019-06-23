# Copyright 2019 Martin Strobel
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import decimal
import envelopes

UNITED_STATES = "USD"
EUROPEAN_UNION = "EUR"


def test_balance_add_single():
    test_cases = [
        {
            "left": decimal.Decimal("0.01"),
            "right": decimal.Decimal("0.02"),
            "answer": decimal.Decimal("0.03"),
        },
        {
            "left": decimal.Decimal("-0.05"),
            "right": decimal.Decimal("-0.10"),
            "answer": decimal.Decimal("-0.15"),
        },
        {
            "left": decimal.Decimal("0.05"),
            "right": decimal.Decimal("-0.10"),
            "answer": decimal.Decimal("-0.05"),
        },
        {
            "left": decimal.Decimal("1.1"),
            "right": decimal.Decimal("2.2"),
            "answer": decimal.Decimal("3.3"),
        },
    ]

    for tc in test_cases:
        a = envelopes.Balance()
        a[UNITED_STATES] = tc["left"]
        b = envelopes.Balance()
        b[UNITED_STATES] = tc["right"]

        c = a + b
        assert tc["answer"] == c[UNITED_STATES]


def test_balance_sub_single():
    test_cases = [
        {
            "left": decimal.Decimal("0.01"),
            "right": decimal.Decimal("0.02"),
            "answer": decimal.Decimal("-0.01")
        },
        {
            "left": decimal.Decimal("-0.05"),
            "right": decimal.Decimal("-0.10"),
            "answer": decimal.Decimal("0.05"),
        },
        {
            "left": decimal.Decimal("0.05"),
            "right": decimal.Decimal("-0.10"),
            "answer": decimal.Decimal("0.15"),
        },
    ]

    for tc in test_cases:
        a = envelopes.Balance()
        a[UNITED_STATES] = tc["left"]
        b = envelopes.Balance()
        b[UNITED_STATES] = tc["right"]

        c = a - b
        assert tc["answer"] == c[UNITED_STATES]

        assert a[UNITED_STATES] == tc["left"]
        assert b[UNITED_STATES] == tc["right"]


def test_balance_equal():
    ten_dollars = envelopes.Balance()
    ten_dollars[UNITED_STATES] = decimal.Decimal('10')

    five_dollars = envelopes.Balance()
    five_dollars[UNITED_STATES] = decimal.Decimal('5')

    ten_euro = envelopes.Balance()
    ten_euro[EUROPEAN_UNION] = decimal.Decimal('10')

    ten_euro_not_empty = envelopes.Balance()
    ten_euro_not_empty[EUROPEAN_UNION] = decimal.Decimal('10')
    ten_euro_not_empty[UNITED_STATES] = decimal.Decimal('0')

    ten_dollars_not_empty = envelopes.Balance()
    ten_dollars_not_empty[UNITED_STATES] = decimal.Decimal('10')
    ten_dollars_not_empty[EUROPEAN_UNION] = decimal.Decimal('0')

    test_cases = [
        {
            "left": ten_dollars,
            "right": ten_dollars,
            "answer": True,
        },
        {
            "left": ten_dollars,
            "right": five_dollars,
            "answer": False,
        },
        {
            "left": five_dollars,
            "right": ten_dollars,
            "answer": False,
        },
        {
            "left": ten_euro,
            "right": ten_dollars,
            "answer": False,
        },
        {
            "left": ten_euro_not_empty,
            "right": ten_euro,
            "answer": True,
        },
        {
            "left": ten_dollars_not_empty,
            "right": ten_dollars,
            "answer": True,
        },
    ]

    for tc in test_cases:
        got = tc["left"] == tc["right"]
        assert got == tc["answer"]


def test_parse_balance():
    forty_two_dollars = envelopes.Balance()
    forty_two_dollars[UNITED_STATES] = decimal.Decimal("42")

    zero_euro = envelopes.Balance()
    zero_euro[EUROPEAN_UNION] = decimal.Decimal("0")

    one_four_two_three_point_nine_one_dollars = envelopes.Balance()
    one_four_two_three_point_nine_one_dollars[UNITED_STATES] = decimal.Decimal("1423.91")

    negative_ten_dollars = envelopes.Balance()
    negative_ten_dollars[UNITED_STATES] = decimal.Decimal("-10.00")

    test_cases = [
        {
            "raw": "{} 42.00".format(UNITED_STATES),
            "expected": forty_two_dollars,
        },
        {
            "raw": "{} 0".format(EUROPEAN_UNION),
            "expected": zero_euro,
        },
        {
            "raw": "{} 1,423.91".format(UNITED_STATES),
            "expected": one_four_two_three_point_nine_one_dollars,
        },
        {
            "raw": "{} -10.00".format(UNITED_STATES),
            "expected": negative_ten_dollars,
        },
    ]

    for tc in test_cases:
        subject = envelopes.Balance(tc["raw"])
        assert subject == tc["expected"]
