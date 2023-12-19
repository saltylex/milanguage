import unittest

from structures.grammar import Grammar
from structures.parser import Parser


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.g = Grammar()
        self.g.read('g1.in')
        self.w = "aacbc"
        self.p = Parser(self.g, self.w)

    def tests_advance_insuccess(self):
        self.p.success()
        self.assertEqual(self.p.get_config().get_current_state(), 'final')
        self.p.momentary_insuccess()
        self.assertEqual(self.p.get_config().get_current_state(), 'back')
        self.p.advance()
        self.assertEqual(self.p.get_config().get_current_state(), 'back')
        self.assertEqual(self.p.get_config().get_current_position(), 2)
        self.assertEqual(self.p.get_config().get_stack(), ['S'])
        self.p.back()
        self.assertEqual(self.p.get_config().get_current_state(), 'back')
        self.assertEqual(self.p.get_config().get_current_position(), 1)
        self.assertEqual(self.p.get_config().get_stack(), [])
        self.assertEqual(self.p.get_config().get_input(), [['S']])

    def test_expand(self):
        self.p.expand()
        conf = self.p.config
        self.assertEquals(conf.current_state, 'normal')
        self.assertEquals(conf.get_current_position(), 1)
        self.assertEquals(len(conf.stack), 1)
        self.assertEquals(conf.stack[-1][0][0], "A")
        self.assertEquals(len(conf.input), 1)
        self.assertEquals(len(conf.input[-1]), 1)

    def test_another_try(self):
        self.p.expand()
        self.p.momentary_insuccess()
        self.p.another_try()
        conf = self.p.config
        self.assertEquals(conf.current_state, 'normal')
        self.assertEquals(conf.get_current_position(), 1)
        self.assertEquals(len(conf.stack), 1)
        self.assertEquals(conf.stack[-1][0], "A")
        self.assertEquals(len(conf.input), 1)
        self.assertEquals(len(conf.input[-1]), 1)
        self.assertEquals(conf.input[-1], "A")
        self.p.another_try()
        conf = self.p.config
        self.assertEquals(conf.current_state, 'normal')
        self.assertEquals(conf.get_current_position(), 1)
        self.assertEquals(len(conf.stack), 0)
        self.assertEquals(conf.input[-1][0][0], "A")


if __name__ == "__main__":
    t = Test()
    t.setUp()
    t.test()
