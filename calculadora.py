import tkinter as tk
from tkinter import ttk, messagebox


class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x330+450+200')
        self.resizable(False, False)
        self.title('Calculadora')
        self.iconbitmap('calculadora.ico')
        # Atributos:
        self.expresion = ''
        # Caja de texto (input):
        self.entrada = None
        # StringVar para obtener el valor del input
        self.entrada_texto = tk.StringVar()
        # Creamos los componentes
        self._crear_componentes()

    # Métodos de Clase
    # Para crear componentes:
    def _crear_componentes(self):
        # def _from_rgb(rgb):
        #     """translates an rgb tuple of int to a tkinter friendly color code
        #     """
        #     return "#%02x%02x%02x" % rgb

        # Creamos un frame para la caja de texto:
        entrada_frame = tk.Frame(self, width=400, height=50, bg='grey')
        entrada_frame.pack(side=tk.TOP)
        # Caja de texto:
        entrada = tk.Entry(entrada_frame, font=('arial', 18, 'bold'), bg='grey',
                           textvariable=self.entrada_texto, width=35, justify=tk.RIGHT)
        entrada.grid(row=0, column=0, ipady=10)

        # Creamos otro frame para la parte inferior
        botones_frame = tk.Frame(self, width=400, height=450, bg='grey')
        botones_frame.pack()

        # Primer renglón:
        # Botón AC
        boton_limpiar = tk.Button(botones_frame, text='AC', width='32', height=3,
                                  bd=0, bg='#f79239', cursor='hand2',
                                  command=self._evento_limpiar)
        boton_limpiar.grid(row=0, column=0, columnspan=3, padx=1)

        # Botón ÷
        boton_dividir = tk.Button(botones_frame, text='÷', width='10', height=3,
                                  bd=0, bg='#eee', cursor='hand2',
                                  command=lambda: self._evento_clic('÷')
                                  ).grid(row=0, column=3, padx=1, pady=1)
        # boton_dividir.grid(row=0, column=3, padx=1, pady=1)

        # Segundo renglón:
        # Botón 7
        boton_siete = tk.Button(botones_frame, text='7', width='10', height=3,
                                bd=0, bg='#fff', cursor='hand2',
                                command=lambda: self._evento_clic(7))
        boton_siete.grid(row=1, column=0, padx=1, pady=1)

        # Botón 8
        boton_ocho = tk.Button(botones_frame, text='8', width='10', height=3,
                               bd=0, bg='#fff', cursor='hand2',
                               command=lambda: self._evento_clic(8))
        boton_ocho.grid(row=1, column=1, padx=1, pady=1)

        # Botón 9
        boton_nueve = tk.Button(botones_frame, text='9', width='10', height=3,
                                bd=0, bg='#fff', cursor='hand2',
                                command=lambda: self._evento_clic(9))
        boton_nueve.grid(row=1, column=2, padx=1, pady=1)

        # Botón x
        boton_multiplicacion = tk.Button(botones_frame, text='x', width='10', height=3,
                                         bd=0, bg='#eee', cursor='hand2',
                                         command=lambda: self._evento_clic('x'))
        boton_multiplicacion.grid(row=1, column=3, padx=1, pady=1)

        # Tercer renglón:
        # Botón 4
        boton_cuatro = tk.Button(botones_frame, text='4', width='10', height=3,
                                 bd=0, bg='#fff', cursor='hand2',
                                 command=lambda: self._evento_clic(4))
        boton_cuatro.grid(row=2, column=0, padx=1, pady=1)

        # Botón 5
        boton_cinco = tk.Button(botones_frame, text='5', width='10', height=3,
                                bd=0, bg='#fff', cursor='hand2',
                                command=lambda: self._evento_clic(5))
        boton_cinco.grid(row=2, column=1, padx=1, pady=1)

        # Botón 6
        boton_seis = tk.Button(botones_frame, text='6', width='10', height=3,
                               bd=0, bg='#fff', cursor='hand2',
                               command=lambda: self._evento_clic(6))
        boton_seis.grid(row=2, column=2, padx=1, pady=1)

        # Botón -
        boton_resta = tk.Button(botones_frame, text='-', width='10', height=3,
                                bd=0, bg='#eee', cursor='hand2',
                                command=lambda: self._evento_clic('-'))
        boton_resta.grid(row=2, column=3, padx=1, pady=1)

        # Cuarto renglón:
        # Botón 1
        boton_uno = tk.Button(botones_frame, text='1', width='10', height=3,
                              bd=0, bg='#fff', cursor='hand2',
                              command=lambda: self._evento_clic(1))
        boton_uno.grid(row=3, column=0, padx=1, pady=1)

        # Botón 2
        boton_dos = tk.Button(botones_frame, text='2', width='10', height=3,
                              bd=0, bg='#fff', cursor='hand2',
                              command=lambda: self._evento_clic(2))
        boton_dos.grid(row=3, column=1, padx=1, pady=1)

        # Botón 3
        boton_tres = tk.Button(botones_frame, text='3', width='10', height=3,
                               bd=0, bg='#fff', cursor='hand2',
                               command=lambda: self._evento_clic(3))
        boton_tres.grid(row=3, column=2, padx=1, pady=1)

        # Botón +
        boton_suma = tk.Button(botones_frame, text='+', width='10', height=3,
                               bd=0, bg='#eee', cursor='hand2',
                               command=lambda: self._evento_clic('+'))
        boton_suma.grid(row=3, column=3, padx=1, pady=1)

        # Quinto renglón:
        # Botón 0
        boton_cero = tk.Button(botones_frame, text='0', width='21', height=3,
                               bd=0, bg='#fff', cursor='hand2',
                               command=lambda: self._evento_clic(0))
        boton_cero.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

        # Botón .
        boton_decimal = tk.Button(botones_frame, text='.', width='10', height=3,
                                  bd=0, bg='#fff', cursor='hand2',
                                  command=lambda: self._evento_clic('.'))
        boton_decimal.grid(row=4, column=2, padx=1, pady=1)

        # Botón =
        boton_evaluar = tk.Button(botones_frame, text='=', width='10', height=3,
                                  bd=0, bg='#eee', cursor='hand2',
                                  command=self._evento_evaluar)
        boton_evaluar.grid(row=4, column=3, padx=1, pady=1)

    # Eventos botones
    def _evento_limpiar(self):
        self.expresion = ''
        self.entrada_texto.set(self.expresion)

    def _evento_clic(self, elemento):
        # concatenamods el nuevo elemento a la expresion ya existente
        self.expresion = f'{self.expresion}{elemento}'
        self.entrada_texto.set(self.expresion)

    def filtro_simbolos(self):
        # Filtrar y reemplazar los símbolos ÷ y x por:
        self.expresion = self.expresion.replace('÷', '/')
        self.expresion = self.expresion.replace('x', '*')

    def _evento_evaluar(self):
        self.filtro_simbolos()
        try:
            if self.expresion:
                # eval -> para evaluar un string como una expresión aritmética
                resultado = str(eval(self.expresion))
                self.entrada_texto.set(resultado)
        except Exception as e:
            # messagebox.showerror('Error', f'Ocurrió un error: {e}')
            messagebox.showerror('Error', 'Expresión Inválida')
            self.entrada_texto.set('')
        self.expresion = ''

if __name__ == '__main__':
    calculadora = Calculadora()
    calculadora.mainloop()
