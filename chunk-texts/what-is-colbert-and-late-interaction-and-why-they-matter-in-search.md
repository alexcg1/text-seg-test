# what-is-colbert-and-late-interaction-and-why-they-matter-in-search

## SIMPLE_CHUNKING

#### 9 chunk(s)

search notifications NEWS PRODUCTS COMPANY star Featured Tech blog February 20, 2024 What is ColBERT and Late Interaction and Why They Matter in Search? Jina AI's ColBERT on Hugging Face has set Twitter abuzz, bringing a fresh perspective to search with its 8192-token capability. This article unpacks the nuances of ColBERT and ColBERTv2, showcasing their innovative designs and why their late interaction feature is a game-changer for search. Han Xiao • 16 minutes read Jina ColBERT v2: Multilingual Late Interaction Retriever for Embedding and Reranking Jina ColBERT v2 supports 89 languages with superior retrieval performance, user-controlled output dimensions, and 8192 token-length. Update: On Aug. 31st 2024, we released the 2nd version of Jina-ColBERT, with improved performance, multilingual support over 89 languages and flexible output dimensions. Check the release post for more details. Last Friday, the release of the ColBERT model by Jina AI on Hugging Face sparked significant excitement across the AI community, particularly on Twitter/X. While many are familiar with the groundbreaking BERT model, the buzz around ColBERT has left some wondering: What makes ColBERT stand out in the crowded field of information retrieval technologies? Why the AI community is excited about 8192-length ColBERT? This article delves into the intricacies of ColBERT and ColBERTv2, highlighting their design, improvements, and the surprising effectiveness of ColBERT's late interaction.

Reranker API Maximize the search relevancy and RAG accuracy at ease What is ColBERT? The name "ColBERT" stands for Contextualized Late Interaction over BERT, a model stems from the Stanford University, that leverages the deep language understanding of BERT while introducing a novel interaction mechanism. This mechanism, known as late interaction, allows for efficient and precise retrieval by processing queries and documents separately until the final stages of the retrieval process. Specifically, there are two versions of the model: ColBERT: The initial model was the brainchild of Omar Khattab and Matei Zaharia, presenting a novel approach to information retrieval through the "ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT" paper. Their work was published in SIGIR 2020. ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT Recent progress in Natural Language Understanding (NLU) is driving fast-paced advances in Information Retrieval (IR), largely owed to fine-tuning deep language models (LMs) for document ranking. While remarkably effective, the ranking models based on these LMs increase computational cost by orders of magnitude over prior approaches, particularly as they must feed each query-document pair through a massive neural network to compute a single relevance score. To tackle this, we present ColBERT, a novel ranking model that adapts deep LMs (in particular, BERT) for efficient retrieval. ColBERT introduces a late interaction architecture that independently encodes the query and the document using BERT and then employs a cheap yet powerful interaction step that models their fine-grained similarity. By delaying and yet retaining this fine-granular interaction, ColBERT can leverage the expressiveness of deep LMs while simultaneously gaining the ability to pre-compute document representations offline, considerably speeding up query processing. Beyond reducing the cost of re-ranking the documents retrieved by a traditional model, ColBERT’s pruning-friendly interaction mechanism enables leveraging vector-similarity indexes for end-to-end retrieval directly from a large document collection. We extensively evaluate ColBERT using two recent passage search datasets. Results show that ColBERT’s effectiveness is competitive with existing BERT-based models (and outperforms every non-BERT baseline), while executing two orders-of-magnitude faster and requiring four orders-of-magnitude fewer FLOPs per query. arXiv.org Omar Khattab The original ColBERT paper that introduces the "late interaction". ColBERTv2: Building on the foundational work, Omar Khattab continued his research, collaborating with Barlas Oguz, Matei Zaharia, and Michael S. Bernstein to introduce "ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction," presented at SIGIR 2021. This next iteration of ColBERT addressed previous limitations and introduced key improvements, such as denoised supervision and residual compression, enhancing both the model's retrieval effectiveness and its storage efficiency. ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction Neural information retrieval (IR) has greatly advanced search and other knowledge-intensive language tasks. While many neural IR methods encode queries and documents into single-vector representations, late interaction models produce multi-vector representations at the granularity of each token and decompose relevance modeling into scalable token-level computations. This decomposition has been shown to make late interaction more effective, but it inflates the space footprint of these models by an order of magnitude. In this work, we introduce ColBERTv2, a retriever that couples an aggressive residual compression mechanism with a denoised supervision strategy to simultaneously improve the quality and space footprint of late interaction. We evaluate ColBERTv2 across a wide range of benchmarks, establishing state-of-the-art quality within and outside the training domain while reducing the space footprint of late interaction models by 6--10 × ×. arXiv.org Keshav Santhanam ColBERTv2 adding denoised supervision and residual compression to improve the training data's quality and reduce the space footprint. Understand ColBERT's Design

Given that ColBERTv2's architecture remains very similar to that of the original ColBERT, with its key innovations revolving around training techniques and compression mechanisms, we will first delve into the foundational aspects of the original ColBERT. What is late interaction in ColBERT? "Interaction" refers to the process of evaluating the relevance between a query and a document by comparing their representations. "Late interaction" is the essence of ColBERT. The term is derived from the model's architecture and processing strategy, where the interaction between the query and document representations occurs late in the process, after both have been independently encoded. This contrasts with "early interaction" models, where query and document embeddings interact at earlier stages, typically before or during their encoding by the model. Interaction Type Models Early Interaction BERT, ANCE, DPR, Sentence-BERT, DRMM, KNRM, Conv-KNRM, etc. Late Interaction ColBERT, ColBERTv2 Early interaction can increase computational complexity since it requires considering all possible query-document pairs, making it less efficient for large-scale applications. Late interaction models like ColBERT optimize for efficiency and scalability by allowing for the pre-computation of document representations and employing a more lightweight interaction step at the end, which focuses on the already encoded representations. This design choice enables faster retrieval times and reduced computational demands, making it more suitable for processing large document collections. Schematic diagrams illustrating query–document interaction paradigms in neural IR, with ColBERT's late interaction on the left-most. No interaction: cosine similarity of document and query embeddings Many practical vector databases and neural search solutions depend on fast cosine similarity matching between document and query embeddings. While appealing for its straightforwardness and computational efficiency, this method, often referred to as "no interaction" or "not interaction-based" has been found to underperform in comparison to models that incorporate some form of interaction between queries and documents. The core limitation of the "no interaction" approach lies in its inability to capture the complex nuances and relationships between query and document terms. Information retrieval, at its heart, is about understanding and matching the intent behind a query with the content within a document. This process often requires a deep, contextual understanding of the terms involved, something that single, aggregated embeddings for documents and queries struggle to provide. Query and document encoders in ColBERT ColBERT's encoding strategy is grounded in the BERT model, known for its deep contextual understanding of language. The model generates dense vector representations for each token in a query or document, creating a bag of contextualized embeddings for a query and a bag for a document, respectively. This facilitates a nuanced comparison of their embeddings during the late interaction phase. Query encoder of ColBERT For a query 𝑄 Q with tokens 𝑞 1 , 𝑞 2 , . . . , 𝑞 𝑙 q 1 ​ ,q 2 ​ ,...,q l ​ , the process begins by tokenizing 𝑄 Q into BERT-based WordPiece tokens and prepending a special [Q] token. This [Q] token, positioned right after BERT’s [CLS] token, signals the start of a query. If the query is shorter than a predefined number of tokens 𝑁 𝑞 N q ​ , it is padded with [mask] tokens up to 𝑁 𝑞 N q ​ ; otherwise, it's truncated to the first 𝑁 𝑞 N q ​ tokens. The padded sequence is then passed through BERT, followed by a CNN (Convolutional Neural Network) and normalization. The output is a set of embedding vectors termed as 𝐸 𝑞 E q ​ below: 𝐸 𝑞 : = N o r m a l i z e ( B E R T ( [ 𝑄 ] , 𝑞 0 , 𝑞 1 , … , 𝑞 𝑙 [ 𝑚 𝑎 𝑠 𝑘 ] , [ 𝑚 𝑎 𝑠 𝑘 ] , … , [ 𝑚 𝑎 𝑠 𝑘 ] ) ) E q ​ :=Normalize(BERT([Q],q 0 ​ ,q 1 ​ ,…,q l ​ [mask],[mask],…,[mask])) Document encoder of ColBERT Similarly, for a document 𝐷 D with tokens 𝑑 1 , 𝑑 2 , . . . , 𝑑 𝑛 d 1 ​ ,d 2 ​ ,...,d n ​ , a [D] token is prepended to indicate the start of a document. This sequence, without the need for padding, undergoes the same process, results in a set of embedding vectors termed as 𝐸 𝑑 E d ​ below: 𝐸 𝑑 : = F i l t e r ( N o r m a l i z e ( B E R T ( [ 𝐷 ] , 𝑑 0 , 𝑑 1 , . . . , 𝑑 𝑛 ) ) ) E d ​ :=Filter(Normalize(BERT([D],d 0 ​ ,d 1 ​ ,...,d n ​ ))) The use of [mask] tokens for padding queries (coined as query augmentation in the paper) ensures uniform length across all queries, facilitating batch processing. The [Q] and [D] tokens explicitly mark the start of queries and documents, respectively, aiding the model in distinguishing between the two types of inputs. Comparing ColBERT to cross-encoders Cross-encoders process pairs of queries and documents together, making them highly accurate but less efficient for large-scale tasks due to the computational cost of evaluating every possible pair. They excel in specific scenarios where the precise scoring of sentence pairs is necessary, such as in semantic similarity tasks or detailed content comparison. However, this design limits their applicability in situations requiring rapid retrieval from large datasets, where pre-computed embeddings and efficient similarity calculations are paramount. In contrast, ColBERT’s late interaction model allows for pre-computation of document embeddings, significantly speeding up the retrieval process without compromising the depth of semantic analysis. This method, though seemingly counter-intuitive when compared to the direct approach of cross-encoders, offers a scalable solution for real-time and large-scale information retrieval tasks. It represents a strategic compromise between computational efficiency and the quality of interaction modeling. Finding the top-K documents using ColBERT Once we have embeddings for the query and documents, finding the most relevant top-K documents becomes straightforward (but not as straightforward as computing cosine of two vectors). The key operations include a batch dot-product to compute term-wise similarities, max-pooling across document terms to find the highest similarity per query term, and summation across query terms to derive the total document score, followed by sorting the documents based on these scores. The pseudo PyTorch code is described below: import torch def compute_relevance_scores(query_embeddings, document_embeddings, k): """ Compute relevance scores for top-k documents given a query. :param query_embeddings: Tensor representing the query embeddings, shape: [num_query_terms, embedding_dim] :param document_embeddings: Tensor representing embeddings for k documents, shape: [k, max_doc_length, embedding_dim] :param k: Number of top documents to re-rank :return: Sorted document indices based on their relevance scores """ # Ensure document_embeddings is a 3D tensor: [k, max_doc_length, embedding_dim] # Pad the k documents to their maximum length for batch operations # Note: Assuming document_embeddings is already padded and moved to GPU # Compute batch dot-product of Eq (query embeddings) and D (document embeddings) # Resulting shape: [k, num_query_terms, max_doc_length] scores = torch.matmul(query_embeddings.unsqueeze(0), document_embeddings.transpose(1, 2)) # Apply max-pooling across document terms (dim=2) to find the max similarity per query term # Shape after max-pool: [k, num_query_terms] max_scores_per_query_term = scores.max(dim=2).values # Sum the scores across query terms to get the total score for each document # Shape after sum: [k] total_scores = max_scores_per_query_term.sum(dim=1) # Sort the documents based on their total scores sorted_indices = total_scores.argsort(descending=True) return sorted_indices Note that this procedure is used in both training and re-ranking at inference time.

The ColBERT model is trained using a pairwise ranking loss, where the training data consists of triples ( 𝑞 , 𝑑 + , 𝑑 − ) (q,d + ,d − ), where 𝑞 q represents a query, 𝑑 + d + is a relevant (positive) document for the query, and 𝑑 − d − is a non-relevant (negative) document. The model aims to learn representations such that the similarity score between 𝑞 q and 𝑑 + d + is higher than the score between q and 𝑑 − d − . The training objective can be mathematically represented as minimizing the following loss function: L o s s = max ⁡ ( 0 , 1 − 𝑆 ( 𝑞 , 𝑑 + ) + 𝑆 ( 𝑞 , 𝑑 − ) ) Loss=max(0,1−S(q,d + )+S(q,d − )) , where 𝑆 ( 𝑞 , 𝑑 ) S(q,d) denotes the similarity score computed by ColBERT between a query 𝑞 q and a document 𝑑 d. This score is obtained by aggregating the max-similarity scores of the best-matching embeddings between the query and the document, following the late interaction pattern described in the model architecture. This approach ensures that the model is trained to distinguish between relevant and irrelevant documents for a given query, by encouraging a larger margin in the similarity scores for positive and negative document pairs. Denoised supervision in ColBERTv2 Denoised supervision in ColBERTv2 refines the original training process by selecting challenging negatives and leveraging a cross-encoder for distillation. This sophisticated method of augmenting training data quality involves several steps: Initial Training: Utilizing the official triples from the MS MARCO dataset, comprising a query, a relevant document, and a non-relevant document. Indexing and Retrieval: Employing ColBERTv2's compression to index training passages, followed by retrieving top-k passages for each query. Cross-Encoder Reranking: Enhancing passage selection through reranking by a MiniLM cross-encoder, distilling its scores into ColBERTv2. Forming Training Tuples: Generating w-way tuples for training, incorporating both high and lower-ranked passages to create challenging examples. Iterative Refinement: Repeating the process to continually improve the selection of hard negatives, thereby enhancing model performance. Note, this process represents a sophisticated enhancement to the ColBERT training regime rather than a fundamental change to its architecture.

Hyperparameters of ColBERT The hyperparameters of ColBERT is summarized below: Hyperparameter Best Choice Reason Learning Rate 3 x 10^{-6} Selected for fine-tuning to ensure stable and effective model updates. Batch Size 32 Balances computational efficiency and the ability to capture sufficient information per update. Number of Embeddings per Query (Nq) 32 Fixed to ensure a consistent representation size across queries, aiding in efficient processing. Embedding Dimension (m) 128 Demonstrated to provide a good balance between representational power and computational efficiency. Training Iterations 200k (MS MARCO), 125k (TREC CAR) Chosen to ensure thorough learning while avoiding overfitting, with adjustments based on dataset characteristics. Bytes per Dimension in Embeddings 4 (re-ranking), 2 (end-to-end ranking) Trade-off between precision and space efficiency, with consideration for the application context (re-ranking vs. end-to-end). Vector-Similarity Function Cosine (re-ranking), (Squared) L2 (end-to-end) Selected based on performance and efficiency in the respective retrieval contexts. FAISS Index Partitions (P) 2000 Determines the granularity of the search space partitioning, impacting search efficiency. Nearest Partitions Searched (p) 10 Balances the breadth of the search against computational efficiency. Sub-vectors per Embedding (s) 16 Affects the granularity of quantization, influencing both search speed and memory usage. Index Representation per Dimension 16-bit values Chosen for the second stage of end-to-end retrieval to manage the trade-off between accuracy and space. Number of Layers in Encoders 12-layer BERT Optimal balance between depth of contextual understanding and computational efficiency. Max Query Length 128 The maximum number of tokens processed by the query encoder. This gets extended in Jina-ColBERT model. Max Document Length 512 The maximum number of tokens processed by the document encoder. This gets extended to 8192 in Jina-ColBERT model.

Hyperparameters of ColBERT The hyperparameters of ColBERT is summarized below: Hyperparameter Best Choice Reason Learning Rate 3 x 10^{-6} Selected for fine-tuning to ensure stable and effective model updates. Batch Size 32 Balances computational efficiency and the ability to capture sufficient information per update. Number of Embeddings per Query (Nq) 32 Fixed to ensure a consistent representation size across queries, aiding in efficient processing. Embedding Dimension (m) 128 Demonstrated to provide a good balance between representational power and computational efficiency. Training Iterations 200k (MS MARCO), 125k (TREC CAR) Chosen to ensure thorough learning while avoiding overfitting, with adjustments based on dataset characteristics. Bytes per Dimension in Embeddings 4 (re-ranking), 2 (end-to-end ranking) Trade-off between precision and space efficiency, with consideration for the application context (re-ranking vs. end-to-end). Vector-Similarity Function Cosine (re-ranking), (Squared) L2 (end-to-end) Selected based on performance and efficiency in the respective retrieval contexts. FAISS Index Partitions (P) 2000 Determines the granularity of the search space partitioning, impacting search efficiency. Nearest Partitions Searched (p) 10 Balances the breadth of the search against computational efficiency. Sub-vectors per Embedding (s) 16 Affects the granularity of quantization, influencing both search speed and memory usage. Index Representation per Dimension 16-bit values Chosen for the second stage of end-to-end retrieval to manage the trade-off between accuracy and space. Number of Layers in Encoders 12-layer BERT Optimal balance between depth of contextual understanding and computational efficiency. Max Query Length 128 The maximum number of tokens processed by the query encoder. This gets extended in Jina-ColBERT model. Max Document Length 512 The maximum number of tokens processed by the document encoder. This gets extended to 8192 in Jina-ColBERT model. The indexing strategy of ColBERT Unlike representation-based approaches that encode each document into one embedding vector, ColBERT encodes documents (and queries) into bags of embeddings, with each token in a document having its own embedding. This approach inherently means that for longer documents, more embeddings will be stored, which is a pain point of the original ColBERT, and later addressed by ColBERTv2. The key to managing this efficiently lies in ColBERT's use of vector database (e.g. FAISS) for indexing and retrieval, and its detailed indexing process which is designed to handle large volumes of data efficiently. The original ColBERT paper mentions several strategies to enhance the efficiency of indexing and retrieval, including: Offline Indexing: Document representations are computed offline, allowing for the pre-computation and storage of document embeddings. This process leverages batch processing and GPU acceleration to handle large document collections efficiently. Embedding Storage: Document embeddings can be stored using 32-bit or 16-bit values for each dimension, offering a trade-off between precision and storage requirements. This flexibility allows ColBERT to maintain a balance between effectiveness (in terms of retrieval performance) and efficiency (in terms of storage and computational costs). The introduction of residual compression in ColBERTv2, which is a novel approach not present in the original ColBERT, plays a key role in reducing the model's space footprint by 6–10× while preserving quality. This technique compresses the embeddings further by effectively capturing and storing only the differences from a set of fixed reference centroids. Effectiveness and Efficiency of ColBERT One might initially assume that incorporating BERT's deep contextual understanding into search would inherently require significant computational resources, making such an approach less feasible for real-time applications due to high latency and computational costs. However, ColBERT challenges and overturns this assumption through its innovative use of the late interaction mechanism. Here are some noteworthy points: Significant Efficiency Gains: ColBERT achieves an orders-of-magnitude reduction in computational costs (FLOPs) and latency compared to traditional BERT-based ranking models. Specifically, for a given model size (e.g., 12-layer "base" transformer encoder), ColBERT not only matches but in some cases exceeds the effectiveness of BERT-based models with dramatically lower computational demands. For instance, at a re-ranking depth of k=10, BERT requires nearly 180× more FLOPs than ColBERT; this gap widens as k increases, reaching 13900× at k=1000 and even 23000× at k=2000​​. Improved Recall and MRR@10 in End-to-End Retrieval: Contrary to the initial intuition that deeper interaction between query and document representations (as seen in early interaction models) would be necessary for high retrieval performance, ColBERT's end-to-end retrieval setup demonstrates superior effectiveness. For example, its Recall@50 exceeds the official BM25's Recall@1000 and almost all other models' Recall@200, underscoring the model's remarkable ability to retrieve relevant documents from a vast collection without direct comparison of each query-document pair​​. Practicality for Real-World Applications: The experimental results underline ColBERT's practical applicability for real-world scenarios. Its indexing throughput and memory efficiency make it suitable for indexing large document collections like MS MARCO within a few hours, retaining high effectiveness with a manageable space footprint. These qualities highlight ColBERT's suitability for deployment in production environments where both performance and computational efficiency are paramount​​. Scalability with Document Collection Size: Perhaps the most surprising conclusion is ColBERT's scalability and efficiency in handling large-scale document collections. The architecture allows for the pre-computation of document embeddings and leverages efficient batch processing for query-document interaction, enabling the system to scale effectively with the size of the document collection. This scalability is counter-intuitive when considering the complexity and depth of understanding required for effective document retrieval, showcasing ColBERT's innovative approach to balancing computational efficiency with retrieval effectiveness. Using jina-colbert-v1-en: a 8192-length ColBERTv2 model

Example usage of jina-colbert-v1-en This snippet outlines the indexing process with Jina-ColBERT, showcasing its support for long documents. from colbert import Indexer from colbert.infra import Run, RunConfig, ColBERTConfig n_gpu: int = 1 # Set your number of available GPUs experiment: str = "" # Name of the folder where the logs and created indices will be stored index_name: str = "" # The name of your index, i.e. the name of your vector database if __name__ == "__main__": with Run().context(RunConfig(nranks=n_gpu, experiment=experiment)): config = ColBERTConfig( doc_maxlen=8192 # Our model supports 8k context length for indexing long documents ) indexer = Indexer( checkpoint="jinaai/jina-colbert-v1-en", config=config, ) documents = [ "ColBERT is an efficient and effective passage retrieval model.", "Jina-ColBERT is a ColBERT-style model but based on JinaBERT so it can support both 8k context length.", "JinaBERT is a BERT architecture that supports the symmetric bidirectional variant of ALiBi to allow longer sequence length.", "Jina-ColBERT model is trained on MSMARCO passage ranking dataset, following a very similar training procedure with ColBERTv2.", "Jina-ColBERT achieves the competitive retrieval performance with ColBERTv2.", "Jina is an easier way to build neural search systems.", "You can use Jina-ColBERT to build neural search systems with ease.", # Add more documents here to ensure the clustering work correctly ] indexer.index(name=index_name, collection=documents)

Use jina-colbert-v1-en in RAGatouille RAGatouille isa new Python library that facilitates the use of advanced retrieval methods within RAG pipelines. It's designed for modularity and easy integration, allowing users to leverage state-of-the-art research seamlessly. The main goal of RAGatouille is to simplify the application of complex models like ColBERT in RAG pipelines, making it accessible for developers to utilize these methods without needing deep expertise in the underlying research. Thanks to Benjamin Clavié, you can now use jina-colbert-v1-en easily: from ragatouille import RAGPretrainedModel # Get your model & collection of big documents ready RAG = RAGPretrainedModel.from_pretrained("jinaai/jina-colbert-v1-en") my_documents = [ "very long document1", "very long document2", # ... more documents ] # And create an index with them at full length! RAG.index(collection=my_documents, index_name="the_biggest_index", max_document_length=8190,) # or encode them in-memory with no truncation, up to your model's max length RAG.encode(my_documents)

For more detailed information and further exploration of Jina-ColBERT, you can visit the Hugging Face page. Conclusion ColBERT represents a significant leap forward in the field of information retrieval. By enabling longer context lengths with Jina-ColBERT and maintaining compatibility with the ColBERT approach to late interaction, it offers a powerful alternative for developers looking to implement state-of-the-art search functionality. Coupled with the RAGatouille library, which simplifies the integration of complex retrieval models into RAG pipelines, developers can now harness the power of advanced retrieval with ease, streamlining their workflows and enhancing their applications. The synergy between Jina-ColBERT and RAGatouille illustrates a remarkable stride in making advanced AI search models accessible and efficient for practical use. Categories: star Featured Tech blog rss_feed Top-5 similar articles play_arrow GET TOP-5 Select reranker Read more August 26, 2024 • 13 minutes read The What and Why of Text-Image Modality Gap in CLIP Models You can't just use a CLIP model to retrieve text and images and sort the results by score. Why? Because of the modality gap. What is it, and where does it come from? August 22, 2024 • 8 minutes read Late Chunking in Long-Context Embedding Models Chunking long documents while preserving contextual information is challenging. We introduce the "Late Chunking" that leverages long-context embedding models to generate contextual chunk embeddings for better retrieval applications. July 31, 2024 • 17 minutes read Rephrased Labels Improve Zero-Shot Text Classification by 30% When using embedding models for zero-shot classification, rephrasing the class label to "This is seriously about 'LABEL'" gives higher accuracy vs. using LABEL alone. But how, and why? OFFICES location_on Berlin, Germany (HQ) Prinzessinnenstraße 19-20, 10969 Berlin, Germany Geschäftsanschrift: Leipzigerstr. 96, 10117 Berlin, Germany location_on Beijing, China Level 5, Building 6, No.48 Haidian West St. Beijing Haidian, China location_on Shenzhen, China 402, Floor 4, Fu'an Technology Building, Shenzhen Nanshan, China SEARCH FOUNDATION Embeddings Reranker Reader Segmenter Get Jina AI API key API Status COMPANY About us Contact sales Newsroom Intern program Join us open_in_new Download logo open_in_new TERMS Terms & Conditions Privacy Manage Cookies email language English science Jina AI GmbH © 2020-2024.

## SUMMARY_CHUNKING

#### 0 chunk(s)

## COT_TOPIC_CHUNKING

#### 3 chunk(s)

Reranker API Maximize the search relevancy and RAGaccuracy at ease What is ColBERT? The name "ColBERT" stands for Contextualized Late Interaction over BERT, a model stems from the Stanford University, that leverages the deep language understanding of BERT while introducing a novel interaction mechanism. This mechanism, known as late interaction, allows for efficient and precise retrieval by processing queries and documents separately until the final stages of the retrieval process. Specifically, there are two versions of the model: ColBERT: The initial model was the brainchild of Omar Khattab and Matei Zaharia, presenting a novel approach to information retrieval through the "ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT" paper. Their work was published in SIGIR 2020. ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT Recent progress in Natural Language Understanding (NLU) is driving fast-paced advances in Information Retrieval (IR), largely owed to fine-tuning deep language models (LMs) for document ranking. While remarkably effective, the ranking models based on these LMs increase computational cost by orders of magnitude over prior approaches, particularly as they must feed each query-document pair through a massive neural network to compute a single relevance score. To tackle this, we present ColBERT, a novel ranking model that adapts deep LMs (in particular, BERT) for efficient retrieval. ColBERT introduces a late interaction architecture that independently encodes the query and the document using BERT and then employs a cheap yet powerful interaction step that models their fine-grained similarity. By delaying and yet retaining this fine-granular interaction, ColBERT can leverage the expressiveness of deep LMs while simultaneously gaining the ability to pre-compute document representations offline, considerably speeding up query processing. Beyond reducing the cost of re-ranking the documents retrieved by a traditional model, ColBERT’s pruning-friendly interaction mechanism enables leveraging vector-similarity indexes for end-to-end retrieval directly from a large document collection. We extensively evaluate ColBERT using two recent passage search datasets. Results show that ColBERT’s effectiveness is competitive with existing BERT-based models (and outperforms every non-BERT baseline), while executing two orders-of-magnitude faster and requiring four orders-of-magnitude fewer FLOPs per query.

The ColBERT model is trained using a pairwise ranking loss, where the training data consists of triples ( 𝑞 , 𝑑 + , 𝑑 − ) (q,d + ,d − ), where 𝑞 q represents a query, 𝑑 + d + is a relevant (positive) document for the query, and 𝑑 − d − is a non-relevant (negative) document. The model aims to learn representations such that the similarity score between 𝑞 q and 𝑑 + d + is higher than the score between q and 𝑑 − d − . The training objective can be mathematically represented as minimizing the following loss function: L o s s = max ⁡ ( 0 , 1 − 𝑆 ( 𝑞 , 𝑑 + ) + 𝑆 ( 𝑞 , 𝑑 − ) ) Loss=max(0,1−S(q,d + )+S(q,d − )) , where 𝑆 ( 𝑞 , 𝑑 ) S(q,d) denotes the similarity score computed by ColBERT between a query 𝑞 q and a document 𝑑 d. This score is obtained by aggregating the max-similarity scores of the best-matching embeddings between the query and the document, following the late interaction pattern described in the model architecture.

OFFICES location_on Berlin, Germany (HQ) Prinzessinnenstraße 19-20, 10969 Berlin, Germany Geschäftsanschrift: Leipzigerstr. 96, 10117 Berlin, Germany location_on Beijing, China Level 5, Building 6, No.48 Haidian West St. Beijing Haidian, China location_on Shenzhen, China 402, Floor 4, Fu'an Technology Building, Shenzhen Nanshan, China SEARCH FOUNDATION Embeddings Reranker Reader Segmenter Get Jina AI API key API Status COMPANY About us Contact sales Newsroom Intern program Join us open_in_new Download logo open_in_new TERMS Terms & Conditions Privacy Manage Cookies email language English science Jina AI GmbH © 2020-2024.

## JINA-SEGMENTER-API

#### 453 chunk(s)

search


notifications


NEWS


PRODUCTS


COMPANY


star


Featured


Tech blog


February 20, 2024


What is ColBERT and Late Interaction and Why They Matter in Search?


Jina AI's ColBERT on Hugging Face has set Twitter abuzz, bringing a fresh perspective to search with its 8192-token capability. This article unpacks the nuances of ColBERT and ColBERTv2, showcasing their innovative designs and why their late interaction feature is a game-changer for search.


Han Xiao • 16 minutes read


Jina ColBERT v2: Multilingual Late Interaction Retriever for Embedding and Reranking


Jina ColBERT v2 supports 89 languages with superior retrieval performance, user-controlled output dimensions, and 8192 token-length.



Update: On Aug. 31st 2024, we released the 2nd version of Jina-ColBERT, with improved performance, multilingual support over 89 languages and flexible output dimensions. Check the release post for more details.



Last Friday, the release of the ColBERT model by Jina AI on Hugging Face sparked significant excitement across the AI community, particularly on Twitter/X. While many are familiar with the groundbreaking BERT model, the buzz around ColBERT has left some wondering: What makes ColBERT stand out in the crowded field of information retrieval technologies? Why the AI community is excited about 8192-length ColBERT? This article delves into the intricacies of ColBERT and ColBERTv2, highlighting their design, improvements, and the surprising effectiveness of ColBERT's late interaction.



Reranker API


Maximize the search relevancy and RAG accuracy at ease


What is ColBERT?



The name "ColBERT" stands for Contextualized Late Interaction over BERT, a model stems from the Stanford University, that leverages the deep language understanding of BERT while introducing a novel interaction mechanism. This mechanism, known as late interaction, allows for efficient and precise retrieval by processing queries and documents separately until the final stages of the retrieval process. Specifically, there are two versions of the model:



ColBERT: The initial model was the brainchild of Omar Khattab and Matei Zaharia, presenting a novel approach to information retrieval through the "ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT" paper. Their work was published in SIGIR 2020.


ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT


Recent progress in Natural Language Understanding (NLU) is driving fast-paced advances in Information Retrieval (IR), largely owed to fine-tuning deep language models (LMs) for document ranking. While remarkably effective, the ranking models based on these LMs increase computational cost by orders of magnitude over prior approaches, particularly as they must feed each query-document pair through a massive neural network to compute a single relevance score. 

To tackle this, we present ColBERT, a novel ranking model that adapts deep LMs (in particular, BERT) for efficient retrieval. ColBERT introduces a late interaction architecture that independently encodes the query and the document using BERT and then employs a cheap yet powerful interaction step that models their fine-grained similarity. 

By delaying and yet retaining this fine-granular interaction, ColBERT can leverage the expressiveness of deep LMs while simultaneously gaining the ability to pre-compute document representations offline, considerably speeding up query processing. Beyond reducing the cost of re-ranking the documents retrieved by a traditional model, ColBERT’s pruning-friendly interaction mechanism enables leveraging vector-similarity indexes for end-to-end retrieval directly from a large document collection. 

We extensively evaluate ColBERT using two recent passage search datasets. Results show that ColBERT’s effectiveness is competitive with existing BERT-based models (and outperforms every non-BERT baseline), while executing two orders-of-magnitude faster and requiring four orders-of-magnitude fewer FLOPs per query.


arXiv.org


Omar Khattab



The original ColBERT paper that introduces the "late interaction".



ColBERTv2: Building on the foundational work, Omar Khattab continued his research, collaborating with Barlas Oguz, Matei Zaharia, and Michael S. Bernstein to introduce "ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction," presented at SIGIR 2021. This next iteration of ColBERT addressed previous limitations and introduced key improvements, such as denoised supervision and residual compression, enhancing both the model's retrieval effectiveness and its storage efficiency.


ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction


Neural information retrieval (IR) has greatly advanced search and other knowledge-intensive language tasks. While many neural IR methods encode queries and documents into single-vector representations, late interaction models produce multi-vector representations at the granularity of each token and decompose relevance modeling into scalable token-level computations. This decomposition has been shown to make late interaction more effective, but it inflates the space footprint of these models by an order of magnitude. In this work, we introduce ColBERTv2, a retriever that couples an aggressive residual compression mechanism with a denoised supervision strategy to simultaneously improve the quality and space footprint of late interaction. We evaluate ColBERTv2 across a wide range of benchmarks, establishing state-of-the-art quality within and outside the training domain while reducing the space footprint of late interaction models by 6--10


×


×.


arXiv.org


Keshav Santhanam



ColBERTv2 adding denoised supervision and residual compression to improve the training data's quality and reduce the space footprint.



Understand ColBERT's Design



Given that ColBERTv2's architecture remains very similar to that of the original ColBERT, with its key innovations revolving around training techniques and compression mechanisms, we will first delve into the foundational aspects of the original ColBERT.



What is late interaction in ColBERT?



"Interaction" refers to the process of evaluating the relevance between a query and a document by comparing their representations.



"Late interaction" is the essence of ColBERT. The term is derived from the model's architecture and processing strategy, where the interaction between the query and document representations occurs late in the process, after both have been independently encoded. This contrasts with "early interaction" models, where query and document embeddings interact at earlier stages, typically before or during their encoding by the model.



Interaction Type	Models


Early Interaction	BERT, ANCE, DPR, Sentence-BERT, DRMM, KNRM, Conv-KNRM, etc.


Late Interaction	ColBERT, ColBERTv2



Early interaction can increase computational complexity since it requires considering all possible query-document pairs, making it less efficient for large-scale applications.



Late interaction models like ColBERT optimize for efficiency and scalability by allowing for the pre-computation of document representations and employing a more lightweight interaction step at the end, which focuses on the already encoded representations. This design choice enables faster retrieval times and reduced computational demands, making it more suitable for processing large document collections.



Schematic diagrams illustrating query–document interaction paradigms in neural IR, with ColBERT's late interaction on the left-most.


No interaction: cosine similarity of document and query embeddings



Many practical vector databases and neural search solutions depend on fast cosine similarity matching between document and query embeddings. While appealing for its straightforwardness and computational efficiency, this method, often referred to as "no interaction" or "not interaction-based" has been found to underperform in comparison to models that incorporate some form of interaction between queries and documents.



The core limitation of the "no interaction" approach lies in its inability to capture the complex nuances and relationships between query and document terms. Information retrieval, at its heart, is about understanding and matching the intent behind a query with the content within a document. This process often requires a deep, contextual understanding of the terms involved, something that single, aggregated embeddings for documents and queries struggle to provide.



Query and document encoders in ColBERT



ColBERT's encoding strategy is grounded in the BERT model, known for its deep contextual understanding of language. The model generates dense vector representations for each token in a query or document, creating a bag of contextualized embeddings for a query and a bag for a document, respectively. This facilitates a nuanced comparison of their embeddings during the late interaction phase.



Query encoder of ColBERT



For a query 


𝑄


Q with tokens 


𝑞


1
,


𝑞


2
,
.
.
.
,


𝑞


𝑙


q


1


	​


q


2


	​


q


l


	​


the process begins by tokenizing 


𝑄


Q into BERT-based WordPiece tokens and prepending a special [Q] token. This [Q] token, positioned right after BERT’s [CLS] token, signals the start of a query.



If the query is shorter than a predefined number of tokens 


𝑁


𝑞


N


q


	​


it is padded with [mask] tokens up to 


𝑁


𝑞


N


q


	​


otherwise, it's truncated to the first 


𝑁


𝑞


N


q


	​


tokens. The padded sequence is then passed through BERT, followed by a CNN (Convolutional Neural Network) and normalization. The output is a set of embedding vectors termed as 


𝐸


𝑞


E


q


	​


below:



𝐸


𝑞


:


=


N


o


r


m


a


l


i


z


e


(


B


E


R


T


(


[


𝑄
]
,


𝑞


0
,


𝑞


1
,
…
,


𝑞


𝑙


[


𝑚


𝑎


𝑠


𝑘
]
,


[


𝑚


𝑎


𝑠


𝑘
]
,
…
,


[


𝑚


𝑎


𝑠


𝑘
]
)
)


E


q


	​


:=Normalize(BERT([Q],q


0


	​


q


1


	​


q


l


	​


[mask],[mask],…,[mask]))



Document encoder of ColBERT



Similarly, for a document 


𝐷


D with tokens 


𝑑


1
,


𝑑


2
,
.
.
.
,


𝑑


𝑛


d


1


	​


d


2


	​


d


n


	​


a [D] token is prepended to indicate the start of a document. This sequence, without the need for padding, undergoes the same process, results in a set of embedding vectors termed as 


𝐸


𝑑


E


d


	​


below:



𝐸


𝑑


:


=


F


i


l


t


e


r


(


N


o


r


m


a


l


i


z


e


(


B


E


R


T


(


[


𝐷
]
,


𝑑


0
,


𝑑


1
,
.
.
.
,


𝑑


𝑛
)
)
)


E


d


	​


:=Filter(Normalize(BERT([D],d


0


	​


d


1


	​


d


n


	​


The use of [mask] tokens for padding queries (coined as query augmentation in the paper) ensures uniform length across all queries, facilitating batch processing. The [Q] and [D] tokens explicitly mark the start of queries and documents, respectively, aiding the model in distinguishing between the two types of inputs.



Comparing ColBERT to cross-encoders



Cross-encoders process pairs of queries and documents together, making them highly accurate but less efficient for large-scale tasks due to the computational cost of evaluating every possible pair. They excel in specific scenarios where the precise scoring of sentence pairs is necessary, such as in semantic similarity tasks or detailed content comparison. However, this design limits their applicability in situations requiring rapid retrieval from large datasets, where pre-computed embeddings and efficient similarity calculations are paramount.



In contrast, ColBERT’s late interaction model allows for pre-computation of document embeddings, significantly speeding up the retrieval process without compromising the depth of semantic analysis. This method, though seemingly counter-intuitive when compared to the direct approach of cross-encoders, offers a scalable solution for real-time and large-scale information retrieval tasks. It represents a strategic compromise between computational efficiency and the quality of interaction modeling.



Finding the top-K documents using ColBERT



Once we have embeddings for the query and documents, finding the most relevant top-K documents becomes straightforward (but not as straightforward as computing cosine of two vectors).



The key operations include a batch dot-product to compute term-wise similarities, max-pooling across document terms to find the highest similarity per query term, and summation across query terms to derive the total document score, followed by sorting the documents based on these scores. The pseudo PyTorch code is described below:



import torch



def compute_relevance_scores(query_embeddings, document_embeddings, k):


    """
    Compute relevance scores for top-k documents given a query.
    
    :param query_embeddings: Tensor representing the query embeddings, shape: [num_query_terms, embedding_dim]
    :param document_embeddings: Tensor representing embeddings for k documents, shape: [k, max_doc_length, embedding_dim]
    :param k: Number of top documents to re-rank
    :return: Sorted document indices based on their relevance scores
    """
    
    # Ensure document_embeddings is a 3D tensor: [k, max_doc_length, embedding_dim]
    # Pad the k documents to their maximum length for batch operations
    # Note: Assuming document_embeddings is already padded and moved to GPU
    
    # Compute batch dot-product of Eq (query embeddings) and D (document embeddings)
    # Resulting shape: [k, num_query_terms, max_doc_length]
    scores = torch.matmul(query_embeddings.unsqueeze(0), document_embeddings.transpose(1, 2))
    
    # Apply max-pooling across document terms (dim=2) to find the max similarity per query term
    # Shape after max-pool: [k, num_query_terms]
    max_scores_per_query_term = scores.max(dim=2).values
    


    # Sum the scores across query terms to get the total score for each document
    # Shape after sum: [k]
    total_scores = max_scores_per_query_term.sum(dim=1)
    
    # Sort the documents based on their total scores
    sorted_indices = total_scores.argsort(descending=True)
    
    return sorted_indices


Note that this procedure is used in both training and re-ranking at inference time. The ColBERT model is trained using a pairwise ranking loss, where the training data consists of triples 


(


𝑞
,


𝑑


+
,


𝑑


−
)


(q,d


+


d


−


where 


𝑞


q represents a query, 


𝑑


+


d


+


is a relevant (positive) document for the query, and 


𝑑


−


d


−


is a non-relevant (negative) document. The model aims to learn representations such that the similarity score between 


𝑞


q and 


𝑑


+


d


+


is higher than the score between q and 


𝑑


−


d


−
.



The training objective can be mathematically represented as minimizing the following loss function:


L


o


s


s


=


max


⁡


(


0
,


1


−


𝑆


(


𝑞
,


𝑑


+
)


+


𝑆


(


𝑞
,


𝑑


−
)
)


Loss=max(0,1−S(q,d


+


+S(q,d


−
))



where 


𝑆


(


𝑞
,


𝑑
)


S(q,d) denotes the similarity score computed by ColBERT between a query 


𝑞


q and a document 


𝑑


d. This score is obtained by aggregating the max-similarity scores of the best-matching embeddings between the query and the document, following the late interaction pattern described in the model architecture. This approach ensures that the model is trained to distinguish between relevant and irrelevant documents for a given query, by encouraging a larger margin in the similarity scores for positive and negative document pairs.



Denoised supervision in ColBERTv2



Denoised supervision in ColBERTv2 refines the original training process by selecting challenging negatives and leveraging a cross-encoder for distillation. This sophisticated method of augmenting training data quality involves several steps:



Initial Training: Utilizing the official triples from the MS MARCO dataset, comprising a query, a relevant document, and a non-relevant document.


Indexing and Retrieval: Employing ColBERTv2's compression to index training passages, followed by retrieving top-k passages for each query.


Cross-Encoder Reranking: Enhancing passage selection through reranking by a MiniLM cross-encoder, distilling its scores into ColBERTv2.


Forming Training Tuples: Generating w-way tuples for training, incorporating both high and lower-ranked passages to create challenging examples.


Iterative Refinement: Repeating the process to continually improve the selection of hard negatives, thereby enhancing model performance.



Note, this process represents a sophisticated enhancement to the ColBERT training regime rather than a fundamental change to its architecture.



Hyperparameters of ColBERT



The hyperparameters of ColBERT is summarized below:



Hyperparameter	Best Choice	Reason


Learning Rate	3 x 10^{-6}	Selected for fine-tuning to ensure stable and effective model updates.


Batch Size	32	Balances computational efficiency and the ability to capture sufficient information per update.


Number of Embeddings per Query (Nq)	32	Fixed to ensure a consistent representation size across queries, aiding in efficient processing.


Embedding Dimension (m)	128	Demonstrated to provide a good balance between representational power and computational efficiency.


Training Iterations	200k (MS MARCO), 125k (TREC CAR)	Chosen to ensure thorough learning while avoiding overfitting, with adjustments based on dataset characteristics.


Bytes per Dimension in Embeddings	4 (re-ranking), 2 (end-to-end ranking)	Trade-off between precision and space efficiency, with consideration for the application context (re-ranking vs. end-to-end).


Vector-Similarity Function	Cosine (re-ranking), (Squared) L2 (end-to-end)	Selected based on performance and efficiency in the respective retrieval contexts.


FAISS Index Partitions (P)	2000	Determines the granularity of the search space partitioning, impacting search efficiency.


Nearest Partitions Searched (p)	10	Balances the breadth of the search against computational efficiency.


Sub-vectors per Embedding (s)	16	Affects the granularity of quantization, influencing both search speed and memory usage.


Index Representation per Dimension	16-bit values	Chosen for the second stage of end-to-end retrieval to manage the trade-off between accuracy and space.


Number of Layers in Encoders	12-layer BERT	Optimal balance between depth of contextual understanding and computational efficiency.


Max Query Length	128	The maximum number of tokens processed by the query encoder. This gets extended in Jina-ColBERT model.


Max Document Length	512	The maximum number of tokens processed by the document encoder. This gets extended to 8192 in Jina-ColBERT model.


The indexing strategy of ColBERT



Unlike representation-based approaches that encode each document into one embedding vector, ColBERT encodes documents (and queries) into bags of embeddings, with each token in a document having its own embedding. This approach inherently means that for longer documents, more embeddings will be stored, which is a pain point of the original ColBERT, and later addressed by ColBERTv2.



The key to managing this efficiently lies in ColBERT's use of vector database (e.g. FAISS) for indexing and retrieval, and its detailed indexing process which is designed to handle large volumes of data efficiently. The original ColBERT paper mentions several strategies to enhance the efficiency of indexing and retrieval, including:



Offline Indexing: Document representations are computed offline, allowing for the pre-computation and storage of document embeddings. This process leverages batch processing and GPU acceleration to handle large document collections efficiently.


Embedding Storage: Document embeddings can be stored using 32-bit or 16-bit values for each dimension, offering a trade-off between precision and storage requirements. This flexibility allows ColBERT to maintain a balance between effectiveness (in terms of retrieval performance) and efficiency (in terms of storage and computational costs).



The introduction of residual compression in ColBERTv2, which is a novel approach not present in the original ColBERT, plays a key role in reducing the model's space footprint by 6–10× while preserving quality. This technique compresses the embeddings further by effectively capturing and storing only the differences from a set of fixed reference centroids.



Effectiveness and Efficiency of ColBERT



One might initially assume that incorporating BERT's deep contextual understanding into search would inherently require significant computational resources, making such an approach less feasible for real-time applications due to high latency and computational costs. However, ColBERT challenges and overturns this assumption through its innovative use of the late interaction mechanism. Here are some noteworthy points:



Significant Efficiency Gains: ColBERT achieves an orders-of-magnitude reduction in computational costs (FLOPs) and latency compared to traditional BERT-based ranking models. Specifically, for a given model size (e.g., 12-layer "base" transformer encoder), ColBERT not only matches but in some cases exceeds the effectiveness of BERT-based models with dramatically lower computational demands. For instance, at a re-ranking depth of k=10, BERT requires nearly 180× more FLOPs than ColBERT; this gap widens as k increases, reaching 13900× at k=1000 and even 23000× at k=2000​​.


Improved Recall and MRR@10 in End-to-End Retrieval: Contrary to the initial intuition that deeper interaction between query and document representations (as seen in early interaction models) would be necessary for high retrieval performance, ColBERT's end-to-end retrieval setup demonstrates superior effectiveness. For example, its Recall@50 exceeds the official BM25's Recall@1000 and almost all other models' Recall@200, underscoring the model's remarkable ability to retrieve relevant documents from a vast collection without direct comparison of each query-document pair​​.


Practicality for Real-World Applications: The experimental results underline ColBERT's practical applicability for real-world scenarios. Its indexing throughput and memory efficiency make it suitable for indexing large document collections like MS MARCO within a few hours, retaining high effectiveness with a manageable space footprint. These qualities highlight ColBERT's suitability for deployment in production environments where both performance and computational efficiency are paramount​​.


Scalability with Document Collection Size: Perhaps the most surprising conclusion is ColBERT's scalability and efficiency in handling large-scale document collections. The architecture allows for the pre-computation of document embeddings and leverages efficient batch processing for query-document interaction, enabling the system to scale effectively with the size of the document collection. This scalability is counter-intuitive when considering the complexity and depth of understanding required for effective document retrieval, showcasing ColBERT's innovative approach to balancing computational efficiency with retrieval effectiveness.


Using jina-colbert-v1-en: a 8192-length ColBERTv2 model



Jina-ColBERT is designed for both fast and accurate retrieval, supporting longer context lengths up to 8192, leveraging the advancements of JinaBERT, which allows for longer sequence processing due to its architecture enhancements.



Strictly speaking Jina-ColBERT supports 8190-token length. Recall that in ColBERT document encoder, each document is padded with [D],[CLS] in the beginning.


jinaai/jina-colbert-v1-en · Hugging Face


We’re on a journey to advance and democratize artificial intelligence through open source and open science.


Jina's improvement over original ColBERT



Jina-ColBERT's main advancement is its backbone, jina-bert-v2-base-en, which enables processing of significantly longer contexts (up to 8192 tokens) compared to the original ColBERT that uses bert-base-uncased. This capability is crucial for handling documents with extensive content, providing more detailed and contextual search results.



jina-colbert-v1-en performance comparison vs. ColBERTv2



We evaluated jina-colbert-v1-en on BEIR datasets and new LoCo benchmark which favors long-context, tested it against the original ColBERTv2 implementation and non-interaction based jina-embeddings-v2-base-en model.



Dataset	ColBERTv2	jina-colbert-v1-enjina-embeddings-v2-base-en


Arguana	46.5	49.4	44.0


Climate-Fever	18.1	19.6	23.5


DBPedia	45.2	41.3	35.1


FEVER	78.8	79.5	72.3


FiQA	35.4	36.8	41.6


HotpotQA	67.5	65.9	61.4


NFCorpus	33.7	33.8	32.5


NQ	56.1	54.9	60.4


Quora	85.5	82.3	88.2


SCIDOCS	15.4	16.9	19.9


SciFact	68.9	70.1	66.7


TREC-COVID	72.6	75.0	65.9


Webis-touch2020	26.0	27.0	26.2


LoCo	74.3	83.7	85.4


Average	51.7	52.6	51.6



This table demonstrates jina-colbert-v1-en's superior performance, especially in scenarios requiring longer context lengths vs the original ColBERTv2. Note that jina-embeddings-v2-base-en uses more training data, whereas jina-colbert-v1-en only uses MSMARCO, which may justify the good performance of jina-embeddings-v2-base-en on some tasks.



Example usage of jina-colbert-v1-en



This snippet outlines the indexing process with Jina-ColBERT, showcasing its support for long documents.



from colbert import Indexer


from colbert.infra import Run, RunConfig, ColBERTConfig



n_gpu: int = 1  # Set your number of available GPUs


experiment: str = ""  # Name of the folder where the logs and created indices will be stored


index_name: str = ""  # The name of your index, i.e. the name of your vector database



if __name__ == "__main__":


    with Run().context(RunConfig(nranks=n_gpu, experiment=experiment)):
        config = ColBERTConfig(
          doc_maxlen=8192  # Our model supports 8k context length for indexing long documents
        )
        indexer = Indexer(
          checkpoint="jinaai/jina-colbert-v1-en",
          config=config,
        )
        documents = [
          "ColBERT is an efficient and effective passage retrieval model.",
          "Jina-ColBERT is a ColBERT-style model but based on JinaBERT so it can support both 8k context length.",
          "JinaBERT is a BERT architecture that supports the symmetric bidirectional variant of ALiBi to allow longer sequence length.",
          "Jina-ColBERT model is trained on MSMARCO passage ranking dataset, following a very similar training procedure with ColBERTv2.",
          "Jina-ColBERT achieves the competitive retrieval performance with ColBERTv2.",
          "Jina is an easier way to build neural search systems.",
          "You can use Jina-ColBERT to build neural search systems with ease.",
          # Add more documents here to ensure the clustering work correctly
        ]
        indexer.index(name=index_name, collection=documents)


Use jina-colbert-v1-en in RAGatouille



RAGatouille is a new Python library that facilitates the use of advanced retrieval methods within RAG pipelines. It's designed for modularity and easy integration, allowing users to leverage state-of-the-art research seamlessly. The main goal of RAGatouille is to simplify the application of complex models like ColBERT in RAG pipelines, making it accessible for developers to utilize these methods without needing deep expertise in the underlying research. Thanks to Benjamin Clavié, you can now use jina-colbert-v1-en easily:



from ragatouille import RAGPretrainedModel



# Get your model & collection of big documents ready


RAG = RAGPretrainedModel.from_pretrained("jinaai/jina-colbert-v1-en")


my_documents = [


    "very long document1",
    "very long document2",
    # ... more documents


# And create an index with them at full length!


RAG.index(collection=my_documents,


          index_name="the_biggest_index",
          max_document_length=8190,)


# or encode them in-memory with no truncation, up to your model's max length


RAG.encode(my_documents)




For more detailed information and further exploration of Jina-ColBERT, you can visit the Hugging Face page.



Conclusion



ColBERT represents a significant leap forward in the field of information retrieval. By enabling longer context lengths with Jina-ColBERT and maintaining compatibility with the ColBERT approach to late interaction, it offers a powerful alternative for developers looking to implement state-of-the-art search functionality.



Coupled with the RAGatouille library, which simplifies the integration of complex retrieval models into RAG pipelines, developers can now harness the power of advanced retrieval with ease, streamlining their workflows and enhancing their applications. The synergy between Jina-ColBERT and RAGatouille illustrates a remarkable stride in making advanced AI search models accessible and efficient for practical use.



Categories:


star


Featured


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