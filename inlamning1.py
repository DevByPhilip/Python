import machine
import time
import socket
import network
import json

class LEDControl:
    def __init__(self, pin_name):
        self.led = machine.Pin(pin_name, machine.Pin.OUT)
    
    def turn_on(self):
        self.led.value(1)
    
    def turn_off(self):
        self.led.value(0)
    
    def get_state(self):
        return 'On' if self.led.value() == 1 else 'Off'


class WiFiConnection:
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password
        self.wifi = network.WLAN(network.STA_IF)
    
    def connect(self):
        self.wifi.active(True)
        self.wifi.disconnect()
        self.wifi.connect(self.ssid, self.password)
        
        while not self.wifi.isconnected():
            print('Försöker ansluta till Wi-Fi...')
            time.sleep(1)
        
        print('Wi-Fi-anslutning lyckades!')
        print('IP-adress:', self.wifi.ifconfig()[0])
    
    def is_connected(self):
        return self.wifi.isconnected()


class WebServer:
    def __init__(self, led_control):
        self.led_control = led_control
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def start(self):
        self.server_socket.bind(('', 80))
        self.server_socket.listen(5)
        print("Webbservern startad, väntar på anslutningar...")
    
    def handle_requests(self):
        try:
            conn, addr = self.server_socket.accept()
            print(f"Ansluten från {addr}")
            
            req = conn.recv(1024).decode('utf-8')
            print("Begäran:", req)
            
            # Kontrollera vilken typ av req vi har
            if '/api/led' in req:
                self.handle_api_led(conn)
            else:
                self.handle_request(req, conn)

            conn.close()
        except Exception as e:
            print(f"Serverfel: {e}")
            conn.close()

    def handle_api_led(self, conn):
        """
        Hanterar API-anrop till /api/led och returnerar JSON-data med LED-status.
        """
        gpio_state = self.led_control.get_state()
        response = json.dumps({'status': gpio_state})  
        
        # Skicka HTTP-svar med JSON
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: application/json\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)

    def handle_request(self, request, conn):
        """
        Hanterar begäran till webbsidan och styr LED.
        """
        if '/?led=on' in request:
            print("LED PÅ")
            self.led_control.turn_on()
        elif '/?led=off' in request:
            print("LED AV")
            self.led_control.turn_off()

        response = self.generate_webpage()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)

    def generate_webpage(self):
        gpio_state = self.led_control.get_state()
        html = f"""
        <html>
            <head>
                <title>Pico W Web Server</title>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <style>
                    html{{font-family: Helvetica; text-align: center;}}
                    h1{{color: #0F3376; padding: 2vh;}}
                    p{{font-size: 1.5rem;}}
                    button{{background-color: #4286f4; border: none; color: white; padding: 16px 40px; font-size: 30px; cursor: pointer;}}
                </style>
            </head>
            <body>
                <h1>Pico W Web Server</h1>
                <p>GPIO state: <strong>{gpio_state}</strong></p>
                <p><a href="/?led=on"><button>ON</button></a></p>
                <p><a href="/?led=off"><button>OFF</button></a></p>
            </body>
        </html>
        """
        return html


# main
if __name__ == "__main__":
    ssid = '********************************'
    password = '******'

    # Skapa objekt
    led_control = LEDControl("LED")
    wifi = WiFiConnection(ssid, password)

    # Anslut till Wi-Fi
    wifi.connect()

    # Starta webbservern om Wi-Fi-anslutningen är framgångsrik
    if wifi.is_connected():
        webserver = WebServer(led_control)

        try:
            webserver.start()
            while True:
                webserver.handle_requests()
        except Exception as e:
            print("Exception -", e)
            # Eventuell städning vid fel
            pass

