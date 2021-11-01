<p align="center">
  <img align="center" height="200" src="https://pht.qoo-static.com/VHB9bVB8cTcnqwnu0nJqKYbiutRclnbGxTpwnayKB4vMxZj8pk1220Rg-6oQ68DwAkqO=w512">
</p>
<h1 align="center">BOTAmongUS</h1>

BOT para ser utilizado no Discord, com o intuito de automatizar as partidas do AmongUS. Durante as fases de Task's, o BOT fica responsável de mutar os usuários; e durante a fase de report o BOT desmuta os usuários. Tudo acontece através da captura de tela de um "host" que será também responsável de levantar o BOT.

### Bibliotecas usadas

- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
- [Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)

### Comandos

Comando|Função
---|---
**!host** | É a pessoa responsável de poder dar todos os outros comandos. O bot irá capturar a tela do host, então ele sempre precisa ficar telando o jogo.
**!start** | O bot começa a capturar a tela do host.
**!quit** | O bot para de capturar a tela do host, e também desmuta todos do canal de voz. 
**!user** | Verificar os usuários|hosts que estão no canal de voz.
**!mute** | Muta todo mundo.
**!unmute** | Desmuta todo mundo.

