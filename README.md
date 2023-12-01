## Info
Скрипт, который преобразует task5.csv, добавив поле
process.parent.command_line, в котором содержится process.command_line родителя процесса.

Руководство
```
python3 parse.py -h
```
| --help       | --file       | --output |
|:-------------:|:-------------: |:---------:|
| Помощь | Название csv файла | Название результируемого файла |

## Example
Вывести в файл
```
py parse.py -f=task5.csv -o=out.csv
```
Вывести в stdout
```
py parse.py -f=task5.csv
```
