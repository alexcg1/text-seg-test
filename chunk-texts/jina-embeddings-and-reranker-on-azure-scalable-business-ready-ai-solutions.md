# jina-embeddings-and-reranker-on-azure-scalable-business-ready-ai-solutions

## SIMPLE_CHUNKING

#### 6 chunk(s)

Maximizing Search Relevance and RAG Accuracy with Jina Reranker Boost your search and RAG accuracy with Jina Reranker. Our new model improves the accuracy and relevance by 20% over simple vector search. Try it now for free!

In this tutorial, we'll create a search applicationfor music. We want to search not with the exact title of the song, but with an ambiguous query that really tests the quality of our search foundation models. To do that, the first step is to set up everything on Azure. Sign up for Azure Make sure you have an Azure account subscription with a valid payment method. You can sign up for an account on the Azure home page if you don't already have one. Deploying Jina models on Azure On the Azure Marketplace, you can find all of Jina AI's embedding and reranker models by searching for "jina". Choose the one from there that best suits your needs. In the Basics tab of the deployment setup, you will need to provide some details about your deployment. By default, the configuration is set to use four CPU cores and 8 GB of memory. Depending on your specific requirements, you may adjust these settings to better suit your application's needs. This will start the deployment. It may take several minutes. After this, you should see the following screen: Your models are now deployed and ready to use.

Start Jina Embeddings v2 and Reranker Endpoints First, deploy the embedding and reranker endpoints in the Azure portal. You will need to decide what region to use and assign one DNS prefix to the embedding service and another to the reranker service. Then, store that information in the variables embeddings_url and reranker_url in the code below. The functionsjina_embed and jina_rerank generate text embeddings and perform rerankings by making requests to an API hosted on Azure. import json import requests embeddings_url = "http://<Your DNS prefix>.<Your region>.azurecontainer.io:8080/invocations" reranker_url = "http://<Your DNS prefix>.<Your region>.azurecontainer.io:8080/invocations" def jina_embed(text): headers = {"Content-Type": "application/json"} json_data = {"data": [{"text": text}]} response = requests.post(embeddings_url, headers=headers, data=json.dumps(json_data)) return response.json()["data"][0]["embedding"] def jina_rerank(query, search_results): headers = {"Content-Type": "application/json"} json_data = { "data": { "documents": [ {"text": search_result[0]} for search_result in search_results ], "query": query, "top_n": 3, } } response = requests.post(reranker_url, headers=headers, data=json.dumps(json_data)) return response.json()["data"][0]["results"]

Load the Dataset This data was collected for AI model training and therefore splits the data into training and test datasets. For simplicity, we will only use the training data in this tutorial. The code below converts the training data into a pandas DataFrame: ds = dataset['train'] input_df = ds.dataset.to_pandas() Generate Embeddings and Make an Index in FAISS This function processes text data and extracts features in the form of embeddings. This will take some time. import numpy as np from tqdm import tqdm tqdm.pandas() def generate_embeddings(input_df): all_embeddings = [] for t in input_df.text: review_embeddings = [] all_embeddings.append(np.array(jina_embed(t))) input_df["embeddings"] = all_embeddings return input_df enhanced_dataframe = generate_embeddings(input_df) This code iterates over each entry in the text column of the DataFrame and calls jina_embed() to get an embedding. We store the embeddings as NumPy arrays in the list all_embeddings. It then adds them to a new column in the DataFrame called embeddings. We can visualize what we just did by printing the value of enhanced_dataframe: The last column contains the embeddings in a readable form. Now we need to create a FAISS (Facebook AI Similarity Search) index to store and search through the embeddings: import faiss dim = 768 # dimension of Jina v2 embeddings index_with_ids = faiss.IndexIDMap(faiss.IndexFlatIP(dim)) for idx, row in enhanced_dataframe.iterrows(): embeddings = row["embeddings"] normalized_embedding = np.ascontiguousarray( np.array(embeddings, dtype="float32").reshape(1, -1) ) faiss.normalize_L2(normalized_embedding) index_with_ids.add_with_ids(normalized_embedding, idx)

This code also normalizes the embedding vectors to simplify and speed up searching. Retrieve Matches for Query The function find_similar_texts searches the index you just created for the closest matches: def find_similar_texts(query, n=20): query_embedding = jina_embed(query) query_embedding = np.ascontiguousarray( np.array(query_embedding, dtype="float32").reshape(1, -1) ) faiss.normalize_L2(query_embedding) similarities, indices = index_with_ids.search(query_embedding, n) results = [] for i in range(n): similarity = similarities[0][i] index_id = indices[0][i] results.append((enhanced_dataframe.loc[index_id, "text"], similarity)) return results Rerank to Get Most Relevant Matches After retrieving results from FAISS index, we will send the set of results to jina_rerank function to assign all answers a relevance score, and return a sorted list of results by relevance. Let's use a query that needs a lot of semantic understanding to test our solution: query = "What are some jazz songs that reached the top of the music charts in 1960s?" search_results = find_similar_texts(query) most_relevant_results = jina_rerank(query, search_results) pprint.pprint(most_relevant_results) Here are the most relevant results: [{'id': 'c26a67d979cb73474e9f80221b14b5c9', 'index': 0, 'document': {'id': 'd2183fd857661fbf9ca60a22e91888a0', 'text': 'An instrumental version by Heywood and Hugo Winterhalter reached No. 2 on the Billboard Hot 100 chart and No. 7 on the R&B chart in 1956. A version sung by Andy Williams was also popular that year. The tune has been covered by a number of jazz performers beginning in the 1960s.'}, 'relevance_score': 0.7132052183151245, 'usage': {'id': '037b9d22a5f13b68258ab51cbab1a7ad', 'total_tokens': 64}}, {'id': 'a9205e69a4e76ca49717b8497a2798bf', 'index': 4, 'document': {'id': '25e78e92da17f01df111a7ed2716b057', 'text': '"Take Five" is a jazz standard composed by Paul Desmond and originally recorded by the Dave Brubeck Quartet for their album Time Out on July 1, 1959. Two years later it became a surprise hit and the biggest-selling jazz single ever. The single was inducted into the Grammy Hall of Fame in 1996. It became the first jazz single to surpass a million in sales.'}, 'relevance_score': 0.204337015748024, 'usage': {'id': '6d55f32b339b83350ffb9489fbf31f5d', 'total_tokens': 80}}, {'id': '50a610653b307f6f1ae6ec796b72ca83', 'index': 9, 'document': {'id': '70278633234c32775b1a28b364f6783a', 'text': 'Oh, You Crazy Moon is a jazz standard by Jimmy Van Heusen, with lyrics by Johnny Burke. It was recorded by Mel Torme in 1960 and Frank Sinatra in 1965.'}, 'relevance_score': 0.16270869970321655, 'usage': {'id': '79eabc46bf3c659d3ad3e4d4d7e7a8f2', 'total_tokens': 40}}] And that's it. Try it out yourself with different queries, and see what results you get.

Jina Embeddings and Rerankers: Enterprise-Ready AIon Azure Jina AI is focused on bringing state-of-the-art AI to enterprises for real applications that businesses need. Placing our models on Azure Marketplace removes barriers to adding AI to your business processes, making integration simple and billing you as part of your existing Azure plan. We value input from everyone using or considering using Jina Embeddings and Jina Reranker. Contact us via our website or join our Discord channel to share feedback and stay up-to-date with Jina AI's rapidly developing offerings. We believe in an inclusive AI ecosystem and would love to talk with you about your use cases. Jina AI - Your Search Foundation, Supercharged. Jina AI offers best-in-class embeddings, reranker and prompt optimizer, enabling advanced multimodal AI. Your Search Foundation, Supercharged. Join the Jina AI Discord Server! Check out the Jina AI community on Discord - hang out with 4981 other members and enjoy free voice and text chat. Discord Categories: Tech blog rss_feed Top-5 similar articles play_arrow GET TOP-5 Select reranker Read more August 26, 2024 • 13 minutes read The What and Why of Text-Image Modality Gap in CLIP Models You can't just use a CLIP model to retrieve text and images and sort the results by score. Why? Because of the modality gap. What is it, and where does it come from? August 22, 2024 • 8 minutes read Late Chunking in Long-Context Embedding Models Chunking long documents while preserving contextual information is challenging. We introduce the "Late Chunking" that leverages long-context embedding models to generate contextual chunk embeddings for better retrieval applications. July 31, 2024 • 17 minutes read Rephrased Labels Improve Zero-Shot Text Classification by 30% When using embedding models for zero-shot classification, rephrasing the class label to "This is seriously about 'LABEL'" gives higher accuracy vs. using LABEL alone. But how, and why? OFFICES location_on Berlin, Germany (HQ) Prinzessinnenstraße 19-20, 10969 Berlin, Germany Geschäftsanschrift: Leipzigerstr. 96, 10117 Berlin, Germany location_on Beijing, China Level 5, Building 6, No.48 Haidian West St. Beijing Haidian, China location_on Shenzhen, China 402, Floor 4, Fu'an Technology Building, Shenzhen Nanshan, China SEARCH FOUNDATION Embeddings Reranker Reader Segmenter Get Jina AI API key API Status COMPANY About us Contact sales Newsroom Intern program Join us open_in_new Download logo open_in_new TERMS Terms & Conditions Privacy Manage Cookies email language English science Jina AI GmbH © 2020-2024.

## COT_TOPIC_CHUNKING

#### 4 chunk(s)

Jina Embeddings and Rerankers are now available on Azure Marketplace. Enterprises that prioritize privacy and security can now easily integrate Jina AI's state-of-the-art models right in their existing Azure ecosystem. Susana Guzmán • 7 minutes read Jina Embeddings and Rerankers are now available on Azure Marketplace. This integration is important for companies where data security and operational efficiency are top priorities. Jina AI Launches World’s First Open-Source 8K Text Embedding, Rivaling OpenAI Jina AI introduces jina-embeddings-v2, the world’s first open-source model boasting an 8K context length. Matching the prowess of OpenAI’s proprietary models, this innovation is now publicly accessible on Huggingface, signaling a significant milestone in the landscape of text embeddings. Maximizing Search Relevance and RAG Accuracy with Jina Reranker Boost your search and RAG accuracy with Jina Reranker. Our new model improves the accuracy and relevance by 20% over simple vector search. Try it now for free! We have seven models available: Jina Embeddings v2 Base - code Jina Embeddings v2 Base - de Jina Embeddings v2 Base - zh Jina Embeddings v2 Base - es Jina Embeddings v2 Base - en Jina Reranker v1 Base - en Jina Reranker v1 Turbo - en Jina Reranker v1 Tiny - en Jina ColBERT v1 - en Built for Privacy and Performance Making sure your data is secure is our top priority. Our partnership with Azure allows us to offer AI solutions that meet the demand for data privacy and efficiency. Azure's unparalleled privacy standards ensure the strictest protection of your data, making it a trusted platform for healthcare, finance, and other sectors requiring critical data protection. If you're an existing customer of Azure, then you can get all the benefits of Jina AI's state-of-the-art Embedding and Reranker models with your existing subscription. Seamless Integration and High Scalability Deploying on Azure not only ensures privacy but also gives you seamless integration with your existing Azure services. This provides a smooth transition and allows you to scale your AI deployments so you can meet fluctuating demands without compromising on performance. Get Started with Azure

In this tutorial, we'll create a search application for music. We want to search not with the exact title of the song, but with an ambiguous query that really tests the quality of our search foundation models. To do that, the first step is to set up everything on Azure. Sign up for Azure Make sure you have an Azure account subscription with a valid payment method. You can sign up for an account on the Azure home page if you don't already have one. Deploying Jina models on Azure On the Azure Marketplace, you can find all of Jina AI's embedding and reranker models by searching for "jina". Choose the one from there that best suits your needs. In the Basics tab of the deployment setup, you will need to provide some details about your deployment. By default, the configuration is set to use four CPU cores and 8 GB of memory. Depending on your specific requirements, you may adjust these settings to better suit your application's needs. This will start the deployment. It may take several minutes. After this, you should see the following screen: Your models are now deployed and ready to use. Tutorial: Search for Songs

After retrieving results from FAISS index, we will send the set of results to jina_rerank function to assign all answers a relevance score, and return a sorted list of results by relevance. Let's use a query that needs a lot of semantic understanding to test our solution: query = "What are some jazz songs that reached the top of the music charts in 1960s?" search_results = find_similar_texts(query) most_relevant_results = jina_rerank(query, search_results) pprint.pprint(most_relevant_results) Here are the most relevant results: [{'id': 'c26a67d979cb73474e9f80221b14b5c9', 'index': 0, 'document': {'id': 'd2183fd857661fbf9ca60a22e91888a0', 'text': 'An instrumental version by Heywood and Hugo Winterhalter reached No. 2 on the Billboard Hot 100 chart and No. 7 on the R&B chart in 1956. A version sung by Andy Williams was also popular that year. The tune has been covered by a number of jazz performers beginning in the 1960s.'}, 'relevance_score': 0.7132052183151245, 'usage': {'id': '037b9d22a5f13b68258ab51cbab1a7ad', 'total_tokens': 64}}, {'id': 'a9205e69a4e76ca49717b8497a2798bf', 'index': 4, 'document': {'id': '25e78e92da17f01df111a7ed2716b057', 'text': '"Take Five" is a jazz standard composed by Paul Desmond and originally recorded by the Dave Brubeck Quartet for their album Time Out on July 1, 1959. Two years later it became a surprise hit and the biggest-selling jazz single ever. The single was inducted into the Grammy Hall of Fame in 1996. It became the first jazz single to surpass a million in sales.'}, 'relevance_score': 0.204337015748024, 'usage': {'id': '6d55f32b339b83350ffb9489fbf31f5d', 'total_tokens': 80}}, {'id': '50a610653b307f6f1ae6ec796b72ca83', 'index': 9, 'document': {'id': '70278633234c32775b1a28b364f6783a', 'text': 'Oh, You Crazy Moon is a jazz standard by Jimmy Van Heusen, with lyrics by Johnny Burke. It was recorded by Mel Torme in 1960 and Frank Sinatra in 1965.'}, 'relevance_score': 0.16270869970321655, 'usage': {'id': '79eabc46bf3c659d3ad3e4d4d7e7a8f2', 'total_tokens': 40}}] And that's it. Try it out yourself with different queries, and see what results you get.

Jina AI is focused on bringing state-of-the-art AI to enterprises for real applications that businesses need. Placing our models on Azure Marketplace removes barriers to adding AI to your business processes, making integration simple and billing you as part of your existing Azure plan. We value input from everyone using or considering using Jina Embeddings and Jina Reranker. Contact us via our website or join our Discord channel to share feedback and stay up-to-date with Jina AI's rapidly developing offerings. We believe in an inclusive AI ecosystem and would love to talk with you about your use cases. Jina AI - Your Search Foundation, Supercharged. Jina AI offers best-in-class embeddings, reranker and prompt optimizer, enabling advanced multimodal AI. Your Search Foundation, Supercharged. Join the Jina AI Discord Server! Check out the Jina AI community on Discord - hang out with 4981 other members and enjoy free voice and text chat. Discord Categories: Tech blog rss_feed Top-5 similar articles play_arrow GET TOP-5 Select reranker Read more August 26, 2024 • 13 minutes read The What and Why of Text-Image Modality Gap in CLIP Models You can't just use a CLIP model to retrieve text and images and sort the results by score. Why? Because of the modality gap. What is it, and where does it come from? August 22, 2024 • 8 minutes read Late Chunking in Long-Context Embedding Models Chunking long documents while preserving contextual information is challenging. We introduce the "Late Chunking" that leverages long-context embedding models to generate contextual chunk embeddings for better retrieval applications. July 31, 2024 • 17 minutes read Rephrased Labels Improve Zero-Shot Text Classification by 30% When using embedding models for zero-shot classification, rephrasing the class label to "This is seriously about 'LABEL'" gives higher accuracy vs. using LABEL alone. But how, and why?

## SUMMARY_CHUNKING

#### 2 chunk(s)

First, deploy the embedding and reranker endpoints in the Azure portal. You will need to decide what region to use and assign one DNS prefix to the embedding service and another to the reranker service. Then, store that information in the variables embeddings_url and reranker_url in the code below. The functionsjina_embed and jina_rerank generate text embeddings and perform rerankings by making requests to an API hosted on Azure. import json import requests embeddings_url = "http://<Your DNS prefix>.<Your region>.azurecontainer.io:8080/invocations" reranker_url = "http://<Your DNS prefix>.<Your region>.azurecontainer.io:8080/invocations" def jina_embed(text): headers = {"Content-Type": "application/json"} json_data = {"data": [{"text": text}]} response = requests.post(embeddings_url, headers=headers, data=json.dumps(json_data)) return response.json()["data"][0]["embedding"] def jina_rerank(query, search_results): headers = {"Content-Type": "application/json"} json_data = { "data": { "documents": [ {"text": search_result[0]} for search_result in search_results ], "query": query, "top_n": 3, } } response = requests.post(reranker_url, headers=headers, data=json.dumps(json_data)) return response.json()["data"][0]["results"]

Load the Dataset This data was collected for AI model training and therefore splits the data into training and test datasets. For simplicity, we will only use the training data in this tutorial. The code below converts the training data into a pandas DataFrame: ds = dataset['train'] input_df = ds.dataset.to_pandas() Generate Embeddings and Make an Index in FAISS This function processes text data and extracts features in the form of embeddings. This will take some time. import numpy as np from tqdm import tqdm tqdm.pandas() def generate_embeddings(input_df): all_embeddings = [] for t in input_df.text: review_embeddings = [] all_embeddings.append(np.array(jina_embed(t))) input_df["embeddings"] = all_embeddings return input_df enhanced_dataframe = generate_embeddings(input_df) This code iterates over each entry in the text column of the DataFrame and calls jina_embed() to get an embedding. We store the embeddings as NumPy arrays in the list all_embeddings. It then adds them to a new column in the DataFrame called embeddings. We can visualize what we just did by printing the value of enhanced_dataframe: The last column contains the embeddings in a readable form. Now we need to create a FAISS (Facebook AI Similarity Search) index to store and search through the embeddings: import faiss dim = 768 # dimension of Jina v2 embeddings index_with_ids = faiss.IndexIDMap(faiss.IndexFlatIP(dim)) for idx, row in enhanced_dataframe.iterrows(): embeddings = row["embeddings"] normalized_embedding = np.ascontiguousarray( np.array(embeddings, dtype="float32").reshape(1, -1) ) faiss.normalize_L2(normalized_embedding) index_with_ids.add_with_ids(normalized_embedding, idx) This code also normalizes the embedding vectors to simplify and speed up searching. Retrieve Matches for Query The function find_similar_texts searches the index you just created for the closest matches: def find_similar_texts(query, n=20): query_embedding = jina_embed(query) query_embedding = np.ascontiguousarray( np.array(query_embedding, dtype="float32").reshape(1, -1) ) faiss.normalize_L2(query_embedding) similarities, indices = index_with_ids.search(query_embedding, n) results = [] for i in range(n): similarity = similarities[0][i] index_id = indices[0][i] results.append((enhanced_dataframe.loc[index_id, "text"], similarity)) return results

## JINA-SEGMENTER-API

#### 181 chunk(s)

search


notifications


NEWS


PRODUCTS


COMPANY


Tech blog


April 29, 2024


Jina Embeddings and Reranker on Azure: Scalable Business-Ready AI Solutions


Jina Embeddings and Rerankers are now available on Azure Marketplace. Enterprises that prioritize privacy and security can now easily integrate Jina AI's state-of-the-art models right in their existing Azure ecosystem.


Susana Guzmán • 7 minutes read



Jina Embeddings and Rerankers are now available on Azure Marketplace. This integration is important for companies where data security and operational efficiency are top priorities.



Jina AI Launches World’s First Open-Source 8K Text Embedding, Rivaling OpenAI


Jina AI introduces jina-embeddings-v2, the world’s first open-source model boasting an 8K context length. Matching the prowess of OpenAI’s proprietary models, this innovation is now publicly accessible on Huggingface, signaling a significant milestone in the landscape of text embeddings.


Maximizing Search Relevance and RAG Accuracy with Jina Reranker


Boost your search and RAG accuracy with Jina Reranker. Our new model improves the accuracy and relevance by 20% over simple vector search. Try it now for free!



We have seven models available:



Jina Embeddings v2 Base - code


Jina Embeddings v2 Base - de


Jina Embeddings v2 Base - zh


Jina Embeddings v2 Base - es


Jina Embeddings v2 Base - en


Jina Reranker v1 Base - en


Jina Reranker v1 Turbo - en


Jina Reranker v1 Tiny - en


Jina ColBERT v1 - en


Built for Privacy and Performance



Making sure your data is secure is our top priority. Our partnership with Azure allows us to offer AI solutions that meet the demand for data privacy and efficiency. Azure's unparalleled privacy standards ensure the strictest protection of your data, making it a trusted platform for healthcare, finance, and other sectors requiring critical data protection. If you're an existing customer of Azure, then you can get all the benefits of Jina AI's state-of-the-art Embedding and Reranker models with your existing subscription.



Seamless Integration and High Scalability



Deploying on Azure not only ensures privacy but also gives you seamless integration with your existing Azure services. This provides a smooth transition and allows you to scale your AI deployments so you can meet fluctuating demands without compromising on performance.



Get Started with Azure



In this tutorial, we'll create a search application for music. We want to search not with the exact title of the song, but with an ambiguous query that really tests the quality of our search foundation models.



To do that, the first step is to set up everything on Azure.



Sign up for Azure



Make sure you have an Azure account subscription with a valid payment method. You can sign up for an account on the Azure home page if you don't already have one.



Deploying Jina models on Azure



On the Azure Marketplace, you can find all of Jina AI's embedding and reranker models by searching for "jina". Choose the one from there that best suits your needs.



In the Basics tab of the deployment setup, you will need to provide some details about your deployment. By default, the configuration is set to use four CPU cores and 8 GB of memory. Depending on your specific requirements, you may adjust these settings to better suit your application's needs.



This will start the deployment. It may take several minutes. After this, you should see the following screen:



Your models are now deployed and ready to use.



Tutorial: Search for Songs



In this tutorial, you will use your Azure deployments to build a basic search engine for a collection of data files about popular music.



You can also follow this tutorial on Colab or download it and run it in your own notebook.


Load the Dataset


from datasets import load_dataset



dataset = load_dataset("sander-wood/wikimusictext")




This loads the WikiMusicText (WikiMT) dataset.



Start Jina Embeddings v2 and Reranker Endpoints



First, deploy the embedding and reranker endpoints in the Azure portal. You will need to decide what region to use and assign one DNS prefix to the embedding service and another to the reranker service. Then, store that information in the variables embeddings_url and reranker_url in the code below.



The functionsjina_embed and jina_rerank generate text embeddings and perform rerankings by making requests to an API hosted on Azure.



import json



import requests



embeddings_url = "http://<Your DNS prefix>.<Your region>.azurecontainer.io:8080/invocations"


reranker_url = "http://<Your DNS prefix>.<Your region>.azurecontainer.io:8080/invocations"



def jina_embed(text):


    headers = {"Content-Type": "application/json"}
    json_data = {"data": [{"text": text}]}



    response = requests.post(embeddings_url, headers=headers, data=json.dumps(json_data))
    return response.json()["data"][0]["embedding"]


def jina_rerank(query, search_results):


    headers = {"Content-Type": "application/json"}



    json_data = {
        "data": {
            "documents": [
                {"text": search_result[0]} for search_result in search_results
            ],
            "query": query,
            "top_n": 3,
        }
    }



    response = requests.post(reranker_url, headers=headers, data=json.dumps(json_data))
    return response.json()["data"][0]["results"]


Load the Dataset



This data was collected for AI model training and therefore splits the data into training and test datasets. For simplicity, we will only use the training data in this tutorial. The code below converts the training data into a pandas DataFrame:



ds = dataset['train']


input_df = ds.dataset.to_pandas()



Generate Embeddings and Make an Index in FAISS



This function processes text data and extracts features in the form of embeddings. This will take some time.



import numpy as np


from tqdm import tqdm



tqdm.pandas()




def generate_embeddings(input_df):


    all_embeddings = []



    for t in input_df.text:
        review_embeddings = []
        all_embeddings.append(np.array(jina_embed(t)))



    input_df["embeddings"] = all_embeddings



    return input_df


enhanced_dataframe = generate_embeddings(input_df)




This code iterates over each entry in the text column of the DataFrame and calls jina_embed() to get an embedding. We store the embeddings as NumPy arrays in the list all_embeddings. It then adds them to a new column in the DataFrame called embeddings.



We can visualize what we just did by printing the value of enhanced_dataframe:



The last column contains the embeddings in a readable form.



Now we need to create a FAISS (Facebook AI Similarity Search) index to store and search through the embeddings:



import faiss



dim = 768  # dimension of Jina v2 embeddings


index_with_ids = faiss.IndexIDMap(faiss.IndexFlatIP(dim))



for idx, row in enhanced_dataframe.iterrows():


    embeddings = row["embeddings"]
    normalized_embedding = np.ascontiguousarray(
        np.array(embeddings, dtype="float32").reshape(1, -1)
    )
    faiss.normalize_L2(normalized_embedding)
    index_with_ids.add_with_ids(normalized_embedding, idx)


This code also normalizes the embedding vectors to simplify and speed up searching.



Retrieve Matches for Query



The function find_similar_texts searches the index you just created for the closest matches:



def find_similar_texts(query, n=20):


    query_embedding = jina_embed(query)
    query_embedding = np.ascontiguousarray(
        np.array(query_embedding, dtype="float32").reshape(1, -1)
    )
    faiss.normalize_L2(query_embedding)



    similarities, indices = index_with_ids.search(query_embedding, n)



    results = []
    for i in range(n):
        similarity = similarities[0][i]
        index_id = indices[0][i]
        results.append((enhanced_dataframe.loc[index_id, "text"], similarity))



    return results


Rerank to Get Most Relevant Matches



After retrieving results from FAISS index, we will send the set of results to jina_rerank function to assign all answers a relevance score, and return a sorted list of results by relevance.



Let's use a query that needs a lot of semantic understanding to test our solution:



query = "What are some jazz songs that reached the top of the music charts in 1960s?"


search_results = find_similar_texts(query)



most_relevant_results = jina_rerank(query, search_results)


pprint.pprint(most_relevant_results)





Here are the most relevant results:



[{'id': 'c26a67d979cb73474e9f80221b14b5c9',


'index': 0,

'document': {'id': 'd2183fd857661fbf9ca60a22e91888a0',

'text': 'An instrumental version by Heywood and Hugo Winterhalter reached No. 2 on the Billboard Hot 100 chart and No. 7 on the R&B chart in 1956. A version sung by Andy Williams was also popular that year. The tune has been covered by a number of jazz performers beginning in the 1960s.'},

'relevance_score': 0.7132052183151245,

'usage': {'id': '037b9d22a5f13b68258ab51cbab1a7ad', 'total_tokens': 64}},

{'id': 'a9205e69a4e76ca49717b8497a2798bf',
  '

index': 4,
  '

document': {'id': '25e78e92da17f01df111a7ed2716b057',
   '

text': '"Take Five" is a jazz standard composed by Paul Desmond and originally recorded by the Dave Brubeck Quartet for their album Time Out on July 1, 1959. Two years later it became a surprise hit and the biggest-selling jazz single ever. The single was inducted into the Grammy Hall of Fame in 1996. It became the first jazz single to surpass a million in sales.'},
  '

relevance_score': 0.204337015748024,
  '

usage': {'id': '6d55f32b339b83350ffb9489fbf31f5d', 'total_tokens': 80}},
 

{'id': '50a610653b307f6f1ae6ec796b72ca83',
  '

index': 9,
  '

document': {'id': '70278633234c32775b1a28b364f6783a',
   '

text': 'Oh, You Crazy Moon is a jazz standard by Jimmy Van Heusen, with lyrics by Johnny Burke. It was recorded by Mel Torme in 1960 and Frank Sinatra in 1965.'},
  '

relevance_score': 0.16270869970321655,
  '

usage': {'id': '79eabc46bf3c659d3ad3e4d4d7e7a8f2', 'total_tokens': 40}}]




And that's it. Try it out yourself with different queries, and see what results you get.



Jina Embeddings and Rerankers: Enterprise-Ready AI on Azure



Jina AI is focused on bringing state-of-the-art AI to enterprises for real applications that businesses need. Placing our models on Azure Marketplace removes barriers to adding AI to your business processes, making integration simple and billing you as part of your existing Azure plan.



We value input from everyone using or considering using Jina Embeddings and Jina Reranker. Contact us via our website or join our Discord channel to share feedback and stay up-to-date with Jina AI's rapidly developing offerings. We believe in an inclusive AI ecosystem and would love to talk with you about your use cases.



Jina AI - Your Search Foundation, Supercharged.


Jina AI offers best-in-class embeddings, reranker and prompt optimizer, enabling advanced multimodal AI.


Your Search Foundation, Supercharged.


Join the Jina AI Discord Server!


Check out the Jina AI community on Discord - hang out with 4981 other members and enjoy free voice and text chat.


Discord


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