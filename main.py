#!/usr/bin/env python
# coding=utf-8

"""a demo to write a repl using cmd module.

This demo simulate a simple k-v store, supports set and get sub-command.

Example Usage:
    python main.py
    demo> set x 1
    demo> get x
    demo> set x 5
    demo> get x

"""

from __future__ import print_function, unicode_literals

import sys
import cmd


class KVCmd(cmd.Cmd):

    def __init__(self, *args, **kwargs):
        cmd.Cmd.__init__(self, *args, **kwargs)
        self.data = {}

    def do_set(self, line):
        """set KEY INTEGER.

        set KEY to given INTEGER.

        """
        args = line.split(' ')
        try:
            self.data[args[0]] = int(args[1])
            print("OK")
        except ValueError:
            print("Error: only integer value is supported in this demo")

    def do_get(self, line):
        """get KEY's value.

        """
        args = line.split(' ')
        print(self.data.get(args[0], "nil"))

    def do_incr(self, line):
        """incr KEY.

        increment KEY's value by 1. If KEY doesn't exist, create it and assign
        value 1.

        """
        args = line.split(' ')
        increment = 1
        if len(args) > 1:
            try:
                increment = int(args[1])
            except ValueError:
                print("Error: INCREMENT should be integer")
                return
        try:
            self.data[args[0]] += increment
            print(self.data[args[0]])
        except KeyError:
            self.data[args[0]] = 1
            print(self.data[args[0]])

    def do_exit(self, _line):    # pylint: disable=no-self-use
        """exit the program.

        """
        print()
        sys.exit(0)

    def do_EOF(self, line):    # pylint: disable=invalid-name
        self.do_exit(line)

    def default(self, line):
        print("command not supported:", line)


def main():
    repl = KVCmd()
    repl.prompt = "demo> "
    repl.cmdloop(u"""\
A Demo to show how to build a REPL using python's cmd module.

Try:
    set x 56
    get x
    set y 38
    get y
    incr x
    exit
""")


if __name__ == '__main__':
    main()
