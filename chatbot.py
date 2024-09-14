import openai
import os

# 設置你的 OpenAI API 密鑰
openai.api_key = "你的API密鑰"

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # 或者使用其他可用的模型
            messages=[
                {"role": "system", "content": "你是一個有幫助的助手。"},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"發生錯誤：{str(e)}"

def main():
    print("歡迎使用 ChatGPT 聊天機器人！（輸入 'quit' 退出）")
    while True:
        user_input = input("你: ")
        if user_input.lower() == 'quit':
            break
        response = chat_with_gpt(user_input)
        print("ChatGPT:", response)

if __name__ == "__main__":
    main()