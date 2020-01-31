#  Copyright 2019 Martin Strobel
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import decimal
import os
import pathlib

import envelopes
import index


def test_load_repo1():
    wanted_budget_base = envelopes.Balance()
    wanted_budget_base["USD"] = decimal.Decimal("0")
    wanted_budget_grocery = envelopes.Balance()
    wanted_budget_grocery["USD"] = decimal.Decimal("107.92")

    wanted_accounts = envelopes.Accounts()
    wanted_accounts["checking"] = decimal.Decimal("107.92")

    target_dir = pathlib.Path(__file__).parent.absolute()
    target_dir = os.path.join(target_dir.parent, "testdata", "repo1")

    subject = index.load_state(target_dir)

    assert subject.budget.balance == wanted_budget_base
    assert subject.budget.children["grocery"].balance == wanted_budget_grocery

    assert len(subject.accounts) == 1
    assert 'checking' in subject.accounts.keys()
    assert wanted_accounts == subject.accounts


def test_load_repo2():
    wanted_budget_base = envelopes.Balance()
    wanted_budget_base["USD"] = decimal.Decimal("39621.38")

    wanted_accounts = envelopes.Accounts()
    wanted_accounts['usbank/checking'] = 492.89
    wanted_accounts['usbank/savings'] = 9071.33
    wanted_accounts['etrade/retirement'] = 30056.16

    target_dir = pathlib.Path(__file__).parent.absolute()
    target_dir = os.path.join(target_dir.parent, "testdata", "repo2")

    subject = index.load_state(target_dir)

    assert subject.budget.balance == wanted_budget_base
    assert len(subject.budget.children) == 0

    assert len(subject.accounts) == 3
    assert 'etrade/retirement' in subject.accounts.keys()
    assert 'us_bank/checking' in subject.accounts.keys()
    assert 'us_bank/savings' in subject.accounts.keys()
