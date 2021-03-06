#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Her Majesty the Queen in Right of Canada, as represented
# by the Minister of Statistics Canada, 2019.
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

"""
Dynamic property creation testing suite
"""
import unittest

from artemis_base.core.properties import Properties


class PropertyTestCase(unittest.TestCase):
    class DummyClass:
        def __init__(self, **kwargs):
            self.static_prop = "static"
            self.properties = Properties()
            for key in kwargs:
                print(key, kwargs[key])
                self.properties.add_property(key, kwargs[key])

    def setUp(self):
        print("================================================")
        print("Beginning new TestCase %s" % self._testMethodName)
        print("================================================")

        self.mydummy = self.DummyClass()
        self.mydummy2 = self.DummyClass(a_property="dynamic")

    def tearDown(self):
        pass

    def test_dummy(self):
        assert self.mydummy.static_prop == "static"

    def test_property(self):

        print(self.mydummy2.__dict__)
        assert self.mydummy2.properties.a_property == "dynamic"

    def test_dict(self):
        _props = self.mydummy2.properties.to_dict()
        print(_props)
        # json.dumps(_props, indent=4)

    def test_protobuf(self):
        a_dummy = self.DummyClass(prop1="string", prop2=2.0, prop3=3, prop4=False)
        msg = a_dummy.properties.to_msg()
        for p in msg.property:
            print(p.name, p.type, p.value)

        a_dict = Properties.from_msg(msg)
        print(a_dict)


if __name__ == "__main__":
    unittest.main()
