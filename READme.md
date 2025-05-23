# 📖 Limpide Letture - WebApp con Velvet 2B in Locale

Limpide Letture è una webapp pensata per facilitare la comprensione dei testi in italiano, progettata per essere eseguita **in locale** sfruttando il modello linguistico **Velvet 2B di Almawave**, attraverso **Ollama** e un semplice proxy Python.

---

## 🚀 Funzionalità principali

* **Semplificazione del testo**: riformula in modo più semplice e accessibile
* **Spiegazione parole difficili**: evidenzia e spiega le parole non contenute nel vocabolario selezionato
* **Analisi dell'indice Gulpease**: individua frasi complesse e ne offre spiegazione
* **Spiegazione del testo evidenziato**: seleziona una parte di testo e ottieni chiarimenti
* **Chat linguistica (LucIA)**: chatbot dedicato per chiarimenti linguistici sul testo

---

## 🧰 Requisiti

* Python 3
* [Ollama](https://ollama.com/) installato e funzionante
* Modello `almawave/velvet:2b` disponibile in Ollama
* Browser moderno (Chrome, Edge, Firefox)
* File vocabolari (JSON): `fondamentale.json`, `altouso.json`, `altadisponibilita.json`, `basecompleto.json`

> 📚 **Nota:** Nella web app sono già forniti 4 vocabolari di De Mauro in formato JSON pronti per l'uso.

---

## 🛠️ Avvio

1. **Scarica tutti i file** nella stessa cartella:

   * `index.html` (la webapp)
   * `ollama_proxy.py` (proxy FastAPI per inoltro richieste)
   * i vocabolari JSON

2. **Avvia Ollama** e il modello Velvet:

```bash
ollama run almawave/velvet:2b
```

3. **Esegui il proxy Python**:

```bash
uvicorn ollama_proxy:app --port 8000
```

4. **Esegui il server per la webapp**:

```bash
python -m http.server 8080
```

5. **Apri il browser** su:

```
http://localhost:8080
```

---

## 🖱️ Interfaccia utente

* `📚 Seleziona vocabolario`: scegli tra 4 vocabolari De Mauro
* `✍️ Semplifica il Testo`: riformula il testo in forma semplice
* `🧩 Parole Difficili`: evidenzia e spiega parole non contenute nel vocabolario
* `🔴 Frasi complesse`: sottolinea le frasi difficili in base all'indice Gulpease
* `🟨 Spiega testo evidenziato`: seleziona e spiega una parte del testo
* `⚙️ Impostazioni`: personalizza i prompt
* `💬 Chat Linguistica`: assistente linguistico LucIA
* `📥 Esporta`: esporta in PDF (funzione in sviluppo)

---

## ⚙️ Prompt personalizzabili

Premi il tasto "⚙️ Impostazioni" per accedere a:

* Prompt semplificazione
* Prompt spiegazione parole/frasi
* Prompt chatbot

I valori modificati vengono salvati nel browser (localStorage).

---

## 🧩 Vocabolari compatibili

Ogni vocabolario è un file JSON contenente un array di parole. Le parole che **non sono nel vocabolario** vengono evidenziate e rese cliccabili per la spiegazione.

Esempio di file `fondamentale.json`:

```json
["casa", "libro", "mangiare", "vedere", "grande"]
```

---

## 📦 File avvio automatico

Il file `avvio.bat` è già fornito nella cartella del progetto. Se vuoi modificarlo o ricrearlo manualmente, ecco il contenuto:

```bat
@echo off
start cmd /k "ollama run velvet-2b"
start cmd /k "uvicorn ollama_proxy:app --port 8000 --reload"
start cmd /k "python -m http.server 8080"
start "" http://localhost:8080
```

---

## 📋 Licenza

Questo progetto è distribuito secondo i termini della **GNU General Public License v3.0 (GPL-3.0)**.

Puoi:

* Usare, studiare, modificare e ridistribuire il codice

Devi:

* Mantenere la stessa licenza in eventuali distribuzioni o derivazioni
* Citare gli autori originali

Per maggiori dettagli: [https://www.gnu.org/licenses/gpl-3.0.html](https://www.gnu.org/licenses/gpl-3.0.html)

---

## 🤝 Realizzato da

Fondazione ASPHI Onlus con supporto di tecnologie AI per l'inclusione e l'accessibilità.

---

Per supporto o suggerimenti: [https://www.asphi.it](https://www.asphi.it)
