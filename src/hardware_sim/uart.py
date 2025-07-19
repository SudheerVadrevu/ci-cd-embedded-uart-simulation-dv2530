class UART:
    def __init__(self):
        self.tx_buffer = []
        self.rx_buffer = []

    def transmit(self, data):
        if isinstance(data, str):
            self.tx_buffer.append(data)
            print(f"Transmitted: {data}")
        else:
            raise ValueError("UART can only transmit string data")

    def receive(self):
        if self.rx_buffer:
            data = self.rx_buffer.pop(0)
            print(f"Received: {data}")
            return data
        return None

    def inject_received_data(self, data):
        if isinstance(data, str):
            self.rx_buffer.append(data)
        else:
            raise ValueError("UART can only receive string data")
