# Analiza Stochastică a Strategiilor de Evadare în Sisteme de Urmărire-Intercepție pe Domeniu Circular
## Descrierea Scenariului
Sistemul de studiu este reprezentat de un domeniu circular de rază $R$, în cadrul căruia interacționează două persoane, **A** și **B**, ambele deplasându-se cu viteze constante. Problema urmărește dinamica dintre un agent care încearcă să părăsească un perimetru și un interceptor care restricționează această ieșire.



---

## Definirea Agenților

### **Persoana A**
* **Poziția inițială:** Centrul cercului (originea sistemului).
* **Libertate de mișcare:** Se poate deplasa în orice direcție în interiorul discului (planul bidimensional).
* **Obiectiv:** Să atingă orice punct de pe circumferința cercului pentru a ieși din domeniu fără a fi interceptată de Persoana B.

### **Persoana B**
* **Poziția inițială:** Orice punct situat pe lungimea cercului (frontieră).
* **Libertate de mișcare:** Este restricționată exclusiv la deplasarea pe circumferința discului (perimetru).
* **Obiectiv:** Să ajungă în punctul de ieșire ales de Persoana A înaintea acesteia sau exact în același moment, pentru a realiza intercepția.

## **Exemplu vizual**

<img src="https://github.com/user-attachments/assets/b096bbd9-aa53-41f0-8978-b7782dfbcac1" width="50%">

## Strategia Optimă

Strategia optimă a persoanei **A** pentru a maximiza șansele de evadare constă în două etape distincte:

1. **Faza de Poziționare:** Persoana **A** se deplaseaza în cercuri concentrice în apropierea centrului cercului, exploatând faptul că la o rază mică posedă o viteză unghiulară superioară persoanei **B** ($\omega_A > \omega_B$). Scopul este atingerea unei poziții **diametral opuse** față de **B**.
2. **Faza de Sprint:** Odată ce atinge raza critică $r = R/k$, **A** abandonează mișcarea circulară și pornește într-un sprint liniar spre cea mai apropiată margine.

## Ce vom simula?
Din punct de vedere teoretic, dacă raportul vitezelor $k = v_B / v_A$ este mai mic decât pragul critic $\pi + 1$, Persoana A poate evada garantat, presupunând o execuție perfectă a strategiei optime. Simularea  Monte Carlo va investiga robustețea acestei teorii în condiții de incertitudine, cand $k = v_B / v_A$ se afla in vecinatatea lui $\pi + 1$.

Pentru a transforma modelul geometric ideal într-o simulare probabilistică realistă, am introdus variabilitate stocastică asupra a trei parametri cheie, folosind distribuții normale $\mathcal{N}(\mu, \sigma^2)$:

* **Poziția de start a sprintului ($r$):** Modelează eroarea umană în estimarea distanței critice față de centru ($R/k$) înainte de a începe sprintul.
* **Unghiul de sprint ($\alpha$):** Reprezintă dificultatea Persoanei A de a menține o traiectorie perfect dreaptă către circumferinta.
* **Timpul de reacție ($\tau$):** Simulează latența Persoanei B în perceperea atacului și schimbarea direcției de alergare pe circumferință.

Am ales să variem acești parametri, menținând vitezele constante, pentru a observa cum incertitudinea umană afectează rata de succes a evadării în vecinătatea pragului critic $k \approx 4.14$. Această abordare permite aplicarea riguroasă a **Inegalității Hoeffding** pentru analiza erorii de eșantionare.
