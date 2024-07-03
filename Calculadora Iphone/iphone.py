import flet as ft
from flet import colors
from decimal import Decimal

# Definição dos botões da calculadora
botoes = [
    {'operador': 'AC', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '±',  'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '%',  'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '/',  'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '7',  'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '8',  'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '9',  'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '*',  'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '4',  'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '5',  'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '6',  'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '-',  'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '1',  'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '2',  'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '3',  'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '+',  'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': ' ',  'fonte': colors.BLACK, 'fundo': colors.BLACK},  # Botão invisivel 
    {'operador': '0',  'fonte': colors.WHITE, 'fundo': colors.WHITE24, 'colspan': 2},
    {'operador': '.',  'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '=',  'fonte': colors.WHITE, 'fundo': colors.ORANGE},
]

def main(pagina: ft.page):
    pagina.bgcolor = '#000'
    pagina.window_resizable = False
    pagina.window_width = 250
    pagina.window_height = 380
    pagina.title = 'Calculadora'

    global result
    result = ft.Text(value='0', color=colors.WHITE, size=20)

    def calcular(expressao):
        try:
            resultado = eval(expressao)
            return str(resultado)
        except Exception as e:
            print(f"Erro ao calcular: {e}")
            return 'Erro'

    def selecionar_botao(e):
        botao_clicado = e.control.content.value

        if botao_clicado == '=':
            resultado = calcular(result.value)
            result.value = resultado
        elif botao_clicado == 'AC':
            result.value = '0'
        else:
            if result.value == '0' or result.value == 'Erro':
                result.value = botao_clicado
            else:
                result.value += botao_clicado

        result.update()

    display = ft.Row(
        width=250,
        controls=[result],
        alignment='end'
    )

    botoes_calculadora = []
    for btn in botoes:
        if 'colspan' in btn:
            largura = 110
        else:
            largura = 50

        botao = ft.Container(
            content=ft.Text(value=btn['operador'], color=btn['fonte']),
            width=largura,
            height=50,
            bgcolor=btn['fundo'],
            border_radius=100,
            alignment=ft.alignment.center,
        )
        botao.on_click = lambda e, valor=btn['operador']: selecionar_botao(e)
        botoes_calculadora.append(botao)

    teclado = ft.GridView(
        expand=1,
        max_extent=60,
        child_aspect_ratio=1.0,
        padding=5,
        run_spacing=5,
        spacing=5,
        controls=botoes_calculadora,
    )

    pagina.add(display)
    pagina.add(teclado)

ft.app(target=main)
