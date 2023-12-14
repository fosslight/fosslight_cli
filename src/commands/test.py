from src.commands.base import cli


@cli.command("test")
def test():
    print("test success")
