# jina-colbert-v2-multilingual-late-interaction-retriever-for-embedding-and-reranking

## SIMPLE_CHUNKING

#### 6 chunk(s)

search notifications NEWS PRODUCTS COMPANY star Featured Press release August 30, 2024 Jina ColBERT v2: Multilingual Late Interaction Retriever for Embedding and Reranking Jina ColBERT v2 supports 89 languages with superior retrieval performance, user-controlled output dimensions, and 8192 token-length. Jina AI • 10 minutes read Today, we’re excited to release Jina ColBERT v2 (jina-colbert-v2), an advanced late interaction retrieval model built on the ColBERT architecture. This new language model improves performance of jina-colbert-v1-en and adds multilingual support and dynamic output dimensions. This new release highlights the following features: Superior retrieval performance compared to the original ColBERT-v2 (+6.5%) and our previous release, jina-colbert-v1-en(+5.4%). Multilingual support for 89 languages, delivering strong performance across major global languages. User-controlled output embedding sizes through Matryoshka representation learning, enabling users to flexibly balance between efficiency and precision. Technical Summary of jina-colbert-v2 The full technical report can be found on arXiv:

Jina-ColBERT-v2: A General-Purpose Multilingual Late Interaction Retriever Multi-vector dense models, such as ColBERT, have proven highly effective in information retrieval. ColBERT’s late interaction scoring approximates the joint query-document attention seen in cross-encoders while maintaining inference efficiency closer to traditional dense retrieval models, thanks to its bi-encoder architecture and recent optimizations in indexing and search. In this paper, we introduce several improvements to the ColBERT model architecture and training pipeline, leveraging techniques successful in the more established single-vector embedding model paradigm, particularly those suited for heterogeneous multilingual data. Our new model, Jina-ColBERT-v2, demonstrates strong performance across a range of English and multilingual retrieval tasks, while also cutting storage requirements by up to 50% compared to previous models. arXiv.org Rohan Jha jina-colbert-v2 jina-colbert-v1-en Original ColBERTv2 Average of 14 English BEIR tasks 0.521 0.494 0.489 Multilingual 89 languages English-only English-only Output dimensions 128, 96, or 64 Fixed 128 Fixed 128 Max query length 32 tokens 32 tokens 32 tokens Max document length 8192 tokens 8192 tokens 512 tokens Parameters 560M 137M 110M Model size 1.1GB 550MB 438MB Asymmetric Embedding in ColBERT ColBERT builds on the BERT architecture by adding late interaction and asymmetric query-document encoding. What is ColBERT and Late Interaction and Why They Matter in Search? Jina AI’s ColBERT on Hugging Face has set Twitter abuzz, bringing a fresh perspective to search with its 8192-token capability. This article unpacks the nuances of ColBERT and ColBERTv2, showcasing their innovative designs and why their late interaction feature is a game-changer for search. The asymmetric nature of ColBERT means that when using models like jina-colbert-v2 or jina-colbert-v1-en, you need to specify whether you are embedding a query, a document, or both (for reranking purposes). This added flexibility enhances performance over homogeneous embedding models in retrieval tasks.

Multilingual Support For Over 89 Languages Jina ColBERT v2 has extensive multilingual capabilities, designed to meet the demands of modern, globalized information retrieval and AI applications. The training corpus for jina-colbert-v2 incorporates 89 languages, with additional stages of training for major international languages including Arabic, Chinese, English, French, German, Japanese, Russian, and Spanish, as well as programming languages. The training also included a corpus of aligned bilingual texts to unlock cross-lingual potentials, allowing queries and documents in different languages to be matched in reranking/retrieval tasks. Pre-training dataset data distribution by language (specified by ISO-639 code) in logarithmic scale. Today, Jina ColBERT v2 stands out as the only multilingual ColBERT-like model that generates compact embeddings, significantly outperforming BM25-based retrieval across all languages tested on MIRACL benchmarks. Jina ColBERT v2 performance over 16 languages, compared to BM25, on MIRACL benchmarks. Furthermore, on English-language retrieval tasks, Jina ColBERT v2 exceeds the performance of its predecessor jina-colbert-v1-en and the original ColBERT v2 model, with comparable performance to the highly specialized English-only AnswerAI-ColBERT-small model. Model Name Average score (14 BEIR English-only benchmarks) Multilingual Support jina-colbert-v2 0.521 Multilingual jina-colbert-v1-en 0.494 English-only ColBERT v2.0 0.489 English-only AnswerAI-ColBERT-small 0.549 English-only Evaluation of jina-colbert-v2 on a selection of English-only datasets from BEIR benchmark.

For Reranking To use jina-colbert-v2 via the Jina Reranker API, passing in one query and several documents and getting back rankable match scores, construct your request like the one below: curl https://api.jina.ai/v1/rerank \\ -H "Content-Type: application/json" \\ -H "Authorization: Bearer <YOUR JINA API KEY>" \\ -d '{ "model": "jina-colbert-v2", "query": "What is the population of Berlin?", "top_n": 3, "documents": [ "Berlin's population grew by 0.7 percent in 2023 compared with the previous year. Accordingly, around 27,300 more residents lived in Berlin at the end of the last year than in 2022. Those of 30 to under 40 years old form the numerically largest age group. With roughly 881,000 foreign residents from around 170 nations and an average age of the population of 42.5 years old.", "Mount Berlin is a glacier-covered volcano in Marie Byrd Land, Antarctica, 100 kilometres (62 mi) from the Amundsen Sea. It is a roughly 20-kilometre-wide (12 mi) mountain with parasitic vents that consists of two coalesced volcanoes: Berlin proper with the 2-kilometre-wide (1.2 mi) Berlin Crater and Merrem Peak with a 2.5-by-1-kilometre-wide (1.55 mi × 0.62 mi) crater, 3.5 kilometres (2.2 mi) away from Berlin.", "Population as of 31.12.2023 by nationality and federal states Land\\tTotal\\tGermans\\tForeigners\\tincluding EU-states number\\t%\\tnumber\\t%", "The urban area of Berlin has a population of over 4.5 million and is therefore the most populous urban area in Germany. The Berlin-Brandenburg capital region has around 6.2 million inhabitants and is Germany's second-largest metropolitan region after the Rhine-Ruhr region, and the sixth-biggest metropolitan region by GDP in the European Union.", "Irving Berlin (born Israel Beilin) was an American composer and songwriter. His music forms a large part of the Great American Songbook. Berlin received numerous honors including an Academy Award, a Grammy Award, and a Tony Award.", "Berlin is a town in the Capitol Planning Region, Connecticut, United States. The population was 20,175 at the 2020 census.", "Berlin is the capital and largest city of Germany, both by area and by population. Its more than 3.85 million inhabitants make it the European Union's most populous city, as measured by population within city limits.", "Berlin, Berlin ist eine für die ARD produzierte Fernsehserie, die von 2002 bis 2005 im Vorabendprogramm des Ersten ausgestrahlt wurde. Regie führten unter anderem Franziska Meyer Price, Christoph Schnee, Sven Unterwaldt Jr. und Titus Selge." ] }' Note the top_n argument, which specifies the number of documents you want to retrieve. For example, if your application only uses the top match, set top_n to 1. For code snippets in Python and other programming languages and frameworks, go to the Jina AI Embeddings API page, or select jina-colbert-v2 from the drop-down menu on the Jina Reranker API page.

Reranker API Maximize the search relevancy and RAGaccuracy at ease. Via Stanford ColBERT You can also use Jina ColBERT v2 as a drop-in replacement for ColBERT v2 in the Stanford ColBERT library. Just specify jinaai/jina-colbert-v2 as the model source: from colbert.infra import ColBERTConfig from colbert.modeling.checkpoint import Checkpoint ckpt = Checkpoint("jinaai/jina-colbert-v2", colbert_config=ColBERTConfig()) docs = ["Your list of texts"] query_vectors = ckpt.queryFromText(docs) ⚠️ You must install einops and flash_attn to use the above code. Via RAGatouille Jina ColBERT v2 is similarly integrated into RAGatouille. You can download and use it via the method RAGPretrainedModel.from_pretrained(): from ragatouille import RAGPretrainedModel RAG = RAGPretrainedModel.from_pretrained("jinaai/jina-colbert-v2") docs = ["Your list of texts"] RAG.index(docs, index_name="your_index_name") query = "Your query" results = RAG.search(query) ⚠️ You must install einops and flash_attn to use the above code. Via Qdrant

Summary Jina ColBERT v2 (jina-colbert-v2) builds onthe high performance of jina-colbert-v1-en and expands its capabilities to a wide range of global languages. With support for multiple embedding sizes, jina-colbert-v2 allows users to tune the precision/efficiency trade-off to suit their specific use cases, potentially offering significant savings in time and computing costs. This model combines all these features into a single, competitively priced package, accessible via an intuitive web API and compatible with any computing framework that supports HTTP requests. Try it out for yourself with 1 million free tokens to see how it can enhance your applications and processes. Categories: star Featured Press release rss_feed Top-5 similar articles play_arrow GET TOP-5 Select reranker Read more September 18, 2024 • 10 minutes read Jina Embeddings V3: A Frontier Multilingual Embedding Model jina-embeddings-v3 is a frontier multilingual text embedding model with 570M parameters and 8192 token-length, outperforming the latest proprietary embeddings from OpenAI and Cohere on MTEB. September 11, 2024 • 12 minutes read Reader-LM: Small Language Models for Cleaning and Converting HTML to Markdown Reader-LM-0.5B and Reader-LM-1.5B are two novel small language models inspired by Jina Reader, designed to convert raw, noisy HTML from the open web into clean markdown. June 25, 2024 • 15 minutes read Jina Reranker v2 for Agentic RAG: Ultra-Fast, Multilingual, Function-Calling & Code Search Jina Reranker v2 is the best-in-class reranker built for Agentic RAG. It features function-calling support, multilingual retrieval for over 100 languages, code search capabilities, and offers a 6x speedup over v1. OFFICES location_on Berlin, Germany (HQ) Prinzessinnenstraße 19-20, 10969 Berlin, Germany Geschäftsanschrift: Leipzigerstr. 96, 10117 Berlin, Germany location_on Beijing, China Level 5, Building 6, No.48 Haidian West St. Beijing Haidian, China location_on Shenzhen, China 402, Floor 4, Fu'an Technology Building, Shenzhen Nanshan, China SEARCH FOUNDATION Embeddings Reranker Reader Segmenter Get Jina AI API key API Status COMPANY About us Contact sales Newsroom Intern program Join us open_in_new Download logo open_in_new TERMS Terms & Conditions Privacy Manage Cookies email language English science Jina AI GmbH © 2020-2024.

## COT_TOPIC_CHUNKING

#### 7 chunk(s)

Multi-vector dense models, such as ColBERT, have proven highly effective in information retrieval. ColBERT’s late interaction scoring approximates the joint query-document attention seen in cross-encoders while maintaining inference efficiency closer to traditional dense retrieval models, thanks to its bi-encoder architecture and recent optimizations in indexing and search. In this paper, we introduce several improvements to the ColBERT model architecture and training pipeline, leveraging techniques successful in the more established single-vector embedding model paradigm, particularly those suited for heterogeneous multilingual data. Our new model, Jina-ColBERT-v2, demonstrates strong performance across a range of English and multilingual retrieval tasks, while also cutting storage requirements by up to 50% compared to previous models. arXiv.org Rohan Jha jina-colbert-v2 jina-colbert-v1-en Original ColBERTv2 Average of 14 English BEIR tasks 0.521 0.494 0.489 Multilingual 89 languages English-only English-only Output dimensions 128, 96, or 64 Fixed 128 Fixed 128 Max query length 32 tokens 32 tokens 32 tokens Max document length 8192 tokens 8192 tokens 512 tokens Parameters 560M 137M 110M Model size 1.1GB 550MB 438MB Asymmetric Embedding in ColBERT ColBERT builds on the BERT architecture by adding late interaction and asymmetric query-document encoding. What is ColBERT and Late Interaction and Why They Matter in Search? Jina AI’s ColBERT on Hugging Face has set Twitter abuzz, bringing a fresh perspective to search with its 8192-token capability. This article unpacks the nuances of ColBERT and ColBERTv2, showcasing their innovative designs and why their late interaction feature is a game-changer for search. The asymmetric nature of ColBERT means that when using models like jina-colbert-v2 or jina-colbert-v1-en, you need to specify whether you are embedding a query, a document, or both (for reranking purposes). This added flexibility enhances performance over homogeneous embedding models in retrieval tasks.

Getting Started with Jina ColBERT v2 Jina ColBERT v2 is available via the Jina Search Foundation API, the AWS marketplace, and on Azure. It is also available for non-commercial use only (CC BY-NC-4.0) via Hugging Face. Via Jina Search Foundation API For Embedding The following curl command shows how to specify the input and options to get document embeddings from jina-colbert-v2 via the Jina Embeddings API. To get vectors of your preferred size, specify 128 or 64 for the dimensions parameter. This parameter is optional and the default value is 128. Input documents will be truncated if longer than 8192 tokens. Specify your Jina API key in the authorization header Authorization: Bearer <YOUR JINA API KEY>: curl https://api.jina.ai/v1/multi-vector \\ -H "Content-Type: application/json" \\ -H "Authorization: Bearer <YOUR JINA API KEY>" \\ -d '{ "model": "jina-colbert-v2", "dimensions": 128, # Or 64 for half-size vectors "input_type": "document", # For query embeddings see below "embedding_type": "float", "input": [ "Your document text string goes here", "You can send multiple texts", "Each text can be up to 8192 tokens long" ]}' To get query embeddings, set the input_type parameter to query instead of document. Note that queries have much stricter size limits than documents. They will be truncated at 32 tokens. Query encoding will always return 32 tokens, including embeddings for the padding if less than 32 tokens long. curl https://api.jina.ai/v1/multi-vector \\ -H "Content-Type: application/json" \\ -H "Authorization: Bearer <YOUR JINA API KEY>" \\ -d '{ "model": "jina-colbert-v2", "dimensions": 128, # Or 64 for half-size vectors "input_type": "query", # This must be specified for query embeddings "embedding_type": "float", "input": [ "Your query text string goes here", "You can send multiple texts", "Each query text can be up to 32 tokens long" ]}' Embedding API Multimodal, bilingual long-context embeddings for your search and RAG. For Reranking

To use jina-colbert-v2 via the Jina Reranker API,passing in one query and several documents and getting back rankable match scores, construct your request like the one below: curl https://api.jina.ai/v1/rerank \\ -H "Content-Type: application/json" \\ -H "Authorization: Bearer <YOUR JINA API KEY>" \\ -d '{ "model": "jina-colbert-v2", "query": "What is the population of Berlin?", "top_n": 3, "documents": [ "Berlin's population grew by 0.7 percent in 2023 compared with the previous year. Accordingly, around 27,300 more residents lived in Berlin at the end of the last year than in 2022. Those of 30 to under 40 years old form the numerically largest age group. With roughly 881,000 foreign residents from around 170 nations and an average age of the population of 42.5 years old.", "Mount Berlin is a glacier-covered volcano in Marie Byrd Land, Antarctica, 100 kilometres (62 mi) from the Amundsen Sea. It is a roughly 20-kilometre-wide (12 mi) mountain with parasitic vents that consists of two coalesced volcanoes: Berlin proper with the 2-kilometre-wide (1.2 mi) Berlin Crater and Merrem Peak with a 2.5-by-1-kilometre-wide (1.55 mi × 0.62 mi) crater, 3.5 kilometres (2.2 mi) away from Berlin.", "Population as of 31.12.2023 by nationality and federal states Land\\tTotal\\tGermans\\tForeigners\\tincluding EU-states number\\t%\\tnumber\\t%", "The urban area of Berlin has a population of over 4.5 million and is therefore the most populous urban area in Germany. The Berlin-Brandenburg capital region has around 6.2 million inhabitants and is Germany's second-largest metropolitan region after the Rhine-Ruhr region, and the sixth-biggest metropolitan region by GDP in the European Union.", "Irving Berlin (born Israel Beilin) was an American composer and songwriter. His music forms a large part of the Great American Songbook. Berlin received numerous honors including an Academy Award, a Grammy Award, and a Tony Award.", "Berlin is a town in the Capitol Planning Region, Connecticut, United States. The population was 20,175 at the 2020 census.", "Berlin is the capital and largest city of Germany, both by area and by population. Its more than 3.85 million inhabitants make it the European Union's most populous city, as measured by population within city limits.", "Berlin, Berlin ist eine für die ARD produzierte Fernsehserie, die von 2002 bis 2005 im Vorabendprogramm des Ersten ausgestrahlt wurde. Regie führten unter anderem Franziska Meyer Price, Christoph Schnee, Sven Unterwaldt Jr. und Titus Selge." ] }' Note the top_n argument, which specifies the number of documents you want to retrieve. For example, if your application only uses the top match, set top_n to 1. For code snippets in Python and other programming languages and frameworks, go to the Jina AI Embeddings API page, or select jina-colbert-v2 from the drop-down menu on the Jina Reranker API page.

Reranker API Maximize the search relevancy and RAG accuracy at ease. Via Stanford ColBERT You can also use Jina ColBERT v2 as a drop-in replacement for ColBERT v2 in the Stanford ColBERT library. Just specify jinaai/jina-colbert-v2 as the model source: from colbert.infra import ColBERTConfig from colbert.modeling.checkpoint import Checkpoint ckpt = Checkpoint("jinaai/jina-colbert-v2", colbert_config=ColBERTConfig()) docs = ["Your list of texts"] query_vectors = ckpt.queryFromText(docs) ⚠️ You must install einops and flash_attn to use the above code. Via RAGatouille Jina ColBERT v2 is similarly integrated into RAGatouille. You can download and use it via the method RAGPretrainedModel.from_pretrained(): from ragatouille import RAGPretrainedModel RAG = RAGPretrainedModel.from_pretrained("jinaai/jina-colbert-v2") docs = ["Your list of texts"] RAG.index(docs, index_name="your_index_name") query = "Your query" results = RAG.search(query) ⚠️ You must install einops and flash_attn to use the above code. Via Qdrant

Since version 1.10, Qdrant has added support for multi-vectors and late-interaction models. Existing users of Qdrant engines, whether local or managed cloud versions, can benefit by directly integrating jina-colbert-v2 using Qdrant’s client. Creating a new Collection using the MAX_SIM operation from qdrant_client import QdrantClient, models qdrant_client = QdrantClient( url="<YOUR_ENDPOINT>", api_key="<YOUR_API_KEY>", ) qdrant_client.create_collection( collection_name="{collection_name}", vectors_config={ "colbert": models.VectorParams( size=128, distance=models.Distance.COSINE, multivector_config=models.MultiVectorConfig( comparator=models.MultiVectorComparator.MAX_SIM ), ) } ) ⚠️ Correctly setting the multivector_config parameter is essential to using ColBERT-style models in Qdrant. Inserting Documents Into Multi-vector Collections import requests from qdrant_client import QdrantClient, models url = 'https://api.jina.ai/v1/multi-vector' headers = { 'Content-Type': 'application/json', 'Authorization': 'Bearer <YOUR BEARER>' } data = { 'model': 'jina-colbert-v2', 'input_type': 'query', 'embedding_type': 'float', 'input': [ 'Your text string goes here', 'You can send multiple texts', 'Each text can be up to 8192 tokens long' ] } response = requests.post(url, headers=headers, json=data) rows = response.json()["data"] qdrant_client = QdrantClient( url="<YOUR_ENDPOINT>", api_key="<YOUR_API_KEY>", ) for i, row in enumerate(rows): qdrant_client.upsert( collection_name="{collection_name}", points=[ models.PointStruct( id=i, vector=row["embeddings"], payload={"text": data["input"][i]} ) ], )

Summary Jina ColBERT v2 (jina-colbert-v2) builds on the high performance of jina-colbert-v1-en and expands its capabilities to a wide range of global languages. With support for multiple embedding sizes, jina-colbert-v2 allows users to tune the precision/efficiency trade-off to suit their specific use cases, potentially offering significant savings in time and computing costs. This model combines all these features into a single, competitively priced package, accessible via an intuitive web API and compatible with any computing framework that supports HTTP requests. Try it out for yourself with 1 million free tokens to see how it can enhance your applications and processes.

Categories: star Featured Press release rss_feed Top-5 similar articles play_arrow

## SUMMARY_CHUNKING

#### 7 chunk(s)

Today, we’re excited to release Jina ColBERT v2 (jina-colbert-v2), an advanced late interaction retrieval model built on the ColBERT architecture. This new language model improves performance of jina-colbert-v1-en and adds multilingual support and dynamic output dimensions. This new release highlights the following features: Superior retrieval performance compared to the original ColBERT-v2 (+6.5%) and our previous release, jina-colbert-v1-en(+5.4%). Multilingual support for 89 languages, delivering strong performance across major global languages. User-controlled output embedding sizes through Matryoshka representation learning, enabling users to flexibly balance between efficiency and precision. Technical Summary of jina-colbert-v2 The full technical report can be found on arXiv: Jina-ColBERT-v2: A General-Purpose Multilingual Late Interaction Retriever Multi-vector dense models, such as ColBERT, have proven highly effective in information retrieval. ColBERT’s late interaction scoring approximates the joint query-document attention seen in cross-encoders while maintaining inference efficiency closer to traditional dense retrieval models, thanks to its bi-encoder architecture and recent optimizations in indexing and search. In this paper, we introduce several improvements to the ColBERT model architecture and training pipeline, leveraging techniques successful in the more established single-vector embedding model paradigm, particularly those suited for heterogeneous multilingual data. Our new model, Jina-ColBERT-v2, demonstrates strong performance across a range of English and multilingual retrieval tasks, while also cutting storage requirements by up to 50% compared to previous models. arXiv.org Rohan Jha jina-colbert-v2 jina-colbert-v1-en Original ColBERTv2 Average of 14 English BEIR tasks 0.521 0.494 0.489 Multilingual 89 languages English-only English-only Output dimensions 128, 96, or 64 Fixed 128 Fixed 128 Max query length 32 tokens 32 tokens 32 tokens Max document length 8192 tokens 8192 tokens 512 tokens Parameters 560M 137M 110M Model size 1.1GB 550MB 438MB

Getting Started with Jina ColBERT v2 Jina ColBERT v2 is available via the Jina Search Foundation API, the AWS marketplace, and on Azure. It is also available for non-commercial use only (CC BY-NC-4.0) via Hugging Face. Via Jina Search Foundation API

For Embedding The following curl command shows howto specify the input and options to get document embeddings from jina-colbert-v2 via the Jina Embeddings API. To get vectors of your preferred size, specify 128 or 64 for the dimensions parameter. This parameter is optional and the default value is 128. Input documents will be truncated if longer than 8192 tokens. Specify your Jina API key in the authorization header Authorization: Bearer <YOUR JINA API KEY>: curl https://api.jina.ai/v1/multi-vector \\ -H "Content-Type: application/json" \\ -H "Authorization: Bearer <YOUR JINA API KEY>" \\ -d '{ "model": "jina-colbert-v2", "dimensions": 128, # Or 64 for half-size vectors "input_type": "document", # For query embeddings see below "embedding_type": "float", "input": [ "Your document text string goes here", "You can send multiple texts", "Each text can be up to 8192 tokens long" ]}' To get query embeddings, set the input_type parameter to query instead of document. Note that queries have much stricter size limits than documents. They will be truncated at 32 tokens. Query encoding will always return 32 tokens, including embeddings for the padding if less than 32 tokens long. curl https://api.jina.ai/v1/multi-vector \\ -H "Content-Type: application/json" \\ -H "Authorization: Bearer <YOUR JINA API KEY>" \\ -d '{ "model": "jina-colbert-v2", "dimensions": 128, # Or 64 for half-size vectors "input_type": "query", # This must be specified for query embeddings "embedding_type": "float", "input": [ "Your query text string goes here", "You can send multiple texts", "Each query text can be up to 32 tokens long" ]}' Embedding API Multimodal, bilingual long-context embeddings for your search and RAG. For Reranking To use jina-colbert-v2 via the Jina Reranker API, passing in one query and several documents and getting back rankable match scores, construct your request like the one below: curl https://api.jina.ai/v1/rerank \\ -H "Content-Type: application/json" \\ -H "Authorization: Bearer <YOUR JINA API KEY>" \\ -d '{ "model": "jina-colbert-v2", "query": "What is the population of Berlin?", "top_n": 3, "documents": [ "Berlin's population grew by 0.7 percent in 2023 compared with the previous year. Accordingly, around 27,300 more residents lived in Berlin at the end of the last year than in 2022. Those of 30 to under 40 years old form the numerically largest age group. With roughly 881,000 foreign residents from around 170 nations and an average age of the population of 42.5 years old.", "Mount Berlin is a glacier-covered volcano in Marie Byrd Land, Antarctica, 100 kilometres (62 mi) from the Amundsen Sea. It is a roughly 20-kilometre-wide (12 mi) mountain with parasitic vents that consists of two coalesced volcanoes: Berlin proper with the 2-kilometre-wide (1.2 mi) Berlin Crater and Merrem Peak with a 2.5-by-1-kilometre-wide (1.55 mi × 0.62 mi) crater, 3.5 kilometres (2.2 mi) away from Berlin.", "Population as of 31.12.2023 by nationality and federal states Land\\tTotal\\tGermans\\tForeigners\\tincluding EU-states number\\t%\\tnumber\\t%", "The urban area of Berlin has a population of over 4.5 million and is therefore the most populous urban area in Germany. The Berlin-Brandenburg capital region has around 6.2 million inhabitants and is Germany's second-largest metropolitan region after the Rhine-Ruhr region, and the sixth-biggest metropolitan region by GDP in the European Union.", "Irving Berlin (born Israel Beilin) was an American composer and songwriter. His music forms a large part of the Great American Songbook. Berlin received numerous honors including an Academy Award, a Grammy Award, and a Tony Award.", "Berlin is a town in the Capitol Planning Region, Connecticut, United States. The population was 20,175 at the 2020 census.", "Berlin is the capital and largest city of Germany, both by area and by population. Its more than 3.85 million inhabitants make it the European Union's most populous city, as measured by population within city limits.", "Berlin, Berlin ist eine für die ARD produzierte Fernsehserie, die von 2002 bis 2005 im Vorabendprogramm des Ersten ausgestrahlt wurde. Regie führten unter anderem Franziska Meyer Price, Christoph Schnee, Sven Unterwaldt Jr. und Titus Selge." ] }' Note the top_n argument, which specifies the number of documents you want to retrieve. For example, if your application only uses the top match, set top_n to 1. For code snippets in Python and other programming languages and frameworks, go to the Jina AI Embeddings API page, or select jina-colbert-v2 from the drop-down menu on the Jina Reranker API page.

Reranker API Maximize the search relevancy and RAG accuracy at ease.

Summary Jina ColBERT v2 (jina-colbert-v2) builds on the high performance of jina-colbert-v1-en and expands its capabilities to a wide range of global languages. With support for multiple embedding sizes, jina-colbert-v2 allows users to tune the precision/efficiency trade-off to suit their specific use cases, potentially offering significant savings in time and computing costs. This model combines all these features into a single, competitively priced package, accessible via an intuitive web API and compatible with any computing framework that supports HTTP requests. Try it out for yourself with 1 million free tokens to see how it can enhance your applications and processes.

Categories: star Featured Press release rss_feed Top-5 similar articles play_arrow GET TOP-5 Select reranker Read more September 18, 2024 • 10 minutes read Jina Embeddings V3: A Frontier Multilingual Embedding Model jina-embeddings-v3 is a frontier multilingual text embedding model with 570M parameters and 8192 token-length, outperforming the latest proprietary embeddings from OpenAI and Cohere on MTEB. September 11, 2024 • 12 minutes read

Reader-LM: Small Language Models for Cleaning and Converting HTML to Markdown Reader-LM-0.5B and Reader-LM-1.5B are two novel small language models inspired by Jina Reader, designed to convert raw, noisy HTML from the open web into clean markdown. June 25, 2024 • 15 minutes read Jina Reranker v2 for Agentic RAG: Ultra-Fast, Multilingual, Function-Calling & Code Search

## JINA-SEGMENTER-API

#### 201 chunk(s)

search


notifications


NEWS


PRODUCTS


COMPANY


star


Featured


Press release


August 30, 2024


Jina ColBERT v2: Multilingual Late Interaction Retriever for Embedding and Reranking


Jina ColBERT v2 supports 89 languages with superior retrieval performance, user-controlled output dimensions, and 8192 token-length.


Jina AI • 10 minutes read



Today, we’re excited to release Jina ColBERT v2 (jina-colbert-v2), an advanced late interaction retrieval model built on the ColBERT architecture. This new language model improves performance of jina-colbert-v1-en and adds multilingual support and dynamic output dimensions.



This new release highlights the following features:



Superior retrieval performance compared to the original ColBERT-v2 (+6.5%) and our previous release, jina-colbert-v1-en(+5.4%).


Multilingual support for 89 languages, delivering strong performance across major global languages.


User-controlled output embedding sizes through Matryoshka representation learning, enabling users to flexibly balance between efficiency and precision.


Technical Summary of jina-colbert-v2



The full technical report can be found on arXiv:



Jina-ColBERT-v2: A General-Purpose Multilingual Late Interaction Retriever


Multi-vector dense models, such as ColBERT, have proven highly effective in information retrieval. ColBERT’s late interaction scoring approximates the joint query-document attention seen in cross-encoders while maintaining inference efficiency closer to traditional dense retrieval models, thanks to its bi-encoder architecture and recent optimizations in indexing and search. In this paper, we introduce several improvements to the ColBERT model architecture and training pipeline, leveraging techniques successful in the more established single-vector embedding model paradigm, particularly those suited for heterogeneous multilingual data. Our new model, Jina-ColBERT-v2, demonstrates strong performance across a range of English and multilingual retrieval tasks, while also cutting storage requirements by up to 50% compared to previous models.


arXiv.org


Rohan Jha


	jina-colbert-v2	jina-colbert-v1-en	Original ColBERTv2


Average of 14 English


BEIR tasks	0.521	0.494	0.489


Multilingual	89 languages	English-only	English-only


Output dimensions	128, 96, or 64	Fixed 128	Fixed 128


Max query length	32 tokens	32 tokens	32 tokens


Max document length	8192 tokens	8192 tokens	512 tokens


Parameters	560M	137M	110M


Model size	1.1GB	550MB	438MB


Asymmetric Embedding in ColBERT



ColBERT builds on the BERT architecture by adding late interaction and asymmetric query-document encoding.



What is ColBERT and Late Interaction and Why They Matter in Search?


Jina AI’s ColBERT on Hugging Face has set Twitter abuzz, bringing a fresh perspective to search with its 8192-token capability. This article unpacks the nuances of ColBERT and ColBERTv2, showcasing their innovative designs and why their late interaction feature is a game-changer for search.



The asymmetric nature of ColBERT means that when using models like jina-colbert-v2 or jina-colbert-v1-en, you need to specify whether you are embedding a query, a document, or both (for reranking purposes). This added flexibility enhances performance over homogeneous embedding models in retrieval tasks.



Multilingual Support For Over 89 Languages



Jina ColBERT v2 has extensive multilingual capabilities, designed to meet the demands of modern, globalized information retrieval and AI applications. The training corpus for jina-colbert-v2 incorporates 89 languages, with additional stages of training for major international languages including Arabic, Chinese, English, French, German, Japanese, Russian, and Spanish, as well as programming languages. The training also included a corpus of aligned bilingual texts to unlock cross-lingual potentials, allowing queries and documents in different languages to be matched in reranking/retrieval tasks.



Pre-training dataset data distribution by language (specified by ISO-639 code) in logarithmic scale.



Today, Jina ColBERT v2 stands out as the only multilingual ColBERT-like model that generates compact embeddings, significantly outperforming BM25-based retrieval across all languages tested on MIRACL benchmarks.



Jina ColBERT v2 performance over 16 languages, compared to BM25, on MIRACL benchmarks.



Furthermore, on English-language retrieval tasks, Jina ColBERT v2 exceeds the performance of its predecessor jina-colbert-v1-en and the original ColBERT v2 model, with comparable performance to the highly specialized English-only AnswerAI-ColBERT-small model.



Model Name	Average score


(14 BEIR English-only benchmarks)


	Multilingual Support


jina-colbert-v2	0.521	Multilingual


jina-colbert-v1-en	0.494	English-only


ColBERT v2.0	0.489	English-only


AnswerAI-ColBERT-small	0.549	English-only


Evaluation of jina-colbert-v2 on a selection of English-only datasets from BEIR benchmark.


Matryoshka Representation Learning



Matryoshka Representation Learning is a technique for training models to support different output vector sizes while minimizing any loss in accuracy. We train the hidden layers of the network with several different linear projection heads — the final layers of a neural network — each supporting a different output size. Jina ColBERT v2 supports output vectors of 128, 96, and 64 dimensions.



Jina ColBERT v2 produces 128-dimension output embeddings by default, but can produce 96 and 64 dimensions that are nearly identical in performance but are 25% and 50% shorter respectively.



The table below shows the nDGC performance of jina-colbert-v2 for the top ten results (nDGC@10) over six datasets from the BEIR benchmark. You can see here that the difference in performance between 128 dimensions and 96 is barely 1% and under 1.5% between 128 and 64 dimensions.



Output Dimensions	Average Score


(nDGC@10 for 6 benchmarks)



128	0.565


96	0.558


64	0.556


Jina ColBERT v2 performance at different output dimensions.



Reducing the size of the output vectors saves space and speeds up applications like vector-based information retrieval that have to compare different vectors or measure the distance between them.



This has significant cost consequences, even just in terms of reduced storage. For example, using Qdrant’s cloud cost estimator, storing 100 million documents on AWS with 128-dimension vectors for each has an estimated cost of US$1,319.24 per month. At 64 dimensions, this falls to US$659.62.



Getting Started with Jina ColBERT v2



Jina ColBERT v2 is available via the Jina Search Foundation API, the AWS marketplace, and on Azure. It is also available for non-commercial use only (CC BY-NC-4.0) via Hugging Face.



Via Jina Search Foundation API


For Embedding



The following curl command shows how to specify the input and options to get document embeddings from jina-colbert-v2 via the Jina Embeddings API. To get vectors of your preferred size, specify 128 or 64 for the dimensions parameter. This parameter is optional and the default value is 128.



Input documents will be truncated if longer than 8192 tokens.



Specify your Jina API key in the authorization header Authorization: Bearer <YOUR JINA API KEY>:



curl https://api.jina.ai/v1/multi-vector \\


	 -H "Content-Type: application/json" \\
	 -H "Authorization: Bearer <YOUR JINA API KEY>" \\
	 -d '{
	"model": "jina-colbert-v2",
	"dimensions": 128, # Or 64 for half-size vectors
	"input_type": "document", # For query embeddings see below
	"embedding_type": "float",
	"input": [
		"Your document text string goes here", 
		"You can send multiple texts", 
		"Each text can be up to 8192 tokens long"
    ]}'


To get query embeddings, set the input_type parameter to query instead of document. Note that queries have much stricter size limits than documents. They will be truncated at 32 tokens. Query encoding will always return 32 tokens, including embeddings for the padding if less than 32 tokens long.



curl https://api.jina.ai/v1/multi-vector \\


	 -H "Content-Type: application/json" \\
	 -H "Authorization: Bearer <YOUR JINA API KEY>" \\
	 -d '{
	"model": "jina-colbert-v2",
	"dimensions": 128, # Or 64 for half-size vectors	
	"input_type": "query", # This must be specified for query embeddings
	"embedding_type": "float",
	"input": [
		"Your query text string goes here", 
		"You can send multiple texts", 
		"Each query text can be up to 32 tokens long"
    ]}'


Embedding API


Multimodal, bilingual long-context embeddings for your search and RAG.


For Reranking



To use jina-colbert-v2 via the Jina Reranker API, passing in one query and several documents and getting back rankable match scores, construct your request like the one below:



curl https://api.jina.ai/v1/rerank \\


	 -H "Content-Type: application/json" \\
	 -H "Authorization: Bearer <YOUR JINA API KEY>" \\
	 -d '{
      "model": "jina-colbert-v2",
      "query": "What is the population of Berlin?",
      "top_n": 3,
      "documents": [
        "Berlin's population grew by 0.7 percent in 2023 compared with the previous year. Accordingly, around 27,300 more residents lived in Berlin at the end of the last year than in 2022. Those of 30 to under 40 years old form the numerically largest age group. With roughly 881,000 foreign residents from around 170 nations and an average age of the population of 42.5 years old.",
        "Mount Berlin is a glacier-covered volcano in Marie Byrd Land, Antarctica, 100 kilometres (62 mi) from the Amundsen Sea. It is a roughly 20-kilometre-wide (12 mi) mountain with parasitic vents that consists of two coalesced volcanoes: Berlin proper with the 2-kilometre-wide (1.2 mi) Berlin Crater and Merrem Peak with a 2.5-by-1-kilometre-wide (1.55 mi × 0.62 mi) crater, 3.5 kilometres (2.2 mi) away from Berlin.",
        "Population as of 31.12.2023 by nationality and federal states Land\\tTotal\\tGermans\\tForeigners\\tincluding EU-states number\\t%\\tnumber\\t%",
        "The urban area of Berlin has a population of over 4.5 million and is therefore the most populous urban area in Germany. The Berlin-Brandenburg capital region has around 6.2 million inhabitants and is Germany's second-largest metropolitan region after the Rhine-Ruhr region, and the sixth-biggest metropolitan region by GDP in the European Union.",
        "Irving Berlin (born Israel Beilin) was an American composer and songwriter. His music forms a large part of the Great American Songbook. Berlin received numerous honors including an Academy Award, a Grammy Award, and a Tony Award.",
        "Berlin is a town in the Capitol Planning Region, Connecticut, United States. The population was 20,175 at the 2020 census.",
        "Berlin is the capital and largest city of Germany, both by area and by population. Its more than 3.85 million inhabitants make it the European Union's most populous city, as measured by population within city limits.",
        "Berlin, Berlin ist eine für die ARD produzierte Fernsehserie, die von 2002 bis 2005 im Vorabendprogramm des Ersten ausgestrahlt wurde. Regie führten unter anderem Franziska Meyer Price, Christoph Schnee, Sven Unterwaldt Jr. und Titus Selge."
        ]
    }'


Note the top_n argument, which specifies the number of documents you want to retrieve. For example, if your application only uses the top match, set top_n to 1.



For code snippets in Python and other programming languages and frameworks, go to the Jina AI Embeddings API page, or select jina-colbert-v2 from the drop-down menu on the Jina Reranker API page.



Reranker API


Maximize the search relevancy and RAG accuracy at ease.


Via Stanford ColBERT



You can also use Jina ColBERT v2 as a drop-in replacement for ColBERT v2 in the Stanford ColBERT library. Just specify jinaai/jina-colbert-v2 as the model source:



from colbert.infra import ColBERTConfig


from colbert.modeling.checkpoint import Checkpoint



ckpt = Checkpoint("jinaai/jina-colbert-v2", colbert_config=ColBERTConfig())


docs = ["Your list of texts"] 


query_vectors = ckpt.queryFromText(docs)



️


You must install einops and flash_attn to use the above code.


Via RAGatouille



Jina ColBERT v2 is similarly integrated into RAGatouille. You can download and use it via the method RAGPretrainedModel.from_pretrained():



from ragatouille import RAGPretrainedModel



RAG = RAGPretrainedModel.from_pretrained("jinaai/jina-colbert-v2")


docs = ["Your list of texts"]


RAG.index(docs, index_name="your_index_name")


query = "Your query"


results = RAG.search(query)



️


You must install einops and flash_attn to use the above code.


Via Qdrant



Since version 1.10, Qdrant has added support for multi-vectors and late-interaction models. Existing users of Qdrant engines, whether local or managed cloud versions, can benefit by directly integrating jina-colbert-v2 using Qdrant’s client.



Creating a new Collection using the MAX_SIM operation



from qdrant_client import QdrantClient, models



qdrant_client = QdrantClient(


    url="<YOUR_ENDPOINT>",
    api_key="<YOUR_API_KEY>",


qdrant_client.create_collection(


    collection_name="{collection_name}",
    vectors_config={
        "colbert": models.VectorParams(
            size=128,
            distance=models.Distance.COSINE,
            multivector_config=models.MultiVectorConfig(
                comparator=models.MultiVectorComparator.MAX_SIM
            ),
        )
    }


️


Correctly setting the multivector_config parameter is essential to using ColBERT-style models in Qdrant.



Inserting Documents Into Multi-vector Collections



import requests


from qdrant_client import QdrantClient, models



url = 'https://api.jina.ai/v1/multi-vector'



headers = {


    'Content-Type': 'application/json',
    'Authorization': 'Bearer <YOUR BEARER>'


data = {


    'model': 'jina-colbert-v2',
    'input_type': 'query',
    'embedding_type': 'float',
    'input': [
        'Your text string goes here',
        'You can send multiple texts',
        'Each text can be up to 8192 tokens long'
    ]


response = requests.post(url, headers=headers, json=data)


rows = response.json()["data"]



qdrant_client = QdrantClient(


    url="<YOUR_ENDPOINT>",
    api_key="<YOUR_API_KEY>",


for i, row in enumerate(rows):


    qdrant_client.upsert(
        collection_name="{collection_name}",
        points=[
            models.PointStruct(
                id=i,  
                vector=row["embeddings"],  
                payload={"text": data["input"][i]} 
            )
        ],
    )


Querying Collections



from qdrant_client import QdrantClient, models


import requests



url = 'https://api.jina.ai/v1/multi-vector'



headers = {


    'Content-Type': 'application/json',
    'Authorization': 'Bearer <YOUR BEARER>'


data = {


    'model': 'jina-colbert-v2',
    "input_type": "query",
    "embedding_type": "float",
    "input": [
        "how many tokens in an input do Jina AI's embedding models support?"
    ]


response = requests.post(url, headers=headers, json=data)


vector = response.json()["data"][0]["embeddings"]




qdrant_client = QdrantClient(


    url="<YOUR_ENDPOINT>",
    api_key="<YOUR_API_KEY>",


results = qdrant_client.query_points(


    collection_name="{collection_name}",
    query=vector,


print(results)


Summary



Jina ColBERT v2 (jina-colbert-v2) builds on the high performance of jina-colbert-v1-en and expands its capabilities to a wide range of global languages. With support for multiple embedding sizes, jina-colbert-v2 allows users to tune the precision/efficiency trade-off to suit their specific use cases, potentially offering significant savings in time and computing costs.



This model combines all these features into a single, competitively priced package, accessible via an intuitive web API and compatible with any computing framework that supports HTTP requests. Try it out for yourself with 1 million free tokens to see how it can enhance your applications and processes.



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


June 25, 2024 • 15 minutes read


Jina Reranker v2 for Agentic RAG: Ultra-Fast, Multilingual, Function-Calling & Code Search


Jina Reranker v2 is the best-in-class reranker built for Agentic RAG. It features function-calling support, multilingual retrieval for over 100 languages, code search capabilities, and offers a 6x speedup over v1.


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