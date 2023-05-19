from prompt_optimizer.metric import TokenMetric
from prompt_optimizer.poptim import EntropyOptim
from langchain.schema import (
    HumanMessage,
    SystemMessage
)

messages = [
    SystemMessage(content="You are a helpful assistant that translates English to French."),
    HumanMessage(content="I love programming.")
]

p_optimizer = EntropyOptim(verbose=True, p=0.5, metrics=[TokenMetric()])
optim_batch_messages = p_optimizer(messages, langchain=True)

print(messages)
print(optim_batch_messages)
