import openai 

openai.api_key = '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'

openai.Completion.create(
    model = 'text-davinci-003',
    prompt = "Explain the cicle of fifth's"
)

