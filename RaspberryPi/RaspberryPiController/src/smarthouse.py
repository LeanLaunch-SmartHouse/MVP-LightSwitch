__author__ = 'Jordan'

#import RPi.GPIO as GPIO
import time
import BaseHTTPServer

LED_PIN = 4         # board pin 7
BUTTON_PIN = 17     # board pin 9

HOST_NAME = 'localhost'
POST_NUMBER = 8080

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()

    def do_GET(self):
        """Respond to a GET request."""
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()

        self.wfile.write("<html><head><title>Hello</title></head><body>Hello Jordan</body></html>")


def setup_gpio():
    GPIO.setmode(GPIO.BCM)

    # LED output
    GPIO.setup(LED_PIN, GPIO.OUT)

    # Pushbutton input
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def turn_on_LED():
    pass
    GPIO.output(LED_PIN, 1)


def turn_off_LED():
    GPIO.output(LED_PIN, 0)


def main():
    try:
        print("Setting up HTTP server")
        server_class = BaseHTTPServer.HTTPServer
        httpd = server_class((HOST_NAME, POST_NUMBER), MyHandler)

        print("Setting up GPIO...")
#        setup_gpio()

        httpd.serve_forever()
            
    finally:
        if 'httpd' in locals():
            print("Closing down HTTP daemon")
            httpd.server_close()

        print("Cleaning up GPIO...")
#        GPIO.cleanup()
        

if __name__ == '__main__':
	main()
