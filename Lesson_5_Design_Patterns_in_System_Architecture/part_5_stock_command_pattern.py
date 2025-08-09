class Command:
    def execute(self):
        raise NotImplementedError

class BuyCommand(Command):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        return f"Buying stock: {self.stock}"

class SellCommand(Command):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        return f"Selling stock: {self.stock}"

class CommandInvoker:
    def __init__(self):
        self._commands = []

    def add_command(self, command: Command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            print(command.execute())
        self._commands.clear()

# Example usage
invoker = CommandInvoker()
invoker.add_command(BuyCommand("AAPL"))
invoker.add_command(SellCommand("GOOG"))
invoker.execute_commands()
