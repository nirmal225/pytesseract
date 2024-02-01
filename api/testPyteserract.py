from Pytesseract import Pytesseract
encoded_text = 'iVBORw0KGgoAAAANSUhEUgAAAMsAAAAyCAYAAADyZi/iAAAECklEQVR42u2cT2RcQRzHYw8R0UvE6qGiRFWsVaWiIlaFHmLl0EtU9dDDUjlXLj1UrCpROURVrjlUhYqoFVUi9lA99FIVFWuJqKoeylpVa61l+xt+y/hl9u17+/a9N/ve98NPyM783sy8+Zrf/HtjYwAAAAAAAAAAAAAAAAAAACBUOkNgFMoYZfmH3Ba5Ua8DxAKxhPGuJsnOIBaIBWLp3w7bcRgdYyMW1MXaui1qVatDLOhgqIu5XhMi/CpALOhgqIu5XltatcpxH0UT28HI5R2yt2Q/yVpkTbJfZHtk+VEVC7lfJtslOyFrkLX57yn//+6QnnNbq5Jqu1mIJWZiIVdpsg8u5tdlssvDKEsYHYjcLpFVXa4dfCPL+njWOFlF87eehPlZosTCQql6WJBS8fi07WIhl08GWGz7qwQ24PM2deElZTEjaWIpC7dtfvEZshRbluwl/6Y4sFks5G7NUKfXPNKMayPBKtlXkbbWDZ88PG9ePCsDscRMLOTisXD5j2zBIf0Cp+nYKhZyNcfzrS5/VGd2SJ/iOZnOocfw61TL+yIpixlJE8u5cFkYQGC2iaUkXC+57PAVkS/r8nlFLU+lO3JBLJaJxc/uN6986VQ9lKNio1hU+CTcfvQRuj13keeGFpoqFqNe+QPBiGVL/Fz0UI4NS8WyLtw+8JB3RuQ96pNehW/ftfQ7Ua78gWDFcih+znsoR95SsewLt3M+ylT3EH6pvahLEEtM5yw88dWZ8pB3ylKxyDlY04X1ounwnKwIv1aiWvkD4YilOagvDkFsFEsj6BPOXPcTLdleVIsZIDyxtKLs7AGJpROCWJ6JPZlpiAUjyyiOLC3hNhXAO9DDr4dR1RWEK5ZaDOcsNT8T/ChGL4hnNMQSx9UwuSF5H2KBWIYhljjusxSF232IBWIZhliWfOzgVy0VS1a4VXOYq3F6byCiRjfsS6y5yFOw/GzYsbyDA7FALEGdOs45pM/12suwSCwZw2bjgdMOu8ivzswdQywQi8lnz/ssIrzZ1JZN9y2/z/LIoGd1JOUp2a3ukjIvgV8hu8dzuLOAygOxxEQsadMpYgfODTcl27Z1IA4X2zZMuiGWGMW+LJiSyzv4aUNZGjZ2IB4RP3nQiBLXO/XhCYgFYnETr6uvu/zgjtPmL72om4TLWrpJUZTfNncgDr3Utegjvmff5pUyNUf7QvZG7cl42ZiFWIDbl78iJ9BoFQDMYtkRYtlAqwBwUSjXDQcWb6JlQFIE8N7N538ozTWez+h8RguCJC4clHiiO6vtRUzwwclXhs2+lp+vOAIwymLpeFxmXUXrAYil/3eB59FyIIlimeEjIrv8gfAanwHrftShzgcUt53OjgEAAAAAAAAAAAAAcIH/E/DB7eAxBLwAAAAASUVORK5CYII='
py = Pytesseract()
py.save_mage(encoded_text)