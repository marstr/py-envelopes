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


class Accounts(dict):
    def __init__(self):
        self._underlyer = {}

    def __sub__(self, other):
        retval = Accounts()

        unseen = retval.keys()

        for name, bal in other._underlyer:
            if name in self._underlyer.keys():
                unseen.discard(name)

    def __eq__(self, other):
        unseen = set(self._underlyer.keys())

        for k, v in other._underlyer:
            if (not k in self._underlyer) or self._underlyer[k] != v:
                return False
            unseen.remove(k)

        if len(unseen) > 0:
            return False
        return True
