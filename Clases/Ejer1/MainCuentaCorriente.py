from CuentaCorriente import *

def main():
    cuenta = CuentaCorriente("52077975H", 2001)
    cuenta1 = CuentaCorriente("5207775H", 2000)
    (cuenta == cuenta1)
    print(cuenta < cuenta1)

if __name__ == "__main__":
    main()