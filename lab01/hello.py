import typer

def main(
    name: str,
    lastname: str = typer.Option("", help="Фамилия пользователя."),
    formal: bool = typer.Option(False, "--formal", "-f", help="Использовать формальное приветствие."),
):
    """
    Говорит "Привет" пользователю, опционально используя фамилию и формальный стиль.
    
    Args:
        name (str): Имя пользователя (обязательный параметр)
        lastname (str): Фамилия пользователя (опционально)
        formal (bool): Флаг формального приветствия
    """
    if formal:
        # Формальное приветствие с именем и фамилией
        print(f"Добрый день, {name} {lastname}!")
    else:
        # Неформальное приветствие только с именем
        # Обычный комментарий
        print(f"Привет, {name}!")

if name == "main":
    typer.run(main)
