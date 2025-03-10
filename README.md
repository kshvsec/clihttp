# **clihttp**  
*A simple and efficient CLI tool for making HTTP/S requests.*  

`clihttp` is a command-line interface for interacting with HTTP/S APIs using Python. It provides an easy way to send requests, handle responses, and debug API calls—all from the terminal.  

## **✨ Features**
- Lightweight and easy to use  
- Supports `GET`, `POST`, `PUT`, `DELETE`, and more  
- Custom headers, JSON data, and query parameters  
- Easily installable via `pip`  
- Open-source and customizable  

---

## **📦 Installation**  

### **Install via PyPI**  
You can install `clihttp` directly from [PyPI](https://pypi.org/project/clihttp/):  
```bash
pip install clihttp
```

### **Build from Source**  
If you prefer to install from source, clone the repository and install manually:  
```bash
git clone https://github.com/kshvsec/clihttp.git
cd clihttp
pip install .
```

---

## **🚀 Usage**  

Once installed, you can use `clihttp` from your terminal. Here are some basic examples:  

### **Make a GET request**  
```bash
clihttp get https://api.example.com/data
```

### **Send a POST request with JSON data**  
```bash
clihttp post https://api.example.com/create -d '{"name": "Keshav", "role": "admin"}'
```

### **Pass custom headers**  
```bash
clihttp get https://api.example.com/auth -H "Authorization: Bearer YOUR_TOKEN"
```

### **Send query parameters**  
```bash
clihttp get https://api.example.com/search?q=python
```

### **View full response details**  
```bash
clihttp get https://api.example.com/status -v
```

---

## **🛠 Development & Contribution**  
Want to contribute? Fork the repository, make your changes, and submit a pull request!  

```bash
git clone https://github.com/kshvsec/clihttp.git
cd clihttp
```

---

## **📝 License**  
This project is licensed under a **custom restrictive license**—usage is allowed, but modification and redistribution are prohibited.  

---

## **📞 Support**  
For any issues or feature requests, open an issue on [GitHub](https://github.com/kshvsec/clihttp/issues).  