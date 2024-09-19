# distilled-ai-using-large-models-to-teach-smaller-ones

## SIMPLE_CHUNKING

#### 1 chunk(s)

One major barrier to implementing AI coding is one that holds up a lot of AI work: The kinds of very large AI models that produce high-quality results are very expensive to train and run. Members of the GPT family of closed-access models are not only expensive but also remotely hosted with unclear security. Ideally, we would like to have smaller but more specialized models that can give comparable performance to the large models but run on less expensive hardware that users can keep under their own control. This article is a step in that direction, demonstrating that it is feasible, and a way to do it inexpensively. More data vs. better data: Scaling factors in AI All else being equal, we know that the performance of an AI model depends on three scaling factors: Training time. Models trained for more cycles perform better than identical models trained for fewer on the same data. Data size. Models trained with more data perform better than identical models trained with less, given the same training time. Number of parameters, i.e., the size of the model. A model with more weights (or more neurons, which is the same thing) performs better than one with fewer, given the same training data and training time. To build a model with a smaller size but comparable performance to a larger one, we should, logically, use more data and more training cycles. But all else is not always equal. Data quality is a more difficult factor to quantify than training time, data size, or model size, but it makes a significant difference to performance. Intuitively, the model should learn better to solve a particular kind of problem if it learns from the most instructive examples. The problem with improving data quality is that it can be difficult or expensive to curate enough high-quality data to make a difference. Using AI models as both teacher and student One solution is to use AI models to create training data. This has the benefit of being much cheaper than commissioning humans to create enough data or paying them to curate existing data, picking out just the most relevant examples. At first glance, this seems counter-intuitive. If the model is already good enough to create high-quality training data to learn to solve a problem, then surely it can’t use this knowledge to improve its own performance. And this is true. But when the goal is to train a smaller, less capable AI to improve its performance, and we use a much more capable AI to create the training data, it makes just as much sense as a child learning to read from a teacher who is already literate. This is especially relevant to our goal of creating a smaller model with performance comparable to larger ones. We know that a smaller model will need more examples and more training time to reach the same result as a larger one, if it can reach it at all. What a 100 billion parameter model can learn from a thousand examples of sufficient quality might take a million equally high-quality examples for a 1 billion parameter model. The cost of human construction or curation of a million items of training data is a lot more than a thousand, no matter what the problem is.

## COT_TOPIC_CHUNKING

#### 13 chunk(s)

AI models that write code A number of AI models have had some success actually writing code directly in response to problem descriptions. GitHub Copilot is available commercially, and the GPT series from OpenAI will write code for you if you ask it to, but there are also dozens of other models that have at least some coding ability. This technology has the potential to be very disruptive to the software development industry. One major barrier to implementing AI coding is one that holds up a lot of AI work: The kinds of very large AI models that produce high-quality results are very expensive to train and run. Members of the GPT family of closed-access models are not only expensive but also remotely hosted with unclear security. Ideally, we would like to have smaller but more specialized models that can give comparable performance to the large models but run on less expensive hardware that users can keep under their own control. This article is a step in that direction, demonstrating that it is feasible, and a way to do it inexpensively.

More data vs. better data: Scaling factors in AI All else being equal, we know that the performance of an AI model depends on three scaling factors: Training time. Models trained for more cycles perform better than identical models trained for fewer on the same data. Data size. Models trained with more data perform better than identical models trained with less, given the same training time. Number of parameters, i.e., the size of the model. A model with more weights (or more neurons, which is the same thing) performs better than one with fewer, given the same training data and training time. To build a model with a smaller size but comparable performance to a larger one, we should, logically, use more data and more training cycles. But all else is not always equal. Data quality is a more difficult factor to quantify than training time, data size, or model size, but it makes a significant difference to performance. Intuitively, the model should learn better to solve a particular kind of problem if it learns from the most instructive examples. The problem with improving data quality is that it can be difficult or expensive to curate enough high-quality data to make a difference.

Using AI models as both teacher and student One solution is to use AI models to create training data. This has the benefit of being much cheaper than commissioning humans to create enough data or paying them to curate existing data, picking out just the most relevant examples. At first glance, this seems counter-intuitive. If the model is already good enough to create high-quality training data to learn to solve a problem, then surely it can’t use this knowledge to improve its own performance. And this is true. But when the goal is to train a smaller, less capable AI to improve its performance, and we use a much more capable AI to create the training data, it makes just as much sense as a child learning to read from a teacher who is already literate. This is especially relevant to our goal of creating a smaller model with performance comparable to larger ones.

We decided that we would use only 42 of them in this experiment (the ones marked with a 1 in the Mixing column). For each of those 42 topics, we queried GPT 4 to give us 10 sub-topics using the prompt below: For a Python textbook give me 10 subtopics of {topic}, formatted as a Python list. Just provide the titles and give no explanation. Format the result as Python list. We then repeated this procedure to get five very fine-grained topics for each of the 420 subtopics. This yields approximately 2000 topics.

We furthermore manually constructed a list of 40 professions. For example: Economist Engineer Social Worker Game Developer The complete list of professions is also documented in the project’s GitHub repository. GitHub - jina-ai/textbook: distill chatGPT coding ability into small model (1b) distill chatGPT coding ability into small model (1b) - GitHub - jina-ai/textbook: distill chatGPT coding ability into small model (1b) GitHub jina-ai To generate code exercises, we selected two topics randomly from the list of 2000 and one profession from the list of 40 and then prompted ChatGPT 3.5 with the following: Create a code completion exercise on the intersection of {topic 1} and {topic 2}. Write it for a {profession}. The exercise must be of the style: def name(args): """Docstring explaining the exercise""" python code to solve the exercise NO CLASSES MAKE IT VERY DIFFICULT The result was snippets of code like this: def find_gene(sequence, target_gene): """ Given a DNA sequence and a target gene, this function should return the starting index of the target gene in the given sequence, using a while loop and boolean expressions. Note: The target gene is represented as a string of characters, and we assume that it only occurs once in the sequence. Args: - sequence: a string representing the DNA sequence to search in - target_gene: a string representing the target gene to find Returns: - The starting index (integer) of the target gene in the sequence, or -1 if the target gene is not found. """ index = 0 gene_len = len(target_gene) while index <= len(sequence) - gene_len: # Check if current substring matches the target gene if sequence[index:index+gene_len] == target_gene: return index index += 1 return -1 # Target gene not found in the given sequence Another example: def calculate_average_price(prices): """ Calculate the average price of a list of fashion items. Args: prices (list): A list of prices of fashion items. Returns: float: The average price of the fashion items. """ total = 0 while prices: # Slices the prices list to get the first item # and remove it from the original list price = prices.pop(0) # Complete the missing code to update the total variable # by adding the current price # Calculate the average price by dividing the total by the # number of fashion items average_price = total / len(prices) return average_price We repeated this until we had 150,000 Python functions with explanatory docstrings. We filtered the results to remove results containing non-runnable code, yielding approximately 120,000 individual training items. This formed the training corpus we used to fine-tune StarCoder 1B. 💡 The cost of data acquisition — the price we paid to query ChatGPT 3.5 150,000 times — was approximately 600 USD. You can download the synthetic data we used for training as a HuggingFace dataset.

jinaai/code_exercises · Datasets at Hugging Face We’re on a journey to advance and democratize artificial intelligence through open source and open science. Fine-tuning StarCoder 1B StarCoder 1B is a one-billion-parameter model from a family of pre-trained models designed to perform programming tasks in multiple programming languages. It was pre-trained on The Stack dataset, a collection of code items from GitHub with permissive licenses. We did full parameter fine-tuning using the synthetic dataset described above, with a batch size of 128 and a micro-batch size of 8. Our training hardware was a RunPod cloud instance with an NVIDIA A40 GPU. 💡 The fine-tuning compute cost, using a cloud-based rented GPU, was approximately 10 USD. This compares very favorably to the cost of fine-tuning OpenAI’s closed-access GPT models or the larger open-access models like Llama 2. We have made the entire weight set of our fine-tuned StarCoder 1B available as a HuggingFace model. You are free to download, use, and retrain it. jinaai/starcoder-1b-textbook · Hugging Face We’re on a journey to advance and democratize artificial intelligence through open source and open science. Evaluation To evaluate our training, we used the standard HumanEval benchmark (Chen et al. 2021). This benchmark consists of 164 human-made programming problems written in English and a set of Python unit tests to verify that a proposed solution correctly solves the problem. For example, we gave our fine-tuned model the following prompt from HumanEval: from typing import List, Optional def longest(strings: List[str]) -> Optional[str]: """ Out of list of strings, return the longest one. Return the first one in case of multiple strings of the same length. Return None in case the input list is empty. >>> longest([]) >>> longest(['a', 'b', 'c']) 'a' >>> longest(['a', 'bb', 'ccc']) 'ccc' """ The modified StarCoder 1B produced as output: from typing import List, Optional def longest(strings: List[str]) -> Optional[str]: """ Out of list of strings, return the longest one. Return the first one in case of multiple strings of the same length. Return None in case the input list is empty. >>> longest([]) >>> longest(['a', 'b', 'c']) 'a' >>> longest(['a', 'bb', 'ccc']) 'ccc' """ if not strings: return None longest_string = strings[0] for string in strings[1:]: if len(string) > len(longest_string): longest_string = string return longest_string This function passes all the unit tests for finding the longest string in a list of strings and is therefore marked as successful. Our fine-tuned StarCoder 1B is also able to handle more abstract problems that can involve world knowledge. For example, it generated the code for this function from the text docstring description. The actual number-to-letter maps for Roman numeral conversion were not provided in the prompt: def int_to_mini_roman(number): """ Given a positive integer, obtain its roman numeral equivalent as a string, and return it in lowercase. Restrictions: 1 <= num <= 1000 Examples: >>> int_to_mini_roman(19) == 'xix' >>> int_to_mini_roman(152) == 'clii' >>> int_to_mini_roman(426) == 'cdxxvi' """ roman_numerals = { 1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I' } roman_numeral = "" for value, symbol in roman_numerals.items(): while number >= value: roman_numeral += symbol number -= value return roman_numeral.lower()

Existing large language models and models specifically trained for programming have a range of scores on HumanEval that, at first glance, are broadly proportionate to model size, training data size, and the amount of money invested in developing it. For example, GPT-4 with no fine-tuning or special prompt engineering currently scores 67.0%, according to the latest report. That is to say, it writes code that correctly solves the problem about two-thirds of the time. GPT 3.5 without fine-tuning — the model we used to generate our training data — scores 48.1% on the same benchmark. The highest current performer is a prompt-engineered GPT-4 that scores 91%. Among the open-access models, Llama 2 without fine-tuning currently scores 29.9%, while StarCoder 1B — the model we fine-tuned — has a zero-shot performance (i.e., unmodified, out-of-the-box) of 15.2% according to its model card on HuggingFace. Our fine-tuning improved StarCoder 1B performance to 27.0% on HumanEval, nearly doubling the number of problems it solved correctly and placing its performance above many larger models. Given that the net inputs were so small — well under 1000 USD in compute costs, a few hours of engineer time, and no human data oversight at all — this is a very large improvement on a very small model.

Summing up AI models are a little like children: They can sometimes learn a lot from a good teacher.

We tested the hypothesis that we could distill the task-specific knowledge of a large, complex AI model into a smaller and simpler one by using the larger one to generate training examples for the smaller one. Specifically, writing Python functions to solve a verbal problem description.

Given that GPT 3.5 scores just under 50% on the HumanEval benchmark, it would be very unreasonable for us to expect our fine-tuned one-billion parameter model to equal, much less beat, that score using this training method. It’s not so easy for the student to surpass the teacher. Nonetheless, we improved the performance of the StarCoder 1B from about a third as accurate as GPT 3.5 to about half as accurate. We might wonder, given that the highest-performing models currently score around 90%, if the added cost of using an even larger and more expensive model to create training examples might improve StarCoder 1B’s performance even more.

We also know that both pre-training and model size factor into performance both before and after fine-tuning, so we might get still better results using other foundation models. This kind of AI-led training has much lower costs than conventional methods, and that opens up a large space for future experimentation.

Getting involved You can download the code for thisproject from the project’s GitHub repository, and download the training data from its HuggingFace page. The trained model is also available from its model page on HugglingFace. GitHub - jina-ai/textbook: distill chatGPT coding ability into small model (1b) distill chatGPT coding ability into small model (1b) - GitHub - jina-ai/textbook: distill chatGPT coding ability into small model (1b) GitHub jina-ai jinaai/code_exercises · Datasets at Hugging Face We’re on a journey to advance and democratize artificial intelligence through open source and open science. jinaai/starcoder-1b-textbook · Hugging Face We’re on a journey to advance and democratize artificial intelligence through open source and open science. Categories: Tech blog rss_feed Top-5 similar articles play_arrow GET TOP-5 Select reranker Read more

OFFICES location_on Berlin, Germany (HQ) Prinzessinnenstraße 19-20, 10969 Berlin, Germany Geschäftsanschrift: Leipzigerstr. 96, 10117 Berlin, Germany location_on Beijing, China Level 5, Building 6, No.48 Haidian West St. Beijing Haidian, China location_on Shenzhen, China 402, Floor 4, Fu'an Technology Building, Shenzhen Nanshan, China SEARCH FOUNDATION Embeddings Reranker Reader Segmenter Get Jina AI API key API Status COMPANY About us Contact sales Newsroom Intern program Join us open_in_new Download logo open_in_new TERMS Terms & Conditions Privacy Manage Cookies email language English science Jina AI GmbH © 2020-2024.

## SUMMARY_CHUNKING

#### 8 chunk(s)

The cost of data acquisition — the price we paid to query ChatGPT 3.5 150,000 times — was approximately 600 USD. You can download the synthetic data we used for training as a HuggingFace dataset. jinaai/code_exercises · Datasets at Hugging Face We’re on a journey to advance and democratize artificial intelligence through open source and open science. Fine-tuning StarCoder 1B

StarCoder 1B is a one-billion-parameter model from a family of pre-trained models designed to perform programming tasks in multiple programming languages. It was pre-trained on The Stack dataset, a collection of code items from GitHub with permissive licenses. We did full parameter fine-tuning using the synthetic dataset described above, with a batch size of 128 and a micro-batch size of 8. Our training hardware was a RunPod cloud instance with an NVIDIA A40 GPU. 💡 The fine-tuning compute cost, using a cloud-based rented GPU, was approximately 10 USD. This compares very favorably to the cost of fine-tuning OpenAI’s closed-access GPT models or the larger open-access models like Llama 2. We have made the entire weight set of our fine-tuned StarCoder 1B available as a HuggingFace model. You are free to download, use, and retrain it. jinaai/starcoder-1b-textbook · Hugging Face We’re on a journey to advance and democratize artificial intelligence through open source and open science.

Evaluation To evaluate our training, we used the standard HumanEval benchmark (Chen et al. 2021). This benchmark consists of 164 human-made programming problems written in English and a set of Python unit tests to verify that a proposed solution correctly solves the problem. For example, we gave our fine-tuned model the following prompt from HumanEval: from typing import List, Optional def longest(strings: List[str]) -> Optional[str]: """ Out of list of strings, return the longest one. Return the first one in case of multiple strings of the same length. Return None in case the input list is empty. >>> longest([]) >>> longest(['a', 'b', 'c']) 'a' >>> longest(['a', 'bb', 'ccc']) 'ccc' """ The modified StarCoder 1B produced as output: from typing import List, Optional def longest(strings: List[str]) -> Optional[str]: """ Out of list of strings, return the longest one. Return the first one in case of multiple strings of the same length. Return None in case the input list is empty. >>> longest([]) >>> longest(['a', 'b', 'c']) 'a' >>> longest(['a', 'bb', 'ccc']) 'ccc' """ if not strings: return None longest_string = strings[0] for string in strings[1:]: if len(string) > len(longest_string): longest_string = string return longest_string This function passes all the unit tests for finding the longest string in a list of strings and is therefore marked as successful. Our fine-tuned StarCoder 1B is also able to handle more abstract problems that can involve world knowledge. For example, it generated the code for this function from the text docstring description. The actual number-to-letter maps for Roman numeral conversion were not provided in the prompt: def int_to_mini_roman(number): """ Given a positive integer, obtain its roman numeral equivalent as a string, and return it in lowercase. Restrictions: 1 <= num <= 1000 Examples: >>> int_to_mini_roman(19) == 'xix' >>> int_to_mini_roman(152) == 'clii' >>> int_to_mini_roman(426) == 'cdxxvi' """ roman_numerals = { 1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I' } roman_numeral = "" for value, symbol in roman_numerals.items(): while number >= value: roman_numeral += symbol number -= value return roman_numeral.lower() Existing large language models and models specifically trained for programming have a range of scores on HumanEval that, at first glance, are broadly proportionate to model size, training data size, and the amount of money invested in developing it. For example, GPT-4 with no fine-tuning or special prompt engineering currently scores 67.0%, according to the latest report. That is to say, it writes code that correctly solves the problem about two-thirds of the time. GPT 3.5 without fine-tuning — the model we used to generate our training data — scores 48.1% on the same benchmark. The highest current performer is a prompt-engineered GPT-4 that scores 91%. Among the open-access models, Llama 2 without fine-tuning currently scores 29.9%, while StarCoder 1B — the model we fine-tuned — has a zero-shot performance (i.e., unmodified, out-of-the-box) of 15.2% according to its model card on HuggingFace. Our fine-tuning improved StarCoder 1B performance to 27.0% on HumanEval, nearly doubling the number of problems it solved correctly and placing its performance above many larger models. Given that the net inputs were so small — well under 1000 USD in compute costs, a few hours of engineer time, and no human data oversight at all — this is a very large improvement on a very small model.

Summing up AI models are a little like children: They can sometimes learn a lot from a good teacher. We tested the hypothesis that we could distill the task-specific knowledge of a large, complex AI model into a smaller and simpler one by using the larger one to generate training examples for the smaller one. Specifically, writing Python functions to solve a verbal problem description. Given that GPT 3.5 scores just under 50% on the HumanEval benchmark, it would be very unreasonable for us to expect our fine-tuned one-billion parameter model to equal, much less beat, that score using this training method. It’s not so easy for the student to surpass the teacher. Nonetheless, we improved the performance of the StarCoder 1B from about a third as accurate as GPT 3.5 to about half as accurate. We might wonder, given that the highest-performing models currently score around 90%, if the added cost of using an even larger and more expensive model to create training examples might improve StarCoder 1B’s performance even more. We also know that both pre-training and model size factor into performance both before and after fine-tuning, so we might get still better results using other foundation models. This kind of AI-led training has much lower costs than conventional methods, and that opens up a large space for future experimentation.

Getting involved You can download the code for this project from the project’s GitHub repository, and download the training data from its HuggingFace page. The trained model is also available from its model page on HugglingFace. GitHub - jina-ai/textbook: distill chatGPT coding ability into small model (1b) distill chatGPT coding ability into small model (1b) - GitHub - jina-ai/textbook: distill chatGPT coding ability into small model (1b) GitHub jina-ai jinaai/code_exercises · Datasets at Hugging Face We’re on a journey to advance and democratize artificial intelligence through open source and open science. jinaai/starcoder-1b-textbook · Hugging Face We’re on a journey to advance and democratize artificial intelligence through open source and open science. Categories: Tech blog rss_feed Top-5 similar articles play_arrow GET TOP-5 Select reranker Read more August 26, 2024 • 13 minutes read The What and Why of Text-Image Modality Gap in CLIP Models

You can't just use a CLIP model to retrieve text and images and sort the results by score. Why? Because of the modality gap. What is it, and where does it come from? August 22, 2024 • 8 minutes read Late Chunking in Long-Context Embedding Models Chunking long documents while preserving contextual information is challenging. We introduce the "Late Chunking" that leverages long-context embedding models to generate contextual chunk embeddings for better retrieval applications.

July 31, 2024 • 17 minutes read Rephrased Labels Improve Zero-Shot Text Classification by 30% When using embedding models for zero-shot classification, rephrasing the class label to "This is seriously about 'LABEL'" gives higher accuracy vs. using LABEL alone. But how, and why?

SEARCH FOUNDATION Embeddings Reranker Reader Segmenter Get Jina AI API key API Status COMPANY About us Contact sales Newsroom Intern program Join us open_in_new Download logo open_in_new TERMS Terms & Conditions Privacy Manage Cookies email language English science Jina AI GmbH © 2020-2024.

## JINA-SEGMENTER-API

#### 182 chunk(s)

search


notifications


NEWS


PRODUCTS


COMPANY


Tech blog


September 07, 2023


Distilled AI: Using Large Models to Teach Smaller Ones


Better AI with smaller models and cheaper data costs! But only if you use AI to train AI.


Alaeddine Abdessalem, Sebastian Weisshaar, Sami Jaghouar, Scott Martens • 11 minutes read



A lot of public attention has gone into generative large language models and AI art because they produce striking results, even in the eyes of people who don’t know anything about AI. However, one area has garnered a lot of research and commercial interest without attracting as much attention from the general public: Using AI models to write computer code.



In this article, we'll show how we fine-tuned a one-billion-parameter AI model – StarCoder 1B, a relatively small model – to improve its Python programming skills, raising its score on the HumanEval benchmark from 15.2% to 27.0%. We did this by distilling the knowledge present in GPT 3.5, a 180-billion-parameter large language model that itself scores 48.1% on the same benchmark, into the much smaller model. Our method was to prompt GPT 3.5 into creating a roughly 120-thousand item Python programming dataset, which we then used to fine-tune the StarCoder model.



AI models that write code



A number of AI models have had some success actually writing code directly in response to problem descriptions. GitHub Copilot is available commercially, and the GPT series from OpenAI will write code for you if you ask it to, but there are also dozens of other models that have at least some coding ability.



This technology has the potential to be very disruptive to the software development industry.



One major barrier to implementing AI coding is one that holds up a lot of AI work: The kinds of very large AI models that produce high-quality results are very expensive to train and run. Members of the GPT family of closed-access models are not only expensive but also remotely hosted with unclear security. Ideally, we would like to have smaller but more specialized models that can give comparable performance to the large models but run on less expensive hardware that users can keep under their own control.



This article is a step in that direction, demonstrating that it is feasible, and a way to do it inexpensively.



More data vs. better data: Scaling factors in AI



All else being equal, we know that the performance of an AI model depends on three scaling factors:



Training time. Models trained for more cycles perform better than identical models trained for fewer on the same data.


Data size. Models trained with more data perform better than identical models trained with less, given the same training time.


Number of parameters, i.e., the size of the model. A model with more weights (or more neurons, which is the same thing) performs better than one with fewer, given the same training data and training time.



To build a model with a smaller size but comparable performance to a larger one, we should, logically, use more data and more training cycles. But all else is not always equal. Data quality is a more difficult factor to quantify than training time, data size, or model size, but it makes a significant difference to performance. Intuitively, the model should learn better to solve a particular kind of problem if it learns from the most instructive examples. The problem with improving data quality is that it can be difficult or expensive to curate enough high-quality data to make a difference.



Using AI models as both teacher and student



One solution is to use AI models to create training data. This has the benefit of being much cheaper than commissioning humans to create enough data or paying them to curate existing data, picking out just the most relevant examples.



At first glance, this seems counter-intuitive. If the model is already good enough to create high-quality training data to learn to solve a problem, then surely it can’t use this knowledge to improve its own performance. And this is true. But when the goal is to train a smaller, less capable AI to improve its performance, and we use a much more capable AI to create the training data, it makes just as much sense as a child learning to read from a teacher who is already literate.



This is especially relevant to our goal of creating a smaller model with performance comparable to larger ones. We know that a smaller model will need more examples and more training time to reach the same result as a larger one, if it can reach it at all. What a 100 billion parameter model can learn from a thousand examples of sufficient quality might take a million equally high-quality examples for a 1 billion parameter model. The cost of human construction or curation of a million items of training data is a lot more than a thousand, no matter what the problem is.



To address this problem, we took inspiration from the recent paper Textbooks Are All You Need (Gunasekar et al. 2023), which introduces the phi-1 family of models, which write Python code after being trained on a mixture of human and synthetic data. While they started with completely untrained models, we took an existing open access model — the one billion parameter StarCoder 1B model (Li et al. 2023) that has already been trained to write code in 86 languages – and then fine-tuned it exclusively with Python code examples created by ChatGPT 3.5.



Creating the data



We constructed roughly 120,000 training exercises using ChatGPT 3.5.



We were aware that one major issue in using model-synthesized data is ensuring sufficient diversity. To address this problem, we first decided on 60 broad topic labels in Python programming. For example:



Python Basic Operators


Control Structures in Python


Functions in Python


Python Lambda Functions



The complete list of topics is documented in the project’s GitHub repository.



GitHub - jina-ai/textbook: distill chatGPT coding ability into small model (1b)


distill chatGPT coding ability into small model (1b) - GitHub - jina-ai/textbook: distill chatGPT coding ability into small model (1b)


GitHub


jina-ai



We decided that we would use only 42 of them in this experiment (the ones marked with a 1 in the Mixing column). For each of those 42 topics, we queried GPT 4 to give us 10 sub-topics using the prompt below:



For a Python textbook give me 10 subtopics of {topic}, formatted as a Python list. 


Just provide the titles and give no explanation.


Format the result as Python list.




We then repeated this procedure to get five very fine-grained topics for each of the 420 subtopics. This yields approximately 2000 topics.



We furthermore manually constructed a list of 40 professions. For example:



Economist


Engineer


Social Worker


Game Developer



The complete list of professions is also documented in the project’s GitHub repository.



GitHub - jina-ai/textbook: distill chatGPT coding ability into small model (1b)


distill chatGPT coding ability into small model (1b) - GitHub - jina-ai/textbook: distill chatGPT coding ability into small model (1b)


GitHub


jina-ai



To generate code exercises, we selected two topics randomly from the list of 2000 and one profession from the list of 40 and then prompted ChatGPT 3.5 with the following:



Create a code completion exercise on the intersection of {topic 1} and {topic 2}.


Write it for a {profession}.



The exercise must be of the style: 



def name(args): 


	"""Docstring explaining the exercise"""
    
    python code to solve the exercise


NO CLASSES


MAKE IT VERY DIFFICULT



The result was snippets of code like this:



def find_gene(sequence, target_gene):


	"""
	Given a DNA sequence and a target gene, this function should
	return the starting index of the target gene in the given 
    sequence, using a while loop and boolean expressions.
	
	Note: The target gene is represented as a string of characters, 
    and we assume that it only occurs once in the sequence.
	
	Args:
	- sequence: a string representing the DNA sequence to search in
	- target_gene: a string representing the target gene to find
	
	Returns:
	- The starting index (integer) of the target gene in the
      sequence, or -1 if the target gene is not found.
	"""
	
	index = 0
	gene_len = len(target_gene)
	
	while index <= len(sequence) - gene_len:


	    
	    # Check if current substring matches the target gene
	    if sequence[index:index+gene_len] == target_gene:
	        return index
	    
	    index += 1
	
	return -1  # Target gene not found in the given sequence


Another example:



def calculate_average_price(prices):


    """
    Calculate the average price of a list of fashion items.



    Args:
    prices (list): A list of prices of fashion items.



    Returns:
    float: The average price of the fashion items.
    """



    total = 0



    while prices:
        # Slices the prices list to get the first item 
        # and remove it from the original list
        price = prices.pop(0)



        # Complete the missing code to update the total variable 
        # by adding the current price 
        
    
    # Calculate the average price by dividing the total by the 
    # number of fashion items
    average_price = total / len(prices)



    return average_price


We repeated this until we had 150,000 Python functions with explanatory docstrings. We filtered the results to remove results containing non-runnable code, yielding approximately 120,000 individual training items. This formed the training corpus we used to fine-tune StarCoder 1B.



The cost of data acquisition — the price we paid to query ChatGPT 3.5 150,000 times — was approximately 600 USD.



You can download the synthetic data we used for training as a HuggingFace dataset.



jinaai/code_exercises · Datasets at Hugging Face


We’re on a journey to advance and democratize artificial intelligence through open source and open science.


Fine-tuning StarCoder 1B



StarCoder 1B is a one-billion-parameter model from a family of pre-trained models designed to perform programming tasks in multiple programming languages. It was pre-trained on The Stack dataset, a collection of code items from GitHub with permissive licenses.



We did full parameter fine-tuning using the synthetic dataset described above, with a batch size of 128 and a micro-batch size of 8. Our training hardware was a RunPod cloud instance with an NVIDIA A40 GPU.



The fine-tuning compute cost, using a cloud-based rented GPU, was approximately 10 USD. This compares very favorably to the cost of fine-tuning OpenAI’s closed-access GPT models or the larger open-access models like Llama 2.



We have made the entire weight set of our fine-tuned StarCoder 1B available as a HuggingFace model. You are free to download, use, and retrain it.



jinaai/starcoder-1b-textbook · Hugging Face


We’re on a journey to advance and democratize artificial intelligence through open source and open science.


Evaluation



To evaluate our training, we used the standard HumanEval benchmark (Chen et al. 2021). This benchmark consists of 164 human-made programming problems written in English and a set of Python unit tests to verify that a proposed solution correctly solves the problem.



For example, we gave our fine-tuned model the following prompt from HumanEval:



from typing import List, Optional



def longest(strings: List[str]) -> Optional[str]:


    """
    Out of list of strings, return the longest one. Return the first one 
    in case of multiple strings of the same length. Return None in case 
    the input list is empty.
    
    >>> longest([])



    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """


The modified StarCoder 1B produced as output:



from typing import List, Optional



def longest(strings: List[str]) -> Optional[str]:


    """
    Out of list of strings, return the longest one. Return the first one 
    in case of multiple strings of the same length. Return None in case 
    the input list is empty.
    
    >>> longest([])



    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    
    if not strings:
        return None



    longest_string = strings[0]
    for string in strings[1:]:
        if len(string) > len(longest_string):
            longest_string = string



    return longest_string


This function passes all the unit tests for finding the longest string in a list of strings and is therefore marked as successful.



Our fine-tuned StarCoder 1B is also able to handle more abstract problems that can involve world knowledge. For example, it generated the code for this function from the text docstring description. The actual number-to-letter maps for Roman numeral conversion were not provided in the prompt:




def int_to_mini_roman(number):


    """
    Given a positive integer, obtain its roman numeral equivalent as
    a string, and return it in lowercase.
    Restrictions: 1 <= num <= 1000



    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """



    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }



    roman_numeral = ""
    for value, symbol in roman_numerals.items():
        while number >= value:
            roman_numeral += symbol
            number -= value



    return roman_numeral.lower()


Existing large language models and models specifically trained for programming have a range of scores on HumanEval that, at first glance, are broadly proportionate to model size, training data size, and the amount of money invested in developing it. For example, GPT-4 with no fine-tuning or special prompt engineering currently scores 67.0%, according to the latest report. That is to say, it writes code that correctly solves the problem about two-thirds of the time.



GPT 3.5 without fine-tuning — the model we used to generate our training data — scores 48.1% on the same benchmark. The highest current performer is a prompt-engineered GPT-4 that scores 91%. Among the open-access models, Llama 2 without fine-tuning currently scores 29.9%, while StarCoder 1B — the model we fine-tuned — has a zero-shot performance (i.e., unmodified, out-of-the-box) of 15.2% according to its model card on HuggingFace.



Our fine-tuning improved StarCoder 1B performance to 27.0% on HumanEval, nearly doubling the number of problems it solved correctly and placing its performance above many larger models.



Given that the net inputs were so small — well under 1000 USD in compute costs, a few hours of engineer time, and no human data oversight at all — this is a very large improvement on a very small model.



Summing up



AI models are a little like children: They can sometimes learn a lot from a good teacher.



We tested the hypothesis that we could distill the task-specific knowledge of a large, complex AI model into a smaller and simpler one by using the larger one to generate training examples for the smaller one. Specifically, writing Python functions to solve a verbal problem description.



Given that GPT 3.5 scores just under 50% on the HumanEval benchmark, it would be very unreasonable for us to expect our fine-tuned one-billion parameter model to equal, much less beat, that score using this training method. It’s not so easy for the student to surpass the teacher. Nonetheless, we improved the performance of the StarCoder 1B from about a third as accurate as GPT 3.5 to about half as accurate.



We might wonder, given that the highest-performing models currently score around 90%, if the added cost of using an even larger and more expensive model to create training examples might improve StarCoder 1B’s performance even more. We also know that both pre-training and model size factor into performance both before and after fine-tuning, so we might get still better results using other foundation models. This kind of AI-led training has much lower costs than conventional methods, and that opens up a large space for future experimentation.



Getting involved



You can download the code for this project from the project’s GitHub repository, and download the training data from its HuggingFace page. The trained model is also available from its model page on HugglingFace.



GitHub - jina-ai/textbook: distill chatGPT coding ability into small model (1b)


distill chatGPT coding ability into small model (1b) - GitHub - jina-ai/textbook: distill chatGPT coding ability into small model (1b)


GitHub


jina-ai


jinaai/code_exercises · Datasets at Hugging Face


We’re on a journey to advance and democratize artificial intelligence through open source and open science.


jinaai/starcoder-1b-textbook · Hugging Face


We’re on a journey to advance and democratize artificial intelligence through open source and open science.


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