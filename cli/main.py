import click

@click.group()
def cli():
    """This click group allows us to group multiple commands into one cli."""
    pass


@cli.command()
@click.argument('name')
def hello(name):
    """Says hello to the name provided."""
    # The docstring (the comment just below the function definition) above
    # is used by click as the contents of the --help option to for this command.
    click.echo(f"Hello {name}")


@cli.command()
@click.argument("x")
@click.argument("y")
def add(x, y):
    """Sums x and y and prints a result."""
    click.echo(f"The sum of {x} and {y} is {x+y}")


if __name__ == "__main__":
    """This function is only called when invoking the script with something
    like `python main.py`. Then the python interpreter runs a module (.py file)
    it sets __name__ to "__main__", so we can check for that here and invoke
    our cli using the decorated function above. See the README.md and setup.py
    for some information on how to install the cli so that it is callable by
    name.
    """
    cli()
