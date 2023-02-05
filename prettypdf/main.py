import typer
from rich import print
from typing import Optional

app = typer.Typer()


@app.command()
def create():
    typer.echo("Creating user")

@app.command()
def delete():
    print("delete user")

@app.command()
def greeter(name: str, city: Optional[str] = None):
    print(f"Hello {name}!")
    
    if city:
        print(f"Let's have a coffee in {city}.")

if __name__ == "__main__":
    app()
