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

            aliasX = nomeX[0]
            aliasY = nomeY[0]

            indep = self.analisar_entrada(self.ent_indep.get())
            dep = self.analisar_entrada(self.ent_dep.get())

            if len(indep) != len(dep) or len(indep) == 0:
                raise ValueError("Inconsistência na quantidade de dados entre X e Y.")

            n = methods.getNumDuplas(indep)
            
            media_variavel_x = methods.calcularMediaAritmetica(indep, n)
            media_variavel_y = methods.calcularMediaAritmetica(dep, n)
            media_produto_xy = methods.calcularMediaDoProduto(indep, dep, n)
            
            cov = methods.calcularCovariancia(media_variavel_x, media_variavel_y, media_produto_xy)
            
            media_quadrados_x = methods.calcularMediaDosQuadrados(indep, n)
            media_quadrados_y = methods.calcularMediaDosQuadrados(dep, n)
            
            desvio_padrao_x = methods.calcularDesvioPadrao(media_quadrados_x, media_variavel_x)
            desvio_padrao_y = methods.calcularDesvioPadrao(media_quadrados_y, media_variavel_y)
            
            coeficiente_pearson = methods.calcularCoeficienteDePearson(cov, desvio_padrao_x, desvio_padrao_y)
            coeficiente_determinacao = methods.calcularCoeficienteDeDeterminacao(coeficiente_pearson)

            soma_variavel_x, soma_variavel_y, soma_produto_xy, soma_quadrados_x, soma_quadrados_y = methods.calcularSomas(indep, dep, n)
            a, b = methods.calcularRetaRegressao(indep, dep, n)

            porcentagem_determinacao = coeficiente_determinacao * 100

            rel = f"Análise de Regressão Linear\n\n"

            rel += f"Quantidade de pares: {n}\n"

            rel += f"Somatório da {nomeX}(Σ{aliasX}): {soma_variavel_x:.4f}\n"
            rel += f"Somatório da {nomeY}(Σ{aliasY}): {soma_variavel_y:.4f}\n"
            rel += f"Somatório do produto(Σ({aliasX} . {aliasY})): {soma_produto_xy:.4f}\n"
            rel += f"Somatório das {nomeX} ao quadrado(Σ{aliasX}²): {soma_quadrados_x:.4f}\n"
            rel += f"Somatório das {nomeY} ao quadrado (Σ{aliasY}²): {soma_quadrados_y:.4f}\n\n"

            rel += f"Desvio padrão da {nomeX} (σ({aliasX})): {desvio_padrao_x:.8f}\n"
            rel += f"Desvio padrão da {nomeY}(σ({aliasY})): {desvio_padrao_y:.8f}\n\n"

            rel += f"Média de {nomeX}(μ({aliasX})): {media_variavel_x:.4f}\n"
            rel += f"Média de {nomeY} (μ({aliasY})): {media_variavel_y:.4f}\n"
            rel += f"Média do produto(μ({aliasX} . {aliasY})): {media_produto_xy:.4f}\n\n"

            rel += f"r [Coeficiente de Pearson]: {coeficiente_pearson:.8f}\n"
            rel += f"r² [Coeficiente de determinação]: {porcentagem_determinacao:.2f}%\n\n"

            rel += f"a: {a:.6f}\n"
            rel += f"b: {b:.6f}\n"
            if b > 0:
                rel += f"Equação: {nomeY} = {a:.6f} + {b:.6f} . {nomeX}\n"
            else:
                rel += f"Equação: {nomeY} = {a:.6f} - {b:.6f} . {nomeX}\n"

            self.visor.delete(1.0, tk.END)
            self.visor.insert(tk.END, rel)

            plt.figure(num="Diagrama de Dispersão")
            plt.scatter(indep, dep, color='blue', label='Dados Observados')
            
            x_line = [min(indep), max(indep)]
            y_line = [a + b * val for val in x_line]
            plt.plot(x_line, y_line, color='red', label=f'y = {a:.6f} + {b:.6f}x (R² = {porcentagem_determinacao:.2f}%)')
            
            plt.title('Regressão Linear')
            plt.xlabel(f'{nomeX}  (X)')
            plt.ylabel(f'{nomeY}  (Y)')
            plt.legend()
            plt.grid(True, linestyle='--', alpha=0.6)
            plt.show()

            valor_x = float(input(f"Digite um valor de {nomeX}: "))
            valor_estimado = a + b * valor_x
            print(f"{nomeY} estimado: {valor_estimado:.4f}")

        except Exception as e:
            messagebox.showerror("Erro", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    AppRegressaoLinear(root)
    root.mainloop()