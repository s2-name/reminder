# reminder
## Russian

Это напоминалка, которая выводит окно с зацикленным видеороликом (его можно изменить в коде), при нажатии на кнопку окно закрывается. 
По задумке запуск данного скрипта должен был осуществляться из-под cron командой `* * * * * cd /path/to/files/ && python3 main.py`, 
но из-под cron не получается инициализировать программу (она падает на строке app = QApplication(sys.argv)). Вы можете попробовать это реализовать. 
Интерфейс написан на `PySide2` (в pyqt5 не нашлось QtMultimedia). Тестировалось на `Kubuntu 21.04`. Видеоролик был нагло украден с канала [Доктор Дью](https://www.youtube.com/channel/UCsJR1qQDNyFvsX_9_bNM63A)

## English

This is a reminder that displays a window with a looped video (it can be changed in the code), when you click on the button, the window closes.
According to the idea, the launch of this script was to be carried out from under the cron command `* * * * * cd /path/to/files/ & & python 3 main.py`,
but it is not possible to initialize the program from under cron (it crashes on the app line = QApplication(sys.argv)). You can try to implement this.
The interface is written in `PySide2` (there was no QtMultimedia in pyqt5). Tested on `Kubuntu 21.04`. The video was brazenly stolen from the channel [Доктор Дью](https://www.youtube.com/channel/UCsJR1qQDNyFvsX_9_bNM63A)

