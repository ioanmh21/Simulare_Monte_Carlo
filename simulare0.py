import numpy as np
import matplotlib.pyplot as plt

def simuleaza_scenariu_fix(k, sigma, n_simulari=25000):
    VA = 1.0
    VB = k * VA
    RC_IDEAL = 1 / k
    LATENCY_B = 0.004
    MAX_ERR_THETA = 15 * (np.pi / 180)
    MAX_ERR_DIST = 0.1

    err_r = np.random.normal(0, MAX_ERR_DIST * sigma, n_simulari)
    rc_perceput = np.clip(RC_IDEAL + err_r, 0.01, 0.95)
    
    err_theta = np.random.normal(0, MAX_ERR_THETA * sigma, n_simulari)

    unghi_plecare_b = np.where(rc_perceput <= RC_IDEAL, 
                               np.pi, 
                               np.pi * (RC_IDEAL / rc_perceput))

    t_spirala = (1/VB) * np.arcsin(np.minimum(rc_perceput * VB / VA, 1.0))
    t_sprint_a = (1.0 - rc_perceput) / VA
    t_util_b = np.maximum(0, t_sprint_a - LATENCY_B)

    dist_unghiulara_necesara = unghi_plecare_b - np.abs(err_theta)
    dist_unghiulara_reala_b = VB * t_util_b
    
    succese_mask = dist_unghiulara_reala_b < dist_unghiulara_necesara
    rata_succes = (np.sum(succese_mask) / n_simulari) * 100

    theta_exit = (VB * t_spirala + np.pi) % (2 * np.pi)
    raza_afisare = 1.02
    escape_x = raza_afisare * np.cos(theta_exit[succese_mask])
    escape_y = raza_afisare * np.sin(theta_exit[succese_mask])

    return rata_succes, escape_x, escape_y

try:
    k_input = float(input("Introduceți k: "))
    sigma_input = float(input("Introduceți sigma: "))
except ValueError:
    exit()

rata, x_evadare, y_evadare = simuleaza_scenariu_fix(k_input, sigma_input)

plt.figure(figsize=(10, 10))

theta_cerc = np.linspace(0, 2*np.pi, 500)
plt.plot(np.cos(theta_cerc), np.sin(theta_cerc), color='red', lw=3, label='Bariera', zorder=1)

plt.scatter(x_evadare, y_evadare, color='#00FF00', s=15, alpha=0.8, edgecolors='none', label=f'Evadări ({len(x_evadare)})', zorder=2)

plt.xlim(-1.3, 1.3)
plt.ylim(-1.3, 1.3)
plt.gca().set_aspect('equal')
plt.title(f"Probabilitate: {rata:.2f}% | k={k_input} | $sigma$={sigma_input}")
plt.legend()
plt.show()

