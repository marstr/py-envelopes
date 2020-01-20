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

import os
from envelopes import Accounts, Balance, Budget, State


def load_state(dirname):
    retval = State()
    retval.budget = load_budget(os.join(dirname, "budget"))
    retval.accounts = load_accounts(os.join(dirname, "accounts"))
    return retval


def load_budget(dirname):
    with os.open(os.join(dirname, "cash.txt")) as handle:
        contents = handle.read()
    retval = Budget()
    retval.balance = Balance(contents)

    children = (child for child in os.scandir(path=dirname) if child.is_dir())

    for child in children:
        try:
            retval.children[child.name] = load_budget(os.join(dirname, child.name))
        except OSError:
            continue
    return retval


def load_accounts(dirname):
    retval = Accounts()
    def load_accounts_helper(dirname):
