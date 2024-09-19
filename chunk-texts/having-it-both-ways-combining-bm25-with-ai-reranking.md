# having-it-both-ways-combining-bm25-with-ai-reranking

## SIMPLE_CHUNKING

#### 2 chunk(s)

Jina Reranker adds a deeper level of understanding to traditional search technologies. Algorithms like BM25 do a good job of retrieving documents based on term frequency but struggle to evaluate the meaning of the texts they retrieve in light of the user's intent. This is where AI excels: Reranker helps produce outcomes that are better aligned with what users are looking for. Therefore, for businesses that want to bring the powerful advantages of AI models to their search frameworks, adding Jina Reranker can be a wise decision and doesn't incur the burdens of replacing an existing search infrastructure. It’s about refining search results to make them not just acceptable, but exceptional: more relevant and more accurate. Why Jina Reranker? Among reranker models, Jina Reranker models stand out as frontrunners with state-of-the-art scores on performance benchmarks. Maximizing Search Relevance and RAG Accuracy with Jina Reranker Boost your search and RAG accuracy with Jina Reranker. Our new model improves the accuracy and relevance by 20% over simple vector search. Try it now for free!

Here's an overview of how this integration improves the search experience: Boosted Hit Rates: The fusion of Jina Reranker and traditional search has notably increased the frequency of relevant results. This makes the search process more accurate, aligning closely with user queries. Improved User Experience: There's a tangible improvement in the quality of search results. This indicates that the combined capabilities of Jina Reranker and BM25 are better aligned with users' specific needs, enhancing their overall search experience. High Precision for Complex Queries: When it comes to difficult searches, this synergy ensures a more detailed understanding of both the query and related content. This translates to sharper, more accurate results. Ready to Elevate Your Search Experience? Jina Reranker is your ideal solution for increasing the relevance of your search results. It seamlessly integrates with your existing search system and can be implemented swiftly with minimal coding. If you're intrigued by what you've read so far and eager to see the difference Jina Reranker can make, why not give it a try? Start your journey and witness the transformative power of Jina AI's Search Foundation models in your own environment. Categories: Tech blog rss_feed Top-5 similar articles play_arrow GET TOP-5 Select reranker Read more August 26, 2024 • 13 minutes read The What and Why of Text-Image Modality Gap in CLIP Models You can't just use a CLIP model to retrieve text and images and sort the results by score. Why? Because of the modality gap. What is it, and where does it come from? August 22, 2024 • 8 minutes read Late Chunking in Long-Context Embedding Models Chunking long documents while preserving contextual information is challenging. We introduce the "Late Chunking" that leverages long-context embedding models to generate contextual chunk embeddings for better retrieval applications. July 31, 2024 • 17 minutes read Rephrased Labels Improve Zero-Shot Text Classification by 30% When using embedding models for zero-shot classification, rephrasing the class label to "This is seriously about 'LABEL'" gives higher accuracy vs. using LABEL alone. But how, and why? OFFICES location_on Berlin, Germany (HQ) Prinzessinnenstraße 19-20, 10969 Berlin, Germany Geschäftsanschrift: Leipzigerstr. 96, 10117 Berlin, Germany location_on Beijing, China Level 5, Building 6, No.48 Haidian West St. Beijing Haidian, China location_on Shenzhen, China 402, Floor 4, Fu'an Technology Building, Shenzhen Nanshan, China SEARCH FOUNDATION Embeddings Reranker Reader Segmenter Get Jina AI API key API Status COMPANY About us Contact sales Newsroom Intern program Join us open_in_new Download logo open_in_new TERMS Terms & Conditions Privacy Manage Cookies email language English science Jina AI GmbH © 2020-2024.

## COT_TOPIC_CHUNKING

#### 11 chunk(s)

Retrieval-Agnostic Neural Reranking Reranker is agroundbreaking addition to the search system landscape. Designed to enhance the value of existing search engines such as Elasticsearch, it serves as an extra layer, working like an add-on to refine the delivered search quality. It doesn't need to know what kind of search technology it's connected to, it just takes a list of matches and reorders them to be better. Jina Reranker adds a deeper level of understanding to traditional search technologies. Algorithms like BM25 do a good job of retrieving documents based on term frequency but struggle to evaluate the meaning of the texts they retrieve in light of the user's intent. This is where AI excels: Reranker helps produce outcomes that are better aligned with what users are looking for. Therefore, for businesses that want to bring the powerful advantages of AI models to their search frameworks, adding Jina Reranker can be a wise decision and doesn't incur the burdens of replacing an existing search infrastructure. It’s about refining search results to make them not just acceptable, but exceptional: more relevant and more accurate. Why Jina Reranker? Among reranker models, Jina Reranker models stand out as frontrunners with state-of-the-art scores on performance benchmarks. Maximizing Search Relevance and RAG Accuracy with Jina Reranker Boost your search and RAG accuracy with Jina Reranker. Our new model improves the accuracy and relevance by 20% over simple vector search. Try it now for free!

In this article, we'll show you how to implement arecommendation system for e-commerce platforms. First, we'll analyze the performance of a BM25 retriever by itself. Then, we'll add Jina Reranker to the retrieval pipeline and see how the results become more relevant and effective. 💡 You can follow along in Colab or by downloading the notebook. Add Jina Reranker to Your Existing Workflow: Here’s a breakdown of the updated workflow integrating Jina Reranker: Initial Retrieval: When a query is entered, the BM25 search engine retrieves relevant documents based largely on matching the query terms to documents. Reranking: jina-reranker-v1-base-en takes these initial results and uses state-of-the-art AI to evaluate the relevance of each retrieved document in light of the user's query. Returning Results: Jina Reranker then reorders the search results, ensuring that the most relevant documents are presented at the top. Our easy-to-use API and comprehensive documentation will guide you through the whole process, requiring only minimal changes to your system. Reranker API Maximize the search relevancy and RAG accuracy at ease See It in Action: Enhancing E-Commerce Search with Jina Reranker

A query passes through BM25 and the retrieved documents are refined by Jina Reranker. Let's walk through a practical e-commerce example to demonstrate Jina Reranker's impact in real-world applications. The goal here is to search product listings based on a user's query. To illustrate this, we'll set up two search pipelines using the popular AI search and orchestration framework Haystack by deepset. The first pipeline uses BM25 by itself. The second one integrates jina-reranker-v1-base-en into the BM25 system. You can easily replace Haystack's InMemoryDocumentStore component with ElasticsearchDocumentStore to do the same experiment if you have an existing Elasticsearch cluster. We'll use a sample dataset from Kaggle. You can directly download the CSV here. This side-by-side comparison showcases the enhancements brought by incorporating Jina Reranker into the search workflow. To start, install all the necessary components: pip install --q haystack-ai jina-haystack Set the Jina API Key as an environment variable. You can generate one here. import os import getpass os.environ["JINA_API_KEY"] = getpass.getpass() Query for a product based on product names. For example: short_query = "Nightwear for Women" Transform each CSV row into a Document: import csv from haystack import Document documents = [] with open("fashion_data.csv") as f: data = csv.reader(f, delimiter=";") for row in data: row_text = ''.join(row) row_doc = Document(content=row_text, meta={"prod_id": row[0], "prod_image": row[1]}) documents.append(row_doc) Pipeline #1: BM25 Only from haystack import Pipeline from haystack.document_stores.types import DuplicatePolicy from haystack.document_stores.in_memory import InMemoryDocumentStore from haystack.components.retrievers.in_memory import InMemoryBM25Retriever document_store=InMemoryDocumentStore() document_store.write_documents(documents=documents, policy=DuplicatePolicy.OVERWRITE) retriever = InMemoryBM25Retriever(document_store=document_store) rag_pipeline = Pipeline() rag_pipeline.add_component("retriever", retriever) result = rag_pipeline.run( { "retriever": {"query": query, "top_k": 50}, } ) for doc in result["retriever"]["documents"]: print("Product ID:", doc.meta["prod_id"]) print("Product Image:", doc.meta["prod_image"]) print("Score:", doc.score) print("-"*100) Here are thumbnails of the 50 results returned by BM25:

We can see that the results are related to nightwear, partially matching the query, but the most relevant matches (emboldened images in the grid above) seem to get lost within the multitude of products retrieved by BM25.

In practice, using just BM25 means that a user would receive mainly unrelated results at the top of the page. Pipeline #2: BM25 + Jina Reranker The script below outlines how to construct this pipeline step-by-step: from haystack_integrations.components.rankers.jina import JinaRanker ranker_retriever = InMemoryBM25Retriever(document_store=document_store) ranker = JinaRanker() ranker_pipeline = Pipeline() ranker_pipeline.add_component("ranker_retriever", ranker_retriever) ranker_pipeline.add_component("ranker", ranker) ranker_pipeline.connect("ranker_retriever.documents", "ranker.documents") result = ranker_pipeline.run( { "ranker_retriever": {"query": query, "top_k": 50}, "ranker": {"query": query, "top_k": 10}, } ) for doc in result["ranker"]["documents"]: print("Product ID:", doc.meta["prod_id"]) print("Product Image:", doc.meta["prod_image"]) print("Score:", doc.score) print("-"*100) Here are the top 10 results returned by Jina Reranker: Compared to BM25, Jina Reranker returns a much more relevant collection of answers.

Compared to BM25, Jina Reranker returns a much more relevant collection of answers. In our e-commerce setting, this translates to a better user experience and increased likelihood of purchases. Impact of Integrating Jina Reranker with BM25 Following our case study in the e-commerce domain, it’s clear that Jina Reranker’s integration with traditional search engines such as Elasticsearch marks a significant leap in search technology. Here's an overview of how this integration improves the search experience: Boosted Hit Rates: The fusion of Jina Reranker and traditional search has notably increased the frequency of relevant results. This makes the search process more accurate, aligning closely with user queries. Improved User Experience: There's a tangible improvement in the quality of search results. This indicates that the combined capabilities of Jina Reranker and BM25 are better aligned with users' specific needs, enhancing their overall search experience. High Precision for Complex Queries: When it comes to difficult searches, this synergy ensures a more detailed understanding of both the query and related content. This translates to sharper, more accurate results. Ready to Elevate Your Search Experience?

Jina Reranker is your ideal solution for increasing the relevance of your search results. It seamlessly integrates with your existing search system and can be implemented swiftly with minimal coding. If you're intrigued by what you've read so far and eager to see the difference Jina Reranker can make, why not give it a try? Start your journey and witness the transformative power of Jina AI's Search Foundation models in your own environment. Categories: Tech blog rss_feed Top-5 similar articles play_arrow GET TOP-5 Select reranker Read more

August 26, 2024 • 13 minutes read The What and Why of Text-Image Modality Gap in CLIP Models You can't just use a CLIP model to retrieve text and images and sort the results by score. Why? Because of the modality gap. What is it, and where does it come from? August 22, 2024 • 8 minutes read

Late Chunking in Long-Context Embedding Models Chunking long documents while preserving contextual information is challenging. We introduce the "Late Chunking" that leverages long-context embedding models to generate contextual chunk embeddings for better retrieval applications. July 31, 2024 • 17 minutes read Rephrased Labels Improve Zero-Shot Text Classification by 30% When using embedding models for zero-shot classification, rephrasing the class label to "This is seriously about 'LABEL'" gives higher accuracy vs. using LABEL alone. But how, and why?

OFFICES location_on Berlin, Germany (HQ) Prinzessinnenstraße 19-20, 10969 Berlin, Germany Geschäftsanschrift: Leipzigerstr. 96, 10117 Berlin, Germany location_on Beijing, China Level 5, Building 6, No.48 Haidian West St. Beijing Haidian, China location_on Shenzhen, China 402, Floor 4, Fu'an Technology Building, Shenzhen Nanshan, China SEARCH FOUNDATION Embeddings

Reranker Reader Segmenter Get Jina AI API key APIStatus COMPANY About us Contact sales Newsroom Intern program Join us open_in_new Download logo open_in_new TERMS Terms & Conditions Privacy Manage Cookies email language English science Jina AI GmbH © 2020-2024.

## SUMMARY_CHUNKING

#### 6 chunk(s)

search notifications NEWS PRODUCTS COMPANY Tech blog April 24, 2024 Having It Both Ways: Combining BM25 with AI Reranking Learn how to integrate Jina Reranker with lexical search engines to take advantage of superior semantic understanding while avoiding the downsides of migrating to a fully-fledged vector search infrastructure. Yuting Zhang, Francesco Kruk • 6 minutes read It's important to keep pace with new information retrieval technology, but it’s equally important to not break components that are tried and tested and have already demonstrated their business value. Despite the growth in AI-driven vector search, the reality is that most companies still rely on traditional search technologies, often using variants of the BM25 algorithm. It’s a reliable and time-tested technology. Switching to a completely new system isn't just a major step, it often proves to be impractical, demanding substantial resources and a thorough overhaul of operations. Additionally, BM25 is a cornerstone of lexical search engines, commonly employed in widespread search engine platforms like Elasticsearch and Solr. It already delivers strong results for many use cases. Many companies therefore hesitate to completely transition to neural search, despite convincing evidence that AI-based search significantly improves user satisfaction and result quality.

Retrieval-Agnostic Neural Reranking Reranker is a groundbreaking addition to the search system landscape. Designed to enhance the value of existing search engines such as Elasticsearch, it serves as an extra layer, working like an add-on to refine the delivered search quality. It doesn't need to know what kind of search technology it's connected to, it just takes a list of matches and reorders them to be better. Jina Reranker adds a deeper level of understanding to traditional search technologies. Algorithms like BM25 do a good job of retrieving documents based on term frequency but struggle to evaluate the meaning of the texts they retrieve in light of the user's intent. This is where AI excels: Reranker helps produce outcomes that are better aligned with what users are looking for. Therefore, for businesses that want to bring the powerful advantages of AI models to their search frameworks, adding Jina Reranker can be a wise decision and doesn't incur the burdens of replacing an existing search infrastructure. It’s about refining search results to make them not just acceptable, but exceptional: more relevant and more accurate. Why Jina Reranker? Among reranker models, Jina Reranker models stand out as frontrunners with state-of-the-art scores on performance benchmarks. Maximizing Search Relevance and RAG Accuracy with Jina Reranker Boost your search and RAG accuracy with Jina Reranker. Our new model improves the accuracy and relevance by 20% over simple vector search. Try it now for free!

Pipeline #1: BM25 Only from haystack import Pipelinefrom haystack.document_stores.types import DuplicatePolicy from haystack.document_stores.in_memory import InMemoryDocumentStore from haystack.components.retrievers.in_memory import InMemoryBM25Retriever document_store=InMemoryDocumentStore() document_store.write_documents(documents=documents, policy=DuplicatePolicy.OVERWRITE) retriever = InMemoryBM25Retriever(document_store=document_store) rag_pipeline = Pipeline() rag_pipeline.add_component("retriever", retriever) result = rag_pipeline.run( { "retriever": {"query": query, "top_k": 50}, } ) for doc in result["retriever"]["documents"]: print("Product ID:", doc.meta["prod_id"]) print("Product Image:", doc.meta["prod_image"]) print("Score:", doc.score) print("-"*100) Here are thumbnails of the 50 results returned by BM25: We can see that the results are related to nightwear, partially matching the query, but the most relevant matches (emboldened images in the grid above) seem to get lost within the multitude of products retrieved by BM25. In practice, using just BM25 means that a user would receive mainly unrelated results at the top of the page. Pipeline #2: BM25 + Jina Reranker The script below outlines how to construct this pipeline step-by-step: from haystack_integrations.components.rankers.jina import JinaRanker ranker_retriever = InMemoryBM25Retriever(document_store=document_store) ranker = JinaRanker() ranker_pipeline = Pipeline() ranker_pipeline.add_component("ranker_retriever", ranker_retriever) ranker_pipeline.add_component("ranker", ranker) ranker_pipeline.connect("ranker_retriever.documents", "ranker.documents") result = ranker_pipeline.run( { "ranker_retriever": {"query": query, "top_k": 50}, "ranker": {"query": query, "top_k": 10}, } ) for doc in result["ranker"]["documents"]: print("Product ID:", doc.meta["prod_id"]) print("Product Image:", doc.meta["prod_image"]) print("Score:", doc.score) print("-"*100) Here are the top 10 results returned by Jina Reranker: Compared to BM25, Jina Reranker returns a much more relevant collection of answers. In our e-commerce setting, this translates to a better user experience and increased likelihood of purchases. Impact of Integrating Jina Reranker with BM25

Following our case study in the e-commerce domain,it’s clear that Jina Reranker’s integration with traditional search engines such as Elasticsearch marks a significant leap in search technology. Here's an overview of how this integration improves the search experience: Boosted Hit Rates: The fusion of Jina Reranker and traditional search has notably increased the frequency of relevant results. This makes the search process more accurate, aligning closely with user queries. Improved User Experience: There's a tangible improvement in the quality of search results. This indicates that the combined capabilities of Jina Reranker and BM25 are better aligned with users' specific needs, enhancing their overall search experience. High Precision for Complex Queries: When it comes to difficult searches, this synergy ensures a more detailed understanding of both the query and related content. This translates to sharper, more accurate results. Ready to Elevate Your Search Experience?

Jina Reranker is your ideal solution for increasing the relevance of your search results. It seamlessly integrates with your existing search system and can be implemented swiftly with minimal coding. If you're intrigued by what you've read so far and eager to see the difference Jina Reranker can make, why not give it a try? Start your journey and witness the transformative power of Jina AI's Search Foundation models in your own environment. Categories: Tech blog rss_feed Top-5 similar articles play_arrow GET TOP-5 Select reranker Read more August 26, 2024 • 13 minutes read The What and Why of Text-Image Modality Gap in CLIP Models You can't just use a CLIP model to retrieve text and images and sort the results by score. Why? Because of the modality gap.

API Status COMPANY About us Contact sales Newsroom Intern program Join us open_in_new Download logo open_in_new TERMS Terms & Conditions Privacy Manage Cookies email language English science Jina AI GmbH © 2020-2024.

## JINA-SEGMENTER-API

#### 142 chunk(s)

search


notifications


NEWS


PRODUCTS


COMPANY


Tech blog


April 24, 2024


Having It Both Ways: Combining BM25 with AI Reranking


Learn how to integrate Jina Reranker with lexical search engines to take advantage of superior semantic understanding while avoiding the downsides of migrating to a fully-fledged vector search infrastructure.


Yuting Zhang, Francesco Kruk • 6 minutes read



It's important to keep pace with new information retrieval technology, but it’s equally important to not break components that are tried and tested and have already demonstrated their business value.



Despite the growth in AI-driven vector search, the reality is that most companies still rely on traditional search technologies, often using variants of the BM25 algorithm. It’s a reliable and time-tested technology. Switching to a completely new system isn't just a major step, it often proves to be impractical, demanding substantial resources and a thorough overhaul of operations. Additionally, BM25 is a cornerstone of lexical search engines, commonly employed in widespread search engine platforms like Elasticsearch and Solr. It already delivers strong results for many use cases.



Many companies therefore hesitate to completely transition to neural search, despite convincing evidence that AI-based search significantly improves user satisfaction and result quality.



Retrieval-Agnostic Neural Reranking



Reranker is a groundbreaking addition to the search system landscape. Designed to enhance the value of existing search engines such as Elasticsearch, it serves as an extra layer, working like an add-on to refine the delivered search quality. It doesn't need to know what kind of search technology it's connected to, it just takes a list of matches and reorders them to be better.



Jina Reranker adds a deeper level of understanding to traditional search technologies. Algorithms like BM25 do a good job of retrieving documents based on term frequency but struggle to evaluate the meaning of the texts they retrieve in light of the user's intent. This is where AI excels: Reranker helps produce outcomes that are better aligned with what users are looking for.



Therefore, for businesses that want to bring the powerful advantages of AI models to their search frameworks, adding Jina Reranker can be a wise decision and doesn't incur the burdens of replacing an existing search infrastructure. It’s about refining search results to make them not just acceptable, but exceptional: more relevant and more accurate.



Why Jina Reranker?



Among reranker models, Jina Reranker models stand out as frontrunners with state-of-the-art scores on performance benchmarks.



Maximizing Search Relevance and RAG Accuracy with Jina Reranker


Boost your search and RAG accuracy with Jina Reranker. Our new model improves the accuracy and relevance by 20% over simple vector search. Try it now for free!



In this article, we'll show you how to implement a recommendation system for e-commerce platforms. First, we'll analyze the performance of a BM25 retriever by itself. Then, we'll add Jina Reranker to the retrieval pipeline and see how the results become more relevant and effective.



You can follow along in Colab or by downloading the notebook.


Add Jina Reranker to Your Existing Workflow:



Here’s a breakdown of the updated workflow integrating Jina Reranker:



Initial Retrieval: When a query is entered, the BM25 search engine retrieves relevant documents based largely on matching the query terms to documents.


Reranking: jina-reranker-v1-base-en takes these initial results and uses state-of-the-art AI to evaluate the relevance of each retrieved document in light of the user's query.


Returning Results: Jina Reranker then reorders the search results, ensuring that the most relevant documents are presented at the top.



Our easy-to-use API and comprehensive documentation will guide you through the whole process, requiring only minimal changes to your system.



Reranker API


Maximize the search relevancy and RAG accuracy at ease


See It in Action: Enhancing E-Commerce Search with Jina Reranker


A query passes through BM25 and the retrieved documents are refined by Jina Reranker.



Let's walk through a practical e-commerce example to demonstrate Jina Reranker's impact in real-world applications. The goal here is to search product listings based on a user's query.



To illustrate this, we'll set up two search pipelines using the popular AI search and orchestration framework Haystack by deepset. The first pipeline uses BM25 by itself. The second one integrates jina-reranker-v1-base-en into the BM25 system. You can easily replace Haystack's InMemoryDocumentStore component with ElasticsearchDocumentStore to do the same experiment if you have an existing Elasticsearch cluster.



We'll use a sample dataset from Kaggle. You can directly download the CSV here. This side-by-side comparison showcases the enhancements brought by incorporating Jina Reranker into the search workflow.



To start, install all the necessary components:



pip install --q haystack-ai jina-haystack




Set the Jina API Key as an environment variable. You can generate one here.



import os


import getpass



os.environ["JINA_API_KEY"] = getpass.getpass()




Query for a product based on product names. For example:



short_query = "Nightwear for Women"




Transform each CSV row into a Document:



import csv


from haystack import Document



documents = []


with open("fashion_data.csv") as f:


    data = csv.reader(f, delimiter=";")
    for row in data:
      row_text = ''.join(row)
      row_doc = Document(content=row_text, meta={"prod_id": row[0], "prod_image": row[1]})
      documents.append(row_doc)


Pipeline #1: BM25 Only


from haystack import Pipeline


from haystack.document_stores.types import DuplicatePolicy


from haystack.document_stores.in_memory import InMemoryDocumentStore


from haystack.components.retrievers.in_memory import InMemoryBM25Retriever



document_store=InMemoryDocumentStore()


document_store.write_documents(documents=documents, policy=DuplicatePolicy.OVERWRITE)



retriever = InMemoryBM25Retriever(document_store=document_store)



rag_pipeline = Pipeline()


rag_pipeline.add_component("retriever", retriever)



result = rag_pipeline.run(


            {
                "retriever": {"query": query, "top_k": 50},
            }
        )


for doc in result["retriever"]["documents"]:


    print("Product ID:", doc.meta["prod_id"])
    print("Product Image:", doc.meta["prod_image"])
    print("Score:", doc.score)
    print("-"*100)


Here are thumbnails of the 50 results returned by BM25:




We can see that the results are related to nightwear, partially matching the query, but the most relevant matches (emboldened images in the grid above) seem to get lost within the multitude of products retrieved by BM25. In practice, using just BM25 means that a user would receive mainly unrelated results at the top of the page.



Pipeline #2: BM25 + Jina Reranker



The script below outlines how to construct this pipeline step-by-step:



from haystack_integrations.components.rankers.jina import JinaRanker



ranker_retriever = InMemoryBM25Retriever(document_store=document_store)



ranker = JinaRanker()



ranker_pipeline = Pipeline()


ranker_pipeline.add_component("ranker_retriever", ranker_retriever)


ranker_pipeline.add_component("ranker", ranker)



ranker_pipeline.connect("ranker_retriever.documents", "ranker.documents")



result = ranker_pipeline.run(


            {
                "ranker_retriever": {"query": query, "top_k": 50},
                "ranker": {"query": query, "top_k": 10},
            }
        )


for doc in result["ranker"]["documents"]:


    print("Product ID:", doc.meta["prod_id"])
    print("Product Image:", doc.meta["prod_image"])
    print("Score:", doc.score)
    print("-"*100)


Here are the top 10 results returned by Jina Reranker:



Compared to BM25, Jina Reranker returns a much more relevant collection of answers. In our e-commerce setting, this translates to a better user experience and increased likelihood of purchases.



Impact of Integrating Jina Reranker with BM25



Following our case study in the e-commerce domain, it’s clear that Jina Reranker’s integration with traditional search engines such as Elasticsearch marks a significant leap in search technology. Here's an overview of how this integration improves the search experience:



Boosted Hit Rates: The fusion of Jina Reranker and traditional search has notably increased the frequency of relevant results. This makes the search process more accurate, aligning closely with user queries.


Improved User Experience: There's a tangible improvement in the quality of search results. This indicates that the combined capabilities of Jina Reranker and BM25 are better aligned with users' specific needs, enhancing their overall search experience.


High Precision for Complex Queries: When it comes to difficult searches, this synergy ensures a more detailed understanding of both the query and related content. This translates to sharper, more accurate results.


Ready to Elevate Your Search Experience?



Jina Reranker is your ideal solution for increasing the relevance of your search results. It seamlessly integrates with your existing search system and can be implemented swiftly with minimal coding.



If you're intrigued by what you've read so far and eager to see the difference Jina Reranker can make, why not give it a try? Start your journey and witness the transformative power of Jina AI's Search Foundation models in your own environment.



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