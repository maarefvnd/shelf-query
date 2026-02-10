```
# Shelf Query (Qt + Python)

**Shelf Query** is a desktop application built with **Qt (C++)** and **Python** for fetching books from OpenLibrary.  
It saves the output to a CSV file and can display the data in a `tableView`.

---

## 🎯 Features

- Randomly fetches 50 books from OpenLibrary from the year 2000 onwards  
- CSV output with UTF-8 encoding, sorted by publication year  
- Randomized output on each run  
- Symbolic progress bar while Python script runs  
- Displays books in a `tableView`  
- Can be packaged as a portable release  

---

## 🗂️ Project Structure
```
shelf-query/

├── python-fetcher/

│ └── books.py # Python script

├── shelf-query.pro # Qt project file

├── mainwindow.h / .cpp # Main Qt source files

└── README.md
```
- When building Release, `shelf-query.exe` is generated.  
- The `python-fetcher` folder must be next to the exe for the Python script to run.

---

## ⚡ Running the Application

### 1️⃣ With Qt Creator (Debug)

- Open the project  
- Build → Build All  
- Run → the program launches  
- TableView will always start on page 0  
- Buttons:
  - **pushButton_2** → Run Python script + progress bar 50% → 100%  
  - **pushButton_3** → Display books from CSV in tableView  

---

### 2️⃣ With Qt Creator (Release / Portable)

- Switch **Build Configuration** → Release  
- Build All → exe is generated  
- Place the `python-fetcher` folder next to the exe  
- (Optional) Use `windeployqt` to include all required Qt DLLs:

```powershell
"C:\Qt\6.6.2\msvc2019_64\bin\windeployqt.exe" "path\to\shelf-query.exe"
```
Now you have a portable, standalone application
🐍 Python Requirements

Python 3.x must be installed (or use Python embeddable package for portable deployment)

Required Python packages: `requests`

```
pip install requests
```
CSV output path is relative to the exe:
```
QString filePath = QDir(QCoreApplication::applicationDirPath())
                   .filePath("python-fetcher/books.csv");
```
📦 Running the Python Script

pushButton_2 → runs books.py with the exe path as argument

Generates books.csv

Progress bar moves symbolically from 50% → 100%

📄 Displaying CSV in TableView

pushButton_3 → reads CSV and fills tableView

TableView always starts on page 0 when the program launches:
```
ui->stackedWidget->setCurrentIndex(0); // or ui->tableView->scrollTo(index)
```
🔧 Portable / Release Notes

Copy all Qt DLLs using windeployqt next to the exe

Copy python-fetcher and books.py next to the exe

For portable Python: use Python embeddable + requests in Lib/site-packages

The exe is standalone and does not require Qt installed on the target system

📌 Important Notes

CSV output is always different (random query, shuffled pages, random selection of 50 books)

TableView and progress bar provide simple, user-friendly UX

Always starts on page 0 at launch

⚡ References

Qt Documentation

OpenLibrary API

Python embeddable package
```

---

💡 Features of this README:

- Step-by-step instructions for Debug & Release  
- Python + Qt usage  
- Portable deployment explained  
- Progress bar and tableView behavior documented  
- File structure and relative paths clearly described  

---

If you want, I can make a **version with diagrams/screenshots of the tableView + project structure**, so it’s super ready for GitHub or presentation.  

Do you want me to do that?
```

