"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from unittest import TestCase

from src.stack import Stack, Node


class TestNode(TestCase):
    def setUp(self):
        self.n1 = Node(5, None)
        self.n2 = Node('a', self.n1)

    def test_next_node(self):
        self.assertEqual(self.n1.data, 5)
        self.assertEqual(self.n2.data, 'a')


class TestStack(TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.assertEqual(self.stack.push('data1'), None)
        self.assertEqual(self.stack.push('data2'), None)
        self.assertEqual(self.stack.push('data3'), None)
        self.assertEqual(self.stack.top.data, 'data3')
        self.assertEqual(self.stack.top.next_node.data, 'data2')
        self.assertEqual(self.stack.top.next_node.next_node.data, 'data1')
        self.assertEqual(self.stack.top.next_node.next_node.next_node, None)


if __name__ == '__main__':
    unittest.main()
