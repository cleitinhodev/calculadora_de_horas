"""
Hours Calculator - Hours calculation tool (C) 2025 CleitinhoDEV

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.

---

Calculadora de Horas - Ferramenta de calculo para horas (C) 2025 CleitinhoDEV

Este programa é um software livre: você pode redistribuí-lo e/ou modificá-lo
sob os termos da Licença Pública Geral GNU, conforme publicada pela
Free Software Foundation, na versão 3 da Licença, ou (a seu critério) qualquer versão posterior.

Este programa é distribuído na esperança de que seja útil,
mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
COMERCIABILIDADE ou ADEQUAÇÃO A UM DETERMINADO PROPÓSITO. Consulte a
Licença Pública Geral GNU para mais detalhes.

Você deve ter recebido uma cópia da Licença Pública Geral GNU
junto com este programa. Caso contrário, veja <https://www.gnu.org/licenses/>."""

import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")


class BooleanOperacao(ctk.CTkFrame):
    def __init__(self, master, tempos_ecritos, resultado_de_tempos):
        super().__init__(master)
        self.tempos_ecritos = tempos_ecritos
        self.resultado_de_tempos = resultado_de_tempos

        self.var_ativo = ctk.BooleanVar(value=True)

        self.cor_ativa = "white"
        self.cor_inativa = "#444"
        self.cor_fundo_conteudo = "#222"

        self.frame_de_selecao = ctk.CTkFrame(self)

        self.label_selecione = ctk.CTkLabel(self.frame_de_selecao,
                                            text='Selecione uma Opção:',
                                            font=('Arial', 20))
        self.label_selecione.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.botao_calcular = ctk.CTkButton(
            self.frame_de_selecao,
            text='Calcular',
            font=('Arial', 20),
            width=200,
            height=80,
            fg_color="#222222",  # Cor de fundo normal (escuro)
            hover_color="#111111",  # Quando passa o mouse (ainda mais escuro)
            text_color="white",  # Cor da fonte
            border_color="white",  # Cor da borda
            border_width=2,  # Espessura da borda
            command=self.calcular_valores
        )
        self.botao_calcular.grid(row=2, column=0, columnspan=2, padx=10, pady=18)

        # Moldura 1
        self.moldura1 = ctk.CTkFrame(self.frame_de_selecao, fg_color=self.cor_ativa, corner_radius=1)
        self.conteudo1 = ctk.CTkFrame(self.moldura1, fg_color=self.cor_fundo_conteudo, corner_radius=8)
        self.label1 = ctk.CTkLabel(self.conteudo1,
                                   text="+",
                                   fg_color="transparent",
                                   text_color="white",
                                   width=100,
                                   height=100,
                                   font=('Arial', 50))
        self.label1.pack(expand=True, fill="both")
        self.conteudo1.pack(padx=2, pady=2)
        self.moldura1.grid(row=1, column=0, padx=10, pady=10)
        self.label1.bind("<Button-1>", lambda e: self.toggle(True))

        # Moldura 2
        self.moldura2 = ctk.CTkFrame(self.frame_de_selecao, fg_color=self.cor_inativa, corner_radius=1)
        self.conteudo2 = ctk.CTkFrame(self.moldura2, fg_color=self.cor_fundo_conteudo, corner_radius=8)
        self.label2 = ctk.CTkLabel(self.conteudo2,
                                   text="-",
                                   fg_color="transparent",
                                   text_color="white",
                                   width=100,
                                   height=100,
                                   font=('Arial', 50))
        self.label2.pack(expand=True, fill="both")
        self.conteudo2.pack(padx=2, pady=2)
        self.moldura2.grid(row=1, column=1, padx=10, pady=10)
        self.label2.bind("<Button-1>", lambda e: self.toggle(False))

        self.atualizar_bordas()
        self.frame_de_selecao.pack()

    def toggle(self, estado: bool):
        self.var_ativo.set(estado)
        self.atualizar_bordas()

    def atualizar_bordas(self):
        if self.var_ativo.get():
            self.moldura1.configure(fg_color=self.cor_ativa)
            self.moldura2.configure(fg_color=self.cor_inativa)
        else:
            self.moldura1.configure(fg_color=self.cor_inativa)
            self.moldura2.configure(fg_color=self.cor_ativa)

    def calcular_valores(self):
        """Pega os valores em lista [[HH:MM:SS:ms], [HH:MM:SS:cs]]"""
        lista_de_datas = self.tempos_ecritos.reunir_valores()
        for i in range(4):
            try:
                lista_de_datas[0][i] = int(lista_de_datas[0][i] or 0)
            except ValueError:
                lista_de_datas[0][i] = 0

            try:
                lista_de_datas[1][i] = int(lista_de_datas[1][i] or 0)
            except ValueError:
                lista_de_datas[1][i] = 0
        if self.var_ativo.get():
            cs = []
            seg = []
            minu = []

            horas = int(lista_de_datas[0][0]) + int(lista_de_datas[1][0])
            minutos = int(lista_de_datas[0][1]) + int(lista_de_datas[1][1])
            segundos = int(lista_de_datas[0][2]) + int(lista_de_datas[1][2])
            centesimos = int(lista_de_datas[0][3]) + int(lista_de_datas[1][3])

            cs.append(centesimos // 100)
            cs.append(centesimos % 100)

            centesimos = cs[1]
            segundos += cs[0]

            seg.append(segundos // 60)
            seg.append(segundos % 60)

            segundos = seg[1]
            minutos += seg[0]

            minu.append(minutos // 60)
            minu.append(minutos % 60)

            minutos = minu[1]
            horas += minu[0]

            lista_final = [horas, minutos, segundos, centesimos]

            if any(num > 100000 for num in lista_final):
                messagebox.showinfo("Valores muito grandes!", "Use valores menores.")
                self.tempos_ecritos.zerar_valores()
                self.resultado_de_tempos.zerar_resultados()
            else:
                self.resultado_de_tempos.exibir_resultados(lista_final)

        else:
            def tempo_para_centesimos(t):
                h, m, s, c = t
                return h * 360000 + m * 6000 + s * 100 + c

            def centesimos_para_tempo(total):
                h = total // 360000
                total %= 360000
                m = total // 6000
                total %= 6000
                s = total // 100
                c = total % 100
                return [h, m, s, c]

            def diferenca_tempos(t1, t2):
                total1 = tempo_para_centesimos(t1)
                total2 = tempo_para_centesimos(t2)
                diff = abs(total1 - total2)  # <- sempre positivo!
                return centesimos_para_tempo(diff)

            lista_final = diferenca_tempos(lista_de_datas[0], lista_de_datas[1])

            self.resultado_de_tempos.exibir_resultados(lista_final)


class ResultadoDeTempos(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(
            master,
            border_color="white",
            border_width=1,
        )

        # Pega a cor de fundo do tema atual
        self.cor_fundo_resultado = ctk.ThemeManager.theme["CTkEntry"]["fg_color"]

        # Stringvars

        self.var_horas_resultado = ctk.StringVar()
        self.var_minutos_resultado = ctk.StringVar()
        self.var_segundos_resultado = ctk.StringVar()
        self.var_milesimos_resultado = ctk.StringVar()

        # Display Resultados

        self.resultado_horas = ctk.CTkLabel(self,
                                            textvariable=self.var_horas_resultado,
                                            font=('Arial', 50),
                                            fg_color=self.cor_fundo_resultado,
                                            bg_color=self.cor_fundo_resultado,
                                            width=200
                                            )
        self.resultado_minutos = ctk.CTkLabel(self,
                                              textvariable=self.var_minutos_resultado,
                                              font=('Arial', 50),
                                              fg_color=self.cor_fundo_resultado,
                                              bg_color=self.cor_fundo_resultado,
                                              width=200
                                              )
        self.resultado_segundos = ctk.CTkLabel(self,
                                               textvariable=self.var_segundos_resultado,
                                               font=('Arial', 50),
                                               fg_color=self.cor_fundo_resultado,
                                               bg_color=self.cor_fundo_resultado,
                                               width=200
                                               )
        self.resultado_milesimos = ctk.CTkLabel(self,
                                                textvariable=self.var_milesimos_resultado,
                                                font=('Arial', 50),
                                                fg_color=self.cor_fundo_resultado,
                                                bg_color=self.cor_fundo_resultado,
                                                width=200
                                                )

        for ele in range(1, 7, 2):
            self.label_ponto_resultado = ctk.CTkLabel(self, text=':', font=('Arial', 50),
                                                      fg_color='transparent')
            self.label_ponto_resultado.grid(row=0, column=ele)

        self.resultado_horas.grid(row=0, column=0, padx=10, pady=10)
        self.resultado_minutos.grid(row=0, column=2, padx=10, pady=10)
        self.resultado_segundos.grid(row=0, column=4, padx=10, pady=10)
        self.resultado_milesimos.grid(row=0, column=6, padx=10, pady=10)

    def exibir_resultados(self, lista):
        print(lista)
        self.var_horas_resultado.set(str(lista[0]))
        self.var_minutos_resultado.set(str(lista[1]))
        self.var_segundos_resultado.set(str(lista[2]))
        self.var_milesimos_resultado.set(str(lista[3]))

    def zerar_resultados(self):
        self.var_horas_resultado.set('')
        self.var_minutos_resultado.set('')
        self.var_segundos_resultado.set('')
        self.var_milesimos_resultado.set('')


class TemposEscritos(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(
            master,
            border_color="white",  # Cor da borda
            border_width=1  # Largura da borda
        )

        # Validação para aceitar apenas números
        self.vcmd = (self.register(self.somente_numeros), '%P')

        # Pega a cor de fundo do tema atual
        self.cor_fundo = ctk.ThemeManager.theme["CTkEntry"]["fg_color"]

        # StringVar para controlar o texto
        self.var_horas_1 = ctk.StringVar()
        self.var_horas_1.set('00')
        self.var_minutos_1 = ctk.StringVar()
        self.var_minutos_1.set('00')
        self.var_segundos_1 = ctk.StringVar()
        self.var_segundos_1.set('00')
        self.var_milesimos_1 = ctk.StringVar()
        self.var_milesimos_1.set('00')

        self.var_horas_2 = ctk.StringVar()
        self.var_horas_2.set('00')
        self.var_minutos_2 = ctk.StringVar()
        self.var_minutos_2.set('00')
        self.var_segundos_2 = ctk.StringVar()
        self.var_segundos_2.set('00')
        self.var_milesimos_2 = ctk.StringVar()
        self.var_milesimos_2.set('00')

        # Campo de rótulos

        self.label_titulo_hora = ctk.CTkLabel(self, text='Horas', font=('Arial', 20),
                                              fg_color='transparent')
        self.label_titulo_minutos = ctk.CTkLabel(self, text='Minutos', font=('Arial', 20),
                                                 fg_color='transparent')
        self.label_titulo_segundos = ctk.CTkLabel(self, text='Segundos', font=('Arial', 20),
                                                  fg_color='transparent')
        self.label_titulo_milesimos = ctk.CTkLabel(self, text='Centésimos (1/100 s)', font=('Arial', 20),
                                                   fg_color='transparent')

        # Campo de entrada com fonte grande e fundo do tema
        self.caixa_de_horas_1 = ctk.CTkEntry(
            self,
            font=('Arial', 50),
            fg_color=self.cor_fundo,
            textvariable=self.var_horas_1,
            width=200,
            justify="right",
            validate="key",
            validatecommand=self.vcmd
        )
        self.caixa_de_minutos_1 = ctk.CTkEntry(
            self,
            font=('Arial', 50),
            fg_color=self.cor_fundo,
            textvariable=self.var_minutos_1,
            width=200,
            justify="right",
            validate="key",
            validatecommand=self.vcmd
        )
        self.caixa_de_segundos_1 = ctk.CTkEntry(
            self,
            font=('Arial', 50),
            fg_color=self.cor_fundo,
            textvariable=self.var_segundos_1,
            width=200,
            justify="right",
            validate="key",
            validatecommand=self.vcmd
        )
        self.caixa_de_milesimos_1 = ctk.CTkEntry(
            self,
            font=('Arial', 50),
            fg_color=self.cor_fundo,
            textvariable=self.var_milesimos_1,
            width=200,
            justify="right",
            validate="key",
            validatecommand=self.vcmd
        )
        self.caixa_de_horas_2 = ctk.CTkEntry(
            self,
            font=('Arial', 50),
            fg_color=self.cor_fundo,
            textvariable=self.var_horas_2,
            width=200,
            justify="right",
            validate="key",
            validatecommand=self.vcmd
        )
        self.caixa_de_minutos_2 = ctk.CTkEntry(
            self,
            font=('Arial', 50),
            fg_color=self.cor_fundo,
            textvariable=self.var_minutos_2,
            width=200,
            justify="right",
            validate="key",
            validatecommand=self.vcmd
        )
        self.caixa_de_segundos_2 = ctk.CTkEntry(
            self,
            font=('Arial', 50),
            fg_color=self.cor_fundo,
            textvariable=self.var_segundos_2,
            width=200,
            justify="right",
            validate="key",
            validatecommand=self.vcmd
        )
        self.caixa_de_milesimos_2 = ctk.CTkEntry(
            self,
            font=('Arial', 50),
            fg_color=self.cor_fundo,
            textvariable=self.var_milesimos_2,
            width=200,
            justify="right",
            validate="key",
            validatecommand=self.vcmd
        )
        for ele in range(1, 7, 2):
            self.label_ponto_1 = ctk.CTkLabel(self, text=':', font=('Arial', 50),
                                              fg_color='transparent')
            self.label_ponto_1.grid(row=1, column=ele)

        for ele in range(1, 7, 2):
            self.label_ponto_2 = ctk.CTkLabel(self, text=':', font=('Arial', 50),
                                              fg_color='transparent')
            self.label_ponto_2.grid(row=2, column=ele)

        self.label_titulo_hora.grid(row=0, column=0, pady=5)
        self.label_titulo_minutos.grid(row=0, column=2, pady=5)
        self.label_titulo_segundos.grid(row=0, column=4, pady=5)
        self.label_titulo_milesimos.grid(row=0, column=6, pady=5)

        self.caixa_de_horas_1.grid(row=1, column=0, padx=10, pady=10)
        self.caixa_de_minutos_1.grid(row=1, column=2, padx=10, pady=10)
        self.caixa_de_segundos_1.grid(row=1, column=4, padx=10, pady=10)
        self.caixa_de_milesimos_1.grid(row=1, column=6, padx=10, pady=10)

        self.caixa_de_horas_2.grid(row=2, column=0, padx=10, pady=10)
        self.caixa_de_minutos_2.grid(row=2, column=2, padx=10, pady=10)
        self.caixa_de_segundos_2.grid(row=2, column=4, padx=10, pady=10)
        self.caixa_de_milesimos_2.grid(row=2, column=6, padx=10, pady=10)

        # Sempre que o texto muda, chama a função de validação
        self.var_horas_1.trace_add("write", self.limita_texto)
        self.var_minutos_1.trace_add("write", self.limita_texto)
        self.var_segundos_1.trace_add("write", self.limita_texto)
        self.var_milesimos_1.trace_add("write", self.limita_texto)

        self.var_horas_2.trace_add("write", self.limita_texto)
        self.var_minutos_2.trace_add("write", self.limita_texto)
        self.var_segundos_2.trace_add("write", self.limita_texto)
        self.var_milesimos_2.trace_add("write", self.limita_texto)

    def limita_texto(self, *args):
        vars_to_limit = [
            self.var_horas_1, self.var_minutos_1, self.var_segundos_1, self.var_milesimos_1,
            self.var_horas_2, self.var_minutos_2, self.var_segundos_2, self.var_milesimos_2
        ]
        for var in vars_to_limit:
            texto = var.get()
            if len(texto) > 5:
                var.set(texto[:5])

    def reunir_valores(self):
        lista_a = [self.var_horas_1.get(),
                   self.var_minutos_1.get(),
                   self.var_segundos_1.get(),
                   self.var_milesimos_1.get()]
        lista_b = [self.var_horas_2.get(),
                   self.var_minutos_2.get(),
                   self.var_segundos_2.get(),
                   self.var_milesimos_2.get()]
        return [lista_a, lista_b]

    def zerar_valores(self):
        self.var_horas_1.set('00')
        self.var_minutos_1.set('00')
        self.var_segundos_1.set('00')
        self.var_milesimos_1.set('00')

        self.var_horas_2.set('00')
        self.var_minutos_2.set('00')
        self.var_segundos_2.set('00')
        self.var_milesimos_2.set('00')

    @staticmethod
    def somente_numeros(valor):
        return valor.isdigit() or valor == ""


class App:
    def __init__(self, master):
        self.root = master
        self.root.resizable(False, False)
        self.root.title('Calculadora de Horas')

        self.tempos_escritos = TemposEscritos(self.root)
        self.resultado_de_tempos = ResultadoDeTempos(self.root)

        self.tempos_escritos.grid(row=0, column=1)
        self.resultado_de_tempos.grid(row=1, column=1)

        self.seletores = BooleanOperacao(self.root, self.tempos_escritos, self.resultado_de_tempos)
        self.seletores.grid(row=0, column=0, rowspan=2, sticky="nsew")

        self.label_nome = ctk.CTkLabel(self.root,
                                       text='CleitinhoDEV (www.bugzinho.com)',
                                       font=('Arial', 10),
                                       anchor=ctk.N,
                                       fg_color="#333333",
                                       text_color='#505050')
        self.label_nome.place(x=8, y=275)


if __name__ == "__main__":
    root = ctk.CTk()
    app = App(root)

    largura = 1180
    altura = 288

    # Calcula o centro
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()
    pos_x = int((largura_tela / 2) - (largura / 2))
    pos_y = int((altura_tela / 2) - (altura / 2))

    # Aplica tamanho e posição
    root.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

    root.mainloop()
