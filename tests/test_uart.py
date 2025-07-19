import pytest
from src.hardware_sim.uart import UART

def test_transmit_adds_data_to_tx_buffer():
    uart = UART()
    uart.transmit("A")
    assert uart.tx_buffer[-1] == "A"

def test_receive_returns_data_from_rx_buffer():
    uart = UART()
    uart.inject_received_data("B")
    received = uart.receive()
    assert received == "B"

def test_receive_returns_none_if_buffer_empty():
    uart = UART()
    assert uart.receive() is None

def test_transmit_non_string_raises():
    uart = UART()
    with pytest.raises(ValueError):
        uart.transmit(123)
