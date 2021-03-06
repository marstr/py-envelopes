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

from envelopes import Balance
import hashlib


class Budget:
    def __init__(self):
        self.balance = Balance()
        self.children = {}

    def recursive_balance(self):
        sum = self.balance
        for _, child in self.children:
            sum += child
        return sum
