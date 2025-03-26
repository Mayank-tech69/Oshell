Here's your updated `README.md`, incorporating both the C++ and Python versions of O-Shell:  

---

# 🖥️ O-Shell - Custom Command Line Shell  

<p align="center">
  <a href="https://github.com/Mayank-tech69/Oshell"><img src="https://img.shields.io/badge/GitHub-Repo-blue?style=flat&logo=github" alt="GitHub Repo"></a>
</p>

O-Shell is a **custom shell** written in **C++ and Python**, providing Linux-like commands for both **Windows & Linux** with improved performance and flexibility.  

---

## 📌 Table of Contents  
- [🚀 Installation](#installation)  
- [⚙️ Usage](#usage)  
- [📌 Features](#features)  
- [📖 Commands](Commands.md)  
- [📜 License](#license)  

---

## 🚀 Installation  

### 🔹 C++ Version  

#### For Linux:  
1. Clone this repository:  

   ```sh
   git clone https://github.com/Mayank-tech69/Oshell.git
   ```  

2. Navigate to the project directory:  

   ```sh
   cd Oshell
   ```  

3. Compile the source code:  

   ```sh
   g++ -o oshell oshell.cpp -std=c++17
   ```  

4. Run the shell:  

   ```sh
   ./oshell
   ```  

#### For Windows:  
1. Clone this repository:  

   ```sh
   git clone https://github.com/Mayank-tech69/Oshell.git
   ```  

2. Navigate to the project directory:  

   ```sh
   cd Oshell
   ```  

3. Compile the source code using MinGW (or any C++ compiler that supports C++17):  

   ```sh
   g++ -o oshell.exe oshell.cpp -std=c++17
   ```  

4. Run the shell:  

   ```sh
   oshell.exe
   ```  

---

### 🔹 Python Version  

#### Prerequisites:  
Ensure you have Python 3 installed.  

#### Installation:  

1. Clone the repository:  

   ```sh
   git clone https://github.com/Mayank-tech69/Oshell.git
   ```  

2. Navigate to the project directory:  

   ```sh
   cd Oshell
   ```  

3. Run the Python shell:  

   ```sh
   python oshell.py
   ```  

---

## Alternative Method(RECOMMENDED)

Just download the latest released version from the repository and use it.

## ⚙️ Usage  

- Run **O-Shell** using either the C++ or Python version and start entering commands.  
- Example:  

  ```sh
  ls
  ```  

---

## 📌 Features  

### ✅ **C++ Shell Features:**  
- **Cross-Platform Support** - Works on **Windows & Linux**  
- **Custom `ls` command** for listing files  
- **File Operations** - Create, delete, copy, write, append, and rename files  
- **Directory Operations** - Create, remove, and navigate directories  
- **Built-in Commands** - `clear`, `exit`, `speak`, `help`, and more  
- **Command History Support**  

### ✅ **Python Shell Features:**  
- **Cross-Platform Compatibility**  
- **Similar Commands as C++ Shell**  
- **Extensible & Easy to Modify**  
- **Uses Python's `os` and `shutil` modules for efficient file handling**  

---

## 📜 License  

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.  

---
---