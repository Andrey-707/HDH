Компеллирование кода в .exe

После установки расширения "pip install pyinstaller"

Прописывается в коммандной строке:

pyinstaller
-i "<путь-к-икоке> + <название-иконки>.ico" !!! Путь к иконке в кавычках !!!
-F <название-файла>.py !!! Название файла, который содержит код БЕЗ кавычек !!!

Например:

pyinstaller -i "D:\\Python\\Test\\ICON\\Icon.ico" -F Main_file.py
