while True:
    message = input("Enter the message (or type 'exit' to quit): ")
    if message.lower() == 'exit':
        break

    shift = int(input("Enter the shift amount: "))
    shifted_message = ""

    for char in message:
        if char.isalpha():
            is_upper = char.isupper()

            shifted_char = chr((ord(char) - ord('A' if is_upper else 'a') + shift) % 26 + ord('A' if is_upper else 'a'))

            shifted_message += shifted_char
        else:
            shifted_message += char
    print("Shifted Message: " ,shifted_message)
