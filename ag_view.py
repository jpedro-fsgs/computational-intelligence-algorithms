import matplotlib.pyplot as plt
import time
from maximizar_funcao import start_population, evaluation, decode, NUMERO_GERACOES

def plotar_em_tempo_real():
    """
    Executa o AG importado e plota a convergência da aptidão
    em tempo real.
    """
    
    best_fitness_history = []
    
    # Configuração da plotagem interativa
    plt.ion() # Ativa o modo interativo
    fig, ax = plt.subplots(figsize=(10, 6))

    print(f"Iniciando o Algoritmo Genético para {NUMERO_GERACOES} gerações...")
    
    start_time = time.time()

    best_individual = None
    for i, best_individual in enumerate(start_population()):
        
        fitness = evaluation(best_individual)
        best_fitness_history.append(fitness)
        
        # Atualiza o gráfico a cada 5 gerações (para performance)
        if (i + 1) % 5 == 0 or i == 0:
            ax.clear()
            ax.plot(best_fitness_history, color='blue')
            ax.set_title(f'Convergência do AG (Geração {i + 1})')
            ax.set_xlabel('Geração')
            ax.set_ylabel('Melhor Aptidão (Valor de F6)')
            ax.grid(True)
            
            # Adiciona um texto mostrando a melhor aptidão atual
            ax.text(0.02, 0.02, f'Aptidão: {fitness:.8f}', 
                    transform=ax.transAxes, 
                    fontsize=10, 
                    bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
            
            plt.pause(0.001) # Pausa para redesenhar o gráfico

    end_time = time.time()
    print(f"\nConcluído em {end_time - start_time:.2f} segundos.")

    # --- Exibe o resultado final ---
    final_best_chromosome = best_individual
    final_x, final_y = decode(final_best_chromosome)
    final_fitness = best_fitness_history[-1]

    with open("best_fitness_history.txt", "w") as f:
        f.write('\n'.join([str(i) for i in list(dict.fromkeys(best_fitness_history))]))
    
    print("\n--- Resultado Final ---")
    print(f"Melhor Cromossomo: {final_best_chromosome}")
    print(f"Melhor Aptidão (F6): {final_fitness:.8f}")
    print(f"Melhores Coordenadas: x={final_x:.8f}, y={final_y:.8f}")
    
    # Desativa o modo interativo e mostra o gráfico final
    plt.ioff()
    ax.set_title('Convergência Final do AG')
    plt.show()
    

if __name__ == "__main__":
    plotar_em_tempo_real()