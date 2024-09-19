# building-a-streaming-api-for-llama-2-real-time-ai-with-jina-and-docarray

## SIMPLE_CHUNKING

#### 7 chunk(s)

Llama 2 - Meta AI Llama 2 — The next generation of our open source large language model, available for free for research and commercial use. Meta AI Llama 2 7B Chat - a Hugging Face Space by huggingface-projects Discover amazing ML apps made by the community a Hugging Face Space by huggingface-projects 💡 This article comes with a Google Colab notebook you can use to try it out yourself. Getting Access to the Llama-2-chat Model Before starting, you will need permission from Meta to download the model from Hugging Face. First, you will need a Hugging Face account. You can sign up for one for free on the Hugging Face website. Next, you will need to request permission from Meta. You can make the request from the model card page for Llama 2 at Hugging Face, when you are logged in with your Hugging Face credentials. ⚠️ This request may take one to two days to process. Finally, request a token from Hugging Face from your settings page. You will need this token to download the model. You will need the token to access Hugging Face models via the transformers interface. Before running the code in this article, you should log in using the command huggingface-cli: % huggingface-cli login _| _| _| _| _|_|_| _|_|_| _|_|_| _| _| _|_|_| _|_|_|_| _|_| _|_|_| _|_|_|_| _| _| _| _| _| _| _| _|_| _| _| _| _| _| _| _| _|_|_|_| _| _| _| _|_| _| _|_| _| _| _| _| _| _|_| _|_|_| _|_|_|_| _| _|_|_| _| _| _| _| _| _| _| _| _| _| _|_| _| _| _| _| _| _| _| _| _| _|_| _|_|_| _|_|_| _|_|_| _| _| _|_|_| _| _| _| _|_|_| _|_|_|_| To login, `huggingface_hub` requires a token generated from https://huggingface.co/settings/tokens . Token: You should then paste in your token and press enter. You will be asked if you want to add your token as git credential. You can answer yes or no, but no is faster. If successful, you will get a result that looks like this: Token is valid. Your token has been saved to /users/your_name/.cache/huggingface/token Login successful Prompting the Llama-2-chat Model The Llama 2 model marks a significant improvement over its predecessor, Llama 1. Released as a selection of models ranging in size from 7 to 70 billion parameters, Llama 2 offers users considerably more power and flexibility, as well as having been trained on 40% more data and having a context size — the maximum size of any input — of up to 4,000 tokens, twice as much as Llama 1 and comparable to ChatGPT 3.5. But the real highlight is the Llama-2-chat model. Tailored specifically for dialog applications with a million additional human-annotated data items, they are the state-of-the-art in terms of helpfulness and safety, with performance on chat tasks rivaling much larger ChatGPT models.

Llama-2-chat offers users a semi-structured prompt schema that lets you divide your input into a system prompt and user message. It has been trained to respond to the system prompt as a kind of background or meta-instruction that it should consider every time it answers and a user message relevant only to the current interaction. The schema is very simple. The initial interaction with Llama-2-chat should look like this: <s>[INST] <<SYS>> *system_prompt* <</SYS>> *user_message* [/INST] For example, we might create a system prompt like this: You are a helpful, respectful, and honest assistant. Always answer as helpfully as possible while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature. If a question does not make any sense or is not factually coherent, explain why instead of answering something incorrectly. If you don't know the answer to a question, don't share false information. Then, ask a random question like: If I punch myself in the face and it hurts, am I weak or strong? The full message passed to Llama-2-chat model would therefore be: <s>[INST] <<SYS>> You are a helpful, respectful, and honest assistant. Always answer as helpfully as possible while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature. If a question does not make any sense or is not factually coherent, explain why instead of answering something incorrectly. If you don't know the answer to a question, don't share false information. <</SYS>> If I punch myself in the face and it hurts, am I weak or strong? [/INST] In a conversation, you must add the previous interactions, including the output from Llama 2. For longer interactions, the schema looks like this: <s>[INST] <<SYS>> *system_prompt* <</SYS>> *user_msg_1* [/INST] *model_answer_1* </s> <s>[INST] *user_msg_2* [/INST] *model_answer_2* </s> <s>[INST] *user_msg_3* [/INST] etc... Models like Llama 2 have no memory of past interactions, and the surrounding application must provide the memory by including the conversation log in the prompt of each message. But as long as the system prompt is within the 4,000 model’s token limit, it will be remembered and considered when answering.

You can focus on your logic and algorithms, withoutworrying about the infrastructure complexity. Jina provides a smooth Pythonic experience for se… Jina 3.20.1 Documentation docarray.github.io homepage of docarray docarray.github.io You will need to install a number of libraries in your Python environment, specifically the torch, transformers, jina, and docarray libraries, as well as some other supporting libraries if not already present: pip install docarray jina bitsandbytes accelerate transformers Service schemas The first step in creating a streaming service, regardless of framework, is defining service schemas. At its most abstract, the service takes a text input and receives back a stream of tokens. In addition, we provide a parameter for setting the maximum number of tokens to respond with. We construct our schema using DocArray, which is designed to support flexible AI-centric services: from docarray import BaseDoc class PromptDocument(BaseDoc): prompt: str max_tokens: int class ModelOutputDocument(BaseDoc): token_id: int generated_text: str Service initialization Next, we create the token streaming class that is central to our service. This class contains and initializes both the language model and its tokenizer. In the example below, we use the 7B Llama-2-chat model — the smallest of the Llama-2-chat models — and load it using the facilities from the transformer library. It extends the Jina Executor class, which contains a number of methods for handling streams and processes. Note that we've set the device_map parameter to auto, ensuring that the model uses a GPU if it has access to one, and load_in_8bit to True, which quantizes the model to reduce its size in memory. These settings make running our code smoothly on a free Google Colab notebook feasible. from jina import Executor, requests from transformers import AutoTokenizer, AutoModelForCausalLM import torch model_name = 'meta-llama/Llama-2-7b-chat-hf' class TokenStreamingExecutor(Executor): def __init__(self, **kwargs): super().__init__(**kwargs) self.tokenizer = AutoTokenizer.from_pretrained(model_name) self.model = AutoModelForCausalLM.from_pretrained( model_name, device_map='auto', load_in_8bit=True ) Implementing the streaming endpoint We implement the streaming endpoint as the task method of the TokenStreamingExecutor. This method processes an instance of PromptDocument and dynamically streams back a sequence of ModelOutputDocument instances. We implement this using Python’s yield keyword in the code below, generating tokens on the fly up to the user-specified maximum number of tokens or until the END token is encountered (self.tokenizer.eos_token_id). Each ModelOutputDocument that the stream returns encapsulates a numerical token ID and its corresponding text string. class TokenStreamingExecutor(Executor): ... def starts_with_space(self, token_id): token = self.tokenizer.convert_ids_to_tokens(token_id) return token.startswith('▁') @requests(on='/stream') async def task(self, doc: PromptDocument, **kwargs) -> ModelOutputDocument: input = self.tokenizer(doc.prompt, return_tensors='pt') input_len = input['input_ids'].shape[1] for output_length in range(doc.max_tokens): output = self.model.generate(**input, max_new_tokens=1) current_token_id = output[0][-1] if current_token_id == self.tokenizer.eos_token_id: break current_token = self.tokenizer.decode( current_token_id, skip_special_tokens=True ) if self.starts_with_space(current_token_id.item()) and output_length > 1: current_token = ' ' + current_token yield ModelOutputDocument( token_id=current_token_id, generated_text=current_token, ) input = { 'input_ids': output, 'attention_mask': torch.ones(1, len(output[0])), }

You can learn more about streaming endpoints from the Executor class documentation on the Jina website. Using the streaming service Now that all the code is in place, we can run the service and start to use it. The code below deploys an instance of the TokenStreamingExecutor class and sets up a gRPC endpoint at the specified port: from jina import Deployment with Deployment(uses=TokenStreamingExecutor, port=12345, protocol='grpc') as dep: dep.block() Once the service is running, you can send it messages and see how the model responds. The code below uses the Jina Client class to contact the service, pass it a correctly formatted prompt, receive the stream of tokens, and print them out. import asyncio from jina import Client llama_prompt = PromptDocument( prompt=""" <s>[INST] <<SYS>> You are a helpful, respectful, and honest assistant. Always answer as helpfully as possible while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature. If a question does not make any sense or is not factually coherent, explain why instead of answering something incorrectly. If you don't know the answer to a question, don't share false information. <</SYS>> If I punch myself in the face and it hurts, am I weak or strong? [/INST] """, max_tokens=100, ) async def main(): client = Client(port=12345, protocol='grpc', asyncio=True) async for doc in client.stream_doc( on='/stream', inputs=llama_prompt, return_type=ModelOutputDocument, ): print(doc.generated_text, end='') asyncio.run(main())

If you run this code, the result should look something like this: I'm here to help you, but I must inform you that punching oneself in the face is not a safe or healthy practice. It can cause physical harm and lead to injuries, including broken bones, cuts, and bruises. It is not a recommended or acceptable way to handle emotions or stress. Instead of resorting to harmful actions, there are many other ways to manage emotions and cope with stress in a healthy and constructive manner. Some options include: 1. Exercise: Physical activity can help release tension and improve mood. 2. Mindfulness: Practices such as meditation, deep breathing, or yoga can help you focus on the present moment and manage emotions. 3. Talking to someone: Sharing your feelings with a trusted friend, family member, or mental health professional can provide emotional support and help you find healthy ways You can adapt this code to any prompt or extend it to support a fully two-way conversation.

Run Your Own AI Chat Service With the release of Llama 2 and its chat-trained models, you can use Jina and DocArray to create and operate your own chat service with just a few classes and functions. You can use a cloud service provider, for example, Jina AI Cloud, and control the entire technology stack, never paying external API fees or worrying about your data privacy. The smallest model is small enough to run in-house on a well-resourced GPU machine, eliminating even cloud dependencies if desired. Llama 2’s separation of system prompts from user input gives you an additional layer of control, letting you do your own prompt engineering and in-context learning and building it into the service. The possibilities are endless. Get Involved To learn more, check out the websites for Jina AI and DocArray. You can also contact us and the Jina user community via Discord. Jina AI - Your Portal to Multimodal AI Jina AI offers powerful multimodal AI solutions for everyday users, developers, and scalable enterprise solutions. We aim to democratize access to the limitless potential of AI-generated creativity and innovation, empowering individuals and businesses alike. Your Portal to Multimodal AI docarray.github.io homepage of docarray docarray.github.io Categories: Tech blog rss_feed Top-5 similar articles play_arrow GET TOP-5 Select reranker Read more

August 26, 2024 • 13 minutes read The What and Why of Text-Image Modality Gap in CLIP Models You can't just use a CLIP model to retrieve text and images and sort the results by score. Why? Because of the modality gap. What is it, and where does it come from? August 22, 2024 • 8 minutes read Late Chunking in Long-Context Embedding Models Chunking long documents while preserving contextual information is challenging. We introduce the "Late Chunking" that leverages long-context embedding models to generate contextual chunk embeddings for better retrieval applications. July 31, 2024 • 17 minutes read Rephrased Labels Improve Zero-Shot Text Classification by 30% When using embedding models for zero-shot classification, rephrasing the class label to "This is seriously about 'LABEL'" gives higher accuracy vs. using LABEL alone. But how, and why? OFFICES location_on Berlin, Germany (HQ) Prinzessinnenstraße 19-20, 10969 Berlin, Germany Geschäftsanschrift: Leipzigerstr. 96, 10117 Berlin, Germany location_on Beijing, China Level 5, Building 6, No.48 Haidian West St. Beijing Haidian, China location_on Shenzhen, China 402, Floor 4, Fu'an Technology Building, Shenzhen Nanshan, China SEARCH FOUNDATION Embeddings Reranker Reader Segmenter Get Jina AI API key API Status COMPANY About us Contact sales Newsroom Intern program Join us open_in_new Download logo open_in_new TERMS Terms & Conditions Privacy Manage Cookies email language English science Jina AI GmbH © 2020-2024.

## COT_TOPIC_CHUNKING

#### 8 chunk(s)

Streaming Chat Jina and DocArray provide a set of tools that make it possible to construct a streaming connection between an AI model and a user application with a minimum of Python code. Welcome to Jina! Jina lets you build multimodal AI services and pipelines that communicate via gRPC, HTTP and WebSockets, then scale them up and deploy to production.

Implementing the streaming endpoint We implement the streaming endpoint as the task method of the TokenStreamingExecutor. This method processes an instance of PromptDocument and dynamically streams back a sequence of ModelOutputDocument instances. We implement this using Python’s yield keyword in the code below, generating tokens on the fly up to the user-specified maximum number of tokens or until the END token is encountered (self.tokenizer.eos_token_id). Each ModelOutputDocument that the stream returns encapsulates a numerical token ID and its corresponding text string. class TokenStreamingExecutor(Executor): ... def starts_with_space(self, token_id): token = self.tokenizer.convert_ids_to_tokens(token_id) return token.startswith('▁') @requests(on='/stream') async def task(self, doc: PromptDocument, **kwargs) -> ModelOutputDocument: input = self.tokenizer(doc.prompt, return_tensors='pt') input_len = input['input_ids'].shape[1] for output_length in range(doc.max_tokens): output = self.model.generate(**input, max_new_tokens=1) current_token_id = output[0][-1] if current_token_id == self.tokenizer.eos_token_id: break current_token = self.tokenizer.decode( current_token_id, skip_special_tokens=True ) if self.starts_with_space(current_token_id.item()) and output_length > 1: current_token = ' ' + current_token yield ModelOutputDocument( token_id=current_token_id, generated_text=current_token, ) input = { 'input_ids': output, 'attention_mask': torch.ones(1, len(output[0])), }

You can learn more about streaming endpoints from the Executor class documentation on the Jina website. Using the streaming service Now that all the code is in place, we can run the service and start to use it. The code below deploys an instance of the TokenStreamingExecutor class and sets up a gRPC endpoint at the specified port: from jina import Deployment with Deployment(uses=TokenStreamingExecutor, port=12345, protocol='grpc') as dep: dep.block() Once the service is running, you can send it messages and see how the model responds. The code below uses the Jina Client class to contact the service, pass it a correctly formatted prompt, receive the stream of tokens, and print them out. import asyncio from jina import Client llama_prompt = PromptDocument( prompt=""" <s>[INST] <<SYS>> You are a helpful, respectful, and honest assistant. Always answer as helpfully as possible while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature. If a question does not make any sense or is not factually coherent, explain why instead of answering something incorrectly. If you don't know the answer to a question, don't share false information. <</SYS>> If I punch myself in the face and it hurts, am I weak or strong? [/INST] """, max_tokens=100, ) async def main(): client = Client(port=12345, protocol='grpc', asyncio=True) async for doc in client.stream_doc( on='/stream', inputs=llama_prompt, return_type=ModelOutputDocument, ): print(doc.generated_text, end='') asyncio.run(main())

If you run this code, the result should look something like this: I'm here to help you, but I must inform you that punching oneself in the face is not a safe or healthy practice. It can cause physical harm and lead to injuries, including broken bones, cuts, and bruises. It is not a recommended or acceptable way to handle emotions or stress. Instead of resorting to harmful actions, there are many other ways to manage emotions and cope with stress in a healthy and constructive manner. Some options include: 1. Exercise: Physical activity can help release tension and improve mood. 2. Mindfulness: Practices such as meditation, deep breathing, or yoga can help you focus on the present moment and manage emotions. 3. Talking to someone: Sharing your feelings with a trusted friend, family member, or mental health professional can provide emotional support and help you find healthy ways

You can adapt this code to any prompt or extend itto support a fully two-way conversation. Run Your Own AI Chat Service With the release of Llama 2 and its chat-trained models, you can use Jina and DocArray to create and operate your own chat service with just a few classes and functions. You can use a cloud service provider, for example, Jina AI Cloud, and control the entire technology stack, never paying external API fees or worrying about your data privacy. The smallest model is small enough to run in-house on a well-resourced GPU machine, eliminating even cloud dependencies if desired. Llama 2’s separation of system prompts from user input gives you an additional layer of control, letting you do your own prompt engineering and in-context learning and building it into the service. The possibilities are endless. Get Involved To learn more, check out the websites for Jina AI and DocArray. You can also contact us and the Jina user community via Discord.

Jina AI - Your Portal to Multimodal AI Jina AI offers powerful multimodal AI solutions for everyday users, developers, and scalable enterprise solutions. We aim to democratize access to the limitless potential of AI-generated creativity and innovation, empowering individuals and businesses alike. Your Portal to Multimodal AI docarray.github.io homepage of docarray docarray.github.io Categories: Tech blog rss_feed Top-5 similar articles play_arrow GET TOP-5 Select reranker Read more August 26, 2024 • 13 minutes read The What and Why of Text-Image Modality Gap in CLIP Models

When using embedding models for zero-shot classification, rephrasing the class label to "This is seriously about 'LABEL'" gives higher accuracy vs. using LABEL alone. But how, and why?

OFFICES location_on Berlin, Germany (HQ) Prinzessinnenstraße 19-20, 10969 Berlin, Germany Geschäftsanschrift: Leipzigerstr. 96, 10117 Berlin, Germany location_on Beijing, China Level 5, Building 6, No.48 Haidian West St. Beijing Haidian, China location_on Shenzhen, China 402, Floor 4, Fu'an Technology Building, Shenzhen Nanshan, China SEARCH FOUNDATION Embeddings Reranker Reader Segmenter Get Jina AI API key API Status COMPANY About us Contact sales Newsroom Intern program Join us open_in_new Download logo open_in_new TERMS Terms & Conditions Privacy Manage Cookies email language English science Jina AI GmbH © 2020-2024.

## SUMMARY_CHUNKING

#### 8 chunk(s)

Tired of paying for ChatGPT? Want to have your own streaming AI chatbot, with your own engineered prompts running on your own servers or cloud? With Llama2, DocArray, and Jina, you can set it up in a few minutes! Saba Sturua, Scott Martens • 10 minutes read Large language models based on the Transformer architecture have revolutionized AI technology recently. Transformers are versatile and useful for various tasks, but they all have the property that they process their input all at once and generate output one word at a time. This can lead to frustrating delays, inefficient processing, and technical difficulties from time-outs because you cannot know in advance how long a transformer-based model will take to complete its output. To overcome this, it would be better to stream the results. DocArray and Jina provide a streaming mechanism designed for AI models. This article will show you how to use them to stream interaction with the Llama-2-Chat model.

Llama 2 - Meta AI Llama 2 — The next generation of our open source large language model, available for free for research and commercial use. Meta AI Llama 2 7B Chat - a Hugging Face Space by huggingface-projects Discover amazing ML apps made by the community a Hugging Face Space by huggingface-projects 💡 This article comes with a Google Colab notebook you can use to try it out yourself. Getting Access to the Llama-2-chat Model Before starting, you will need permission from Meta to download the model from Hugging Face. First, you will need a Hugging Face account. You can sign up for one for free on the Hugging Face website. Next, you will need to request permission from Meta. You can make the request from the model card page for Llama 2 at Hugging Face, when you are logged in with your Hugging Face credentials. ⚠️ This request may take one to two days to process. Finally, request a token from Hugging Face from your settings page. You will need this token to download the model. You will need the token to access Hugging Face models via the transformers interface. Before running the code in this article, you should log in using the command huggingface-cli: % huggingface-cli login _| _| _| _| _|_|_| _|_|_| _|_|_| _| _| _|_|_| _|_|_|_| _|_| _|_|_| _|_|_|_| _| _| _| _| _| _| _| _|_| _| _| _| _| _| _| _| _|_|_|_| _| _| _| _|_| _| _|_| _| _| _| _| _| _|_| _|_|_| _|_|_|_| _| _|_|_| _| _| _| _| _| _| _| _| _| _| _|_| _| _| _| _| _| _| _| _| _| _|_| _|_|_| _|_|_| _|_|_| _| _| _|_|_| _| _| _| _|_|_| _|_|_|_| To login, `huggingface_hub` requires a token generated from https://huggingface.co/settings/tokens . Token: You should then paste in your token and press enter. You will be asked if you want to add your token as git credential. You can answer yes or no, but no is faster. If successful, you will get a result that looks like this: Token is valid. Your token has been saved to /users/your_name/.cache/huggingface/token Login successful Prompting the Llama-2-chat Model The Llama 2 model marks a significant improvement over its predecessor, Llama 1. Released as a selection of models ranging in size from 7 to 70 billion parameters, Llama 2 offers users considerably more power and flexibility, as well as having been trained on 40% more data and having a context size — the maximum size of any input — of up to 4,000 tokens, twice as much as Llama 1 and comparable to ChatGPT 3.5. But the real highlight is the Llama-2-chat model. Tailored specifically for dialog applications with a million additional human-annotated data items, they are the state-of-the-art in terms of helpfulness and safety, with performance on chat tasks rivaling much larger ChatGPT models.

Llama-2-chat offers users a semi-structured prompt schema that lets you divide your input into a system prompt and user message. It has been trained to respond to the system prompt as a kind of background or meta-instruction that it should consider every time it answers and a user message relevant only to the current interaction. The schema is very simple. The initial interaction with Llama-2-chat should look like this: <s>[INST] <<SYS>> *system_prompt* <</SYS>> *user_message* [/INST] For example, we might create a system prompt like this: You are a helpful, respectful, and honest assistant. Always answer as helpfully as possible while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature. If a question does not make any sense or is not factually coherent, explain why instead of answering something incorrectly. If you don't know the answer to a question, don't share false information. Then, ask a random question like: If I punch myself in the face and it hurts, am I weak or strong? The full message passed to Llama-2-chat model would therefore be: <s>[INST] <<SYS>> You are a helpful, respectful, and honest assistant. Always answer as helpfully as possible while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature. If a question does not make any sense or is not factually coherent, explain why instead of answering something incorrectly. If you don't know the answer to a question, don't share false information. <</SYS>> If I punch myself in the face and it hurts, am I weak or strong? [/INST] In a conversation, you must add the previous interactions, including the output from Llama 2. For longer interactions, the schema looks like this: <s>[INST] <<SYS>> *system_prompt* <</SYS>> *user_msg_1* [/INST] *model_answer_1* </s> <s>[INST] *user_msg_2* [/INST] *model_answer_2* </s> <s>[INST] *user_msg_3* [/INST] etc... Models like Llama 2 have no memory of past interactions, and the surrounding application must provide the memory by including the conversation log in the prompt of each message. But as long as the system prompt is within the 4,000 model’s token limit, it will be remembered and considered when answering.

Once the service is running, you can send it messages and see how the model responds. The code below uses the Jina Client class to contact the service, pass it a correctly formatted prompt, receive the stream of tokens, and print them out. import asyncio from jina import Client llama_prompt = PromptDocument( prompt=""" <s>[INST] <<SYS>> You are a helpful, respectful, and honest assistant. Always answer as helpfully as possible while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature. If a question does not make any sense or is not factually coherent, explain why instead of answering something incorrectly. If you don't know the answer to a question, don't share false information. <</SYS>> If I punch myself in the face and it hurts, am I weak or strong? [/INST] """, max_tokens=100, ) async def main(): client = Client(port=12345, protocol='grpc', asyncio=True) async for doc in client.stream_doc( on='/stream', inputs=llama_prompt, return_type=ModelOutputDocument, ): print(doc.generated_text, end='') asyncio.run(main()) If you run this code, the result should look something like this: I'm here to help you, but I must inform you that punching oneself in the face is not a safe or healthy practice. It can cause physical harm and lead to injuries, including broken bones, cuts, and bruises. It is not a recommended or acceptable way to handle emotions or stress. Instead of resorting to harmful actions, there are many other ways to manage emotions and cope with stress in a healthy and constructive manner. Some options include: 1. Exercise: Physical activity can help release tension and improve mood. 2. Mindfulness: Practices such as meditation, deep breathing, or yoga can help you focus on the present moment and manage emotions. 3. Talking to someone: Sharing your feelings with a trusted friend, family member, or mental health professional can provide emotional support and help you find healthy ways You can adapt this code to any prompt or extend it to support a fully two-way conversation. Run Your Own AI Chat Service With the release of Llama 2 and its chat-trained models, you can use Jina and DocArray to create and operate your own chat service with just a few classes and functions. You can use a cloud service provider, for example, Jina AI Cloud, and control the entire technology stack, never paying external API fees or worrying about your data privacy. The smallest model is small enough to run in-house on a well-resourced GPU machine, eliminating even cloud dependencies if desired. Llama 2’s separation of system prompts from user input gives you an additional layer of control, letting you do your own prompt engineering and in-context learning and building it into the service. The possibilities are endless. Get Involved To learn more, check out the websites for Jina AI and DocArray. You can also contact us and the Jina user community via Discord.

Jina AI - Your Portal to Multimodal AI Jina AI offers powerful multimodal AI solutions for everyday users, developers, and scalable enterprise solutions. We aim to democratize access to the limitless potential of AI-generated creativity and innovation, empowering individuals and businesses alike. Your Portal to Multimodal AI docarray.github.io homepage of docarray docarray.github.io Categories: Tech blog rss_feed Top-5 similar articles play_arrow GET TOP-5 Select reranker Read more August 26, 2024 • 13 minutes read The What and Why of Text-Image Modality Gap in CLIP Models

You can't just use a CLIP model to retrieve text and images and sort the results by score. Why? Because of the modality gap. What is it, and where does it come from? August 22, 2024 • 8 minutes read Late Chunking in Long-Context Embedding Models Chunking long documents while preserving contextual information is challenging. We introduce the "Late Chunking" that leverages long-context embedding models to generate contextual chunk embeddings for better retrieval applications. July 31, 2024 • 17 minutes read Rephrased Labels Improve Zero-Shot Text Classification by 30% When using embedding models for zero-shot classification, rephrasing the class label to "This is seriously about 'LABEL'" gives higher accuracy vs. using LABEL alone. But how, and why?

OFFICES location_on Berlin, Germany (HQ) Prinzessinnenstraße 19-20, 10969 Berlin, Germany Geschäftsanschrift: Leipzigerstr. 96, 10117 Berlin, Germany location_on Beijing, China Level 5, Building 6, No.48 Haidian West St. Beijing Haidian, China location_on Shenzhen, China 402, Floor 4, Fu'an Technology Building, Shenzhen Nanshan, China

SEARCH FOUNDATION Embeddings Reranker Reader Segmenter Get Jina AI API key API Status COMPANY About us Contact sales Newsroom Intern program Join us open_in_new Download logo open_in_new TERMS Terms & Conditions Privacy Manage Cookies email language English science Jina AI GmbH © 2020-2024.

## JINA-SEGMENTER-API

#### 226 chunk(s)

search


notifications


NEWS


PRODUCTS


COMPANY


Tech blog


August 23, 2023


Building a Streaming API for Llama 2: Real-time AI with Jina and DocArray


Tired of paying for ChatGPT? Want to have your own streaming AI chatbot, with your own engineered prompts running on your own servers or cloud? With Llama2, DocArray, and Jina, you can set it up in a few minutes!


Saba Sturua, Scott Martens • 10 minutes read



Large language models based on the Transformer architecture have revolutionized AI technology recently. Transformers are versatile and useful for various tasks, but they all have the property that they process their input all at once and generate output one word at a time. This can lead to frustrating delays, inefficient processing, and technical difficulties from time-outs because you cannot know in advance how long a transformer-based model will take to complete its output.



To overcome this, it would be better to stream the results.



DocArray and Jina provide a streaming mechanism designed for AI models. This article will show you how to use them to stream interaction with the Llama-2-Chat model.



Llama 2 - Meta AI


Llama 2 — The next generation of our open source large language model, available for free for research and commercial use.


Meta AI


Llama 2 7B Chat - a Hugging Face Space by huggingface-projects


Discover amazing ML apps made by the community


a Hugging Face Space by huggingface-projects


This article comes with a Google Colab notebook you can use to try it out yourself.


Getting Access to the Llama-2-chat Model



Before starting, you will need permission from Meta to download the model from Hugging Face.



First, you will need a Hugging Face account. You can sign up for one for free on the Hugging Face website.


Next, you will need to request permission from Meta. You can make the request from the model card page for Llama 2 at Hugging Face, when you are logged in with your Hugging Face credentials.


️


This request may take one to two days to process.


Finally, request a token from Hugging Face from your settings page. You will need this token to download the model.



You will need the token to access Hugging Face models via the transformers interface. Before running the code in this article, you should log in using the command huggingface-cli:



% huggingface-cli login
    


    _|    _|  _|    _|    _|_|_|    _|_|_|  _|_|_|  _|      _|    _|_|_|      _|_|_|_|    _|_|      _|_|_|  _|_|_|_|
    _|    _|  _|    _|  _|        _|          _|    _|_|    _|  _|            _|        _|    _|  _|        _|
    _|_|_|_|  _|    _|  _|  _|_|  _|  _|_|    _|    _|  _|  _|  _|  _|_|      _|_|_|    _|_|_|_|  _|        _|_|_|
    _|    _|  _|    _|  _|    _|  _|    _|    _|    _|    _|_|  _|    _|      _|        _|    _|  _|        _|
    _|    _|    _|_|      _|_|_|    _|_|_|  _|_|_|  _|      _|    _|_|_|      _|        _|    _|    _|_|_|  _|_|_|_|
    
    To login, `huggingface_hub` requires a token generated from https://huggingface.co/settings/tokens .


Token:




You should then paste in your token and press enter. You will be asked if you want to add your token as git credential. You can answer yes or no, but no is faster.



If successful, you will get a result that looks like this:



Token is valid.


Your token has been saved to /users/your_name/.cache/huggingface/token


Login successful



Prompting the Llama-2-chat Model



The Llama 2 model marks a significant improvement over its predecessor, Llama 1. Released as a selection of models ranging in size from 7 to 70 billion parameters, Llama 2 offers users considerably more power and flexibility, as well as having been trained on 40% more data and having a context size — the maximum size of any input — of up to 4,000 tokens, twice as much as Llama 1 and comparable to ChatGPT 3.5.



But the real highlight is the Llama-2-chat model. Tailored specifically for dialog applications with a million additional human-annotated data items, they are the state-of-the-art in terms of helpfulness and safety, with performance on chat tasks rivaling much larger ChatGPT models.



Llama-2-chat offers users a semi-structured prompt schema that lets you divide your input into a system prompt and user message. It has been trained to respond to the system prompt as a kind of background or meta-instruction that it should consider every time it answers and a user message relevant only to the current interaction.



The schema is very simple. The initial interaction with Llama-2-chat should look like this:



<s>[INST] <<SYS>>


*system_prompt*


<</SYS>>


*user_message*


[/INST]




For example, we might create a system prompt like this:



You are a helpful, respectful, and honest assistant. Always answer as helpfully as possible while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.



If a question does not make any sense or is not factually coherent, explain why instead of answering something incorrectly. If you don't know the answer to a question, don't share false information.



Then, ask a random question like:



If I punch myself in the face and it hurts, am I weak or strong?



The full message passed to Llama-2-chat model would therefore be:



<s>[INST] <<SYS>>


You are a helpful, respectful, and honest assistant. Always answer as 


helpfully as possible while being safe.  Your answers should not 


include any harmful, unethical, racist, sexist, toxic, dangerous, or 


illegal content. Please ensure that your responses are socially 


unbiased and positive in nature.



If a question does not make any sense or is not factually coherent, 


explain why instead of answering something incorrectly. If you don't 


know the answer to a question, don't share false information.


<</SYS>>



If I punch myself in the face and it hurts, am I weak or strong?


[/INST]



In a conversation, you must add the previous interactions, including the output from Llama 2. For longer interactions, the schema looks like this:



<s>[INST] <<SYS>>


*system_prompt*


<</SYS>>



*user_msg_1*


[/INST]



*model_answer_1*


</s>


<s>[INST]



*user_msg_2*


[/INST]



*model_answer_2*


</s>


<s>[INST]



*user_msg_3*


[/INST]



etc...



Models like Llama 2 have no memory of past interactions, and the surrounding application must provide the memory by including the conversation log in the prompt of each message. But as long as the system prompt is within the 4,000 model’s token limit, it will be remembered and considered when answering.



Streaming Chat



Jina and DocArray provide a set of tools that make it possible to construct a streaming connection between an AI model and a user application with a minimum of Python code.



Welcome to Jina!


Jina lets you build multimodal AI services and pipelines that communicate via gRPC, HTTP and WebSockets, then scale them up and deploy to production. You can focus on your logic and algorithms, without worrying about the infrastructure complexity. Jina provides a smooth Pythonic experience for se…


Jina 3.20.1 Documentation


docarray.github.io


homepage of docarray


docarray.github.io



You will need to install a number of libraries in your Python environment, specifically the torch, transformers, jina, and docarray libraries, as well as some other supporting libraries if not already present:



pip install docarray jina bitsandbytes accelerate transformers



Service schemas



The first step in creating a streaming service, regardless of framework, is defining service schemas. At its most abstract, the service takes a text input and receives back a stream of tokens. In addition, we provide a parameter for setting the maximum number of tokens to respond with.



We construct our schema using DocArray, which is designed to support flexible AI-centric services:



from docarray import BaseDoc



class PromptDocument(BaseDoc):


    prompt: str
    max_tokens: int


class ModelOutputDocument(BaseDoc):


    token_id: int
    generated_text: str


Service initialization



Next, we create the token streaming class that is central to our service. This class contains and initializes both the language model and its tokenizer. In the example below, we use the 7B Llama-2-chat model — the smallest of the Llama-2-chat models — and load it using the facilities from the transformer library. It extends the Jina Executor class, which contains a number of methods for handling streams and processes.



Note that we've set the device_map parameter to auto, ensuring that the model uses a GPU if it has access to one, and load_in_8bit to True, which quantizes the model to reduce its size in memory. These settings make running our code smoothly on a free Google Colab notebook feasible.



from jina import Executor, requests


from transformers import AutoTokenizer, AutoModelForCausalLM


import torch



model_name = 'meta-llama/Llama-2-7b-chat-hf'



class TokenStreamingExecutor(Executor):


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name, device_map='auto', load_in_8bit=True
        )


Implementing the streaming endpoint



We implement the streaming endpoint as the task method of the TokenStreamingExecutor. This method processes an instance of PromptDocument and dynamically streams back a sequence of ModelOutputDocument instances.



We implement this using Python’s yield keyword in the code below, generating tokens on the fly up to the user-specified maximum number of tokens or until the END token is encountered (self.tokenizer.eos_token_id).



Each ModelOutputDocument that the stream returns encapsulates a numerical token ID and its corresponding text string.



class TokenStreamingExecutor(Executor):
    ...



    def starts_with_space(self, token_id):
        token = self.tokenizer.convert_ids_to_tokens(token_id)
        return token.startswith('▁')



    @requests(on='/stream')
    async def task(self, doc: PromptDocument, **kwargs) -> ModelOutputDocument:
        input = self.tokenizer(doc.prompt, return_tensors='pt')
        input_len = input['input_ids'].shape[1]



        for output_length in range(doc.max_tokens):
            output = self.model.generate(**input, max_new_tokens=1)
            current_token_id = output[0][-1]
            if current_token_id == self.tokenizer.eos_token_id:
                break



            current_token = self.tokenizer.decode(
                current_token_id, skip_special_tokens=True
            )
            if self.starts_with_space(current_token_id.item()) and output_length > 1:
                current_token = ' ' + current_token
            yield ModelOutputDocument(
                token_id=current_token_id,
                generated_text=current_token,
            )



            input = {
                'input_ids': output,
                'attention_mask': torch.ones(1, len(output[0])),
            }


You can learn more about streaming endpoints from the Executor class documentation on the Jina website.



Using the streaming service



Now that all the code is in place, we can run the service and start to use it. The code below deploys an instance of the TokenStreamingExecutor class and sets up a gRPC endpoint at the specified port:



from jina import Deployment



with Deployment(uses=TokenStreamingExecutor, port=12345, protocol='grpc') as dep:


    dep.block()


Once the service is running, you can send it messages and see how the model responds. The code below uses the Jina Client class to contact the service, pass it a correctly formatted prompt, receive the stream of tokens, and print them out.



import asyncio


from jina import Client



llama_prompt = PromptDocument(


    prompt="""


<s>[INST] <<SYS>>


You are a helpful, respectful, and honest assistant. Always answer as helpfully 


as possible while being safe.  Your answers should not include any harmful, 


unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure 


that your responses are socially unbiased and positive in nature.



If a question does not make any sense or is not factually coherent, explain why 


instead of answering something incorrectly. If you don't know the answer to a 


question, don't share false information.


<</SYS>>


If I punch myself in the face and it hurts, am I weak or strong? [/INST]


""",


    max_tokens=100,


async def main():


    client = Client(port=12345, protocol='grpc', asyncio=True)
    async for doc in client.stream_doc(
        on='/stream',
			  inputs=llama_prompt,
			  return_type=ModelOutputDocument,
    ):
        print(doc.generated_text, end='')


asyncio.run(main())




If you run this code, the result should look something like this:



I'm here to help you, but I must inform you that punching oneself in the face


is not a safe or healthy practice. It can cause physical harm and lead to 


injuries, including broken bones, cuts, and bruises. It is not a recommended or


acceptable way to handle emotions or stress.



Instead of resorting to harmful actions, there are many other ways to manage


emotions and cope with stress in a healthy and constructive manner. Some options


include:


1. Exercise: Physical activity can help release tension and improve mood.


2. Mindfulness: Practices such as meditation, deep breathing, or yoga can help


you focus on the present moment and manage emotions.


3. Talking to someone: Sharing your feelings with a trusted friend, family 


member, or mental health professional can provide emotional support and help
   

you find healthy ways




You can adapt this code to any prompt or extend it to support a fully two-way conversation.



Run Your Own AI Chat Service



With the release of Llama 2 and its chat-trained models, you can use Jina and DocArray to create and operate your own chat service with just a few classes and functions.



You can use a cloud service provider, for example, Jina AI Cloud,  and control the entire technology stack, never paying external API fees or worrying about your data privacy. The smallest model is small enough to run in-house on a well-resourced GPU machine, eliminating even cloud dependencies if desired.



Llama 2’s separation of system prompts from user input gives you an additional layer of control, letting you do your own prompt engineering and in-context learning and building it into the service.



The possibilities are endless.



Get Involved



To learn more, check out the websites for Jina AI and DocArray.  You can also contact us and the Jina user community via Discord.



Jina AI - Your Portal to Multimodal AI


Jina AI offers powerful multimodal AI solutions for everyday users, developers, and scalable enterprise solutions. We aim to democratize access to the limitless potential of AI-generated creativity and innovation, empowering individuals and businesses alike.


Your Portal to Multimodal AI


docarray.github.io


homepage of docarray


docarray.github.io


Categories:


Tech blog


rss_feed


Top-5 similar articles


play_arrow


GET TOP-5


Select reranker


Read more


August 26, 2024 • 13 minutes read


The What and Why of Text-Image Modality Gap in CLIP Models


You can't just use a CLIP model to retrieve text and images and sort the results by score. Why? Because of the modality gap. What is it, and where does it come from?


August 22, 2024 • 8 minutes read


Late Chunking in Long-Context Embedding Models


Chunking long documents while preserving contextual information is challenging. We introduce the "Late Chunking" that leverages long-context embedding models to generate contextual chunk embeddings for better retrieval applications.


July 31, 2024 • 17 minutes read


Rephrased Labels Improve Zero-Shot Text Classification by 30%


When using embedding models for zero-shot classification, rephrasing the class label to "This is seriously about 'LABEL'" gives higher accuracy vs. using LABEL alone. But how, and why?


OFFICES


location_on


Berlin, Germany (HQ)


Prinzessinnenstraße 19-20, 10969 Berlin, Germany


Geschäftsanschrift: Leipzigerstr. 96, 10117 Berlin, Germany


location_on


Beijing, China


Level 5, Building 6, No.48 Haidian West St. Beijing Haidian, China


location_on


Shenzhen, China


402, Floor 4, Fu'an Technology Building, Shenzhen Nanshan, China


SEARCH FOUNDATION


Embeddings


Reranker


Reader


Segmenter


Get Jina AI API key


API Status


COMPANY


About us


Contact sales


Newsroom


Intern program


Join us


open_in_new


Download logo


open_in_new


TERMS


Terms & Conditions


Privacy


Manage Cookies


email


language


English


science


Jina AI GmbH © 2020-2024.

---