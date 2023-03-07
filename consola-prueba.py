import cmd

class MyCmd(cmd.Cmd):
    """Class for an interactive command interpreter"""

    prompt = '$ '

    def do_hello(self, args):
        """Greet the user"""
        a = input("ingresa un valor: ")
        print(a)

    def do_exit(self, args):
        """Exits the command interpreter"""
        return True

if __name__ == '__main__':
    MyCmd().cmdloop()
