def ceaser_cipher(message,shift):

    result = ""
    final_letter = 90
    shift_range = 26
    #The final letter and shift range are used to make sure letters stay between the range of A-Z
    
    for char in message.upper():
        if char.isalpha():
            new_char= ord(char)
            encrpyted_char = new_char + shift
            if encrpyted_char > final_letter:
                encrpyted_char-= shift_range
            encrypted_text = chr(encrpyted_char)
            result +=  encrypted_text
        else: result = result + char
        
    print("Your Encrypted Code is = "+ result)
    
user_message = str(input("Enter Text For Encrption"))
shift_key = int(input("Enter Shift Key Size"))

ceaser_cipher(user_message,shift_key)
        
        
def ceaser_decipher(code, shifter):
    first_letter = 65
    shift_ranger2 = 26
    result2 = ""
    for char2 in code.upper():
        if char2.isalpha():
            new_code= ord(char2)
            decrpyted_char = new_code - shifter
            if decrpyted_char < first_letter:
                decrpyted_char+= shift_ranger2
            decrypted_text = chr(decrpyted_char)
            result2 +=  decrypted_text
        else: result2 = result2 + char2
        
    print("Your Decrypted Code is = "+ result2)
    
user_cipher = str(input("Enter Text for Decyrption"))
decrypt_key= int(input("Enter Decrption Key"))
    
ceaser_decipher(user_cipher,decrypt_key)

    
        
    
        
        
        