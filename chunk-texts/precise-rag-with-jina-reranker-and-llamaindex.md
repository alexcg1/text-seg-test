# precise-rag-with-jina-reranker-and-llamaindex

## SIMPLE_CHUNKING

#### 8 chunk(s)

Maximizing Search Relevance and RAG Accuracy with Jina Reranker Boost your search and RAG accuracy with Jina Reranker. Our new model improves the accuracy and relevance by 20% over simple vector search. Try it now for free! In summary, rerankers are cross-encoder models that take as input a document-query pair, and emit a combined relevance score for that input pair. Using rerankers, users can sort documents from most to least relevant for a given query. Why use jina-reranker-v1-base-en? Reranking provides much more relevant information than using solely an embedding model. In our model release post, we demonstrated that Jina Reranker stands out compared to its open- and closed-source competitors and it can improve search systems by 8% in hit rate and 33% in mean reciprocal rank. This has a direct impact on the quality of responses obtained through the applied RAG solution. With the theory backing up this claim, we’ll show you a practical example so you can see with your own eyes what effect Jina Reranker has on a RAG pipeline built with LlamaIndex.

Before we start: A Note on LlamaIndex Node-Postprocessors Node-postprocessors in LlamaIndex are modules that transform or filter nodes after retrieval and before response synthesis within a query engine. As part of this package, LlamaIndex offers both built-in options as well as an API for custom additions. Jina Reranker has now been integrated into LlamaIndex as a node postprocessor. To increase response accuracy, retrieved nodes are re-ordered based on relevance to the query, and the top N nodes are returned. Follow along on Google Colab This tutorial has an accompanying notebook that you can run on Google Colab or locally. llama_index/docs/docs/examples/node_postprocessor/JinaRerank.ipynb at main · run-llama/llama_index LlamaIndex is a data framework for your LLM applications - run-llama/llama_index GitHub run-llama The dataset: 2024 Nike Kids Product Catalog To showcase Jina Reranker’s performance increase for RAG applications, we’ve chosen the 2024 Nike Kids Product Catalog as our dataset. The document contains a structured set of kids’ products offered by Nike in 2024. We selected this dataset as it showcases the effect of using a reranker clearly and is relatable to most users. Install the prerequisites To install the requirements, run: pip install llama-index-postprocessor-jinaai-rerank pip install llama-index-embeddings-jinaai pip install llama-index pip install llama-index-llms-huggingface pip install "huggingface_hub[inference]" Access Mixtral LLM

Access Mixtral LLM To use the Mixtral-8x7B-Instruct-v0.1 LLM, you need a HuggingFace token. from llama_index.llms.huggingface import HuggingFaceInferenceAPI hf_inference_api_key = "<your HuggingFace access token here>" mixtral_llm = HuggingFaceInferenceAPI( model_name="mistralai/Mixtral-8x7B-Instruct-v0.1", token=hf_inference_api_key, )

Access Jina Embeddings and Jina Reranker To use our Jina Embeddings and Jina Reranker, you need a dedicated API key. Store it in a variable called api_key and call the Jina Embeddings model from LlamaIndex: from llama_index.embeddings.jinaai import JinaEmbedding api_key = "<your Jina key here>" jina_embeddings = JinaEmbedding(api_key=api_key) Similarly, you can call the Jina Reranker model. By setting the top_n parameter, you can decide how many of the most relevant documents to return in the final output. In this case, we set top_n=2: from llama_index.postprocessor.jinaai_rerank import JinaRerank jina_rerank = JinaRerank(api_key=api_key, top_n=2)

Download the 2024 Nike Kids Product Catalog To download the data, run the following code: from llama_index.core import SimpleDirectoryReader import requests url = '<https://niketeam-asset-download.nike.net/catalogs/2024/2024_Nike%20Kids_02_09_24.pdf?cb=09302022>' response = requests.get(url) with open('Nike_Catalog.pdf', 'wb') as f: f.write(response.content) reader = SimpleDirectoryReader( input_files=["Nike_Catalog.pdf"] ) documents = reader.load_data() Generate and index embeddings with Jina Embeddings Now that the setup is complete, we’ll generate the embedding vectors (nodes) and index them. Jina Embeddings v2 models accept input of up to 8192 tokens, large enough that for a document like this, we don’t need to do any further text segmentation or check if any section has too many tokens.

To embed and index the document, run the following code: from llama_index.core import VectorStoreIndex index = VectorStoreIndex.from_documents( documents=documents, embed_model=jina_embeddings )

Query for results without Jina Reranker When we query for specific information from this set of texts, the LlamaIndex query_engine does the following: With Jina Embeddings V2, it creates an embedding for the query. It uses the index to get the top_k = 10 stored embeddings with the highest cosine to the query embedding and return its place in the index. It will look up the corresponding text in the vector data array. Let’s ask what the best Nike jersey is in terms of fabric: query_engine = index.as_query_engine( similarity_top_k=10, llm=mixtral_llm ) response = query_engine.query( "What are the best padded pants that Nike sells?", ) print(response.source_nodes[0].text) Result: NIKE KIDS EQUIPMENT87NIKE BRASILIA SMALL DUFFEL 9.5 DM3976 $37.00 SIZES: Misc OFFER DATE: 07/01/22 END DATE: 07/01/25 Tough 600D polyester • Durable 300D polyester • Detachable shoulder strap • Ventilated shoe or wet/dry storage • Secure zip pocket • Limited lifetime guarantee • Screened Swoosh design trademark DIMENSIONS: 20" L x 10" W x 11" H 010 Black/Black/(White) 068 Iron Grey/Black/(White) ...

Query for results with Reranker We now want to apply the reranker to see if the RAG application yields a different, more relevant result. To do so, we need to add the node_postprocessors to the query_engine: query_engine = index.as_query_engine( similarity_top_k=10, llm=mixtral_llm, node_postprocessors=[jina_rerank] ) response = query_engine.query( "What are the best padded pants that Nike sells?", ) print(response.source_nodes[0].text) Note that compared to the previous case without the reranker, the query_engine now also contains the node_postprocessors parameter set to [jina_rerank]. Result: NIKE KIDS FOOTBALL – STOCK10 DJ5731 $47.00 SIZES: XS, S, M, L, XL, 2XL, 3XL FABRIC: Body/panels lining: 100% polyester. Pad: 100% ethylene vinyl acetate. OFFER DATE: 04/01/23 END DATE: 04/01/27 Take the field ready to give it your all in the Nike Recruit Pants. They’re made from lightweight, stretchy fabric with sweat-wicking power to help keep you dry and moving freely when the game heats up.

## COT_TOPIC_CHUNKING

#### 6 chunk(s)

To increase response accuracy, retrieved nodes are re-ordered based on relevance to the query, and the top N nodes are returned. Follow along on Google Colab This tutorial has an accompanying notebook that you can run on Google Colab or locally. llama_index/docs/docs/examples/node_postprocessor/JinaRerank.ipynb at main · run-llama/llama_index LlamaIndex is a data framework for your LLM applications - run-llama/llama_index GitHub run-llama The dataset: 2024 Nike Kids Product Catalog To showcase Jina Reranker’s performance increase for RAG applications, we’ve chosen the 2024 Nike Kids Product Catalog as our dataset. The document contains a structured set of kids’ products offered by Nike in 2024. We selected this dataset as it showcases the effect of using a reranker clearly and is relatable to most users. Install the prerequisites To install the requirements, run: pip install llama-index-postprocessor-jinaai-rerank pip install llama-index-embeddings-jinaai pip install llama-index pip install llama-index-llms-huggingface pip install "huggingface_hub[inference]"

Access Mixtral LLM To use the Mixtral-8x7B-Instruct-v0.1 LLM, you need a HuggingFace token. from llama_index.llms.huggingface import HuggingFaceInferenceAPI hf_inference_api_key = "<your HuggingFace access token here>" mixtral_llm = HuggingFaceInferenceAPI( model_name="mistralai/Mixtral-8x7B-Instruct-v0.1", token=hf_inference_api_key, ) Access Jina Embeddings and Jina Reranker To use our Jina Embeddings and Jina Reranker, you need a dedicated API key. Store it in a variable called api_key and call the Jina Embeddings model from LlamaIndex: from llama_index.embeddings.jinaai import JinaEmbedding api_key = "<your Jina key here>" jina_embeddings = JinaEmbedding(api_key=api_key) Similarly, you can call the Jina Reranker model. By setting the top_n parameter, you can decide how many of the most relevant documents to return in the final output. In this case, we set top_n=2: from llama_index.postprocessor.jinaai_rerank import JinaRerank jina_rerank = JinaRerank(api_key=api_key, top_n=2)

Download the 2024 Nike Kids Product Catalog To download the data, run the following code: from llama_index.core import SimpleDirectoryReader import requests url = '<https://niketeam-asset-download.nike.net/catalogs/2024/2024_Nike%20Kids_02_09_24.pdf?cb=09302022>' response = requests.get(url) with open('Nike_Catalog.pdf', 'wb') as f: f.write(response.content) reader = SimpleDirectoryReader( input_files=["Nike_Catalog.pdf"] ) documents = reader.load_data() Generate and index embeddings with Jina Embeddings Now that the setup is complete, we’ll generate the embedding vectors (nodes) and index them. Jina Embeddings v2 models accept input of up to 8192 tokens, large enough that for a document like this, we don’t need to do any further text segmentation or check if any section has too many tokens. To embed and index the document, run the following code: from llama_index.core import VectorStoreIndex index = VectorStoreIndex.from_documents( documents=documents, embed_model=jina_embeddings ) Query for results without Jina Reranker

Take the field ready to give it your all in the Nike Recruit Pants. They’re made from lightweight, stretchy fabric with sweat-wicking power to help keep you dry and moving freely when the game heats up. With integrated pads shaped for a comfortable fit, you’ll be prepared for a performance you can be proud of. Choose from 6 different colors to outfit your team. Nike Dri-FIT technology moves sweat away from your skin for quicker evaporation, helping you stay dry and comfortable. Lightweight knit fabric stretches with you to let you move naturally. Thigh, knee, hip and tailbone pads are shaped for an optimal fit, without compromising on coverage. A body-hugging fit is designed to help keep the padding in place and close to the body. Belt at the waist lets you dial in your perfect fit to maximize comfort. Elastic at hems. Hip width: 15", Inseam length: 11.75" (size medium). 010 Black/(White) 060 Team Anthracite/(White) 100 White/(Black) 419 Team Navy/(White) 493 Team Royal/(White) 657 Team Scarlet/(White) Conclusion

As we can see, the query without the reranker leads to a top result which mentions “mesh back for breathability” and “slim fit with soft hand feel”. In comparison, by using a reranker, we obtain a top result that is “engineered for optimal breathability”, has a “moisture-wicking design” that “helps keep you dry and cool under match-day pressure”, and features “lightweight fabric in a relaxed, easy fit”. The second result is much more accurate and appropriate for the query we asked.

With our last two posts, we showed both from a theoretical and practical perspective that adding Jina Reranker to your RAG pipeline increases your retrieval accuracy and improves the quality of the responses you obtain from it. Categories: Tech blog rss_feed Top-5 similar articles play_arrow GET TOP-5 Select reranker Read more

## SUMMARY_CHUNKING

#### 3 chunk(s)

Jina Embeddings v2 models accept input of up to 8192tokens, large enough that for a document like this, we don’t need to do any further text segmentation or check if any section has too many tokens.

To embed and index the document, run the following code: from llama_index.core import VectorStoreIndex index = VectorStoreIndex.from_documents( documents=documents, embed_model=jina_embeddings )

Query for results without Jina Reranker When we query for specific information from this set of texts, the LlamaIndex query_engine does the following: With Jina Embeddings V2, it creates an embedding for the query. It uses the index to get the top_k = 10 stored embeddings with the highest cosine to the query embedding and return its place in the index. It will look up the corresponding text in the vector data array. Let’s ask what the best Nike jersey is in terms of fabric: query_engine = index.as_query_engine( similarity_top_k=10, llm=mixtral_llm ) response = query_engine.query( "What are the best padded pants that Nike sells?", ) print(response.source_nodes[0].text) Result: NIKE KIDS EQUIPMENT87NIKE BRASILIA SMALL DUFFEL 9.5 DM3976 $37.00 SIZES: Misc OFFER DATE: 07/01/22 END DATE: 07/01/25 Tough 600D polyester • Durable 300D polyester • Detachable shoulder strap • Ventilated shoe or wet/dry storage • Secure zip pocket • Limited lifetime guarantee • Screened Swoosh design trademark DIMENSIONS: 20" L x 10" W x 11" H 010 Black/Black/(White) 068 Iron Grey/Black/(White) ...

## JINA-SEGMENTER-API

#### 182 chunk(s)

search


notifications


NEWS


PRODUCTS


COMPANY


Tech blog


March 07, 2024


Precise RAG with Jina Reranker and LlamaIndex


Just Rerank It! Jina Reranker and LlamaIndex take your RAG up to the next level.


Francesco Kruk, Saahil Ognawala • 7 minutes read



While bi-encoder models such as Jina Embeddings can quickly retrieve many matching documents from a database of pre-computed embeddings, reranker models can refine this set by using a slower but more precise approach of cross-encoding users’ queries and retrieved documents. Jina AI has released our first reranker model, jina-reranker-v1-base-en, and, in this article, we’ll present in-depth reasoning for why a reranker is essential to optimize RAG accuracy and how to get started building a state-of-the-art RAG system using Jina Embeddings/Reranker, LlamaIndex, and the Mixtral-8x7B-Instruct-v0.1 language model (hosted on HuggingFace).



You’ll need:



A combined key for Jina Embeddings and Reranker API.


A HuggingFace account and token.


Reranker API


Maximize the search relevancy and RAG accuracy at ease



Since the Jina Embeddings and Reranker models as well as Mixtral run remotely and are accessed via a RESTful API, you won’t need any special hardware.



What is a reranker?



Before continuing with the tutorial, it is important to highlight what rerankers are in the first place. For a full understanding of what a reranker is and why Jina Reranker V1 is the best choice for you, we encourage you to read our Jina Reranker V1 release post before continuing.



Maximizing Search Relevance and RAG Accuracy with Jina Reranker


Boost your search and RAG accuracy with Jina Reranker. Our new model improves the accuracy and relevance by 20% over simple vector search. Try it now for free!



In summary, rerankers are cross-encoder models that take as input a document-query pair, and emit a combined relevance score for that input pair. Using rerankers, users can sort documents from most to least relevant for a given query.



Why use jina-reranker-v1-base-en?



Reranking provides much more relevant information than using solely an embedding model. In our model release post, we demonstrated that Jina Reranker stands out compared to its open- and closed-source competitors and it can improve search systems by 8% in hit rate and 33% in mean reciprocal rank.



This has a direct impact on the quality of responses obtained through the applied RAG solution. With the theory backing up this claim, we’ll show you a practical example so you can see with your own eyes what effect Jina Reranker has on a RAG pipeline built with LlamaIndex.



Before we start: A Note on LlamaIndex Node-Postprocessors



Node-postprocessors in LlamaIndex are modules that transform or filter nodes after retrieval and before response synthesis within a query engine. As part of this package, LlamaIndex offers both built-in options as well as an API for custom additions.



Jina Reranker has now been integrated into LlamaIndex as a node postprocessor. To increase response accuracy, retrieved nodes are re-ordered based on relevance to the query, and the top N nodes are returned.



Follow along on Google Colab



This tutorial has an accompanying notebook that you can run on Google Colab or locally.



llama_index/docs/docs/examples/node_postprocessor/JinaRerank.ipynb at main · run-llama/llama_index


LlamaIndex is a data framework for your LLM applications - run-llama/llama_index


GitHub


run-llama


The dataset: 2024 Nike Kids Product Catalog



To showcase Jina Reranker’s performance increase for RAG applications, we’ve chosen the 2024 Nike Kids Product Catalog as our dataset. The document contains a structured set of kids’ products offered by Nike in 2024. We selected this dataset as it showcases the effect of using a reranker clearly and is relatable to most users.



Install the prerequisites



To install the requirements, run:



pip install llama-index-postprocessor-jinaai-rerank


pip install llama-index-embeddings-jinaai


pip install llama-index


pip install llama-index-llms-huggingface


pip install "huggingface_hub[inference]"


Access Mixtral LLM



To use the Mixtral-8x7B-Instruct-v0.1 LLM, you need a HuggingFace token.



from llama_index.llms.huggingface import HuggingFaceInferenceAPI



hf_inference_api_key = "<your HuggingFace access token here>"



mixtral_llm = HuggingFaceInferenceAPI(


    model_name="mistralai/Mixtral-8x7B-Instruct-v0.1",
    token=hf_inference_api_key,


Access Jina Embeddings and Jina Reranker



To use our Jina Embeddings and Jina Reranker, you need a dedicated API key. Store it in a variable called api_key and call the Jina Embeddings model from LlamaIndex:



from llama_index.embeddings.jinaai import JinaEmbedding



api_key = "<your Jina key here>"


jina_embeddings = JinaEmbedding(api_key=api_key)



Similarly, you can call the Jina Reranker model. By setting the top_n parameter, you can decide how many of the most relevant documents to return in the final output. In this case, we set top_n=2:



from llama_index.postprocessor.jinaai_rerank import JinaRerank



jina_rerank = JinaRerank(api_key=api_key, top_n=2)


Download the 2024 Nike Kids Product Catalog



To download the data, run the following code:



from llama_index.core import SimpleDirectoryReader


import requests



url = '<https://niketeam-asset-download.nike.net/catalogs/2024/2024_Nike%20Kids_02_09_24.pdf?cb=09302022>'


response = requests.get(url)



with open('Nike_Catalog.pdf', 'wb') as f:


f.write(response.content)



reader = SimpleDirectoryReader(


input_files=["Nike_Catalog.pdf"]
)



documents = reader.load_data()


Generate and index embeddings with Jina Embeddings



Now that the setup is complete, we’ll generate the embedding vectors (nodes) and index them. Jina Embeddings v2 models accept input of up to 8192 tokens, large enough that for a document like this, we don’t need to do any further text segmentation or check if any section has too many tokens. To embed and index the document, run the following code:



from llama_index.core import VectorStoreIndex



index = VectorStoreIndex.from_documents(


documents=documents, embed_model=jina_embeddings
)


Query for results without Jina Reranker



When we query for specific information from this set of texts, the LlamaIndex query_engine does the following:



With Jina Embeddings V2, it creates an embedding for the query.


It uses the index to get the top_k = 10 stored embeddings with the highest cosine to the query embedding and return its place in the index.


It will look up the corresponding text in the vector data array.



Let’s ask what the best Nike jersey is in terms of fabric:



query_engine = index.as_query_engine(


similarity_top_k=10, llm=mixtral_llm
)


response = query_engine.query(


"What are the best padded pants that Nike sells?",
)



print(response.source_nodes[0].text)



Result:



NIKE KIDS  EQUIPMENT87NIKE BRASILIA SMALL DUFFEL 9.5 


DM3976 $37.00


SIZES: Misc  OFFER DATE: 07/01/22  END DATE: 07/01/25


Tough 600D polyester • Durable 300D polyester • Detachable shoulder


strap • Ventilated shoe or wet/dry storage • Secure zip pocket • 


Limited lifetime guarantee • Screened Swoosh design trademark


DIMENSIONS:  20" L x 10" W x 11" H 


010 Black/Black/(White) 068 Iron Grey/Black/(White)
...


Query for results with Reranker



We now want to apply the reranker to see if the RAG application yields a different, more relevant result. To do so, we need to add the node_postprocessors to the query_engine:



query_engine = index.as_query_engine(


similarity_top_k=10, llm=mixtral_llm, node_postprocessors=[jina_rerank]
)


response = query_engine.query(


"What are the best padded pants that Nike sells?",
)



print(response.source_nodes[0].text)



Note that compared to the previous case without the reranker, the query_engine now also contains the node_postprocessors parameter set to [jina_rerank].



Result:



NIKE KIDS  FOOTBALL – STOCK10


DJ5731 $47.00


SIZES:  XS, S, M, L, XL, 2XL, 3XL


FABRIC:  Body/panels lining: 100% polyester. Pad: 100%


ethylene vinyl acetate.


OFFER DATE:  04/01/23


END DATE:  04/01/27


Take the field ready to give it your all in the Nike Recruit


Pants. They’re made from lightweight, stretchy fabric with


sweat-wicking power to help keep you dry and moving freely


when the game heats up. With integrated pads shaped for a


comfortable fit, you’ll be prepared for a performance you can


be proud of. Choose from 6 different colors to outfit your


team. Nike Dri-FIT technology moves sweat away from your skin


for quicker evaporation, helping you stay dry and comfortable.


Lightweight knit fabric stretches with you to let you move


naturally. Thigh, knee, hip and tailbone pads are shaped for


an optimal fit, without compromising on coverage. A


body-hugging fit is designed to help keep the padding in place


and close to the body. Belt at the waist lets you dial in your


perfect fit to maximize comfort. Elastic at hems.


Hip width: 15", Inseam length: 11.75" (size medium).


010 Black/(White) 060 Team Anthracite/(White) 100 White/(Black)


419 Team Navy/(White) 493 Team Royal/(White) 657 Team Scarlet/(White)



Conclusion



As we can see, the query without the reranker leads to a top result which mentions “mesh back for breathability” and “slim fit with soft hand feel”. In comparison, by using a reranker, we obtain a top result that is “engineered for optimal breathability”, has a “moisture-wicking design” that “helps keep you dry and cool under match-day pressure”, and features “lightweight fabric in a relaxed, easy fit”.



The second result is much more accurate and appropriate for the query we asked. With our last two posts, we showed both from a theoretical and practical perspective that adding Jina Reranker to your RAG pipeline increases your retrieval accuracy and improves the quality of the responses you obtain from it.



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