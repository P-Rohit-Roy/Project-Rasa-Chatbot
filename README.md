Natural Language Understanding for Dialog System Assignment Using Rasa and Python.


Using conversational AI i.e. machine to understand and respond to human language in an interactive manner.
•	Natural Understanding Language (NLU) - extracting meaning from user inputs.
•	Dialogue Management – helps in managing conversational flow with appropriate responses.
Rasa Architecture and Components
•	Rasa NLU – it is an interpreter that helps to understand inputs and extracting data from user by using intent classification and entity extractions.
•	Rasa Core – it helps to built the conversation using ML by using conversation story with user and reply. 
•	Rasa Action Server – handles custom action and generate dynamic responses by API and provide user.
•	Rasa SDK – Extend the functionality, create custom components and implement complex logic in chatbot behaviour.
•	Rasa X – It is used for development and management for training, testing chatbot from user feedback to improve.
Pedestrian Support Chatbot using Flask (my project)
Setting up Development Environment
•	Install Python version 3.9
•	Install PyCharm IDE
•	Install Rasa
•	Flask  

Creating Rasa Environment
•	Create new directory in PyCharm 
•	Now creating a Rasa project by (rasa init) and it sets up directory structures and necessary files.
•	Configure the project by name, training data, NLU pipeline and so on.
•	But (rasa init –no-prompt) uses default initialization.
•	Now it creates a chatbot and use (rasa shell) to track with a chatbot and (/stop) to terminate.
•	Flask is micro web frame work to python to built web applications and API’s. it is lightweight, extensible, routing, templating, built-in development server, RESTful support api, secure and minimal boilerplate.

Project Files Structure
•	“actions” folder contains custom actions for the chatbot you add more files for additional actions to develop the project.
•	Open training data “nlu.yml” file and modify or create intent. which is responsible for user inputs and extract information.it consists of intents, entities, examples, synonyms and rejects to extract information accurately.
•	“rules.yml” file it contains rule-based conversation (rule-intent-action). To have conversational rules to control flow of conversation. “Rules” are likes “Stories” but has by specific conditions to handle dialog management by mapping user to specific responses for complex conversations or explicit conversation.
•	“stories.yml” file it contains the path of conversations flow between user and chatbot (happy path or sad path). Now go to “stories.yml” to configure the conversation between user and chatbot scenarios.it is used for normal conversation flow.it contains user intents, bot actions and uttrances from “domain.yml” file.
•	“domain.yml” file register the intent which has responses. Go to “domain.yml” file because it contains configuration settings i.e. chatbot utterances.it contains intents, entities, responses, actions, slots, forms, templates.
•	“config.yml” contains configuration settings pipeline for NLU, policies for dialog management.
•	“credentials.yml” for external service or API’s.
•	“endpoints.yml” defines endpoint any external services that chatbot needs to connect.
•	“models” folder store trained model of your chatbot i.e. NLU and Dialog management models in the folder.
•	“Synonyms” are used to improve NLU of chatbot by recognizing variation of same entity.
•	“RegEx” in rasa is used to identify specific text patterns from user.
•	“Entity Extraction” is important for NLU in rasa framework, it is used to identifying and extracting information from user input during chat. It consists of intent recognition and entity extraction. 

Steps for Pedestrian Support Chatbot
In this project I have trained model for pedestrians to know (e.g. lake, shopping mall, greeting, emergency, car booking)
1.	Change directory to specified folder.
2.	Create rasa project by “rasa init”.
3.	Select the desired location of the project.
4.	Train the model or train the model later in project directory and use “rasa train”.
5.	You can config chat in nlu.yml, domain.yml, stories.yml to get desired responses.
6.	“Entity” extraction enables the chatbot to gather important details from user. In rasa you need to define entity labels in training data in user text by markdown format or JSON format. [Entity name] (Entity value). 
7.	Open “actions.py” file in actions folder and uncomment it in code menu.it is used in rasa to define custom actions to implement logic and perform action based on user.
8.	And later go to “domain.yml” file to specify your actions.
9.	Also, in “stories.yml” you can use custom action in your story.
10.	In “endpoints.yml” enable action_endpoint when using custom actions.
11.	Last change intents,actions in domain,nlu and stories files.
12.	Install Flask and create python file in “tests” folder 
13.	Create “templates” folder” in project and create “html” file. 
14.	Train the rasa model by “rasa train”.
15.	Test the model by “rasa shell”.
16.	Your chatbot is ready.
