from llms.chatGpt import chatGpt
from llms.gemini import gemini
from llms.mistralAi import mistralAi

prompt = "Quais são os países mais quentes do mundo?"

chatGpt_Response = chatGpt(prompt)
gemini_Response = gemini(prompt)
mistralAi_Response = mistralAi(prompt)

def llms_Responses():
    print("\n--> RESPOSTAS DOS LLMS <--")
    
    print(F"\nCHATGPT:\n\n{chatGpt_Response}\n")
    print(F"\nGEMINI:\n\n{gemini_Response}\n")
    print(F"\nMISTRAL AI:\n\n{mistralAi_Response}\n")
    
llms_Responses()

def llms_Responses_Comparison():
    print("\n--> COMPARAÇÃO DAS RESPOSTAS DOS LLMS <--\n")
    
    prompt = f"""
        Compare as respostas desses 3 llms considerando os critérios:
        
        CHATGPT: {chatGpt_Response}
        GEMMINI: {gemini_Response}
        MISTRAL AI: {mistralAi_Response}
        
        1. Clareza e coerência da resposta
        2. Precisão da informação
        3. Criatividade ou profundidade da resposta
        4. Consistência gramatical
    """
        
    return chatGpt(prompt)

print(llms_Responses_Comparison())

def llms_Responses_Rancking():
    print("\n--> RANKING DAS RESPOSTAS DOS LLMS <--")
    
    prompt = f"""
        Faça um rank das respostas desses 3 LLMs:
        
        CHATGPT: {chatGpt_Response}
        GEMMINI: {gemini_Response}
        MISTRAL AI: {mistralAi_Response}
        
        Me dê apenas o rank e uma pequena justificativa
    """
    
    print("\nRANKING DO CHATGPT\n")
    
    print(chatGpt(prompt))
    
    print("\nRANKING DO GEMINI\n")
    
    print(gemini(prompt))
    
    print("\nRANKING DO MISTRAL AI\n")
    
    print(mistralAi(prompt))
    
llms_Responses_Rancking()
