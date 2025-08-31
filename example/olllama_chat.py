import ollama

# 간단한 프롬프트 실행
response = ollama.chat(
    model="gemma3:1b",
    options={"temperature": 0, "top_p": 0.2},
    messages=[
        # {
        #     "role": "system",
        #     "content": "당신은 친절한 한국어 비서입니다. 언제나 간단 명료하게 알잘딱깔센하게 답해라",
        # },
        {
            "role": "user",
            "content": "How to make gemma3:1b 모델 만드는데 얼마나 시간이 걸렸는가",
        },
    ],
)

print(response["message"]["content"])
