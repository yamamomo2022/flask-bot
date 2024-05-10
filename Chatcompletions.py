from openai import AzureOpenAI,OpenAI
import os
from dotenv import load_dotenv

def get_completion(inuput : str) -> str:

    try:
        load_dotenv()
        
        # client = AzureOpenAI(
        # azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        # api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        # api_version="2024-02-01"
        # )

        client = OpenAI(
          api_key=os.getenv("OPENAI_KEY"),
        )

        response = client.chat.completions.create(
            model=os.getenv("OPENAI_DEPLOYMENT"), # model = "deployment_name".
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": inuput}
            ]
        )
    
    except Exception as e:
        print(e)
        return "メーッセージの取得に失敗しました。"


    return response.choices[0].message.content
    #return inuput


if __name__=="__main__":
    get_completion()
