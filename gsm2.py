import serial
import time
#royb
#+919496707123
# Configure the serial port
ser = serial.Serial(
    port='/dev/ttyAMA0',  # Change this if your SIM800L is on a different port
    baudrate=9600,
    timeout=1
)

if not ser.isOpen():
    ser.open()

# Phone number to call (replace with your number)
phone_number = "+919605980433"

def send_at_command(command, delay=1):
    if not ser.isOpen():
        ser.open()
    """Send AT command to the module and wait for response"""
    ser.write((command + '\r\n').encode())
    time.sleep(delay)
    response = ser.read(ser.in_waiting or 1).decode()
    return response

def make_call(number):
    if not ser.isOpen():
        ser.open()
    global phone_number
    number = phone_number
    """Make a call to the specified number"""
    print("Initializing SIM800L...")
    
    # Check if module is responding
    response = send_at_command("AT")
    if "OK" not in response:
        print("Module not responding. Check connections.")
        return False
    
    # Check SIM card status
    response = send_at_command("AT+CPIN?")
    if "READY" not in response:
        print("SIM card not ready.")
        return False
    
    # Set text mode (just in case)
    send_at_command("AT+CMGF=1")
    
    # Make the call
    print(f"Calling {number}...")
    response = send_at_command(f"ATD{number};", delay=5)
    
    if "OK" in response or "CONNECT" in response:
        print("Call connected!")
        return True
    else:
        print("Failed to make call. Response:", response)
        return False
def call():
    if not ser.isOpen():
        ser.open()
    try:
        # Open serial connection
        if not ser.isOpen():
            ser.open()
        
        # Make the call
        if make_call(phone_number):
            print("Call in progress...")
            # Let the call continue for 20 seconds (you can adjust this)
            time.sleep(20)
            
            # Hang up
            send_at_command("ATH")
            print("Call ended.")
        else:
            print("Failed to initiate call.")

    except Exception as e:
        print("Error:", str(e))

    finally:
        # Close the serial connection
        if ser.isOpen():
            ser.close()

def send_sms(msg):
    if not ser.isOpen():
        ser.open()
    global phone_number
    number = phone_number
    message = f"{msg} Detected!!"
    """Send an SMS to the specified number"""
    print(f"Sending SMS to {number}...")
    
    # Set SMS text mode
    send_at_command("AT+CMGF=1")
    time.sleep(1)
    
    # Send the command to initiate SMS sending
    ser.write((f'AT+CMGS="{number}"\r').encode())
    time.sleep(1)
    
    # Send the message text
    ser.write((message + "\x1A").encode())  # Ctrl+Z ends the message
    time.sleep(3)  # Wait for SMS to be sent
    
    response = ser.read(ser.in_waiting or 1).decode()
    print("SMS Response:", response)
    
    if "OK" in response or "+CMGS" in response:
        print("SMS sent successfully.")
        return True
    else:
        print("Failed to send SMS.")
        return False	

def alert(msg):
    if not ser.isOpen():
        ser.open()
    send_sms(msg)
    call()