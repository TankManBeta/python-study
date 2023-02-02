# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/2 8:00
"""
import os


class MoveFileCommand(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def execute(self):
        self()

    def __call__(self):
        print('renaming {} to {}'.format(self.src, self.dest))
        os.rename(self.src, self.dest)

    def undo(self):
        print('renaming {} to {}'.format(self.dest, self.src))
        os.rename(self.dest, self.src)


if __name__ == "__main__":
    # commands are just pushed into the command stack
    command_stack = [MoveFileCommand('foo.txt', 'bar.txt'), MoveFileCommand('bar.txt', 'baz.txt')]

    # they can be executed later on
    for cmd in command_stack:
        cmd.execute()

    # and can also be undone at will
    for cmd in reversed(command_stack):
        cmd.undo()