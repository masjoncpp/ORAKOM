def convert_to_decimal(value, base):
    """Convert a number from a given base to decimal."""
    if base == 10:
        return float(value) if '.' in value else int(value)
    return int(value, base)

def convert_from_decimal(value, base):
    """Convert a decimal number to a given base."""
    if isinstance(value, str):  # Handle division by zero message
        return value
    
    if base == 16:
        if isinstance(value, float):
            return str(value)  # Hex can't properly represent floats
        return hex(int(value))[2:].upper()
    elif base == 8:
        if isinstance(value, float):
            return str(value)
        return oct(int(value))[2:]
    elif base == 2:
        if isinstance(value, float):
            return str(value)
        return bin(int(value))[2:]
    else:
        return str(value)

def perform_operation(num1, num2, operator):
    """Perform the specified operation on two numbers."""
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return 'Undefined (division by zero)'
        return num1 / num2  # Allow floating point division

def print_process(num1, num2, operator, base):
    """Print the process of the calculation."""
    decimal_num1 = convert_to_decimal(num1, base)
    decimal_num2 = convert_to_decimal(num2, base)
    
    print(f"{num1} \t\t\t {decimal_num1}")
    print(f"{num2} \t\t\t {decimal_num2}")
    print("---- " + operator + " \t\t ---------")
    
    return decimal_num1, decimal_num2

def main():
    while True:
        print("Pilih basis bilangan:")
        print("1. Biner")
        print("2. Oktal")
        print("3. Desimal")
        print("4. Heksadesimal")
        
        try:
            base_choice = int(input("Masukkan pilihan anda (1-4): "))
            if base_choice not in [1, 2, 3, 4]:
                print("Pilihan tidak valid. Silakan coba lagi.")
                continue
        except ValueError:
            print("Harap masukkan angka.")
            continue
        
        print("Masukkan operator proses:")
        print("1. +")
        print("2. -")
        print("3. *")
        print("4. /")
        
        try:
            operator_choice = int(input("Pilihan anda (1-4): "))
            if operator_choice not in [1, 2, 3, 4]:
                print("Pilihan tidak valid. Silakan coba lagi.")
                continue
        except ValueError:
            print("Harap masukkan angka.")
            continue
        
        operator = ['+', '-', '*', '/'][operator_choice - 1]
        
        num1 = input("Masukkan angka 1: ")
        num2 = input("Masukkan angka 2: ")
        
        try:
            # Print the process
            decimal_num1, decimal_num2 = print_process(num1, num2, operator, [2, 8, 10, 16][base_choice - 1])
            
            # Perform the operation
            result = perform_operation(decimal_num1, decimal_num2, operator)
            
            # Convert result back to the original base
            result_in_base = convert_from_decimal(result, [2, 8, 10, 16][base_choice - 1])
            
            print(f"Hasil: {result_in_base} \t\t {result}")
        except ValueError as e:
            print(f"Error: {e}. Pastikan input sesuai dengan basis yang dipilih.")
        
        # Ask if the user wants to continue
        continue_choice = input("Apakah Anda ingin melakukan operasi lain? (y/n): ")
        if continue_choice.lower() != 'y':
            break

if __name__ == "__main__":
    main()
