# reminder
## Russian

Это напоминалка, которая выводит окно с зацикленным видеороликом, при нажатии на кнопку окно закрывается. 
Программа работает в бесконечном цикле и проверяет не пришло ли нужное время (по умолчанию 30 минут), если да, то вызывается окно с видео. Когда пользователь закрывает окно, программа назначает новое время срабатывания и ждёт. Это не лучший алгоритм, и изначально планировалось всё запускать через cron, но cron не смог запустить приложение(программа ложилась на строке app = QAppli...). В файле settings.ini лежат настройки проекта, здесь можно изменить имя входного файла, громкость и период срабатывания (в минутах).
Интерфейс написан на `PySide2` (в pyqt5 не нашлось QtMultimedia). Тестировалось на `Kubuntu 21.04`. Видеоролик был нагло украден с канала [Доктор Дью](https://www.youtube.com/channel/UCsJR1qQDNyFvsX_9_bNM63A). 

## English

This is a reminder that displays a window with a looped video, when you click on the button, the window closes.
The program works in an infinite loop and checks whether the right time has come (by default, 30 minutes), if so, a window with a video is called. When the user closes the window, the program assigns a new trigger time and waits. This is not the best algorithm, and it was originally planned to run everything through cron, but cron could not launch the application(the program fell on the app line = QAppli...). The settings. ini file contains the project settings, here you can change the name of the input file, the volume and the response period (in minutes).
The interface is written in `PySide2` (there was no QtMultimedia in pyqt5). It was tested on `Kubuntu 21.04`. The video was brazenly stolen from the channel [Доктор Дью](https://www.youtube.com/channel/UCsJR1qQDNyFvsX_9_bNM63A).

## Video
https://user-images.githubusercontent.com/80480605/130331941-75a31d2c-2e18-4df7-b83e-2208901c0206.mp4



