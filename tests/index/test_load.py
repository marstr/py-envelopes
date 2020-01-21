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


def test_load_budget_simple():
    target_dir = pathlib.Path(__file__).parent.absolute()
    target_dir = os.path.join(target_dir.parent, "testdata", "repo1", "budget")

    subject = index.load_budget(target_dir)
    wanted_base = envelopes.Balance()
    wanted_base["USD"] = decimal.Decimal("0")
    wanted_groecery = envelopes.Balance()
    wanted_groecery["USD"] = decimal.Decimal("107.92")

    assert subject.balance == wanted_base
    assert subject.children["grocery"].balance == wanted_groecery
