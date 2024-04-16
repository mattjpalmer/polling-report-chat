<<<<<<< HEAD
#%%
#general 
import os
#porject specfic
import boto3
from dotenv import load_dotenv, find_dotenv
from langchain.llms.bedrock import Bedrock
import pandas as pd
#local
from langchain.prompts import PromptTemplate

class LLMHandler:
    """LLM handler class - set up client 
    """
    def __init__(self, env_path):
        
        load_dotenv(env_path)
        boto3.setup_default_session(aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),
                            aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
                           )
        print(os.getenv('AWS_SECRET_ACCESS_KEY'))
        client = boto3.client(service_name='bedrock-runtime', 
                       region_name=os.getenv('AWS_DEFAULT_REGION'))
        self.llm = Bedrock(model_id = "anthropic.claude-instant-v1",
              client = client,
              model_kwargs = {'max_tokens_to_sample':90000,
                      "temperature":0.7,
                      "top_k":50, #previously 250
                      "top_p":1
                      }
             )
        self.problem_cases = {}

    def get_data(self,
                 prompt,
                 data) -> pd.DataFrame:
        """summarise input speech data 

        Args:
            prompt (langchain PromptTemplate): prompt to be passed to LLM

        Returns:
        """

        output = pd.DataFrame()
        chain = prompt | self.llm 
        response = chain.invoke({"prompt":prompt,
                                "data": data})
        return response


#%%


#---- prompt 
prompt = PromptTemplate(
    template = """
    \n\nHuman: As an experienced data analyst for a political organization your task is to analyze a speech and produce strategic summaries. 
    ### Context You have been provided speech data and format guidelines to structure your analysis. 
    ### Instructions from the speech data: 
    1. Write a concise sentence summary 
    2. Provide a relevant one to two sentence quotation 
    3. Indicate whether the speech is relevant to healthcare or social care issues by labeling it as 'True' if so, or 'False' if not. 
    4. Apply any suitable tags from the list of approved topic tags if the speech content matches the tag description. If none of the tags apply or you are unsure, use "Other".  
    
    Organize your responses according to the format instructions.
    Make sure the quotation you return is at least one complete sentence long .
    Ensure you only use tags present in the list of approved topic tags. 
    do you understand these instructions?
    \n\nAssistant:  Yes, I understand the instructions. As an analyst, my task is to analyze speech data and provide strategic summaries following the specified format guidelines.
    \n\nnHuman:  Here are the speech details
    ### Speech Data 
    ### List of approved tags with topic descriptions  
    {data}
    Do not repeat instructions back to me, just complete the task and return a response compatible  with the format instructions and nothing else.
     \n\nAssistant:""",
    input_variables=["topic_tags","speech_table"])


## --------------- set up CFG adn LLM 

handler = LLMHandler(env_path = '.env')

response = handler.get_data(prompt=prompt,
=======
#%%
#general 
import os
#porject specfic
import boto3
from dotenv import load_dotenv, find_dotenv
from langchain.llms.bedrock import Bedrock
import pandas as pd
#local
from langchain.prompts import PromptTemplate

class LLMHandler:
    """LLM handler class - set up client 
    """
    def __init__(self, env_path):
        
        load_dotenv(env_path)
        boto3.setup_default_session(aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),
                            aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
                           )
        client = boto3.client(service_name='bedrock-runtime', 
                       region_name=os.getenv('AWS_DEFAULT_REGION'))
        self.llm = Bedrock(model_id = "anthropic.claude-instant-v1",
              client = client,
              model_kwargs = {'max_tokens_to_sample':90000,
                      "temperature":0.7,
                      "top_k":50, #previously 250
                      "top_p":1
                      }
             )
        self.problem_cases = {}

    def get_data(self,
                 prompt,
                 data) -> pd.DataFrame:
        """summarise input speech data 

        Args:
            prompt (langchain PromptTemplate): prompt to be passed to LLM

        Returns:
        """

        output = pd.DataFrame()
        chain = prompt | self.llm 
        response = chain.invoke({"prompt":prompt,
                                "data": data})
        return response


#%%


#---- prompt 
prompt = PromptTemplate(
    template = """
    \n\nHuman: As an experienced data analyst for a political organization your task is to analyze a speech and produce strategic summaries. 
    ### Context You have been provided speech data and format guidelines to structure your analysis. 
    ### Instructions from the speech data: 
    1. Write a concise sentence summary 
    2. Provide a relevant one to two sentence quotation 
    3. Indicate whether the speech is relevant to healthcare or social care issues by labeling it as 'True' if so, or 'False' if not. 
    4. Apply any suitable tags from the list of approved topic tags if the speech content matches the tag description. If none of the tags apply or you are unsure, use "Other".  
    
    Organize your responses according to the format instructions.
    Make sure the quotation you return is at least one complete sentence long .
    Ensure you only use tags present in the list of approved topic tags. 
    do you understand these instructions?
    \n\nAssistant:  Yes, I understand the instructions. As an analyst, my task is to analyze speech data and provide strategic summaries following the specified format guidelines.
    \n\nnHuman:  Here are the speech details
    ### Speech Data 
    ### List of approved tags with topic descriptions  
    {data}
    Do not repeat instructions back to me, just complete the task and return a response compatible  with the format instructions and nothing else.
     \n\nAssistant:""",
    input_variables=["topic_tags","speech_table"])


## --------------- set up CFG adn LLM 

handler = LLMHandler(env_path = '.env')

response = handler.get_data(prompt=prompt,
>>>>>>> d1d8d7b1733448ae5b469038bbd74f2eb9ef5f2f
                            data = 'some data')