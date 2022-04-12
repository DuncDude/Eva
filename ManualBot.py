#This is a manual version on the bot meant to be used with EVA


import yaml
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


import sys
 
# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)

# Create a new chat bot named Charlie
chatbot = ChatBot('new',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
		'chatterbot.logic.MathematicalEvaluation']
				 )

#train with custom 
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("./TrainingData/wikitalk.yaml",
			 "./TrainingData/wikitrain.yaml")

#train with chatterbot defaults
trainer2 = ChatterBotCorpusTrainer(chatbot)
trainer2.train('chatterbot.corpus.english')



# Get a response to the input text 'I would like to book a flight.'
while True:
	stuff = input("You: ")
	#response = chatbot.get_response(sys.argv[1])
	response = chatbot.get_response(stuff)
	print(response)
#	f = open("response.txt", "w")
#	f.write(str(response))
#	f.close()
#	exit()