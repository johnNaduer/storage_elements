import cmd

class MyCmd(cmd.Cmd):
    """Clase para un intérprete de comandos interactivo"""

    prompt = '>> '

    def do_hello(self, args):
        """Saluda al usuario"""
        print('Hola!')

    def do_exit(self, args):
        """Sale del intérprete de comandos"""
        return True

    def do_EOF(self, line):
        return True

    def do_greet(self, line):
        print("hello")

if __name__ == '__main__':
    MyCmd().cmdloop()
