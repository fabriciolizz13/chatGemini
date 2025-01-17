import google.generativeai as genai
import os
genai.configure(api_key="AIzaSyBl1Mg9iTKVshAfNBK7jd3mRP0GymrmrdU")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
model = genai.GenerativeModel('gemini-pro')
#crio uma lista chamada history#
chat = model.start_chat(history=[])
bem_vindo = '#bem vindo ao chat fabotAI#'
print(len(bem_vindo) * "#")
print("### bem vindo ao fabotAI ###")
print("### digite 'sair' para encerrar ###")
print("")

while True:
    texto = input("escreva uma pergunta:")

    if texto == "sair":
        break
    response = chat.send_message(texto)
    print("Gemini:", response.text, "\n")

    print("encerrando chat")

