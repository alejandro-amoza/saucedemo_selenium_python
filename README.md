# 🧪 SauceDemo - Automatización de pruebas utilizando Selenium con Python

Este proyecto automatiza pruebas funcionales para el sitio de demostración SauceDemo usando Selenium WebDriver con Python, aplicando el patrón Page Object Model (POM) y generando reportes con Allure.

> URL del sitio: [https://www.saucedemo.com](https://www.saucedemo.com)

---

## 🔧 Tecnologías utilizadas

- Selenium WebDriver
- Python 3.10+
- pytest (parametrización, fixtures)
- Allure Framework para reportes
- webdriver-manager para manejo automático de drivers
- CSV para datos externos en pruebas de login

---

## 🎯 Objetivos

- Validar funcionalidad de login con múltiples usuarios desde CSV
- Validar correcto funcionamiento del carrito de compras
- Implementar pruebas modulares con POM para mantener código limpio y reutilizable
- Generar reportes con metadatos enriquecidos (features, stories, severities, tags) usando Allure

---

## 🧪 Casos de prueba automatizados

Casos automatizados:
- TC001 - Login con múltiples usuarios (incluye usuarios bloqueados)
- TC002 - Añadir producto al carrito y validación de su correcta presencia

---

## 📸 Ejemplos de reportes Allure

Aquí algunas capturas de pantalla de los reportes generados con Allure en este proyecto:

- [Overview](docs/screenshots_allure/Overview.png)
- [Test Case TC001](docs/screenshots_allure/TC001.png)
- [Test Case TC002](docs/screenshots_allure/TC002.png)

---

## 🚀 Cómo ejecutar
```bash
git clone https://github.com/alejandro-amoza/saucedemo_selenium_python.git
cd saucedemo_selenium_python
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```
---

## 🙌 Autor
Alejandro Amoza – QA Tester
- [LinkedIn](https://www.linkedin.com/in/alejandro-amoza)
- [Portfolio](https://alejandro-amoza.github.io/portfolio)




