# Analiza Strategiei de Evadare în Domeniu Circular
## Descrierea Scenariului
Sistemul de studiu este reprezentat de un domeniu circular de rază $R$, în cadrul căruia interacționează două persoane, **A** și **B**, ambele deplasându-se cu viteze constante. Problema urmărește dinamica dintre un agent care încearcă să părăsească un perimetru și un interceptor care restricționează această ieșire.



---

## Definirea Agenților

### **Persoana A (Evadatul)**
* **Poziția inițială:** Centrul cercului (originea sistemului).
* **Libertate de mișcare:** Se poate deplasa în orice direcție în interiorul discului (planul bidimensional).
* **Obiectiv:** Să atingă orice punct de pe circumferința cercului pentru a ieși din domeniu fără a fi interceptată de Persoana B.

### **Persoana B (Interceptorul)**
* **Poziția inițială:** Orice punct situat pe lungimea cercului (frontieră).
* **Libertate de mișcare:** Este restricționată exclusiv la deplasarea pe circumferința discului (perimetru).
* **Obiectiv:** Să ajungă în punctul de ieșire ales de Persoana A înaintea acesteia sau exact în același moment, pentru a realiza intercepția.

## **Exemplu vizual**

<img src="https://github.com/user-attachments/assets/b096bbd9-aa53-41f0-8978-b7782dfbcac1" width="50%">

