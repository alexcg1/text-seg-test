# retrieve-jira-tickets-with-jina-reranker-and-haystack-20

## SIMPLE_CHUNKING

#### 2 chunk(s)

To follow this tutorial, you'll need a Jina Reranker API key. You can create one with a free trial quota of a million tokens from the Jina Reranker website. 💡 You can follow along in Colab or by downloading the notebook.

This should create a progress bar and output a brief JSON containing information about what's been stored: Calculating embeddings: 100%|██████████| 1/1 [00:01<00:00, 1.21s/it] {'embedder': {'meta': {'model': 'jina-embeddings-v2-base-en', 'usage': {'total_tokens': 20067, 'prompt_tokens': 20067}}}, 'writer': {'documents_written': 31}} Build the Query Pipeline Let’s create a query pipeline so we can start comparing tickets. In Haystack 2.0 retrievers are tightly coupled to DocumentStores. If we pass the document store in the retriever we initialized earlier, this pipeline can access the documents we generated, and pass them to the reranker. The reranker then compares these documents directly with the question and ranks them based on relevance. We first define the custom cleaner to remove retrieve tickets that contain either the same issue ID or parent ID as the issue passed as query: from typing import Optional @component class RemoveRelated: @component.output_types(documents=List[Document]) def run(self, tickets: List[Document], query_id: Optional[str]): retrieved_tickets = [] for t in tickets: if not t.meta['Issue id'] == query_id and not t.meta['Parent id'] == query_id: retrieved_tickets.append(t) return {'documents': retrieved_tickets} We then embed the query, retrieve relevant documents, clean the selection, and finally rerank it: from haystack_integrations.components.embedders.jina import JinaTextEmbedder from haystack_integrations.components.rankers.jina import JinaRanker query_pipeline_reranker = Pipeline() query_pipeline_reranker.add_component('query_embedder_reranker', JinaTextEmbedder(model='jina-embeddings-v2-base-en')) query_pipeline_reranker.add_component('query_retriever_reranker', retriever_reranker) query_pipeline_reranker.add_component('query_cleaner_reranker', RemoveRelated()) query_pipeline_reranker.add_component('query_ranker_reranker', JinaRanker()) query_pipeline_reranker.connect('query_embedder_reranker.embedding', 'query_retriever_reranker.query_embedding') query_pipeline_reranker.connect('query_retriever_reranker', 'query_cleaner_reranker') query_pipeline_reranker.connect('query_cleaner_reranker', 'query_ranker_reranker') To highlight the difference caused by the reranker, we analyzed the same pipeline without the final reranking step (the corresponding code was omitted in this post for the sake of readability but can be found in the notebook): To compare the results of these two pipelines, we now define our query in the form of an existing ticket, here "ZOOKEEPER-3282": query_ticket_key = 'ZOOKEEPER-3282' with open('tickets.json', 'r') as file: tickets = json.load(file) for ticket in tickets: if ticket['Issue key'] == query_ticket_key: query = str(ticket) query_ticket_id = ticket['Issue id'] It concerns "a big refactor for the documetations" [sic]. You'll see that, despite the misspelling, Jina Reranker will correctly retrieve similar tickets. { "Summary": "a big refactor for the documetations" "Issue key": "ZOOKEEPER-3282" "Issue id:: 13216608 "Parent id": "" "Issue Type": "Task" "Status": "In Progress" "Project lead": "phunt" "Priority": "Major" "Assignee": "maoling" "Reporter": "maoling" "Creator": "maoling" "Created": "19/Feb/19 11:50" "Updated": "04/Aug/19 12:48" "Last Viewed": "12/Mar/24 11:56" "Description": "Hi guys: I'am working on doing a big refactor for the documetations.it aims to - 1.make a better reading experiences and help users know more about zookeeper quickly,as good as other projects' doc(e.g redis,hbase). - 2.have less changes to diff with the original docs as far as possible. - 3.solve the problem when we have some new features or improvements,but cannot find a good place to doc it. The new catalog may looks kile this: * is new one added. ** is the one to keep unchanged as far as possible. *** is the one modified. -------------------------------------------------------------- |---Overview |---Welcome ** [1.1] |---Overview ** [1.2] |---Getting Started ** [1.3] |---Release Notes ** [1.4] |---Developer |---API *** [2.1] |---Programmer's Guide ** [2.2] |---Recipes *** [2.3] |---Clients * [2.4] |---Use Cases * [2.5] |---Admin & Ops |---Administrator's Guide ** [3.1] |---Quota Guide ** [3.2] |---JMX ** [3.3] |---Observers Guide ** [3.4] |---Dynamic Reconfiguration ** [3.5] |---Zookeeper CLI * [3.6] |---Shell * [3.7] |---Configuration flags * [3.8] |---Troubleshooting & Tuning * [3.9] |---Contributor Guidelines |---General Guidelines * [4.1] |---ZooKeeper Internals ** [4.2] |---Miscellaneous |---Wiki ** [5.1] |---Mailing Lists ** [5.2] -------------------------------------------------------------- The Roadmap is: 1.(I pick up it : D) 1.1 write API[2.1], which includes the： 1.1.1 original API Docs which is a Auto-generated java doc,just give a link. 1.1.2. Restful-api (the apis under the /zookeeper-contrib-rest/src/main/java/org/apache/zookeeper/server/jersey/resources) 1.2 write Clients[2.4], which includes the: 1.2.1 C client 1.2.2 zk-python, kazoo 1.2.3 Curator etc....... look at an example from: https://redis.io/clients # write Recipes[2.3], which includes the: - integrate "Java Example" and "Barrier and Queue Tutorial"(Since some bugs in the examples and they are obsolete，we may delete something) into it. - suggest users to use the recipes implements of Curator and link to the Curator's recipes doc. # write Zookeeper CLI[3.6], which includes the: - about how to use the zk command line interface [./zkCli.sh] e.g ls /; get ; rmr;create -e -p etc....... - look at an example from redis: https://redis.io/topics/rediscli # write shell[3.7], which includes the: - list all usages of the shells under the zookeeper/bin. (e.g zkTxnLogToolkit.sh,zkCleanup.sh) # write Configuration flags[3.8], which includes the: - list all usages of configurations properties(e.g zookeeper.snapCount): - move the original Advanced Configuration part of zookeeperAdmin.md into it. look at an example from:https://coreos.com/etcd/docs/latest/op-guide/configuration.html # write Troubleshooting & Tuning[3.9], which includes the: - move the original "Gotchas: Common Problems and Troubleshooting" part of Administrator's Guide.md into it. - move the original "FAQ" into into it. - add some new contents （e.g https://www.yumpu.com/en/document/read/29574266/building-an-impenetrable-zookeeper-pdf-github）. look at an example from:https://redis.io/topics/problems https://coreos.com/etcd/docs/latest/tuning.html # write General Guidelines[4.1], which includes the: - move the original "Logging" part of ZooKeeper Internals into it as the logger specification. - write specifications about code, git commit messages,github PR etc ... look at an example from: http://hbase.apache.org/book.html#hbase.commit.msg.format # write Use Cases[2.5], which includes the: - just move the context from: https://cwiki.apache.org/confluence/display/ZOOKEEPER/PoweredBy into it. - add some new contents.(e.g Apache Projects:Spark;Companies:twitter,fb) -------------------------------------------------------------- BTW: - Any insights or suggestions are very welcomed.After the dicussions,I will create a series of tickets(An umbrella) - Since these works can be done parallelly, if you are interested in them, please don't hesitate,just assign to yourself, pick it up. (Notice: give me a ping to avoid the duplicated work)." } Finally, we run the query pipeline. In this case, it retrieves 20 tickets, eliminates ID-related entries, reranks them, and outputs the final selection of the 10 most relevant issues. Before the reranking step, the output includes 17 tickets: Rank Issue ID Issue Key Summary 1 13191544 ZOOKEEPER-3170 Umbrella for eliminating ZooKeeper flaky tests 2 13400622 ZOOKEEPER-4375 Quota cannot limit the specify value when multiply clients create/set znodes 3 13249579 ZOOKEEPER-3499 [admin server way] Add a complete backup mechanism for zookeeper internal 4 13295073 ZOOKEEPER-3775 Wrong message in IOException 5 13268474 ZOOKEEPER-3617 ZK digest ACL permissions gets overridden 6 13296971 ZOOKEEPER-3787 Apply modernizer-maven-plugin to build 7 13265507 ZOOKEEPER-3600 support the complete linearizable read and multiply read consistency level 8 13222060 ZOOKEEPER-3318 [CLI way]Add a complete backup mechanism for zookeeper internal 9 13262989 ZOOKEEPER-3587 Add a documentation about docker 10 13262130 ZOOKEEPER-3578 Add a new CLI: multi 11 13262828 ZOOKEEPER-3585 Add a documentation about RequestProcessors 12 13262494 ZOOKEEPER-3583 Add new apis to get node type and ttl time info 13 12998876 ZOOKEEPER-2519 zh->state should not be 0 while handle is active 14 13536435 ZOOKEEPER-4696 Update for Zookeeper latest version 15 13297249 ZOOKEEPER-3789 fix the build warnings about @see,@link,@return found by IDEA 16 12728973 ZOOKEEPER-1983 Append to zookeeper.out (not overwrite) to support logrotation 17 12478629 ZOOKEEPER-915 Errors that happen during sync() processing at the leader do not get propagated back to the client. After including the reranker, we now run the query pipeline: result = query_pipeline_reranker.run(data={'query_embedder_reranker':{'text': query}, 'query_retriever_reranker': {'top_k': 20}, 'query_cleaner_reranker': {'query_id': query_ticket_id}, 'query_ranker_reranker': {'query': query, 'top_k': 10} } ) for idx, res in enumerate(result['query_ranker_reranker']['documents']): print('Doc {}:'.format(idx + 1), res) The final output is the 10 most relevant tickets: Rank Issue ID Issue Key Summary 1 13262989 ZOOKEEPER-3587 Add a documentation about docker 2 13265507 ZOOKEEPER-3600 support the complete linearizable read and multiply read consistency level 3 13249579 ZOOKEEPER-3499 [admin server way] Add a complete backup mechanism for zookeeper internal 4 12478629 ZOOKEEPER-915 Errors that happen during sync() processing at the leader do not get propagated back to the client. 5 13262828 ZOOKEEPER-3585 Add a documentation about RequestProcessors 6 13297249 ZOOKEEPER-3789 fix the build warnings about @see,@link,@return found by IDEA 7 12998876 ZOOKEEPER-2519 zh->state should not be 0 while handle is active 8 13536435 ZOOKEEPER-4696 Update for Zookeeper latest version 9 12728973 ZOOKEEPER-1983 Append to zookeeper.out (not overwrite) to support logrotation 10 13222060 ZOOKEEPER-3318 [CLI way]Add a complete backup mechanism for zookeeper internal Advantages of Jina Embeddings and Reranker To sum up this tutorial, we built a duplicate-ticket identification tool based on Jina Embeddings, Jina Reranker and Haystack 2.0. The results above clearly show the necessity for both Jina Embeddings to retrieve relevant documents through vector search, and Jina Reranker to finally obtain the most relevant content. If we take, for example, the two issues that relate to adding documentation, i.e. "ZOOKEEPER-3585" and "ZOOKEEPER-3587", we see that after the retrieval step, they are both correctly included in positions 11 and 9 respectively. After reranking the documents, they are now both within the top 5 most relevant documents at positions 5 and 1 respectively, showing a significant improvement. By integrating both models in Haystack's pipelines, the entire tool is ready for use. This combination makes the Jina Haystack extension the perfect solution for your application. Categories: Tech blog rss_feed Top-5 similar articles play_arrow GET TOP-5 Select reranker Read more August 26, 2024 • 13 minutes read The What and Why of Text-Image Modality Gap in CLIP Models You can't just use a CLIP model to retrieve text and images and sort the results by score. Why? Because of the modality gap. What is it, and where does it come from? August 22, 2024 • 8 minutes read Late Chunking in Long-Context Embedding Models Chunking long documents while preserving contextual information is challenging. We introduce the "Late Chunking" that leverages long-context embedding models to generate contextual chunk embeddings for better retrieval applications. July 31, 2024 • 17 minutes read Rephrased Labels Improve Zero-Shot Text Classification by 30% When using embedding models for zero-shot classification, rephrasing the class label to "This is seriously about 'LABEL'" gives higher accuracy vs. using LABEL alone. But how, and why? OFFICES location_on Berlin, Germany (HQ) Prinzessinnenstraße 19-20, 10969 Berlin, Germany Geschäftsanschrift: Leipzigerstr. 96, 10117 Berlin, Germany location_on Beijing, China Level 5, Building 6, No.48 Haidian West St. Beijing Haidian, China location_on Shenzhen, China 402, Floor 4, Fu'an Technology Building, Shenzhen Nanshan, China SEARCH FOUNDATION Embeddings Reranker Reader Segmenter Get Jina AI API key API Status COMPANY About us Contact sales Newsroom Intern program Join us open_in_new Download logo open_in_new TERMS Terms & Conditions Privacy Manage Cookies email language English science Jina AI GmbH © 2020-2024.

## SUMMARY_CHUNKING

#### 7 chunk(s)

search notifications NEWS PRODUCTS COMPANY Tech blog April 10, 2024 Retrieve Jira Tickets with Jina Reranker and Haystack 2.0 Learn how to use Jina Reranker and Embeddings with Haystack to create your own Jira ticket search engine, streamlining your operations and never again waste time creating duplicate issues.

Francesco Kruk • 10 minutes read Following the integration of Jina Embeddings into Deepset's Haystack 2.0 and the release of Jina Reranker, we're thrilled to announce that Jina Reranker is now also available through the Jina Haystack extension. Jina AI | Haystack Use the latest Jina AI embedding models Haystack Authors deepset Reranker API Maximize the search relevancy and RAG accuracy at ease Haystack is an end-to-end framework that accompanies you in every step of the GenAI project life cycle. Whether you want to perform document search, retrieval-augmented generation (RAG), question answering, or answer generation, Haystack can orchestrate state-of-the-art embedding models and LLMs into pipelines to build end-to-end NLP applications and solve your use case. Haystack | Haystack

Haystack, the composable open-source AI framework Haystack In this post, we'll show how to use them to create your own Jira ticket search engine to streamline your operations and never again waste time creating duplicate issues. To follow this tutorial, you'll need a Jina Reranker API key. You can create one with a free trial quota of a million tokens from the Jina Reranker website. 💡 You can follow along in Colab or by downloading the notebook. Retrieving Jira Support Tickets Any team dealing with a complex project has experienced the frustration of having an issue they want to file but not knowing if a ticket already exists for this problem. In the following tutorial, we'll show you how you can easily create a tool yourself using Jina Reranker and Haystack pipelines, which suggests possible duplicate tickets to a new one being created. By inputting a ticket that needs to be checked against all existing tickets, the pipeline will first retrieve from the database all related issues. It'll then remove the initial ticket from the list (if it already existed in the database) and any child ticket (i.e. tickets whose parent ID corresponds to the original ticket). The final selection now only comprises issues that might cover the same topic as the original ticket but were not marked as such in the database through their IDs. These tickets are reranked to ensure maximal relevance and enable you to identify duplicate entries in the database.

Getting the Dataset To implement our solution, we've chosen all "In-progress" Jira tickets for the Apache Zookeeper project. This is an open-source service for coordinating processes of distributed applications. We have placed the tickets in a JSON file to make them more convenient. Please download the file to your workspace. Set up the Prerequisites To install the requirements, run: pip install --q chromadb haystack-ai jina-haystack chroma-haystack To input the API key, set it as an environment variable: import os import getpass os.environ["JINA_API_KEY"] = getpass.getpass() 💡 If you're running this code through the notebook, getpass.getpass() will prompt you to input the API key below the corresponding code block. You can enter the key there and press enter to resume the tutorial. If you prefer, you can also substitute getpass.getpass() with the API key itself. Build the Indexing Pipeline The indexing pipeline will preprocess the tickets, turn them into vectors, and store them. We’ll use the Chroma DocumentStore as our vector database to store the vector embeddings, via the Chroma Document Store Haystack integration. from haystack_integrations.document_stores.chroma import ChromaDocumentStore document_store = ChromaDocumentStore() We'll start by defining our custom data preprocessor to only consider relevant document fields and delete all empty entries: import json from typing import List from haystack import Document, component relevant_keys = ['Summary', 'Issue key', 'Issue id', 'Parent id', 'Issue type', 'Status', 'Project lead', 'Priority', 'Assignee', 'Reporter', 'Creator', 'Created', 'Updated', 'Last Viewed', 'Due Date', 'Labels', 'Description', 'Comment', 'Comment__1', 'Comment__2', 'Comment__3', 'Comment__4', 'Comment__5', 'Comment__6', 'Comment__7', 'Comment__8', 'Comment__9', 'Comment__10', 'Comment__11', 'Comment__12', 'Comment__13', 'Comment__14', 'Comment__15'] @component class RemoveKeys: @component.output_types(documents=List[Document]) def run(self, file_name: str): with open(file_name, 'r') as file: tickets = json.load(file) cleaned_tickets = [] for t in tickets: t = {k: v for k, v in t.items() if k in relevant_keys and v} cleaned_tickets.append(t) return {'documents': cleaned_tickets} We then need to create a custom JSON converter to transform the tickets into Document objects Haystack can understand: @component class JsonConverter: @component.output_types(documents=List[Document]) def run(self, tickets: List[Document]): tickets_documents = [] for t in tickets: if 'Parent id' in t: t = Document(content=json.dumps(t), meta={'Issue key': t['Issue key'], 'Issue id': t['Issue id'], 'Parent id': t['Parent id']}) else: t = Document(content=json.dumps(t), meta={'Issue key': t['Issue key'], 'Issue id': t['Issue id'], 'Parent id': ''}) tickets_documents.append(t) return {'documents': tickets_documents} Finally, we embed the Documents and write these embeddings into the ChromaDocumentStore: from haystack import Pipeline from haystack.components.writers import DocumentWriter from haystack_integrations.components.retrievers.chroma import ChromaEmbeddingRetriever from haystack.document_stores.types import DuplicatePolicy from haystack_integrations.components.embedders.jina import JinaDocumentEmbedder retriever = ChromaEmbeddingRetriever(document_store=document_store) retriever_reranker = ChromaEmbeddingRetriever(document_store=document_store) indexing_pipeline = Pipeline() indexing_pipeline.add_component('cleaner', RemoveKeys()) indexing_pipeline.add_component('converter', JsonConverter()) indexing_pipeline.add_component('embedder', JinaDocumentEmbedder(model='jina-embeddings-v2-base-en')) indexing_pipeline.add_component('writer', DocumentWriter(document_store=document_store, policy=DuplicatePolicy.SKIP)) indexing_pipeline.connect('cleaner', 'converter') indexing_pipeline.connect('converter', 'embedder') indexing_pipeline.connect('embedder', 'writer') indexing_pipeline.run({'cleaner': {'file_name': 'tickets.json'}}) This should create a progress bar and output a brief JSON containing information about what's been stored: Calculating embeddings: 100%|██████████| 1/1 [00:01<00:00, 1.21s/it] {'embedder': {'meta': {'model': 'jina-embeddings-v2-base-en', 'usage': {'total_tokens': 20067, 'prompt_tokens': 20067}}}, 'writer': {'documents_written': 31}} Build the Query Pipeline Let’s create a query pipeline so we can start comparing tickets. In Haystack 2.0 retrievers are tightly coupled to DocumentStores. If we pass the document store in the retriever we initialized earlier, this pipeline can access the documents we generated, and pass them to the reranker. The reranker then compares these documents directly with the question and ranks them based on relevance. We first define the custom cleaner to remove retrieve tickets that contain either the same issue ID or parent ID as the issue passed as query: from typing import Optional @component class RemoveRelated: @component.output_types(documents=List[Document]) def run(self, tickets: List[Document], query_id: Optional[str]): retrieved_tickets = [] for t in tickets: if not t.meta['Issue id'] == query_id and not t.meta['Parent id'] == query_id: retrieved_tickets.append(t) return {'documents': retrieved_tickets} We then embed the query, retrieve relevant documents, clean the selection, and finally rerank it: from haystack_integrations.components.embedders.jina import JinaTextEmbedder from haystack_integrations.components.rankers.jina import JinaRanker query_pipeline_reranker = Pipeline() query_pipeline_reranker.add_component('query_embedder_reranker', JinaTextEmbedder(model='jina-embeddings-v2-base-en')) query_pipeline_reranker.add_component('query_retriever_reranker', retriever_reranker) query_pipeline_reranker.add_component('query_cleaner_reranker', RemoveRelated()) query_pipeline_reranker.add_component('query_ranker_reranker', JinaRanker()) query_pipeline_reranker.connect('query_embedder_reranker.embedding', 'query_retriever_reranker.query_embedding') query_pipeline_reranker.connect('query_retriever_reranker', 'query_cleaner_reranker') query_pipeline_reranker.connect('query_cleaner_reranker', 'query_ranker_reranker')

To highlight the difference caused by the reranker,we analyzed the same pipeline without the final reranking step (the corresponding code was omitted in this post for the sake of readability but can be found in the notebook):

To compare the results of these two pipelines, we now define our query in the form of an existing ticket, here "ZOOKEEPER-3282": query_ticket_key = 'ZOOKEEPER-3282' with open('tickets.json', 'r') as file: tickets = json.load(file) for ticket in tickets: if ticket['Issue key'] == query_ticket_key: query = str(ticket) query_ticket_id = ticket['Issue id'] It concerns "a big refactor for the documetations" [sic]. You'll see that, despite the misspelling, Jina Reranker will correctly retrieve similar tickets.

Categories: Tech blog rss_feed Top-5 similar articles play_arrow GET TOP-5 Select reranker Read more August 26, 2024 • 13 minutes read The What and Why of Text-Image Modality Gap in CLIP Models You can't just use a CLIP model to retrieve text and images and sort the results by score. Why? Because of the modality gap. What is it, and where does it come from? August 22, 2024 • 8 minutes read Late Chunking in Long-Context Embedding Models Chunking long documents while preserving contextual information is challenging. We introduce the "Late Chunking" that leverages long-context embedding models to generate contextual chunk embeddings for better retrieval applications. July 31, 2024 • 17 minutes read Rephrased Labels Improve Zero-Shot Text Classification by 30% When using embedding models for zero-shot classification, rephrasing the class label to "This is seriously about 'LABEL'" gives higher accuracy vs. using LABEL alone. But how, and why? OFFICES location_on Berlin, Germany (HQ) Prinzessinnenstraße 19-20, 10969 Berlin, Germany Geschäftsanschrift: Leipzigerstr. 96, 10117 Berlin, Germany location_on Beijing, China Level 5, Building 6, No.48 Haidian West St. Beijing Haidian, China location_on Shenzhen, China 402, Floor 4, Fu'an Technology Building, Shenzhen Nanshan, China SEARCH FOUNDATION Embeddings Reranker Reader Segmenter Get Jina AI API key API Status COMPANY About us Contact sales Newsroom Intern program Join us open_in_new Download logo open_in_new TERMS Terms & Conditions Privacy Manage Cookies email language English science Jina AI GmbH © 2020-2024.

## COT_TOPIC_CHUNKING

#### 4 chunk(s)

Haystack, the composable open-source AI framework Haystack In this post, we'll show how to use them to create your own Jira ticket search engine to streamline your operations and never again waste time creating duplicate issues. To follow this tutorial, you'll need a Jina Reranker API key. You can create one with a free trial quota of a million tokens from the Jina Reranker website. 💡 You can follow along in Colab or by downloading the notebook.

BTW: - Any insights or suggestions are very welcomed.After the dicussions,I will create a series of tickets(An umbrella) - Since these works can be done parallelly, if you are interested in them, please don't hesitate,just assign to yourself, pick it up. (Notice: give me a ping to avoid the duplicated work)." } Finally, we run the query pipeline. In this case, it retrieves 20 tickets, eliminates ID-related entries, reranks them, and outputs the final selection of the 10 most relevant issues. Before the reranking step, the output includes 17 tickets: Rank Issue ID Issue Key Summary 1 13191544 ZOOKEEPER-3170 Umbrella for eliminating ZooKeeper flaky tests 2 13400622 ZOOKEEPER-4375 Quota cannot limit the specify value when multiply clients create/set znodes 3 13249579 ZOOKEEPER-3499 [admin server way] Add a complete backup mechanism for zookeeper internal 4 13295073 ZOOKEEPER-3775 Wrong message in IOException 5 13268474 ZOOKEEPER-3617 ZK digest ACL permissions gets overridden 6 13296971 ZOOKEEPER-3787 Apply modernizer-maven-plugin to build 7 13265507 ZOOKEEPER-3600 support the complete linearizable read and multiply read consistency level 8 13222060 ZOOKEEPER-3318 [CLI way]Add a complete backup mechanism for zookeeper internal 9 13262989 ZOOKEEPER-3587 Add a documentation about docker 10 13262130 ZOOKEEPER-3578 Add a new CLI: multi 11 13262828 ZOOKEEPER-3585 Add a documentation about RequestProcessors 12 13262494 ZOOKEEPER-3583 Add new apis to get node type and ttl time info 13 12998876 ZOOKEEPER-2519 zh->state should not be 0 while handle is active 14 13536435 ZOOKEEPER-4696 Update for Zookeeper latest version 15 13297249 ZOOKEEPER-3789 fix the build warnings about @see,@link,@return found by IDEA 16 12728973 ZOOKEEPER-1983 Append to zookeeper.out (not overwrite) to support logrotation 17 12478629 ZOOKEEPER-915 Errors that happen during sync() processing at the leader do not get propagated back to the client. After including the reranker, we now run the query pipeline: result = query_pipeline_reranker.run(data={'query_embedder_reranker':{'text': query}, 'query_retriever_reranker': {'top_k': 20}, 'query_cleaner_reranker': {'query_id': query_ticket_id}, 'query_ranker_reranker': {'query': query, 'top_k': 10} } ) for idx, res in enumerate(result['query_ranker_reranker']['documents']): print('Doc {}:'.format(idx + 1), res) The final output is the 10 most relevant tickets: Rank Issue ID Issue Key Summary 1 13262989 ZOOKEEPER-3587 Add a documentation about docker 2 13265507 ZOOKEEPER-3600 support the complete linearizable read and multiply read consistency level 3 13249579 ZOOKEEPER-3499 [admin server way] Add a complete backup mechanism for zookeeper internal 4 12478629 ZOOKEEPER-915 Errors that happen during sync() processing at the leader do not get propagated back to the client. 5 13262828 ZOOKEEPER-3585 Add a documentation about RequestProcessors 6 13297249 ZOOKEEPER-3789 fix the build warnings about @see,@link,@return found by IDEA 7 12998876 ZOOKEEPER-2519 zh->state should not be 0 while handle is active 8 13536435 ZOOKEEPER-4696 Update for Zookeeper latest version 9 12728973 ZOOKEEPER-1983 Append to zookeeper.out (not overwrite) to support logrotation 10 13222060 ZOOKEEPER-3318 [CLI way]Add a complete backup mechanism for zookeeper internal Advantages of Jina Embeddings and Reranker

To sum up this tutorial, we built a duplicate-ticket identification tool based on Jina Embeddings, Jina Reranker and Haystack 2.0. The results above clearly show the necessity for both Jina Embeddings to retrieve relevant documents through vector search, and Jina Reranker to finally obtain the most relevant content. If we take, for example, the two issues that relate to adding documentation, i.e. "ZOOKEEPER-3585" and "ZOOKEEPER-3587", we see that after the retrieval step, they are both correctly included in positions 11 and 9 respectively.

After reranking the documents, they are now both within the top 5 most relevant documents at positions 5 and 1 respectively, showing a significant improvement. By integrating both models in Haystack's pipelines, the entire tool is ready for use. This combination makes the Jina Haystack extension the perfect solution for your application. Categories: Tech blog rss_feed Top-5 similar articles play_arrow GET TOP-5 Select reranker Read more

## JINA-SEGMENTER-API

#### 209 chunk(s)

search


notifications


NEWS


PRODUCTS


COMPANY


Tech blog


April 10, 2024


Retrieve Jira Tickets with Jina Reranker and Haystack 2.0


Learn how to use Jina Reranker and Embeddings with Haystack to create your own Jira ticket search engine, streamlining your operations and never again waste time creating duplicate issues.


Francesco Kruk • 10 minutes read



Following the integration of Jina Embeddings into Deepset's Haystack 2.0 and the release of Jina Reranker, we're thrilled to announce that Jina Reranker is now also available through the Jina Haystack extension.



Jina AI | Haystack


Use the latest Jina AI embedding models


Haystack


Authors deepset


Reranker API


Maximize the search relevancy and RAG accuracy at ease



Haystack is an end-to-end framework that accompanies you in every step of the GenAI project life cycle. Whether you want to perform document search, retrieval-augmented generation (RAG), question answering, or answer generation, Haystack can orchestrate state-of-the-art embedding models and LLMs into pipelines to build end-to-end NLP applications and solve your use case.



Haystack | Haystack


Haystack, the composable open-source AI framework


Haystack



In this post, we'll show how to use them to create your own Jira ticket search engine to streamline your operations and never again waste time creating duplicate issues.



To follow this tutorial, you'll need a Jina Reranker API key. You can create one with a free trial quota of a million tokens from the Jina Reranker website.



You can follow along in Colab or by downloading the notebook.


Retrieving Jira Support Tickets



Any team dealing with a complex project has experienced the frustration of having an issue they want to file but not knowing if a ticket already exists for this problem.



In the following tutorial, we'll show you how you can easily create a tool yourself using Jina Reranker and Haystack pipelines, which suggests possible duplicate tickets to a new one being created.



By inputting a ticket that needs to be checked against all existing tickets, the pipeline will first retrieve from the database all related issues.


It'll then remove the initial ticket from the list (if it already existed in the database) and any child ticket (i.e. tickets whose parent ID corresponds to the original ticket).


The final selection now only comprises issues that might cover the same topic as the original ticket but were not marked as such in the database through their IDs. These tickets are reranked to ensure maximal relevance and enable you to identify duplicate entries in the database.


Getting the Dataset



To implement our solution, we've chosen all "In-progress" Jira tickets for the Apache Zookeeper project. This is an open-source service for coordinating processes of distributed applications.



We have placed the tickets in a JSON file to make them more convenient. Please download the file to your workspace.



Set up the Prerequisites



To install the requirements, run:



pip install --q chromadb haystack-ai jina-haystack chroma-haystack




To input the API key, set it as an environment variable:



import os


import getpass



os.environ["JINA_API_KEY"] = getpass.getpass()



If you're running this code through the notebook, getpass.getpass() will prompt you to input the API key below the corresponding code block. You can enter the key there and press enter to resume the tutorial. If you prefer, you can also substitute getpass.getpass() with the API key itself.


Build the Indexing Pipeline



The indexing pipeline will preprocess the tickets, turn them into vectors, and store them. We’ll use the Chroma DocumentStore as our vector database to store the vector embeddings, via the Chroma Document Store Haystack integration.



from haystack_integrations.document_stores.chroma import ChromaDocumentStore



document_store = ChromaDocumentStore()




We'll start by defining our custom data preprocessor to only consider relevant document fields and delete all empty entries:



import json


from typing import List


from haystack import Document, component



relevant_keys = ['Summary', 'Issue key', 'Issue id', 'Parent id', 'Issue type', 'Status', 'Project lead', 'Priority', 'Assignee', 'Reporter', 'Creator', 'Created', 'Updated', 'Last Viewed', 'Due Date', 'Labels',


                 'Description', 'Comment', 'Comment__1', 'Comment__2', 'Comment__3', 'Comment__4', 'Comment__5', 'Comment__6', 'Comment__7', 'Comment__8', 'Comment__9', 'Comment__10', 'Comment__11', 'Comment__12',
                 'Comment__13', 'Comment__14', 'Comment__15']


@component


class RemoveKeys:


    @component.output_types(documents=List[Document])
    def run(self, file_name: str):
        with open(file_name, 'r') as file:
            tickets = json.load(file)
        cleaned_tickets = []
        for t in tickets:
            t = {k: v for k, v in t.items() if k in relevant_keys and v}
            cleaned_tickets.append(t)
        return {'documents': cleaned_tickets}


We then need to create a custom JSON converter to transform the tickets into Document objects Haystack can understand:



@component


class JsonConverter:


    @component.output_types(documents=List[Document])
    def run(self, tickets: List[Document]):
        tickets_documents = []
        for t in tickets:
            if 'Parent id' in t:
                t = Document(content=json.dumps(t), meta={'Issue key': t['Issue key'], 'Issue id': t['Issue id'], 'Parent id': t['Parent id']})
            else:
                t = Document(content=json.dumps(t), meta={'Issue key': t['Issue key'], 'Issue id': t['Issue id'], 'Parent id': ''})
            tickets_documents.append(t)
        return {'documents': tickets_documents}


Finally, we embed the Documents and write these embeddings into the ChromaDocumentStore:



from haystack import Pipeline



from haystack.components.writers import DocumentWriter


from haystack_integrations.components.retrievers.chroma import ChromaEmbeddingRetriever


from haystack.document_stores.types import DuplicatePolicy



from haystack_integrations.components.embedders.jina import JinaDocumentEmbedder



retriever = ChromaEmbeddingRetriever(document_store=document_store)


retriever_reranker = ChromaEmbeddingRetriever(document_store=document_store)



indexing_pipeline = Pipeline()


indexing_pipeline.add_component('cleaner', RemoveKeys())


indexing_pipeline.add_component('converter', JsonConverter())


indexing_pipeline.add_component('embedder', JinaDocumentEmbedder(model='jina-embeddings-v2-base-en'))


indexing_pipeline.add_component('writer', DocumentWriter(document_store=document_store, policy=DuplicatePolicy.SKIP))



indexing_pipeline.connect('cleaner', 'converter')


indexing_pipeline.connect('converter', 'embedder')


indexing_pipeline.connect('embedder', 'writer')



indexing_pipeline.run({'cleaner': {'file_name': 'tickets.json'}})




This should create a progress bar and output a brief JSON containing information about what's been stored:



Calculating embeddings: 100%|██████████| 1/1 [00:01<00:00,  1.21s/it]


{'embedder': {'meta': {'model': 'jina-embeddings-v2-base-en',


'usage': {'total_tokens': 20067, 'prompt_tokens': 20067}}},

'writer': {'documents_written': 31}}

Build the Query Pipeline



Let’s create a query pipeline so we can start comparing tickets. In Haystack 2.0 retrievers are tightly coupled to DocumentStores. If we pass the document store in the retriever we initialized earlier, this pipeline can access the documents we generated, and pass them to the reranker. The reranker then compares these documents directly with the question and ranks them based on relevance.



We first define the custom cleaner to remove retrieve tickets that contain either the same issue ID or parent ID as the issue passed as query:



from typing import Optional



@component


class RemoveRelated:


    @component.output_types(documents=List[Document])
    def run(self, tickets: List[Document], query_id: Optional[str]):
        retrieved_tickets = []
        for t in tickets:
            if not t.meta['Issue id'] == query_id and not t.meta['Parent id'] == query_id:
                retrieved_tickets.append(t)
        return {'documents': retrieved_tickets}


We then embed the query, retrieve relevant documents, clean the selection, and finally rerank it:



from haystack_integrations.components.embedders.jina import JinaTextEmbedder


from haystack_integrations.components.rankers.jina import JinaRanker



query_pipeline_reranker = Pipeline()


query_pipeline_reranker.add_component('query_embedder_reranker', JinaTextEmbedder(model='jina-embeddings-v2-base-en'))


query_pipeline_reranker.add_component('query_retriever_reranker', retriever_reranker)


query_pipeline_reranker.add_component('query_cleaner_reranker', RemoveRelated())


query_pipeline_reranker.add_component('query_ranker_reranker', JinaRanker())



query_pipeline_reranker.connect('query_embedder_reranker.embedding', 'query_retriever_reranker.query_embedding')


query_pipeline_reranker.connect('query_retriever_reranker', 'query_cleaner_reranker')


query_pipeline_reranker.connect('query_cleaner_reranker', 'query_ranker_reranker')




To highlight the difference caused by the reranker, we analyzed the same pipeline without the final reranking step (the corresponding code was omitted in this post for the sake of readability but can be found in the notebook):



To compare the results of these two pipelines, we now define our query in the form of an existing ticket, here "ZOOKEEPER-3282":



query_ticket_key = 'ZOOKEEPER-3282'



with open('tickets.json', 'r') as file:


    tickets = json.load(file)


for ticket in tickets:


    if ticket['Issue key'] == query_ticket_key:
        query = str(ticket)
        query_ticket_id = ticket['Issue id']


It concerns "a big refactor for the documetations" [sic]. You'll see that, despite the misspelling, Jina Reranker will correctly retrieve similar tickets.



{


    "Summary": "a big refactor for the documetations"
    "Issue key": "ZOOKEEPER-3282"
    "Issue id:: 13216608
    "Parent id": ""
    "Issue Type": "Task"
    "Status": "In Progress"
    "Project lead": "phunt"
    "Priority": "Major"
    "Assignee": "maoling"
    "Reporter": "maoling"
    "Creator": "maoling"
    "Created": "19/Feb/19 11:50"
    "Updated": "04/Aug/19 12:48"
    "Last Viewed": "12/Mar/24 11:56"
    "Description": "Hi guys: I'am working on doing a big refactor for the documetations.it aims to - 1.make a better reading experiences and help users know more about zookeeper quickly,as good as other projects' doc(e.g redis,hbase). - 2.have less changes to diff with the original docs as far as possible. - 3.solve the problem when we have some new features or improvements,but cannot find a good place to doc it.   The new catalog may looks kile this: * is new one added. ** is the one to keep unchanged as far as possible. *** is the one modified. -------------------------------------------------------------- |---Overview    |---Welcome ** [1.1]    |---Overview ** [1.2]    |---Getting Started ** [1.3]    |---Release Notes ** [1.4] |---Developer    |---API *** [2.1]    |---Programmer's Guide ** [2.2]    |---Recipes *** [2.3]    |---Clients * [2.4]    |---Use Cases * [2.5] |---Admin & Ops    |---Administrator's Guide ** [3.1]    |---Quota Guide ** [3.2]    |---JMX ** [3.3]    |---Observers Gu

ide ** [3.4]    |---Dynamic Reconfiguration ** [3.5]    |---Zookeeper CLI * [3.6]    |---Shell * [3.7]    |---Configuration flags * [3.8]    |---Troubleshooting & Tuning  * [3.9] |---Contributor Guidelines    |---General Guidelines * [4.1]    |---ZooKeeper Internals ** [4.2] |---Miscellaneous    |---Wiki ** [5.1]    |---Mailing Lists ** [5.2] -------------------------------------------------------------- The Roadmap is: 1.(I pick up it : D)  1.1 write API[2.1], which includes the：    1.1.

1  original API Docs which is a Auto-generated java doc,just give a link.    1.1.2. Restful-api (the apis under the /zookeeper-contrib-rest/src/main/java/org/apache/zookeeper/server/jersey/resources)  1.2 write Clients[2.4], which includes the:      1.2.1 C client      1.2.2 zk-python, kazoo      1.2.3 Curator etc.......      look at an example from: https://redis.io/clients # write Recipes[2.

3], which includes the:  - integrate "Java Example" and "Barrier and Queue Tutorial"(Since some bugs in the examples and they are obsolete，we may delete something) into it.  - suggest users to use the recipes implements of Curator and link to the Curator's recipes doc.   # write Zookeeper CLI[3.6], which includes the:  - about how to use the zk command line interface [./zkCli.sh]    e.g ls /; get ; rmr;create -e -p etc.......  - look at an example from redis: https://redis.

io/topics/rediscli   # write shell[3.7], which includes the:   - list all usages of the shells under the zookeeper/bin. (e.g zkTxnLogToolkit.sh,zkCleanup.sh)   # write Configuration flags[3.8], which includes the:   - list all usages of configurations properties(e.g zookeeper.snapCount):   - move the original Advanced Configuration part of zookeeperAdmin.md into it.     look at an example from:https://coreos.com/etcd/docs/latest/op-guide/configuration.html    # write Troubleshooting & Tuning[3.

9], which includes the:   - move the original "Gotchas: Common Problems and Troubleshooting" part of Administrator's Guide.md into it.   - move the original "FAQ" into into it.   - add some new contents （e.g https://www.yumpu.com/en/document/read/29574266/building-an-impenetrable-zookeeper-pdf-github）.   look at an example from:https://redis.io/topics/problems                             https://coreos.com/etcd/docs/latest/tuning.html   # write General Guidelines[4.

1], which includes the:  - move the original "Logging" part of ZooKeeper Internals into it as the logger specification.  - write specifications about code, git commit messages,github PR  etc ...    look at an example from:    http://hbase.apache.org/book.html#hbase.commit.msg.format   # write Use Cases[2.5], which includes the:  - just move the context from: https://cwiki.apache.org/confluence/display/ZOOKEEPER/PoweredBy into it.  - add some new contents.(e.

g Apache Projects:Spark;Companies:twitter,fb)   -------------------------------------------------------------- BTW: - Any insights or suggestions are very welcomed.After the dicussions,I will create a series of tickets(An umbrella) - Since these works can be done parallelly, if you are interested in them, please don't hesitate,just assign to yourself, pick it up. (Notice: give me a ping to avoid the duplicated work)."
}




Finally, we run the query pipeline. In this case, it retrieves 20 tickets, eliminates ID-related entries, reranks them, and outputs the final selection of the 10 most relevant issues.



Before the reranking step, the output includes 17 tickets:



Rank	Issue ID	Issue Key	Summary


1	13191544	ZOOKEEPER-3170	Umbrella for eliminating ZooKeeper flaky tests


2	13400622	ZOOKEEPER-4375	Quota cannot limit the specify value when multiply clients create/set znodes


3	13249579	ZOOKEEPER-3499	[admin server way] Add a complete backup mechanism for zookeeper internal


4	13295073	ZOOKEEPER-3775	Wrong message in IOException


5	13268474	ZOOKEEPER-3617	ZK digest ACL permissions gets overridden


6	13296971	ZOOKEEPER-3787	Apply modernizer-maven-plugin to build


7	13265507	ZOOKEEPER-3600	support the complete linearizable read and multiply read consistency level


8	13222060	ZOOKEEPER-3318	[CLI way]Add a complete backup mechanism for zookeeper internal


9	13262989	ZOOKEEPER-3587	Add a documentation about docker


10	13262130	ZOOKEEPER-3578	Add a new CLI: multi


11	13262828	ZOOKEEPER-3585	Add a documentation about RequestProcessors


12	13262494	ZOOKEEPER-3583	Add new apis to get node type and ttl time info


13	12998876	ZOOKEEPER-2519	zh->state should not be 0 while handle is active


14	13536435	ZOOKEEPER-4696	Update for Zookeeper latest version


15	13297249	ZOOKEEPER-3789	fix the build warnings about @see,@link,@return found by IDEA


16	12728973	ZOOKEEPER-1983	Append to zookeeper.out (not overwrite) to support logrotation


17	12478629	ZOOKEEPER-915	Errors that happen during sync() processing at the leader do not get propagated back to the client.



After including the reranker, we now run the query pipeline:



result = query_pipeline_reranker.run(data={'query_embedder_reranker':{'text': query},


                                  'query_retriever_reranker': {'top_k': 20},
                                  'query_cleaner_reranker': {'query_id': query_ticket_id},
                                  'query_ranker_reranker': {'query': query, 'top_k': 10}
                                  }
                            )


for idx, res in enumerate(result['query_ranker_reranker']['documents']):


    print('Doc {}:'.format(idx + 1), res)


The final output is the 10 most relevant tickets:



Rank	Issue ID	Issue Key	Summary


1	13262989	ZOOKEEPER-3587	Add a documentation about docker


2	13265507	ZOOKEEPER-3600	support the complete linearizable read and multiply read consistency level


3	13249579	ZOOKEEPER-3499	[admin server way] Add a complete backup mechanism for zookeeper internal


4	12478629	ZOOKEEPER-915	Errors that happen during sync() processing at the leader do not get propagated back to the client.


5	13262828	ZOOKEEPER-3585	Add a documentation about RequestProcessors


6	13297249	ZOOKEEPER-3789	fix the build warnings about @see,@link,@return found by IDEA


7	12998876	ZOOKEEPER-2519	zh->state should not be 0 while handle is active


8	13536435	ZOOKEEPER-4696	Update for Zookeeper latest version


9	12728973	ZOOKEEPER-1983	Append to zookeeper.out (not overwrite) to support logrotation


10	13222060	ZOOKEEPER-3318	[CLI way]Add a complete backup mechanism for zookeeper internal


Advantages of Jina Embeddings and Reranker



To sum up this tutorial, we built a duplicate-ticket identification tool based on Jina Embeddings, Jina Reranker and Haystack 2.0. The results above clearly show the necessity for both Jina Embeddings to retrieve relevant documents through vector search, and Jina Reranker to finally obtain the most relevant content.



If we take, for example, the two issues that relate to adding documentation, i.e. "ZOOKEEPER-3585" and "ZOOKEEPER-3587", we see that after the retrieval step, they are both correctly included in positions 11 and 9 respectively. After reranking the documents, they are now both within the top 5 most relevant documents at positions 5 and 1 respectively, showing a significant improvement.



By integrating both models in Haystack's pipelines, the entire tool is ready for use. This combination makes the Jina Haystack extension the perfect solution for your application.



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