# Fungsi untuk mengubah suhu dari celcius ke kelvin
def convert_celcius_to_kelvin(temperature, command):
    if(command == "CK"):
        return temperature + 273.15
    elif(command == "KC"):
        return temperature - 273.15
    return ("Perintah tidak dikenali!")

# Sebuah fungsi untuk mengubah dari Celcius atau Kelvin ke Fahrenheit
def convert_to_fahrenheit(temperature, unit):
    if (unit == "K"):
        return (temperature - 273.15) * 9 / 5 + 32
    elif (unit == "C"):
        return temperature * 9 / 5 + 32
    return "Unit tidak dikenali!"

#Sebuah fungsi untuk mengubah dari Fahrenheit ke Celcius and Kelvin
def convert_from_fahrenheit(temperature):
    return {'K': (temperature - 32) * 5/9 + 273.15, 'C': (temperature-32) * 5/9}

# Fungsi Utama sebuah program
def main():
    print("===== Program sederhana untuk mengkonversi Suhu =====")
    convertFrom = -1
    
    # Fungsi while untuk memilih menu
    while(convertFrom < 1 or convertFrom > 3):
        print("Konversi Suhu, silahkan pilih : ")
        print("1. Celcius")
        print("2. Kelvin")
        print("3. Fahrenheit")
        convertFrom = int(input("Pilihan Anda: "))
        print("==============================")

    convertTo = 0
    while(convertTo < 1 or convertTo > 2):
        print("Konversi Suhu: ")
        if(convertFrom == 1):
            print("1. Kelvin")
            print("2. Fahrenheit")
        elif(convertFrom == 2):
            print("1. Celcius")
            print("2. Fahrenheit")
        elif(convertFrom == 3):
            print("1. Celcius")
            print("2. Kelvin")
        convertTo = int(input("Pilihan anda: "))
        print("==============================")

    # Masukkan temperature
    temperature = float(input("Temperature: "))
    
    if(convertFrom == 1 and convertTo == 1):
        print("Konversi Suhu dari Celcius ke Kelvin: ", convert_celcius_to_kelvin(temperature, "CK"))
    elif(convertFrom == 1 and convertTo == 2):
        print("Konversi Suhu dari Celcius ke Fahrenheit: ", convert_to_fahrenheit(temperature,"C"))
    elif(convertFrom == 2 and convertTo == 1):
        print("Konversi dari Kelvin ke Celcius: ", convert_celcius_to_kelvin(temperature,"KC"))
    elif(convertFrom == 2 and convertTo == 2):
        print("Konversi dari Kelvin ke Fahrenheit: ", convert_to_fahrenheit(temperature,"K"))
    elif(convertFrom == 3 and convertTo == 1):
        print("Konversi dari Fahrenheit ke Celcius: ", convert_from_fahrenheit(temperature)['C'])
    elif(convertFrom == 3 and convertTo == 2):
        print("Konversi dari Fahrenheit ke Kelvin: ", convert_from_fahrenheit(temperature)['K'])

if __name__ == "__main__":
    main()