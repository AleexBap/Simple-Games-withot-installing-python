# In the Create_Games.ipynb, are the games to play on the terminal of python and the respetive interface to play using tkinter.
# In the Games.py, are all of the games and the respetive menu to all the games that we use to create a .exe so anyone can play.

By usind the follow commands in the terminal with the dir in the folder Games we can have a folder name dist that can be send to anyone to play the games even without having python install.

1- You need to install this library:

python -m pip install pyinstaller

2- Running this command on the dir of folder GAMES:

python -m PyInstaller --windowed --onedir --name MyGames "Games.py"

3- Now that we have the folder dist, we can just share the folder with anyone and they can play the games.
