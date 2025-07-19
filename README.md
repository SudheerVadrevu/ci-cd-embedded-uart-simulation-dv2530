# CI/CD Integration for Embedded UART Simulation

This project simulates a simple UART (Universal Asynchronous Receiver/Transmitter) interface in Python and demonstrates CI/CD integration using both Jenkins and GitHub Actions.

---

## 🔧 Features

- UART TX/RX simulation in Python
- Unit testing using Pytest
- Docker-based test execution
- CI/CD pipelines using:
  - ✅ GitHub Actions
  - ✅ Jenkins

---

## 📁 Project Structure

```
.
├── .github/workflows        # GitHub Actions CI
│   └── ci.yml
├── jenkins
│   └── Jenkinsfile          # Jenkins CI pipeline
├── src/hardware_sim
│   └── uart.py              # UART simulation logic
├── tests
│   └── test_uart.py         # Pytest test suite
├── requirements.txt
└── Dockerfile
```

---

## 🚀 How to Run

### Dockerized Test Execution

```bash
docker build -t uart-sim .
docker run uart-sim
```

---

## 🧪 Running Tests Locally

```bash
pip install -r requirements.txt
pytest tests/
```

---

## 👨‍💻 Author

Sudheer Vadrevu – Master's in Computer Science, BTH Sweden
