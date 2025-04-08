# 🏠 Smart Home Monitoring and Control System

## 🔍 Overview

This project was developed as part of the course **CE1113 — Embedded Systems** at the Costa Rica Institute of Technology.

The goal of the project is to design and implement a custom embedded system for monitoring and controlling a smart home model via a web server.

## 📊 Features

- 🔦 **Light Control:**
  - Turn on/off individual lights.
  - Simultaneously control multiple lights.
  - At least 5 lights representing different rooms (2 bedrooms, living room, bath room, kitchen).

- 🚪 **Door Monitoring:**
  - Monitor the status (open/closed) of 4 doors using physical push buttons or switches.

- 📷 **Camera Integration:**
  - Take and display pictures of the house garden remotely through the web application.

- 🔹 **Custom Dynamic Library:**
  - A dynamic library is developed for controlling and acquiring all signals.

- 🌐 **Web Server and Web Application:**
  - Embedded local web server with login authentication.
  - Web page with a graphical representation of the house.
  - Full user control over lights, doors, and camera from the application.

- 🚀 **Autonomous Startup:**
  - The server application starts automatically after the operating system boots.

- ⚙️ **Cross-Development:**
  - Project image and packages are built using the **Yocto Project**.

## 🛠️ Platforms

- 🚀 **Development Board:** Raspberry Pi 4 with a development kit.
- 🔧 **Cross-Compilation Toolchain:** Custom SDK.
- 💻 **Linux Image:** Built using the **Yocto Project**.
- 🏠 **Physical Model:** A scaled smart house model for demonstration purposes.

---

> 📚 Developed for the course **CE1113 — Embedded Systems** | Costa Rica Institute of Technology
