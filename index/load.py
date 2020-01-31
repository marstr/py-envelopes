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

BALANCE_FILE = "cash.txt"
BUDGET_DIRECTORY = "budget"
ACCOUNTS_DIRECTORY = "accounts"


def load_balance(dirname):
    with open(os.path.join(dirname, BALANCE_FILE)) as handle:
        contents = handle.read()
        return Balance(contents)


def load_state(dirname):
    retval = State()
    retval.budget = load_budget(os.path.join(dirname, BUDGET_DIRECTORY))
    retval.accounts = load_accounts(os.path.join(dirname, ACCOUNTS_DIRECTORY))
    return retval


def load_budget(dirname):
    retval = Budget()
    try:
        retval.balance = load_balance(dirname)
    except FileNotFoundError:
        pass

    children = (child for child in os.scandir(path=dirname) if child.is_dir())

    for child in children:
        try:
            retval.children[child.name] = load_budget(os.path.join(dirname, child.name))
        except OSError:
            continue
    return retval


def load_accounts(dir):
    """ Populates a dictionary to reflect the contents of the accounts in a `baronial` index.
    :param dir: The accounts folder of a `baronial` index.
    :return: A dictionary mapping the name of an account to the balance held in that account.
    """
    retval = Accounts()

    def load_accounts_helper(subdir):
        try:
            account_name = os.path.relpath(subdir, dir)
            retval[account_name] = load_balance(subdir)
        except FileNotFoundError:
            pass

        children = (child for child in os.scandir(path=subdir) if child.is_dir())
        for child in children:
            try:
                load_accounts_helper(child)
            except OSError:
                continue

    load_accounts_helper(dir)
    return retval
