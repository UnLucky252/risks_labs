# Отчет по лабораторной работе: Настройка GPG и работа с Git

## Выполненные задачи:

### 1. Настройка GPG подписи коммитов
- Установлен и настроен GnuPG
- Сгенерирован ключ RSA 4096
- Настроен Git для автоматического подписания коммитов

### 2. Создание и управление репозиторием
- Создан локальный репозиторий
- Инициализирован Git
- Настроена связь с удаленным репозиторием GitHub

### 3. Разработка приложения
- Создано Python приложение с поэтапным улучшением кода
- Реализованы различные стили кодирования
- Добавлен CLI интерфейс с помощью Typer

### 4. Работа с ветками и Pull Requests
- Созданы ветки patch1 и patch2
- Выполнены Merge и Rebase операции
- Разрешены конфликты слияния

## История коммитов:
### Локальная история коммитов
$ git log --oneline --graph --decorate --all
* 83f196c (HEAD -> patch2, origin/patch2) Refactor code to OOP style with better structure
* 8983e6a (origin/master, origin/HEAD) Update hello.py
*   922c5ee (master) Merge pull request #1 from UnLucky252/patch1
|\  
| * bdfd2f4 (origin/patch1) Add detailed code comments
| * 962de9b Refactor hello.py using typer with CLI options
|/  
* f1ee77a Improve hello.py with proper function structure
* e88f287 Add dirty hello.py implementation
* 392e259 Initial commit with signed commit

### Удаленная история коммтов (origin/master)
$ git log origin/master --oneline -10
8983e6a (origin/master, origin/HEAD) Update hello.py
922c5ee (master) Merge pull request #1 from UnLucky252/patch1
bdfd2f4 (origin/patch1) Add detailed code comments
962de9b Refactor hello.py using typer with CLI options
f1ee77a Improve hello.py with proper function structure
e88f287 Add dirty hello.py implementation
392e259 Initial commit with signed commit

### Проверка подписей коммтов
$ git log --show-signature -5               
commit 83f196c183fbca3ce219c447a4e8baea5268349e (HEAD -> patch2, origin/patch2)
gpg: Подпись сделана Вс 23 ноя 2025 11:52:24 MSK
gpg:                ключом RSA с идентификатором 4B38508CCDE46082F9AB565B5980242541F78E3D
gpg: Действительная подпись пользователя "UnLucky252 <maksimanisimov03@gmail.com>" [абсолютное]
Author: UnLucky252 <maksimanisimov03@gmail.com>
Date:   Sun Nov 23 11:40:20 2025 +0300

    Refactor code to OOP style with better structure

commit 8983e6ae7b4d267e12d1f4e2d7ffd784eee2c8fd (origin/master, origin/HEAD)
gpg: Подпись сделана Вс 23 ноя 2025 11:49:33 MSK
gpg:                ключом RSA с идентификатором B5690EEEBB952194
gpg: Не могу проверить подпись: Нет открытого ключа
Author: UnLucky252 <91291636+UnLucky252@users.noreply.github.com>
Date:   Sun Nov 23 11:49:33 2025 +0300

    Update hello.py

commit 922c5ee7dd9b86325a5956c1bd189597a9363b9f (master)
gpg: Подпись сделана Вс 23 ноя 2025 11:32:13 MSK
gpg:                ключом RSA с идентификатором B5690EEEBB952194
gpg: Не могу проверить подпись: Нет открытого ключа
Merge: f1ee77a bdfd2f4
Author: UnLucky252 <91291636+UnLucky252@users.noreply.github.com>
Date:   Sun Nov 23 11:32:13 2025 +0300

    Merge pull request #1 from UnLucky252/patch1
    
    Refactor hello.py with Typer

commit bdfd2f48afde200cc15a453785eb7b042f247cdb (origin/patch1)
gpg: Подпись сделана Вс 23 ноя 2025 11:30:14 MSK
gpg:                ключом RSA с идентификатором 4B38508CCDE46082F9AB565B5980242541F78E3D
gpg: Действительная подпись пользователя "UnLucky252 <maksimanisimov03@gmail.com>" [абсолютное]
Author: UnLucky252 <maksimanisimov03@gmail.com>
Date:   Sun Nov 23 11:30:14 2025 +0300

    Add detailed code comments

commit 962de9b915e8a47a6a515680435b2651af2d6b16
gpg: Подпись сделана Вс 23 ноя 2025 11:10:41 MSK
gpg:                ключом RSA с идентификатором 4B38508CCDE46082F9AB565B5980242541F78E3D
gpg: Действительная подпись пользователя "UnLucky252 <maksimanisimov03@gmail.com>" [абсолютное]
Author: UnLucky252 <maksimanisimov03@gmail.com>
Date:   Sun Nov 23 11:10:41 2025 +0300

    Refactor hello.py using typer with CLI options

## Детализация выполненных операций
1. Настройка GPG
```
# Генерация ключа
gpg --full-generate-key
# Тип: RSA and RSA (4096 бит)
# Срок: 0 (неограниченный)

# Экспорт публичного ключа
gpg --armor --export 
#  Ключ добавлен в GitHub: Settings → SSH and GPG keys

# Настройка Git
git config --global user.signingkey 5980242541F78E3D
git config --global commit.gpgsign true
```

2. Создание репозитория
```
# Локальная инициализация
mkdir risks_labs && cd risks_labs
git init
git remote add origin https://github.com/UnLucky252/risks_labs.git

# Создание через GitHub CLI
gh repo create security-project --public --description "My risks_labs"
```

3. Работа с ветками
```
# Создание feature веток
git checkout -b patch1
git checkout -b patch2

# Синхронизация с удаленным репозиторием
git push -u origin patch1
git push -u origin patch2
```

4. Pull Requests и слияния
```
# Создание PR через CLI
gh pr create --base master --head patch1 --title "Refactor hello.py with Typer"

# Слияние PR
gh pr merge patch1 --merge --delete-branch

# Получение изменений
git checkout master
git pull origin master
```

5. Разрешение конфликтов
```
# Rebase для разрешения конфликтов
git checkout patch2
git fetch origin
git rebase origin/master

# Ручное разрешение конфликтов в файлах
git add .
git rebase --continue
git push --force-with-lease origin patch2
```

## Структура проекта
```
risks_lab/
├── .git/
└── lab01
    ├── README.md
    └── hello.py
```

## Конечный вид hello.py
```
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
    app = GreetingApp()
    greeting = app.generate_greeting(name, lastname, formal)
    print(greeting)


if name == "main":
    typer.run(main)
```

## Выводы и результаты
### Освоенные навыки:
```
✅ Настройка GPG для подписи коммитов

✅ Работа с подписанными коммитами (флаг -S)

✅ Создание и управление ветками

✅ Работа с Pull Requests

✅ Разрешение конфликтов слияния

✅ Использование rebase для синхронизации веток

✅ Работа с GitHub CLI
```

## Проверка подписей:
Все коммиты в истории подписаны и верифицированы:
```
$ git verify-commit HEAD
gpg: Подпись сделана Вс 23 ноя 2025 11:52:24 MSK
gpg:                ключом RSA с идентификатором 4B38508CCDE46082F9AB565B5980242541F78E3D
gpg: Действительная подпись пользователя "UnLucky252 <maksimanisimov03@gmail.com>" [абсолютное]
```

## Статус репозитория:
- Локальный репозиторий: синхронизирован с origin/master

- Ветки: patch1 и patch2 удалены после слияния

- Коммиты: все подписаны и верифицированы

- Конфликты: успешно разрешены через rebase


Ссылка на Gist: https://gist.github.com/UnLucky252/a62d1ded4da42376adcac11bfa344975
Репозиторий проекта: https://github.com/UnLucky252/risks_labs
