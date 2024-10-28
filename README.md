# RMCS 2303 Python Driver


### NOTE :
This a very quick and dirty port of the official Arduino implementation of the library. This is not guaranteed to work. Use the code at your own risk.

The official Arduino library can be found at : [RMCS-2303 Arduino Library](https://robokits.download/downloads/RMCS2303drive_V2.zip)

The official datasheet for the driver can be found at : [RMCS-2303 Manual](https://robokits.co.in/downloads/RMCS-2303%20updated%20datasheet.pdf)

<br />

## Getting Started :


### 1. Install dependencies :

1. Clone the repository and `cd` into it : `git clone https://github.com/verhambot/rmcs2303-python-driver.git && cd rmcs2303-python-driver`
2. Create a virtual environment using your preferred method : `python -m venv .venv && source .venv/bin/activate`
3. Install the dependencies : `pip install pyserial minimalmodbus`


### 2. Running `example.py` :

1. Replace all instances of `<REPLACE>` in the both `motor.py` and `example.py` with the appropriate values.
2. Test if everything works by running `example.py` : `python example.py`
