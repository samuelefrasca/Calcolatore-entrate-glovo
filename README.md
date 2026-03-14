# 🛵 Calcolatore Entrate Glovo

Script Python per calcolare le entrate nette come rider Glovo, tenendo conto della **ritenuta d'acconto del 20%**, delle **mance** e dei **prelievi in contanti**.

---

## 📥 Download

> **Non vuoi installare Python?** Scarica direttamente l'eseguibile per Windows:
>
> 👉 [**Download .exe** (Windows)](https://github.com/samuelefrasca/Calcolatore-entrate-glovo/releases/latest)

---

## ▶️ Come funziona

Inserisci questi valori quando richiesto:

| Campo | Descrizione |
|---|---|
| Entrate complessive | Il totale lordo visibile sull'app Glovo |
| Mance | Il totale delle mance ricevute nel periodo |
| Prelievo quotidiano | Contanti ritirati giorno per giorno |
| Prelievo di fine periodo | Contanti ritirati a fine periodo |

Lo script calcolerà automaticamente:
- Entrate nette (tolto il 20% di ritenuta d'acconto)
- Totale con mance incluse
- Importo del bonifico atteso (entrate totali - contanti già ritirati)

---

## 🐍 Eseguire da codice sorgente

**Requisiti:** Python 3.7+

```bash
git clone https://github.com/samuelefrasca/Calcolatore-entrate-glovo.git
cd Calcolatore-entrate-glovo
python calcolatore_entrate_glovo.py
```

Nuovo a Python? → [Installa Python](https://www.python.org/downloads/)

---

## 📦 Creare l'exe (per sviluppatori)

```bash
pip install pyinstaller
pyinstaller --onefile calcolatore_entrate_glovo.py
```

L'eseguibile verrà generato nella cartella `dist/`.

---

## ✍️ Autore

**Samuele Frasca** — [@samuelefrasca](https://github.com/samuelefrasca)

> ⚠️ I calcoli sono stime. Fai sempre riferimento all'app Glovo per i dati ufficiali.
