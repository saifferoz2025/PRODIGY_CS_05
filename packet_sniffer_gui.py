import tkinter as tk
from scapy.all import sniff
import threading

class PacketSnifferGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Packet Analyzer (Educational Use)")
        self.root.geometry("600x400")
        self.root.config(bg="#1e1e2e")

        self.label = tk.Label(root, text="Packet Sniffer", font=("Arial", 16, "bold"), fg="white", bg="#1e1e2e")
        self.label.pack(pady=10)

        self.text_area = tk.Text(root, height=15, width=70, wrap="word", state="disabled", bg="black", fg="lime")
        self.text_area.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Capture", command=self.start_sniffer, bg="#4CAF50", fg="white")
        self.start_button.pack(side="left", padx=10, pady=10)

        self.stop_button = tk.Button(root, text="Stop Capture", command=self.stop_sniffer, bg="#f44336", fg="white")
        self.stop_button.pack(side="right", padx=10, pady=10)

        self.sniffing = False

    def packet_callback(self, packet):
        if packet.haslayer("IP"):
            ip_layer = packet["IP"]
            msg = f"{ip_layer.src} -> {ip_layer.dst} | Protocol: {ip_layer.proto}\n"
            self.text_area.config(state="normal")
            self.text_area.insert(tk.END, msg)
            self.text_area.see(tk.END)
            self.text_area.config(state="disabled")

    def start_sniffer(self):
        if not self.sniffing:
            self.sniffing = True
            self.thread = threading.Thread(target=self.run_sniffer, daemon=True)
            self.thread.start()

    def run_sniffer(self):
        sniff(prn=self.packet_callback, stop_filter=lambda _: not self.sniffing)

    def stop_sniffer(self):
        self.sniffing = False

if __name__ == "__main__":
    root = tk.Tk()
    app = PacketSnifferGUI(root)
    root.mainloop()