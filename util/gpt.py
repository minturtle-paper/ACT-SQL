import json
import openai
import requests
import time
from dotenv import load_dotenv
import os

load_dotenv()

def get_response(prompt, args, max_tokens=150, temperature=0):
    # vLLM 서버 설정 (args에서 가져오거나 기본값 사용)
    # OpenAI 클라이언트를 vLLM 서버로 설정
    openai.api_base = os.getenv('OPENAI_API_BASE')
    openai.api_key = os.getenv('OPENAI_API_KEY')  # vLLM은 API 키가 필요하지 않지만 호환성을 위해 설정
    
    while 1:
        if isinstance(prompt, str):
            try:
                response = openai.Completion.create(
                    model=args.gpt,
                    prompt=prompt,
                    max_tokens=max_tokens,
                    temperature=temperature,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0,
                    stop=[';', '\n\n', 'Given', 'Question', 'Translate']
                )
                return response['choices'][0]['text']
            except Exception as e:
                if str(e).startswith("This model's maximum context length is"):
                    return None
                print('Retrying ...')
                time.sleep(10)
        else:
            try:
                response = openai.ChatCompletion.create(
                    model=args.gpt,
                    messages=prompt,
                    max_tokens=max_tokens,
                    temperature=temperature,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )
                return response['choices'][0]['message']['content']
            except Exception as e:
                if str(e).startswith("This model's maximum context length is"):
                    return None
                print('Retrying ...')
                time.sleep(10)
