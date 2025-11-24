import typer
from typing import Optional


class GreetingApp:
    """Приложение для генерации приветствий."""
    
    def init(self):
        self.formal_prefix = "Добрый день"
        self.informal_prefix = "Привет"
    
    def generate_greeting(
        self, 
        name: str, 
        lastname: Optional[str] = None, 
        formal: bool = False
    ) -> str:
        """
        Генерирует приветственное сообщение.
        
        Parameters:
        name (str): Имя пользователя
        lastname (Optional[str]): Фамилия пользователя
        formal (bool): Флаг формального стиля
        
        Returns:
        str: Приветственное сообщение
        """
        if formal:
            greeting = f"{self.formal_prefix}, {name}"
            if lastname:
                greeting += f" {lastname}"
            greeting += "!"
        else:
            greeting = f"{self.informal_prefix}, {name}!"
        
        return greeting


def main(
    name: str,
    lastname: str = typer.Option("", help="Фамилия пользователя."),
    formal: bool = typer.Option(False, "--formal", "-f", help="Формальное приветствие."),
) -> None:
    """
    CLI приложение для генерации приветствий.
    
    Примеры использования:
    python hello.py Ivan
    python hello.py Ivan --lastname Petrov --formal
    python hello.py Anna -f
    """
<<<<<<< HEAD
    if formal:
        # Формальное приветствие с именем и фамилией
        print(f"Добрый день, {name} {lastname}!")
    else:
        # Неформальное приветствие только с именем
        # Обычный комментарий
        print(f"Привет, {name}!")
=======
    app = GreetingApp()
    greeting = app.generate_greeting(name, lastname, formal)
    print(greeting)

>>>>>>> 7afcae8 (Refactor code to OOP style with better structure)

if name == "main":
    typer.run(main)
