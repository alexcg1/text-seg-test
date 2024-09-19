# maximizing-search-relevancy-and-rag-accuracy-with-jina-reranker

## SIMPLE_CHUNKING

#### 2 chunk(s)

search notifications NEWS PRODUCTS COMPANY star Featured Press release February 29, 2024 Maximizing Search Relevance and RAG Accuracy with Jina Reranker Boost your search and RAG accuracy with Jina Reranker. Our new model improves the accuracy and relevance by 20% over simple vector search. Try it now for free! Jina AI • 11 minutes read Text embeddings, known for their semantic representation capabilities, along with fast vector retrieval, are today's cornerstone in document search within vast datasets. However, the challenge often lies in filtering through these retrieved documents to accurately align with the user's search intent, a task that goes beyond the capabilities of simple cosine similarity measures. Today, we're thrilled to announce Jina Reranker (jina-reranker-v1-base-en), a cutting-edge neural reranking model designed to tackle this critical issue of relevancy. Jina Reranker enhances your search and RAG (Retrieval-Augmented Generation) system by reordering retrieved documents in a manner that deeply and contextually understands the search query terms. Our evaluations demonstrated remarkable improvements for search systems employing the Jina Reranker with +8% in hit rate and +33% in mean reciprocal rank!

Our evaluations demonstrated remarkable improvements for search systems employing the Jina Reranker with +8% in hit rate and +33% in mean reciprocal rank! Reranker API Maximize the search relevancy and RAG accuracy at ease What is a Reranker? Understanding the concept of a reranker often leads us to question the necessity of re-ranking mechanisms in search (ranking) systems. Common questions are, "Why do we need a reranker?" and "Isn't ranking documents by cosine similarity between the query and document embeddings enough already?" To address these questions, let's first revisit the single embedding cosine similarity approach and its limitations. Cosine similarity quantifies the similarity between two documents by measuring the cosine of the angle between their embedding vectors. This metric is valued for its simplicity and has been used in many vector databases as the default way of retrieval. However, this approach, commonly termed as a representation-based approach, tends to oversimplify interaction between query and documents. Specifically, it struggles with capturing the nuanced interaction at the sub-document level and sub-query level, often missing the full depth of user intent and the fine details of document relevance. The comparison of the representation-based cosine similarity (left) and the reranker (right). This is where rerankers come into play. Utilizing deep neural networks, rerankers delve deeper into the interactions between the query and the shortlisted documents. They move beyond basic document-level embeddings to embrace token-level interactions that occur within the query, within the document, and across the query-document boundary. Although this method is more computationally intensive compared to simple cosine similarity, it enables a nuanced comparison that incorporates context, semantic meaning, and the intent behind the query, substantially improving the relevancy of search results. Vector Search via Cosine Similarity Reranker Interaction Level Document-level embeddings Token-level interactions Computational Demand Low High Most computation happens at Offline, i.e. indexing time Online, i.e. query time Result Broad but superficial matching Highly relevant and precise matching Strengths - Fast and efficient - Simple implementation - Deep contextual understanding - Advanced semantic analysis Limitations - Limited by lack of depth and context - May miss nuances of user intent - Computationally intensive - Requires more sophisticated models Best For Provides a quick, efficient first pass Adds depth, enhancing accuracy and relevance of final search results

## COT_TOPIC_CHUNKING

#### 11 chunk(s)

search notifications NEWS PRODUCTS COMPANY star Featured Press release February 29, 2024 Maximizing Search Relevance and RAG Accuracy with Jina Reranker Boost your search and RAG accuracy with Jina Reranker. Our new model improves the accuracy and relevance by 20% over simple vector search. Try it now for free! Jina AI • 11 minutes read Text embeddings, known for their semantic representation capabilities, along with fast vector retrieval, are today's cornerstone in document search within vast datasets. However, the challenge often lies in filtering through these retrieved documents to accurately align with the user's search intent, a task that goes beyond the capabilities of simple cosine similarity measures. Today, we're thrilled to announce Jina Reranker (jina-reranker-v1-base-en), a cutting-edge neural reranking model designed to tackle this critical issue of relevancy. Jina Reranker enhances your search and RAG (Retrieval-Augmented Generation) system by reordering retrieved documents in a manner that deeply and contextually understands the search query terms. Our evaluations demonstrated remarkable improvements for search systems employing the Jina Reranker with +8% in hit rate and +33% in mean reciprocal rank!

Reranker API Maximize the search relevancy and RAG accuracy at ease What is a Reranker? Understanding the concept of a reranker often leads us to question the necessity of re-ranking mechanisms in search (ranking) systems. Common questions are, "Why do we need a reranker?" and "Isn't ranking documents by cosine similarity between the query and document embeddings enough already?" To address these questions, let's first revisit the single embedding cosine similarity approach and its limitations. Cosine similarity quantifies the similarity between two documents by measuring the cosine of the angle between their embedding vectors. This metric is valued for its simplicity and has been used in many vector databases as the default way of retrieval. However, this approach, commonly termed as a representation-based approach, tends to oversimplify interaction between query and documents. Specifically, it struggles with capturing the nuanced interaction at the sub-document level and sub-query level, often missing the full depth of user intent and the fine details of document relevance. The comparison of the representation-based cosine similarity (left) and the reranker (right). This is where rerankers come into play. Utilizing deep neural networks, rerankers delve deeper into the interactions between the query and the shortlisted documents. They move beyond basic document-level embeddings to embrace token-level interactions that occur within the query, within the document, and across the query-document boundary. Although this method is more computationally intensive compared to simple cosine similarity, it enables a nuanced comparison that incorporates context, semantic meaning, and the intent behind the query, substantially improving the relevancy of search results. Vector Search via Cosine Similarity Reranker Interaction Level Document-level embeddings Token-level interactions Computational Demand Low High Most computation happens at Offline, i.e. indexing time Online, i.e. query time Result Broad but superficial matching Highly relevant and precise matching Strengths - Fast and efficient - Simple implementation - Deep contextual understanding - Advanced semantic analysis Limitations - Limited by lack of depth and context - May miss nuances of user intent - Computationally intensive - Requires more sophisticated models Best For Provides a quick, efficient first pass Adds depth, enhancing accuracy and relevance of final search results

In summary, reranker is a critical component in the search pipeline. A high-quality search system typically begins with an embedding-based vector retrieval step, which is then refined by a reranker model. This two-step approach leverages the strengths of both models, ensuring the delivery of precise, high-quality information that aligns seamlessly with the user's needs. A practical search system often chains the embedding-based search and the reranker together to achieve the best search quality. Get Started with Jina Reranker To start using Jina Reranker, head to our Reranker page to get YOUR_API_KEY. You can adapt the example cURL snippet below by changing the query or adding more documents: curl -X 'POST' \ 'https://api.jina.ai/v1/rerank' \ -H 'accept: application/json' \ -H 'Authorization: Bearer YOUR_API_KEY' \ -H 'Content-Type: application/json' \ -d '{ "model": "jina-reranker-v1-base-en", "query": "Organic skincare products for sensitive skin", "documents": [ "Eco-friendly kitchenware for modern homes", "Biodegradable cleaning supplies for eco-conscious consumers", "Organic cotton baby clothes for sensitive skin", "Natural organic skincare range for sensitive skin", "Tech gadgets for smart homes: 2024 edition", "Sustainable gardening tools and compost solutions", "Sensitive skin-friendly facial cleansers and toners", "Organic food wraps and storage solutions", "All-natural pet food for dogs with allergies", "Yoga mats made from recycled materials" ], "top_n": 3 }' In this example, the documents range from home goods to tech gadgets, clothing, and even pet food, showcasing a wide spectrum of products one might find on an e-commerce site. This diversity requires the reranker to effectively identify and prioritize items most relevant to the query about "Organic skincare products for sensitive skin," despite the presence of other organic, eco-friendly, or sensitive skin-related products in different categories. The response is a JSON object as follows: { "model": "jina-reranker-v1-base-en", "usage": { "total_tokens": 38, "prompt_tokens": 38 }, "results": [ { "index": 3, "document": { "text": "Natural organic skincare range for sensitive skin" }, "relevance_score": 0.8292155861854553 }, { "index": 2, "document": { "text": "Organic cotton baby clothes for sensitive skin" }, "relevance_score": 0.14426936209201813 }, { "index": 6, "document": { "text": "Sensitive skin-friendly facial cleansers and toners" }, "relevance_score": 0.13857832551002502 } ] }

Top Performance of Jina Reranker We evaluated Jina Reranker on four key benchmarks to ensure top-tier performance and search relevance. Higher performance in these benchmarks directly translates to better precision, relevance, and contextual understanding in search and retrieval applications. For comparison, we included three other leading rerankers by BGE (BAAI), BCE (Netease Youdao), and Cohere in the benchmark. As shown by the results below, Jina Reranker holds the highest average score in all relevant categories for reranking, making it a clear leader among its peers.

Benchmark 1: LlamaIndex RAG A benchmark study performed by LlamaIndex (which we reproduced), evaluated a combination of different embedding and reranking models in RAG tasks. This combines two scores - Hit-rate (how likely it is that a relevant document is retrieved by an embedding model), and Mean Reciprocal Rank (MRR - how high the most relevant document is ranked by the reranker model). No Reranker jina-reranker bge-reranker-base bce-reranker-base_v1 cohere-reranker Embedding model Hit Rate MRR Hit Rate MRR Hit Rate MRR Hit Rate MRR Hit Rate MRR jina-embeddings-v2-base-en0.8053 0.5156 0.8737 0.7229 0.8368 0.6568 0.8737 0.7007 0.8842 0.7008 bge-base-en-v1.5 0.7842 0.5183 0.8368 0.6895 0.8158 0.6586 0.8316 0.6843 0.8368 0.6739 bce-embedding-base_v1 0.8526 0.5988 0.8895 0.7346 0.8684 0.6927 0.9157 0.7379 0.9158 0.7296 CohereV3-en 0.7211 0.4900 0.8211 0.6894 0.8000 0.6285 0.8263 0.6855 0.8316 0.6710 Average 0.7908 0.5307 0.8553 0.7091 0.8303 0.6592 0.8618 0.7021 0.8671 0.6938 Substantial Improvement Over Simple Cosine Similarity The improvement Jina Reranker brings to both Hit Rate and Mean Reciprocal Rank (MRR) is significant. On average, the introduction of Jina Reranker elevates the Hit Rate from 0.7908 to 0.8553 (+7.9%), and the MRR from 0.5307 to 0.7091 (+33.7%). This showcases the reranker’s ability to enhance the precision and relevance of search results dramatically, ensuring that users are more likely to find what they're searching for with higher accuracy. Embeddings Agnosticism Jina Reranker's performance across different embedding models further illustrates its model-agnostic nature. Whether paired with jina-embeddings-v2-base-en, bge-base-en-v1.5, bce-embedding-base_v1, or CohereV3-en, Jina Reranker consistently improves the Hit Rate and MRR. This versatility makes it an invaluable tool for a wide range of applications, affirming its adaptability to different underlying technologies and use cases.

Benchmark 2: BEIR BIER (Benchmarking IR) assesses a model's retrieval effectiveness, including relevance and NDCG. A higher BIER score correlates to more accurate matches and search result rankings. Dataset jina-reranker bge-reranker-base bce-reranker-base-v1 cohere-rerank-english-v2.0 NQ 0.5951 0.5457 0.5186 0.6004 HotpotQA 0.7447 0.7766 0.7392 0.7202 FiQA-2018 0.3981 0.3228 0.3262 0.4387 CQADupstack 0.4077 0.3516 0.3594 0.3829 Quora 0.8792 0.7001 0.8390 0.6433 FEVER 0.8707 0.8961 0.7203 0.8265 Climate-FEVER 0.2570 0.3399 0.2171 0.2038 TREC-COVID 0.8523 0.7121 0.7364 0.8419 NFCorpus 0.3809 0.3308 0.3534 0.3673 ArguAna 0.5938 0.2620 0.3856 0.3040 Touche-2020 0.3065 0.2965 0.2533 0.3052 DBPedia 0.4387 0.4196 0.4069 0.4236 SciFact 0.7549 0.7104 0.7021 0.7379 SCIDOCS 0.1983 0.1540 0.1802 0.1813 MSMarco 0.7042 0.7303 0.7155 0.7350 Average 0.5588 0.5032 0.4969 0.5141 Benchmark 3: MTEB The MTEB (Multilingual Text Embedding Benchmark), on the whole, tests a model’s abilities in text embeddings, including clustering, classification, retrieval, and other metrics. However, for our comparison, we only used the MTEB’s Reranking tasks. Dataset jina-reranker bge-reranker-base bce-reranker-base-v1 cohere-rerank-english-v2.0 AskUbuntuDupQuestions 0.5793 0.5471 0.5654 0.5536 SciDocsRR 0.8056 0.6741 0.7578 0.6728 StackOverflowDupQuestions 0.4850 0.3764 0.4287 0.4414 Average 0.6233 0.5325 0.5840 0.5559 Benchmark 4: LoCo Through the LoCo benchmark, we measured a model's understanding of local coherence and context, together with query-specific ranking. A LoCo higher score reflects a better ability to identify and prioritize relevant information. Dataset jina-reranker bge-reranker-base bce-reranker-base-v1 cohere-rerank-english-v2.0 qasper_None_abstract 0.996 0.774 0.989 0.919 qasper_None_title 0.980 0.883 0.971 0.983 scrolls_gov_report_output 0.962 0.574 0.922 0.659 scrolls_qmsum_output 0.466 0.549 0.449 0.444 scrolls_summ_screen_fd_output 0.962 0.629 0.920 0.905 Average 0.873 0.682 0.850 0.782

Jina Reranker Model Highlights The Jina Reranker distinguishes itself as a leader in the reranking domain, outperforming key competitors from Cohere, BGE, and BCE, as illustrated in the previous analysis. Its embedding-agnostic nature and unmatched efficacy underscore its premier status in the industry. Furthermore, Jina Reranker boasts notable features that set it apart: Long Context Length Jina Reranker stands out from other reranking solutions by accommodating long context lengths. It is capable of handling queries up to 512 tokens and documents as large as 8192 tokens. Furthermore, the model is designed to process up to 2048 candidate documents for each query. Time cost of rerank(query=1, docs=100) in ms #TokensPerDocument #QueryTokens 256 512 1024 2048 4096 64 156 323 1366 2107 3571 128 194 369 1377 2123 3598 256 273 475 1397 2155 4299 512 468 1385 2114 3536 7068

Affordable API pricing Jina Reranker API comes withidentical pricing to our embedding API (including 1 million free trial), such as jina-embeddings-v2-base-en , based on the total number of tokens, in queries and documents. Token quotas can be bought on our Embeddings/Reranker API page. The API secret and token quotas can be used for both reranker and embedding APIs. Coming Soon to AWS Marketplace Expanding our reach, Jina Reranker will not only be accessible via our API but is also set to debut on the AWS SageMaker Marketplace for seamless private cloud deployment. This upcoming availability aims to offer enhanced data protection and application security within the familiar confines of your AWS cloud subscription.

We highly value your insights and experiences with Jina Reranker. Talk to us on our Discord channel to share your feedback and stay up-to-date with our latest models. Your input is crucial as we continue to refine our technologies and contribute to a more dynamic and inclusive search AI ecosystem. Categories: star Featured Press release rss_feed Top-5 similar articles play_arrow GET TOP-5 Select reranker Read more September 18, 2024 • 10 minutes read Jina Embeddings V3: A Frontier Multilingual Embedding Model jina-embeddings-v3 is a frontier multilingual text embedding model with 570M parameters and 8192 token-length, outperforming the latest proprietary embeddings from OpenAI and Cohere on MTEB. September 11, 2024 • 12 minutes read Reader-LM: Small Language Models for Cleaning and Converting HTML to Markdown Reader-LM-0.5B and Reader-LM-1.5B are two novel small language models inspired by Jina Reader, designed to convert raw, noisy HTML from the open web into clean markdown. August 30, 2024 • 10 minutes read Jina ColBERT v2: Multilingual Late Interaction Retriever for Embedding and Reranking Jina ColBERT v2 supports 89 languages with superior retrieval performance, user-controlled output dimensions, and 8192 token-length.

OFFICES location_on Berlin, Germany (HQ) Prinzessinnenstraße 19-20, 10969 Berlin, Germany Geschäftsanschrift: Leipzigerstr. 96, 10117 Berlin, Germany location_on Beijing, China Level 5, Building 6, No.48 Haidian West St. Beijing Haidian, China location_on Shenzhen, China 402, Floor 4, Fu'an Technology Building, Shenzhen Nanshan, China SEARCH FOUNDATION Embeddings Reranker Reader Segmenter Get Jina AI API key API Status COMPANY About us Contact sales Newsroom Intern program Join us open_in_new Download logo open_in_new TERMS Terms & Conditions Privacy Manage Cookies email language English science

Jina AI GmbH © 2020-2024.

## SUMMARY_CHUNKING

#### 6 chunk(s)

Benchmark 3: MTEB The MTEB (Multilingual Text Embedding Benchmark), on the whole, tests a model’s abilities in text embeddings, including clustering, classification, retrieval, and other metrics. However, for our comparison, we only used the MTEB’s Reranking tasks.

Jina Reranker Model Highlights The Jina Reranker distinguishes itself as a leader in the reranking domain, outperforming key competitors from Cohere, BGE, and BCE, as illustrated in the previous analysis. Its embedding-agnostic nature and unmatched efficacy underscore its premier status in the industry. Furthermore, Jina Reranker boasts notable features that set it apart: Long Context Length Jina Reranker stands out from other reranking solutions by accommodating long context lengths. It is capable of handling queries up to 512 tokens and documents as large as 8192 tokens. Furthermore, the model is designed to process up to 2048 candidate documents for each query. Time cost of rerank(query=1, docs=100) in ms #TokensPerDocument #QueryTokens 256 512 1024 2048 4096 64 156 323 1366 2107 3571 128 194 369 1377 2123 3598 256 273 475 1397 2155 4299 512 468 1385 2114 3536 7068 Enhancing Accuracy with RAG Integration

Retrieval Augmented Generation (RAG) significantly enhances the precision of responses from large language models (LLMs) by incorporating additional, context-specific information—such as a company's internal database—into the query process. This method ensures the LLM's responses are firmly based on provided contextual data. The integration of rerankers with RAG within an information retrieval pipeline paves the way for the development of high-performance applications capable of delivering precise information retrieval across a vast array of domains. Consider, for example, the scenario where you're planning to cook a special meal using specific ingredients favored by your guests. To simplify this task, you decide to employ a chatbot that suggests recipes based on renowned cookbooks. Initially, without a reranker, your input might look something like this: Context information is below. --------------------- {Madhur_Jaffrey_An_Invitation_To_Indian_Cooking} {Julia_Child_Mastering_The_Art_Of_French_Cooking} {Jiro_Ono_Sushi_Estetica_E_Tecnica} --------------------- Given the context information and no prior knowledge, answer the query. Query: Create a recipe using the ingredients below. --------------------- Salmon Asparagus Potatoes --------------------- Incorporating a reranker model, however, allows for a nuanced understanding of document relevance, enhancing the LLM's context with information about the relative importance of each cookbook. The refined input, highlighting the ranked relevance of the context to the query, might then appear as follows: Context information is below. Note that the context is ranked from most to least relevant to the query. --------------------- {Julia_Child_Mastering_The_Art_Of_French_Cooking} {Jiro_Ono_Sushi_Estetica_E_Tecnica} {Madhur_Jaffrey_An_Invitation_To_Indian_Cooking} --------------------- Given the context information and no prior knowledge, answer the query. Query: Create a recipe using the ingredients below. --------------------- Salmon Asparagus Potatoes --------------------- This additional layer of insight into the cookbooks' relevance to the given ingredients makes it evident that the optimal recipe likely falls within French cuisine, steering the chatbot's suggestion in a direction that best matches the ingredients' culinary context. Without reranking, a suggestion based on sushi could have been equally plausible given the prominence of salmon, yet it would have led to a markedly different dining experience. Moreover, by determining the number of documents to be considered in the ranking process, users can fine-tune the operation's precision and computational demands to suit their specific requirements, further illustrating the reranker's versatility and effectiveness.

Affordable API pricing Jina Reranker API comes with identical pricing to our embedding API (including 1 million free trial), such as jina-embeddings-v2-base-en , based on the total number of tokens, in queries and documents. Token quotas can be bought on our Embeddings/Reranker API page. The API secret and token quotas can be used for both reranker and embedding APIs. Coming Soon to AWS Marketplace

Expanding our reach, Jina Reranker will not only be accessible via our API but is also set to debut on the AWS SageMaker Marketplace for seamless private cloud deployment. This upcoming availability aims to offer enhanced data protection and application security within the familiar confines of your AWS cloud subscription.

September 11, 2024 • 12 minutes read Reader-LM: Small Language Models for Cleaning and Converting HTML to Markdown Reader-LM-0.5B and Reader-LM-1.5B are two novel small language models inspired by Jina Reader, designed to convert raw, noisy HTML from the open web into clean markdown. August 30, 2024 • 10 minutes read

## JINA-SEGMENTER-API

#### 227 chunk(s)

search


notifications


NEWS


PRODUCTS


COMPANY


star


Featured


Press release


February 29, 2024


Maximizing Search Relevance and RAG Accuracy with Jina Reranker


Boost your search and RAG accuracy with Jina Reranker. Our new model improves the accuracy and relevance by 20% over simple vector search. Try it now for free!


Jina AI • 11 minutes read



Text embeddings, known for their semantic representation capabilities, along with fast vector retrieval, are today's cornerstone in document search within vast datasets. However, the challenge often lies in filtering through these retrieved documents to accurately align with the user's search intent, a task that goes beyond the capabilities of simple cosine similarity measures.



Today, we're thrilled to announce Jina Reranker (jina-reranker-v1-base-en), a cutting-edge neural reranking model designed to tackle this critical issue of relevancy. Jina Reranker enhances your search and RAG (Retrieval-Augmented Generation) system by reordering retrieved documents in a manner that deeply and contextually understands the search query terms. Our evaluations demonstrated remarkable improvements for search systems employing the Jina Reranker with +8% in hit rate and +33% in mean reciprocal rank!



Reranker API


Maximize the search relevancy and RAG accuracy at ease


What is a Reranker?



Understanding the concept of a reranker often leads us to question the necessity of re-ranking mechanisms in search (ranking) systems. Common questions are, "Why do we need a reranker?" and "Isn't ranking documents by cosine similarity between the query and document embeddings enough already?" To address these questions, let's first revisit the single embedding cosine similarity approach and its limitations.



Cosine similarity quantifies the similarity between two documents by measuring the cosine of the angle between their embedding vectors. This metric is valued for its simplicity and has been used in many vector databases as the default way of retrieval. However, this approach, commonly termed as a representation-based approach, tends to oversimplify interaction between query and documents. Specifically, it struggles with capturing the nuanced interaction at the sub-document level and sub-query level, often missing the full depth of user intent and the fine details of document relevance.



The comparison of the representation-based cosine similarity (left) and the reranker (right).



This is where rerankers come into play. Utilizing deep neural networks, rerankers delve deeper into the interactions between the query and the shortlisted documents. They move beyond basic document-level embeddings to embrace token-level interactions that occur within the query, within the document, and across the query-document boundary. Although this method is more computationally intensive compared to simple cosine similarity, it enables a nuanced comparison that incorporates context, semantic meaning, and the intent behind the query, substantially improving the relevancy of search results.



	Vector Search via Cosine Similarity	Reranker


Interaction Level	Document-level embeddings	Token-level interactions


Computational Demand	Low	High


Most computation happens at	Offline, i.e. indexing time	Online, i.e. query time


Result	Broad but superficial matching	Highly relevant and precise matching


Strengths	- Fast and efficient


- Simple implementation	- Deep contextual understanding


- Advanced semantic analysis


Limitations	- Limited by lack of depth and context


- May miss nuances of user intent	- Computationally intensive


- Requires more sophisticated models


Best For	Provides a quick, efficient first pass	Adds depth, enhancing accuracy and relevance of final search results



In summary, reranker is a critical component in the search pipeline. A high-quality search system typically begins with an embedding-based vector retrieval step, which is then refined by a reranker model. This two-step approach leverages the strengths of both models, ensuring the delivery of precise, high-quality information that aligns seamlessly with the user's needs.



A practical search system often chains the embedding-based search and the reranker together to achieve the best search quality.


Get Started with Jina Reranker



To start using Jina Reranker, head to our Reranker page to get YOUR_API_KEY. You can adapt the example cURL snippet below by changing the query or adding more documents:



curl -X 'POST' \


'https://api.jina.ai/v1/rerank' \

-H 'accept: application/json' \
  

-H 'Authorization: Bearer YOUR_API_KEY' \
  

-H 'Content-Type: application/json' \
  

-d '{
  

"model": "jina-reranker-v1-base-en",
  

"query": "Organic skincare products for sensitive skin",
  

"documents": [
    

"Eco-friendly kitchenware for modern homes",
    

"Biodegradable cleaning supplies for eco-conscious consumers",
    

"Organic cotton baby clothes for sensitive skin",
    

"Natural organic skincare range for sensitive skin",
    

"Tech gadgets for smart homes: 2024 edition",
    

"Sustainable gardening tools and compost solutions",
    

"Sensitive skin-friendly facial cleansers and toners",
    

"Organic food wraps and storage solutions",
    

"All-natural pet food for dogs with allergies",
    

"Yoga mats made from recycled materials"
  ], 
  

"top_n": 3
}'




In this example, the documents range from home goods to tech gadgets, clothing, and even pet food, showcasing a wide spectrum of products one might find on an e-commerce site. This diversity requires the reranker to effectively identify and prioritize items most relevant to the query about "Organic skincare products for sensitive skin," despite the presence of other organic, eco-friendly, or sensitive skin-related products in different categories. The response is a JSON object as follows:



{


"model": "jina-reranker-v1-base-en",
  

"usage": {
    

"total_tokens": 38,
    

"prompt_tokens": 38
  },
  

"results": [
    

{
      

"index": 3,
      

"document": {
        

"text": "Natural organic skincare range for sensitive skin"
      },
      

"relevance_score": 0.8292155861854553
    },
    

{
      

"index": 2,
      

"document": {
        

"text": "Organic cotton baby clothes for sensitive skin"
      },
      

"relevance_score": 0.14426936209201813
    },
    

{
      

"index": 6,
      

"document": {
        

"text": "Sensitive skin-friendly facial cleansers and toners"
      },
      

"relevance_score": 0.13857832551002502
    }
  ]
}


Top Performance of Jina Reranker



We evaluated Jina Reranker on four key benchmarks to ensure top-tier performance and search relevance. Higher performance in these benchmarks directly translates to better precision, relevance, and contextual understanding in search and retrieval applications.



For comparison, we included three other leading rerankers by BGE (BAAI), BCE (Netease Youdao), and Cohere in the benchmark. As shown by the results below, Jina Reranker holds the highest average score in all relevant categories for reranking, making it a clear leader among its peers.



Benchmark 1: LlamaIndex RAG



A benchmark study performed by LlamaIndex (which we reproduced), evaluated a combination of different embedding and reranking models in RAG tasks. This combines two scores - Hit-rate (how likely it is that a relevant document is retrieved by an embedding model), and Mean Reciprocal Rank (MRR - how high the most relevant document is ranked by the reranker model).



	No Reranker	jina-reranker	bge-reranker-base	bce-reranker-base_v1	cohere-reranker


Embedding model	Hit Rate	MRR	Hit Rate	MRR	Hit Rate	MRR	Hit Rate	MRR	Hit Rate	MRR


jina-embeddings-v2-base-en0.8053	0.5156	0.8737	0.7229	0.8368	0.6568	0.8737	0.7007	0.8842	0.7008


bge-base-en-v1.5	0.7842	0.5183	0.8368	0.6895	0.8158	0.6586	0.8316	0.6843	0.8368	0.6739


bce-embedding-base_v1	0.8526	0.5988	0.8895	0.7346	0.8684	0.6927	0.9157	0.7379	0.9158	0.7296


CohereV3-en	0.7211	0.4900	0.8211	0.6894	0.8000	0.6285	0.8263	0.6855	0.8316	0.6710


Average	0.7908	0.5307	0.8553	0.7091	0.8303	0.6592	0.8618	0.7021	0.8671	0.6938


Substantial Improvement Over Simple Cosine Similarity



The improvement Jina Reranker brings to both Hit Rate and Mean Reciprocal Rank (MRR) is significant. On average, the introduction of Jina Reranker elevates the Hit Rate from 0.7908 to 0.8553 (+7.9%), and the MRR from 0.5307 to 0.7091 (+33.7%). This showcases the reranker’s ability to enhance the precision and relevance of search results dramatically, ensuring that users are more likely to find what they're searching for with higher accuracy.



Embeddings Agnosticism



Jina Reranker's performance across different embedding models further illustrates its model-agnostic nature. Whether paired with jina-embeddings-v2-base-en, bge-base-en-v1.5, bce-embedding-base_v1, or CohereV3-en, Jina Reranker consistently improves the Hit Rate and MRR. This versatility makes it an invaluable tool for a wide range of applications, affirming its adaptability to different underlying technologies and use cases.



Benchmark 2: BEIR



BIER (Benchmarking IR) assesses a model's retrieval effectiveness, including relevance and NDCG. A higher BIER score correlates to more accurate matches and search result rankings.



Dataset	jina-reranker	bge-reranker-base	bce-reranker-base-v1	cohere-rerank-english-v2.0


NQ	0.5951	0.5457	0.5186	0.6004


HotpotQA	0.7447	0.7766	0.7392	0.7202


FiQA-2018	0.3981	0.3228	0.3262	0.4387


CQADupstack	0.4077	0.3516	0.3594	0.3829


Quora	0.8792	0.7001	0.8390	0.6433


FEVER	0.8707	0.8961	0.7203	0.8265


Climate-FEVER	0.2570	0.3399	0.2171	0.2038


TREC-COVID	0.8523	0.7121	0.7364	0.8419


NFCorpus	0.3809	0.3308	0.3534	0.3673


ArguAna	0.5938	0.2620	0.3856	0.3040


Touche-2020	0.3065	0.2965	0.2533	0.3052


DBPedia	0.4387	0.4196	0.4069	0.4236


SciFact	0.7549	0.7104	0.7021	0.7379


SCIDOCS	0.1983	0.1540	0.1802	0.1813


MSMarco	0.7042	0.7303	0.7155	0.7350


Average	0.5588	0.5032	0.4969	0.5141


Benchmark 3: MTEB



The MTEB (Multilingual Text Embedding Benchmark), on the whole, tests a model’s abilities in text embeddings, including clustering, classification, retrieval, and other metrics. However, for our comparison, we only used the MTEB’s Reranking tasks.



Dataset	jina-reranker	bge-reranker-base	bce-reranker-base-v1	cohere-rerank-english-v2.0


AskUbuntuDupQuestions	0.5793	0.5471	0.5654	0.5536


SciDocsRR	0.8056	0.6741	0.7578	0.6728


StackOverflowDupQuestions	0.4850	0.3764	0.4287	0.4414


Average	0.6233	0.5325	0.5840	0.5559


Benchmark 4: LoCo



Through the LoCo benchmark, we measured a model's understanding of local coherence and context, together with query-specific ranking. A LoCo higher score reflects a better ability to identify and prioritize relevant information.



Dataset	jina-reranker	bge-reranker-base	bce-reranker-base-v1	cohere-rerank-english-v2.0


qasper_None_abstract	0.996	0.774	0.989	0.919


qasper_None_title	0.980	0.883	0.971	0.983


scrolls_gov_report_output	0.962	0.574	0.922	0.659


scrolls_qmsum_output	0.466	0.549	0.449	0.444


scrolls_summ_screen_fd_output	0.962	0.629	0.920	0.905


Average	0.873	0.682	0.850	0.782


Jina Reranker Model Highlights



The Jina Reranker distinguishes itself as a leader in the reranking domain, outperforming key competitors from Cohere, BGE, and BCE, as illustrated in the previous analysis. Its embedding-agnostic nature and unmatched efficacy underscore its premier status in the industry. Furthermore, Jina Reranker boasts notable features that set it apart:



Long Context Length



Jina Reranker stands out from other reranking solutions by accommodating long context lengths. It is capable of handling queries up to 512 tokens and documents as large as 8192 tokens. Furthermore, the model is designed to process up to 2048 candidate documents for each query.



Time cost of rerank(query=1, docs=100) in ms	#TokensPerDocument


#QueryTokens	256	512	1024	2048	4096


64	156	323	1366	2107	3571


128	194	369	1377	2123	3598


256	273	475	1397	2155	4299


512	468	1385	2114	3536	7068


Enhancing Accuracy with RAG Integration



Retrieval Augmented Generation (RAG) significantly enhances the precision of responses from large language models (LLMs) by incorporating additional, context-specific information—such as a company's internal database—into the query process. This method ensures the LLM's responses are firmly based on provided contextual data. The integration of rerankers with RAG within an information retrieval pipeline paves the way for the development of high-performance applications capable of delivering precise information retrieval across a vast array of domains.



Consider, for example, the scenario where you're planning to cook a special meal using specific ingredients favored by your guests. To simplify this task, you decide to employ a chatbot that suggests recipes based on renowned cookbooks. Initially, without a reranker, your input might look something like this:



Context information is below.
---------------------


{Madhur_Jaffrey_An_Invitation_To_Indian_Cooking}


{Julia_Child_Mastering_The_Art_Of_French_Cooking}


{Jiro_Ono_Sushi_Estetica_E_Tecnica}


---------------------


Given the context information and no prior knowledge, answer the query.


Query: Create a recipe using the ingredients below.
---------------------


Salmon


Asparagus


Potatoes
---------------------


Incorporating a reranker model, however, allows for a nuanced understanding of document relevance, enhancing the LLM's context with information about the relative importance of each cookbook. The refined input, highlighting the ranked relevance of the context to the query, might then appear as follows:



Context information is below.


Note that the context is ranked from most to least relevant to the query.
---------------------


{Julia_Child_Mastering_The_Art_Of_French_Cooking}


{Jiro_Ono_Sushi_Estetica_E_Tecnica}


{Madhur_Jaffrey_An_Invitation_To_Indian_Cooking}


---------------------


Given the context information and no prior knowledge, answer the query.


Query: Create a recipe using the ingredients below.
---------------------


Salmon


Asparagus


Potatoes
---------------------


This additional layer of insight into the cookbooks' relevance to the given ingredients makes it evident that the optimal recipe likely falls within French cuisine, steering the chatbot's suggestion in a direction that best matches the ingredients' culinary context. Without reranking, a suggestion based on sushi could have been equally plausible given the prominence of salmon, yet it would have led to a markedly different dining experience.



Moreover, by determining the number of documents to be considered in the ranking process, users can fine-tune the operation's precision and computational demands to suit their specific requirements, further illustrating the reranker's versatility and effectiveness.



Affordable API pricing



Jina Reranker API comes with identical pricing to our embedding API (including 1 million free trial), such as jina-embeddings-v2-base-en , based on the total number of tokens, in queries and documents. Token quotas can be bought on our Embeddings/Reranker API page. The API secret and token quotas can be used for both reranker and embedding APIs.



Coming Soon to AWS Marketplace



Expanding our reach, Jina Reranker will not only be accessible via our API but is also set to debut on the AWS SageMaker Marketplace for seamless private cloud deployment. This upcoming availability aims to offer enhanced data protection and application security within the familiar confines of your AWS cloud subscription.



We highly value your insights and experiences with Jina Reranker. Talk to us on our Discord channel to share your feedback and stay up-to-date with our latest models. Your input is crucial as we continue to refine our technologies and contribute to a more dynamic and inclusive search AI ecosystem.



Categories:


star


Featured


Press release


rss_feed


Top-5 similar articles


play_arrow


GET TOP-5


Select reranker


Read more


September 18, 2024 • 10 minutes read


Jina Embeddings V3: A Frontier Multilingual Embedding Model


jina-embeddings-v3 is a frontier multilingual text embedding model with 570M parameters and 8192 token-length, outperforming the latest proprietary embeddings from OpenAI and Cohere on MTEB.


September 11, 2024 • 12 minutes read


Reader-LM: Small Language Models for Cleaning and Converting HTML to Markdown


Reader-LM-0.5B and Reader-LM-1.5B are two novel small language models inspired by Jina Reader, designed to convert raw, noisy HTML from the open web into clean markdown.


August 30, 2024 • 10 minutes read


Jina ColBERT v2: Multilingual Late Interaction Retriever for Embedding and Reranking


Jina ColBERT v2 supports 89 languages with superior retrieval performance, user-controlled output dimensions, and 8192 token-length.


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