

## Опис

Цей проєкт є простим макетом калькулятора, створеним за допомогою бібліотеки **Tkinter** в Python.

На даному етапі реалізовано лише графічний інтерфейс користувача без виконання математичних обчислень.

## Функціонал

* поле для введення даних;
* кнопки з цифрами від **0** до **9**;
* кнопки математичних операцій:

  * `+`
  * `-`
  * `*`
  * `/`
* кнопка `=`;
* кнопка `.`.

## Використані технології

* Python 3
* Tkinter

## Як запустити

1. Встановіть Python 3.
2. Завантажте файл проєкту.
3. Запустіть програму командою:

```bash
python calculator.py
```

## Автор

Eduard Slobodian


## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)


## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.


## Authors

- [@octokatherine](https://www.github.com/octokatherine)

