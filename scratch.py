def main():
    print("Bitte geben sie die IDG Nummer ein: ")
    idg_str = input()
    text_str = "1234567"
    length_str = 0
    for i in idg_str:
        length_str += 1

    print(f"Der Text hat {length_str} character.")
    
    return

if __name__ == "__main__":
    main()