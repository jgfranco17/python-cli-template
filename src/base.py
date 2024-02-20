"""
project_template base module.

This is the principal module of the project_template project.
here you put your main classes and objects.

Be creative! do whatever you want!

If you want to replace this with a Flask application run:

    $ make init

and then choose `flask` as template.
"""
import click

# example constant variable
@click.command("greet")
@click.argument("name", type=str)
@click.option("--farewell", is_flag=True, help="Say bye.")
def greet(name: str, farewell: bool):
    """Greet the user."""
    greeting = "Hello" if not farewell else "Bye"
    print(f"{greeting}, {name}!")