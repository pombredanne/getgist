from sys import stderr, stdout, version_info

from click import secho

input_method = input
if version_info < (3, 0):
    input_method = raw_input


class GetGistCommons(object):
    """Basic output methods used to print messages on users' terminal"""

    indent_size = 2
    indent_char = ' '

    def indent(self, message):
        """
        Sets the indent for standardized output
        :param message: (str)
        :return: (str)
        """
        indent = self.indent_char * self.indent_size
        return indent + message

    def output(self, message, color=None):
        """
        A helper to used like print() or click's secho() tunneling all the
        outputs to sys.stdout or sys.stderr
        :param message: (str)
        :param color: (str) check click.secho() documentation
        :return: (None) prints to sys.stdout or sys.stderr
        """
        output_to = stderr if color == 'red' else stdout
        secho(self.indent(message), fg=color, file=output_to)

    def ask(self, message):
        """
        A helper to indent input()
        :param message: (str)
        :return: (str) the user input
        """
        return input_method(self.indent(message))

    def oops(self, message):
        """Helper to colorize error messages"""
        return self.output(message, color='red')

    def yeah(self, message):
        """Helper to colorize success messages"""
        return self.output(message, color='green')

    def warn(self, message):
        """Helper to colorize warning messages"""
        return self.output(message, color='yellow')

    def hey(self, message):
        """Helper to colorize highlihghted messages"""
        return self.output(message, color='blue')
