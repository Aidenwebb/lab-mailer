import smtpd
import asyncore
import threading

class CustomSMTPServer(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        print('Receiving message from:', peer)
        print('Message addressed from:', mailfrom)
        print('Message addressed to:', rcpttos)
        print('Message length:', len(data))
        return

def run_smtp_server():
    server = CustomSMTPServer(('0.0.0.0', 1025), None)
    asyncore.loop()

if __name__ == '__main__':
    thread = threading.Thread(target=run_smtp_server)
    thread.start()
