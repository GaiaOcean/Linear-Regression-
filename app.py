import tkinter as tk
from tkinter import messagebox
import methods
import matplotlib.pyplot as plt

class AppRegressaoLinear:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculo Numérico - Regressão Linear (PUC-SP)")
        self.root.geometry("1150x850")
        self.root.configure(bg="#1e1e24")
        self.build_ui()

    def build_ui(self):
        frame_topo = tk.Frame(self.root, bg="#1e1e24")
        frame_topo.pack(pady=15, fill="x", padx=25)

        tk.Label(frame_topo, text="Valores de X - separados por espaço:", 
                 bg="#1e1e24", fg="white", font=("Arial", 11, "bold")).pack(anchor="w")
        self.ent_x = tk.Entry(frame_topo, font=("Courier", 14), bg="#cfd0d1")
        self.ent_x.pack(fill="x", ipady=8, pady=(0, 10))

        tk.Label(frame_topo, text="Valores de Y - separados por espaço:", 
                 bg="#1e1e24", fg="white", font=("Arial", 11, "bold")).pack(anchor="w")
        self.ent_y = tk.Entry(frame_topo, font=("Courier", 14), bg="#cfd0d1")
        self.ent_y.pack(fill="x", ipady=8)

        tk.Button(self.root, text="CALCULAR REGRESSÃO E GERAR GRÁFICO", bg="#5cb85c", fg="white", 
                  font=("Arial", 12, "bold"), command=self.executar, height=2).pack(fill="x", padx=25, pady=15)

        frame_visor = tk.Frame(self.root, bg="#1e1e24")
        frame_visor.pack(fill="both", expand=True, padx=25, pady=(0, 25))

        self.scroll = tk.Scrollbar(frame_visor)
        self.scroll.pack(side="right", fill="y")

        self.visor = tk.Text(frame_visor, font=("Courier", 11), bg="#2b2b36", fg="#5cb85c", 
                             padx=15, pady=15, yscrollcommand=self.scroll.set)
        self.visor.pack(side="left", fill="both", expand=True)
        self.scroll.config(command=self.visor.yview)

    def analisar_entrada(self, texto):
        texto = texto.replace(',', ' ').strip()
        return [float(i) for i in texto.split()]

    def executar(self):
        try:
            x = self.analisar_entrada(self.ent_x.get())
            y = self.analisar_entrada(self.ent_y.get())

            if len(x) != len(y) or len(x) == 0:
                raise ValueError("Inconsistência na quantidade de dados entre X e Y.")

            n = methods.getNumDuplas(x)
            
            mediaX = methods.calcularMediaAritmetica(x, n)
            mediaY = methods.calcularMediaAritmetica(y, n)
            mediaXY = methods.calcularMediaDoProduto(x, y, n)
            
            cov = methods.calcularCovariancia(mediaX, mediaY, mediaXY)
            
            mediaQuadX = methods.calcularMediaDosQuadrados(x, n)
            mediaQuadY = methods.calcularMediaDosQuadrados(y, n)
            
            desvioX = methods.calcularDesvioPadrao(mediaQuadX, mediaX)
            desvioY = methods.calcularDesvioPadrao(mediaQuadY, mediaY)
            
            r = methods.calcularCoeficienteDePearson(cov, desvioX, desvioY)
            r2 = methods.calcularCoeficienteDeDeterminacao(r)

            somaX, somaY, somaXY, somaX2, somaY2 = methods.calcularSomas(x, y, n)
            a, b = methods.calcularRetaRegressao(x,y,n)

            r2_pct = r2 * 100

            rel = f"RELATÓRIO DE REGRESSÃO LINEAR\n\n"
            rel += f"n: {n}\n"
            rel += f"ΣX: {somaX:.4f}\n"
            rel += f"ΣY: {somaY:.4f}\n"
            rel += f"ΣXY: {somaXY:.4f}\n"
            rel += f"ΣX²: {somaX2:.4f}\n"
            rel += f"ΣY²: {somaY2:.4f}\n"
            rel += f"σx: {desvioX:.8f}\n"
            rel += f"σy: {desvioY:.8f}\n"
            rel += f"μx: {mediaX:.4f}\n"
            rel += f"μy: {mediaY:.4f}\n"
            rel += f"μxy: {mediaXY:.4f}\n"
            rel += f"Cov(X,Y): {cov:.8f}\n"
            rel += f"r: {r:.8f}\n"
            rel += f"r²: {r2_pct:.2f}%\n\n"
            rel += f"a: {a:.6f}\n"
            rel += f"b: {b:.6f}\n"
            rel += f"Equação: Y = {a:.6f} + {b:.6f}X\n"

            self.visor.delete(1.0, tk.END)
            self.visor.insert(tk.END, rel)

            plt.figure(num="Diagrama de Dispersão")
            plt.scatter(x, y, color='blue', label='Dados Observados')
            
            x_line = [min(x), max(x)]
            y_line = [a + b * val for val in x_line]
            plt.plot(x_line, y_line, color='red', label=f'Y = {a:.2f} + {b:.2f}X')
            
            plt.title('Regressão Linear')
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.legend()
            plt.grid(True, linestyle='--', alpha=0.6)
            plt.show()

        except Exception as e:
            messagebox.showerror("Erro", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    AppRegressaoLinear(root)
    root.mainloop()