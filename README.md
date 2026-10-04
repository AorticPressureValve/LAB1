ЛАбараторная работа 1
студент: Ольхов Александр Сергеевич
группа:М8О-105БВ-26

в лабараторной работе были реализованы два модуля на питоне
calc и convert

структура проекта:
LAB1/
├── src/
│   └── toolkit/
│       ├── __init__.py
│       ├── __main__.py
│       ├── converter.py
│       ├── constants.py
│       ├── calculator.py 
│       └── converter.py
│
├── tests/
│   |── conftest.py
│   ├── test_CLI.py
│   ├── test_calculator.py 
│   └── test_converter.py
│
├── pyproject.ini
├── .pre-commit-config.yaml
├── requirements.txt
└── README.md

требования из requirements.txt

установаить можно командой: pip install -r requirements.txt
