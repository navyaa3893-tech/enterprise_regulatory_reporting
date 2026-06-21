import socket

def is_reachable(port):
    try:
        with socket.create_connection(("localhost", port), timeout=3):
            return True
    except OSError:
        return False

services = {
    "redis": 6379,
    "postgres": 5432,
    "cassandra": 9042,
    "rabbitmq": 5672,
    "kafka": 9092,
    "configdb": 5433
}

def test_all_services_reachable():
    for name, port in services.items():
        assert is_reachable(port), f"{name} (port {port} is not reachable)"