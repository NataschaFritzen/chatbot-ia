from pdf_reader import read_pdf

def responder(pergunta, conteudo_pdf):
    pergunta = pergunta.lower()

    if any(p in pergunta for p in ["cachorro", "cães", "pets", "cão"]):
        return "Cuidados com cachorros incluem alimentação equilibrada, vacinação, exercícios diários e carinho."

    elif "gato" in pergunta:
        return "Gatos precisam de caixa de areia limpa, escovação, brinquedos e ambiente seguro para explorar."

    elif "vacina" in pergunta or "vacinação" in pergunta:
        return "Vacinas protegem contra doenças graves. Consulte o veterinário para um plano de vacinação completo."

    elif "alimentação" in pergunta or "comida" in pergunta or "ração" in pergunta:
        return "A alimentação deve ser adequada à idade e porte do animal. Evite dar comida humana sem orientação."

    elif "higiene" in pergunta or "banho" in pergunta or "limpeza" in pergunta:
        return "Mantenha o pet limpo com banhos regulares, escovação e higienização dos utensílios."

    elif "passeio" in pergunta or "exercício" in pergunta:
        return "Passeios diários são importantes para o bem-estar físico e mental, especialmente para cães."

    elif "adoção" in pergunta or "adotar" in pergunta:
        return "Adotar é um ato de amor. Certifique-se de ter estrutura e tempo para cuidar do animal."

    elif "veterinário" in pergunta or "consulta" in pergunta:
        return "Levar o pet ao veterinário regularmente é essencial para prevenir e tratar problemas de saúde."

    elif "comportamento" in pergunta or "educação" in pergunta:
        return "Cada pet tem uma personalidade. Recompensas e paciência ajudam muito no adestramento."

    elif "remédio" in pergunta or "medicação" in pergunta:
        return "Nunca medique seu pet por conta própria. Sempre siga a orientação de um profissional."

    else:
        return "Desculpe, não entendi sua pergunta. Tente reformular com palavras como 'vacina', 'alimentação' ou 'higiene'."

def run_chatbot():
    print("Olá! Sou o Chatbot. Como posso ajudar você? (Digite 'sair' para encerrar)")

    conteudo_pdf = read_pdf("docs/Document_pets.pdf")

    while True:
        pergunta = input("Você: ")
        if pergunta.lower() == "sair":
            print("Chatbot: Até logo!")
            break

        resposta = responder(pergunta, conteudo_pdf)
        print("Chatbot:", resposta)

if __name__ == "__main__":
    run_chatbot()
