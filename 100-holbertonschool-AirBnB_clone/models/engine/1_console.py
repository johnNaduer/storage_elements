#!/usr/bin/python3

import cmd

class MyCLI(cmd.Cmd):
    prompt = '> '

    def do_foo(self, arg):
        """This is the help message for the foo command."""
        print(f"Executing foo command with argument: {arg}")

    def do_bar(self, arg):
        """This is the help message for the bar command."""
        print(f"Executing bar command with argument: {arg}")

    def default(self, line):
        print(f"Invalid command: {line}")

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF"""
        print()
        return True

if __name__ == '__main__':
    MyCLI().cmdloop()
