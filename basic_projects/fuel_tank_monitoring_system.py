# Fuel level monitoring system program

while True:
    try:
        fuel_level = int(input("Enter fuel level in %: "))

        if fuel_level == 0:
            print("No fuel! Car stopped")

            break
        elif fuel_level < 10:
            print("Low fuel, please refill")

        else:
            print(f"Fuel level is {fuel_level}%. You are good to go!" )

    except ValueError:
        print("Please enter a valid number.")