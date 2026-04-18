# SDN Traffic Monitoring and Statistics Collector

An SDN-based traffic monitoring system implemented using **Mininet**, **POX Controller**, and **OpenFlow** to collect real-time traffic statistics such as packet counts, byte counts, and flow information.

---

## 📌 Project Overview

Software Defined Networking (SDN) separates the control plane from the data plane and enables centralized network management.

In this project, a custom **POX Controller module** was developed to:

- Handle switch-controller communication
- Process `PacketIn` events
- Install OpenFlow flow rules
- Periodically request flow statistics
- Display packet and byte counts in real time

---

## 🎯 Objective

To build a controller module that collects and displays traffic statistics by:

- Retrieving flow statistics
- Monitoring packet counts
- Monitoring byte counts
- Performing periodic traffic monitoring
- Demonstrating controller-switch interaction

---

## 🛠️ Technologies Used

- Ubuntu Linux
- VirtualBox
- Python
- Mininet
- POX Controller
- OpenFlow Protocol

---

## 📂 Project Structure

```text
sdn-traffic-monitoring-mininet-pox/
│── custom_controller.py
│── README.md
│── assets/
│   ├── controller-started.png
│   ├── mininet-topology.png
│   ├── pingall-success.png
│   ├── packet-received-output.png
│   ├── flow-stats-output.png
│   ├── code-main-part1.png
│   └── code-main-part2.png
│── report/
│   └── SDN_Traffic_Monitoring_Report_Vankadara_Sri_Kruthi.docx
...
```

##⚙️ Setup and Execution

1️⃣ Start POX Controller
    cd ~/pox
    ./pox.py custom_controller
2️⃣ Start Mininet Topology
    sudo mn --topo single,3 --controller remote,ip=127.0.0.1,port=6633
3️⃣ Test Connectivity
    pingall

---

##🧠 Controller Logic

The custom controller performs the following tasks:
-Detects switch connection (ConnectionUp)
-Handles incoming packets (PacketIn)
-Floods packets for forwarding
-Installs flow rules for future packets
-Sends periodic flow statistics requests every 5 seconds
-Displays packet count and byte count

---

## 📸 Output Screenshots

## 📸 Output Screenshots

### Controller Started Successfully
![Controller](./assets/controller-started.png)

### Mininet Topology Created
![Topology](./assets/mininet-topology.png)

### Ping Test Successful
![Ping](./assets/pingall-success.png)

### Flow Statistics Output
![Stats](./assets/flow-stats-output.png)

### Source Code - Part 1
![Code1](./assets/code-main-part1.png)

### Source Code - Part 2
![Code2](./assets/code-main-part2.png)

---

##📊 Results

-POX controller started successfully
-OpenFlow switch connected successfully
-Mininet topology created with 3 hosts and 1 switch
-pingall result showed 0% packet loss
-Packet logs received continuously
-Flow statistics displayed correctly
-Packet and byte counts monitored successfully

---
##✅ Conclusion
This project successfully implemented a Traffic Monitoring and Statistics Collector using SDN concepts. Using Mininet and POX Controller, controller-switch interaction, packet forwarding, and traffic monitoring were demonstrated successfully.

##👩‍💻 Author
Vankadara Sri Kruthi

##📄 Report
Detailed report is available inside the report/ folder.

⭐ Star this repository if you found it useful.
