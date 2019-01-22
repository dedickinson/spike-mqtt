# Spike - MQTT

General MQTT investigations

## Server

Install in Ubuntu/Mint:

    sudo apt install mosquitto

To run the server in Docker:

    docker run -it -p 1883:1883 -p 9001:9001 -v mosquitto.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto

## Clients

### Python

Setup a Python virtualenv:

    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt



## References

* [MQTT Site](http://mqtt.org/)
* [Eclipse Mosquitto](https://mosquitto.org/)
* [Eclipse Paho MQTT Clients](https://www.eclipse.org/paho/)