import asyncio
from aiosmtpd.controller import Controller

class CustomSMTPHandler:
    async def handle_DATA(self, server, session, envelope):
        print(f"Receiving message from: {envelope.mail_from}")
        print(f"Delivering message to: {envelope.rcpt_tos}")
        print(f"Message length: {len(envelope.content)}")
        
        # Custom processing logic goes here
        return '250 Message accepted for delivery'

if __name__ == '__main__':
    # Set the hostname and port for the SMTP server
    hostname = 'localhost'
    port = 1025

    # Create the SMTP controller
    handler = CustomSMTPHandler()
    controller = Controller(handler, hostname=hostname, port=port)

    # Start the SMTP server
    print(f"Starting SMTP server on {hostname}:{port}")
    try:
        controller.start()
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        print("SMTP server stopped.")
        controller.stop()
