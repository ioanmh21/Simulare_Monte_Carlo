# Analiza Stochastică a Strategiilor de Evadare în Sisteme de Urmărire-Intercepție pe Domeniu Circular
## Descrierea Scenariului
Sistemul de studiu este reprezentat de un domeniu circular de rază $R$, în cadrul căruia interacționează două persoane, **A** și **B**, ambele deplasându-se cu viteze constante. Problema urmărește dinamica dintre un agent care încearcă să părăsească un perimetru și un interceptor care restricționează această ieșire.




---

## Definirea Agenților

### **Persoana A**
* **Poziția inițială:** Centrul cercului (originea sistemului).
* **Libertate de mișcare:** Se poate deplasa în orice direcție în interiorul discului (planul bidimensional).
* **Obiectiv:** Să atingă orice punct de pe circumferința cercului pentru a ieși din domeniu fără a fi interceptată de Persoana B (obiectivul trebuie atins intr-un timp finit).

### **Persoana B**
* **Poziția inițială:** Orice punct situat pe circumferința cercului .
* **Libertate de mișcare:** Este restricționată exclusiv la deplasarea pe circumferința discului (perimetru).
* **Obiectiv:** Să o opreasca pe Persoana A din parasirea cercului.

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

---

Obiectivul principal al acestui studiu este determinarea probabilității de succes a lui $A$ de a părăsi incinta circulară înainte de a fi interceptat de către  $B$, într-un regim de viteză definit de raportul $k$ și sub influența unui indice de zgomot $\sigma$.
De asemenea, dorim să vedem cum influențează fiecare dintre cei trei parametri rezultatul simulării.

### `simulare0.py`
Pentru un $k$ (raportul vitezelor) si un $\sigma$ (factorul de zgomot) date de la tastatura, calculeaza probabilitatea ca A
sa atinga circumferinta fara sa fie prins de B. In plus, afiseaza pe cerc si zona prin care A paraseste cercul in cazurile in care acesta evadeaza.


Pentru a determina robustețea simulării, folosim **Inegalitatea lui Hoeffding**. Deoarece variabilele noastre $X_i$ sunt de tip Bernoulli (0 sau 1), eroarea dintre probabilitatea estimată $\hat{P}$ și cea reală $P$ este limitată de:

$$P(|\hat{P} - P| \geq \epsilon) \leq 2e^{-2N\epsilon^2}$$


Dacă dorim o marjă de eroare $\epsilon = 0.01$ (1%) cu un nivel de încredere de 95% ($\delta = 0.05$):

$$0.05 = 2e^{-2N(0.01)^2} \implies \ln(0.025) = -0.0002N \implies N \approx 18,444$$

Codul nostru utilizează $N = 25,000$ în `simulare0.py`, ceea ce garantează o precizie superioară pragului de 1%.



---

<img width="500" alt="Screenshot 2026-01-10 211125" src="https://github.com/user-attachments/assets/3abb1da6-84d5-4f7d-89a9-3050cc1e49df" />

### `simulare1.py`
Acest script genereaza un heatmap pentru probabilitatea de evadare la orice raport $k$ si la orice factor $\sigma$ (ambii parametri fiind din 2 intervale de lungime finita).

---

### Fara zgomot vs zgomot

<p align="center">
  <img src="https://github.com/user-attachments/assets/fac25ac3-c351-4886-a17b-958f48e529d4" width="48%" height=300/>
  <img src="https://github.com/user-attachments/assets/33a35254-569b-4587-898b-4426db428f85" width="48%" height=300/>
</p>

---

### Efectul poziției de start a sprintului

<p align="center">
  <img src="https://github.com/user-attachments/assets/33a35254-569b-4587-898b-4426db428f85" width="48%" height=300/>
  <img src="https://github.com/user-attachments/assets/7bfbe21e-6873-4f5d-a096-956671cfce96" width="48%" height=300/>

</p>

Variația punctului de start al sprintului lărgește zona de incertitudine pe heatmap, estompând granița dintre succes și eșec. Această stocasticitate transformă limita teoretică fixă într-un gradient de probabilitate difuz. Rezultatul este un spectru unde succesul depinde de interacțiunea erorilor, nu doar de viteză.

---

### Efectul unghiului de sprint

<p align="center">
  <img src="https://github.com/user-attachments/assets/33a35254-569b-4587-898b-4426db428f85" width="48%" height=300/>
  <img src="https://github.com/user-attachments/assets/555ca0e0-a9df-41e3-95cf-ee729157b0f2" width="48%" height=300/>

</p>

Creșterea erorii unghiulare de sprint lărgește considerabil zona de incertitudine (galbenă) și o înclină pronunțat spre stânga pe harta de densitate. Acest fenomen demonstrează că imprecizia direcției de fugă reduce drastic șansele de succes chiar și pentru rapoarte de viteză $k$ teoretic sigure.

---

### Efectul timpului de reacție

<p align="center">
  <img src="https://github.com/user-attachments/assets/33a35254-569b-4587-898b-4426db428f85" width="48%" height=300/>


  <img src="https://github.com/user-attachments/assets/9df7e8c6-3560-4058-b65c-fa0eab9fbe3c" width="48%" height=300/>
</p>
Mărirea timpului de reacție al urmăritorului favorizează direct persoana A, oferindu-i acestuia o fereastră temporală critică pentru a câștiga distanță în faza inițială a sprintului. Vizual, acest avantaj se traduce prin deplasarea frontierei de succes spre dreapta, depășind vizibil limita teoretică ideală de $k \approx 4.14$. 

## 5. Instrucțiuni de Utilizare

### Cerințe sistem
* **Python 3.x**
* **Biblioteci**: `numpy`, `matplotlib`

### Rulare

#### 1. Simulare Punctuală:

```bash
python3 simulare0.py
```
* Introduceți `k` (ex: 4.1) și `sigma` (ex: 0.5).
* Rezultat: Procentajul de succes și distribuția spațială a evadărilor.

#### 2. Generare Analiză Globală:

```bash
python3 simulare1.py
```
* Rezultat: Heatmap-ul care compară raportul de viteze vs. intensitatea zgomotului.







