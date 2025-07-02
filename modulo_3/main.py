caracteres_especiais = "!@#$%^&*"

while True:
    senha = input("Digite uma senha para validar: ")

    tem_maiuscula = False
    tem_numero = False
    tem_especial = False

  
    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.isdigit():
            tem_numero = True
        elif caractere in caracteres_especiais:
            tem_especial = True

    if len(senha) >= 8 and tem_maiuscula and tem_numero and tem_especial:
        print("✅ Senha válida e segura!")
        break  
    else:
        print("\n❌ Senha inválida. Verifique os seguintes requisitos:")
        if len(senha) < 8:
            print("- Deve ter pelo menos 8 caracteres.")
        if not tem_maiuscula:
            print("- Deve conter pelo menos uma letra maiúscula.")
        if not tem_numero:
            print("- Deve conter pelo menos um número.")
        if not tem_especial:
            print("- Deve conter pelo menos um caractere especial (!@#$%^&*)")
        print("Tente novamente.\n")
