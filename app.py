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

        tk.Label(frame_topo, text="Nome da variável independente:", 
        bg="#1e1e24", fg="white", font=("Arial", 11, "bold")).pack(anchor="w")
        self.nome_indep = tk.Entry(frame_topo, font=("Courier", 14), bg="#cfd0d1")
        self.nome_indep.pack(fill="x", pady=(0,10))

        tk.Label(frame_topo, text="Valores da variável independente (separados por espaço):", 
        bg="#1e1e24", fg="white", font=("Arial", 11, "bold")).pack(anchor="w")
        self.ent_indep = tk.Entry(frame_topo, font=("Courier", 14), bg="#cfd0d1")
        self.ent_indep.pack(fill="x", ipady=8, pady=(0, 10))

        tk.Label(frame_topo, text="Nome da variável dependente:", 
        bg="#1e1e24", fg="white", font=("Arial", 11, "bold")).pack(anchor="w")
        self.nome_dep = tk.Entry(frame_topo, font=("Courier", 14), bg="#cfd0d1")
        self.nome_dep.pack(fill="x", pady=(0,10))

        tk.Label(frame_topo, text="Valores da variável dependente (separados por espaço):",
        bg="#1e1e24", fg="white", font=("Arial", 11, "bold")).pack(anchor="w")
        self.ent_dep = tk.Entry(frame_topo, font=("Courier", 14), bg="#cfd0d1")
        self.ent_dep.pack(fill="x", ipady=8, pady=(0,10))


        tk.Button(self.root, text="CALCULAR REGRESSÃO E GERAR GRÁFICO", bg="#5cb85c", fg="white", 
                  font=("Arial", 12, "bold"), command=self.executar, height=2).pack(fill="x", padx=25, pady=15)

        frame_visor = tk.Frame(self.root, bg="#1e1e24")
        frame_visor.pack(fill="both", expand=True, padx=25, pady=(0, 25))

        self.scroll = tk.Scrollbar(frame_visor)
        self.scroll.pack(side="right", fill="y")

        self.visor = tk.Text(
            frame_visor,
            font=("Arial", 12),
            bg="white",
            fg="black",
            padx=15,
            pady=15,
            spacing1=5,   
            spacing2=2,   
            spacing3=5,   
            yscrollcommand=self.scroll.set
        )
        self.visor.pack(side="left", fill="both", expand=True)
        self.scroll.config(command=self.visor.yview)

    def analisar_entrada(self, texto):
        texto = texto.replace(',', ' ').strip()
        return [float(i) for i in texto.split()]

    def executar(self):
        try:
            nomeX = self.nome_indep.get().strip() or "X"
            nomeY = self.nome_dep.get().strip() or "Y"

            indep = self.analisar_entrada(self.ent_indep.get())
            dep = self.analisar_entrada(self.ent_dep.get())

            if len(indep) != len(dep) or len(indep) == 0:
                raise ValueError("Inconsistência na quantidade de dados entre X e Y.")

            n = methods.getNumDuplas(indep)
            
            mediaX = methods.calcularMediaAritmetica(indep, n)
            mediaY = methods.calcularMediaAritmetica(dep, n)
            mediaXY = methods.calcularMediaDoProduto(indep, dep, n)
            
            cov = methods.calcularCovariancia(mediaX, mediaY, mediaXY)
            
            mediaQuadX = methods.calcularMediaDosQuadrados(indep, n)
            mediaQuadY = methods.calcularMediaDosQuadrados(dep, n)
            
            desvioX = methods.calcularDesvioPadrao(mediaQuadX, mediaX)
            desvioY = methods.calcularDesvioPadrao(mediaQuadY, mediaY)
            
            r = methods.calcularCoeficienteDePearson(cov, desvioX, desvioY)
            r2 = methods.calcularCoeficienteDeDeterminacao(r)

            somaX, somaY, somaXY, somaX2, somaY2 = methods.calcularSomas(indep, dep, n)
            a, b = methods.calcularRetaRegressao(indep, dep, n)

            r2_pct = r2 * 100

            rel = f"RELATÓRIO DE REGRESSÃO LINEAR\n\n"

            rel += f"n: {n}\n"

            rel += f"Σ{nomeX} [soma de {nomeX}]: {somaX:.4f}\n"
            rel += f"Σ{nomeY} [soma de {nomeY}]: {somaY:.4f}\n"
            rel += f"Σ{nomeX}{nomeY} [soma de {nomeX}x{nomeY}]: {somaXY:.4f}\n"
            rel += f"Σ{nomeX}² [soma de {nomeX}²]: {somaX2:.4f}\n"
            rel += f"Σ{nomeY}² [soma de {nomeY}²]: {somaY2:.4f}\n\n"

            rel += f"σ({nomeX}) [desvio padrão de {nomeX}]: {desvioX:.8f}\n"
            rel += f"σ({nomeY}) [desvio padrão de {nomeY}]: {desvioY:.8f}\n\n"

            rel += f"μ({nomeX}) [média de {nomeX}]: {mediaX:.4f}\n"
            rel += f"μ({nomeY}) [média de {nomeY}]: {mediaY:.4f}\n"
            rel += f"μ({nomeX}{nomeY}) [média de {nomeX}x{nomeY}]: {mediaXY:.4f}\n\n"

            rel += f"r [coeficiente de Pearson]: {r:.8f}\n"
            rel += f"r² [coeficiente de determinação]: {r2_pct:.2f}%\n\n"

            rel += f"a: {a:.6f}\n"
            rel += f"b: {b:.6f}\n"
            rel += f"Equação: {nomeY} = {a:.6f} + {b:.6f}{nomeX}\n"

            self.visor.delete(1.0, tk.END)
            self.visor.insert(tk.END, rel)

            plt.figure(num="Diagrama de Dispersão")
            plt.scatter(indep, dep, color='blue', label='Dados Observados')
            
            x_line = [min(indep), max(indep)]
            y_line = [a + b * val for val in x_line]
            plt.plot(x_line, y_line, color='red', label=f'y = {a:.2f} + {b:.2f}x (R² = {r2:.4f})')
            
            plt.title('Regressão Linear')
            plt.xlabel(f'{nomeX}  (X)')
            plt.ylabel(f'{nomeY}  (Y)')
            plt.legend()
            plt.grid(True, linestyle='--', alpha=0.6)
            plt.show()

        except Exception as e:
            messagebox.showerror("Erro", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    AppRegressaoLinear(root)
    root.mainloop()