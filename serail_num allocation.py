try:
    with open("temp", "r") as f:
        serial_no = 1
        
        # Read the file line by line safely without crashing
        for line in f:
            name = line.strip()
            print(f"{serial_no} : {name}")
            serial_no += 1

except FileNotFoundError:
    print("File not found. Please make sure the file 'temp' exists.")
