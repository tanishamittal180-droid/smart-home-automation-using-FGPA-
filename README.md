# 🏠 Smart Home Automation Controller using Icarus Verilog + AI Dashboard

## Project Overview

This project is a complete virtual Smart Home Automation System developed using Verilog and Python without requiring FPGA hardware. The system simulates smart home appliances, security systems, energy-saving modes, and AI-powered analytics.

The project integrates:

- Verilog design modules
- Icarus Verilog simulation
- GTKWave waveform visualization
- Streamlit real-time dashboard
- Virtual sensor generation
- SQLite database storage
- AI energy prediction
- Real-time monitoring system

---

## Features

### Hardware Logic Simulation

✔ Smart Home Controller  
✔ PWM-based light brightness control  
✔ PWM-based fan speed control  
✔ FSM (Finite State Machine) architecture  
✔ UART communication simulation  
✔ Security mode  
✔ Energy-saving mode  
✔ Motion sensor simulation  
✔ Temperature sensor simulation  
✔ Door sensor simulation  

---

### Software Features

✔ Real-time dashboard  
✔ Login authentication  
✔ Live device status monitoring  
✔ Fan animation  
✔ Voice command simulation  
✔ Virtual room layout  
✔ AI assistant panel  
✔ Power consumption analytics  
✔ Database integration  
✔ Energy prediction system  
✔ Activity logs  

---

## Project Architecture

```text
Virtual Sensors
        ↓
Verilog Smart Home Controller
        ↓
PWM + FSM + UART
        ↓
Icarus Verilog Simulation
        ↓
Waveform (.vcd)
        ↓
GTKWave
        ↓
CSV Logs
        ↓
SQLite Database
        ↓
AI Prediction Model
        ↓
Real-Time Streamlit Dashboard
```

---

## Project Folder Structure

```text
Smart-Home-Automation-FPGA/

├── rtl/
│   ├── pwm.v
│   ├── uart_controller.v
│   ├── sensor_generator.v
│   ├── smart_home_controller.v
│
├── tb/
│   ├── smart_home_tb.v
│
├── dashboard/
│   ├── dashboard.py
│
├── ai/
│   ├── energy_predictor.py
│
├── database/
│   ├── database.py
│
├── simulation/
│   ├── status.csv
│   ├── smart_home.db
│   ├── live_generator.py
│   ├── run.bat
│
├── README.md
```

---

## Software Requirements

### Install Icarus Verilog

Windows:

Download and install:

Icarus Verilog:
https://bleyer.org/icarus/

GTKWave:
https://gtkwave.sourceforge.net/

---

### Install Python Libraries

Open terminal and run:

```bash
pip install streamlit
pip install pandas
pip install plotly
pip install streamlit-autorefresh
pip install scikit-learn
```

Or:

```bash
pip install streamlit pandas plotly streamlit-autorefresh scikit-learn
```

---

## Running Verilog Simulation

Compile:

```bash
iverilog -o smarthome ^
tb/smart_home_tb.v ^
rtl/pwm.v ^
rtl/uart_controller.v ^
rtl/sensor_generator.v ^
rtl/smart_home_controller.v
```

Run simulation:

```bash
vvp smarthome
```

Open GTKWave:

```bash
gtkwave smart_home.vcd
```

---

## Signals to Add in GTKWave

```text
clk
motion_sensor
light_sensor
temp_high
door_open

light_pwm
fan_pwm

ac
alarm
energy_save
```

---

## Running Real-Time Simulation

Open Terminal 1:

```bash
python simulation/live_generator.py
```

Open Terminal 2:

```bash
streamlit run dashboard/dashboard.py
```

Login Credentials:

```text
Username: admin
Password: 1234
```

---

## Running Database Module

```bash
python database/database.py
```

---

## Running AI Prediction Module

```bash
python ai/energy_predictor.py
```

---

## Expected Output

### Smart Home Controller

Motion detected:

```text
Light ON
```

Temperature high:

```text
Fan ON
AC ON
```

Door open:

```text
Alarm ON
```

No activity:

```text
Energy Saving Mode ON
```

---

## Dashboard Features

- Real-time updates
- Device monitoring
- Power graphs
- Security status
- Voice simulation
- AI assistant
- Activity logs
- Room visualization

---

## Future Improvements

- MQTT communication simulation
- Face recognition door unlock
- Smart scheduling
- PDF report generation
- Voice assistant integration
- AI anomaly detection
- Mobile app interface
- Cloud integration

---
## Screenshots 
<img width="1366" height="768" alt="Screenshot 2026-06-22 121209" src="https://github.com/user-attachments/assets/51ca775a-9ad0-4d97-82bf-29bdfc3f4941" />
<img width="1366" height="768" alt="Screenshot 2026-06-22 121223" src="https://github.com/user-attachments/assets/50816729-22f3-40eb-b019-b08dcb1b6f83" />
<img width="1366" height="768" alt="Screenshot 2026-06-22 121240" src="https://github.com/user-attachments/assets/dc885f5c-efd4-4c3d-92b4-f93f9239af90" />
<img width="1366" height="768" alt="Screenshot 2026-06-22 121249" src="https://github.com/user-attachments/assets/65ec6604-f04d-4bd8-85dc-f4c298ab5a7a" />

## Applications

- Smart Home Automation
- IoT System Simulation
- FPGA Learning
- VLSI Projects
- Embedded Systems
- AI-based Monitoring Systems

---

## Technologies Used

Verilog HDL  
Icarus Verilog  
GTKWave  
Python  
Streamlit  
SQLite  
Pandas  
Scikit-Learn  

---

## Author

Tanisha Mittal

---

## License

This project is open-source and can be used for educational purposes.
