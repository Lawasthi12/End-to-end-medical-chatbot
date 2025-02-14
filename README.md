# End-to-end-medical-chatbot

## Steps to run the project

'''bash
conda create -n mchatbot python=3.8 -y
'''

 '''bash
conda activate mchatbot
 '''
 
 '''bash
pip install -r requirements.txt
 '''

 '''ini
 PINECONE_API_KEY = "***********************"
 '''

 ### Download the quantize model from the link provided in model folder & keep the model in the model directory:

 '''ini
 ## Download the Llama-2 model:

 llama-2-7b-chat.ggmlv3.q4_0.bin

 ## From the following link:
 https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
 '''