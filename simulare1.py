import numpy as np
import matplotlib.pyplot as plt
import time

K_RES = 200           
SIGMA_RES = 120        
N_SIM_PER_CELL = 1000  

MAX_ERR_THETA = 10 * (np.pi / 180)
MAX_ERR_DIST = 0.01
LATENCY_B = 0.004

def calculeaza_probabilitati_limitat(k_min, k_max, sigma_min, sigma_max):
    k_vals = np.linspace(k_min, k_max, K_RES)
    sigma_vals = np.linspace(sigma_min, sigma_max, SIGMA_RES)
    
    K_GRID, SIGMA_GRID = np.meshgrid(k_vals, sigma_vals)
    Z = np.zeros_like(K_GRID)

    for i in range(SIGMA_RES):
        for j in range(K_RES):
            k = K_GRID[i, j]
            sigma = SIGMA_GRID[i, j]
            va = 1.0
            vb = k * va
            rc_real = 1 / k
            
        
            err_r = np.random.normal(0, MAX_ERR_DIST * sigma, N_SIM_PER_CELL)
            rc_perc = np.clip(rc_real + err_r, 0.01, 0.99)
            
            err_theta = np.random.normal(0, MAX_ERR_THETA * sigma, N_SIM_PER_CELL)
            
            unghi_start_real = np.where(rc_perc <= rc_real, 
                                        np.pi, 
                                        np.pi * (rc_real / rc_perc))
            
            t_sprint_a = (1.0 - rc_perc) / va
            t_util_b = np.maximum(0, t_sprint_a - LATENCY_B)
            
            capacitate_b_necesara = unghi_start_real - np.abs(err_theta)
            capacitate_b_reala = vb * t_util_b
            
            succese = np.sum(capacitate_b_reala < capacitate_b_necesara)
            Z[i, j] = (succese / N_SIM_PER_CELL) * 100

    return k_vals, sigma_vals, Z

k_vals, sigma_vals, Z = calculeaza_probabilitati_limitat(3.5, 4.8, 0.0, 1.0)

plt.figure(figsize=(12, 8))
heatmap = plt.pcolormesh(k_vals, sigma_vals, Z, shading='auto', cmap='RdYlGn')

cbar = plt.colorbar(heatmap)

plt.axvline(x=np.pi + 1, color='white', linestyle='--', label=r'Limita ideală $k \approx 4.14$')

plt.title(f"Eroare Unghi Max {MAX_ERR_THETA}\n Dist Max {MAX_ERR_DIST}\nLatență B = {LATENCY_B}s", fontsize=14)
plt.xlabel(r"Raport Viteze $k = v_B / v_A$", fontsize=12)
plt.ylabel(r"Intensitate Zgomot (0 = Ideal, 1 = Maxim)", fontsize=12)
plt.legend()

plt.show()
