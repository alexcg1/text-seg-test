# a-magic-carpet-ride-building-vivid-product-stories-with-scenexplain

## SIMPLE_CHUNKING

#### 6 chunk(s)

"Embrace Yourself" is a piece of art in the form of a carpet, exuding minimalist charm and contemporary simplicity. This piece features the elegant, abstract depiction of a round, white figure at its center—an embodiment of purity and serenity. With meticulously crafted black outlines that grace the soothing white background, this carpet tells a subtle but impactful visual story. Each line is placed with thoughtful precision, evoking emotions and depth without cluttering the visual space. The characteristic round head of the figure in the design adds a touch of futuristic whimsy, creating a space for imagination to soar. The light gray tones and stark white spaces between the lines further enhance the abstract quality, offering a calm and peaceful atmosphere to any room. Whether adorning a modern living area or a chic office space, "Embrace Yourself" promises to be more than just a carpet—it is a promise of self-discovery and a celebration of space and form. Its simplicity and abstraction are not just visually appealing but are crafted to engage the observer in an almost meditative contemplation.

"Dancer" is an evocative piece of home decor where color and geometry resonate to a rhythm of their own. Adorning a rich navy blue background, this carpet features a dynamic composition of blue and orange lines and squares that glide across the fabric, suggesting movement and energy, much like a dancer in the spotlight. The striking orange lines dance diagonally, connecting a series of crisp white squares, which are themselves accented with black detailing, reminiscent of precise footwork on a dance stage. Unequivocally modern, "Dancer" employs the contrast of deep blues with vibrant oranges and whites to create an abstract visual narrative that is open to interpretation, yet commands attention. Each element on "Dancer" is painstakingly arranged to bring a sense of balance and fluidity, paralleling a choreographed performance that tells a story with every twist and turn. The pattern encourages the eye to leap and land much like a viewer watching an enthralling solo dance performance, making "Dancer" not just a carpet, but a conversation piece that captivates and inspires.

Product story generation: A holistic solution In AKIA’s use case, their product manager wants to automatically create stories for all their products. The stories should use some high-quality examples as a guide, which contain aesthetic explanations. Their specific needs are: Textual descriptions of their products Stories for each product that follow the examples they provide Batch processing of images triggered by the chat channel Based on these requirements, visual question answering (VQA) is the best fit, because: Visual question answering outputs textual descriptions. In the question, you can also provide a prompt in a specific format on demand. You can inject your own examples into the prompt to guide the model’s output. Once you have the prompt’s basic structure, you can convert it to a template with variables that can be automatically populated each time you use it. SceneXplain’s API provides a wide range of options for configuring your request, including image captioning, alt-text generation, visual question answering, JSON output, and more.

Several fields are required to execute a VQA task via the API: API endpoint: https://api.scenex.jina.ai/v1/describe API key: 'x-api-key': token ${YOUR_API_KEY}. You can generate and manage your API key on our API page. Request payload, which is your task configuration, providing the image you want to process, setting question_answer in the features property, and setting your prompt in the question property. Here’s a code snippet for such an API call in JavaScript: const body = { "data": [ { "image": "The image you want to process, it can be a base64 string or a URL", "features": [ "question_answer" ], "algorithm": "jelly", "languages": [ "en" ], "question": "your prompt" } ] }; const YOUR_API_KEY = 'your_generated_API_key_here'; fetch('https://api.scenex.jina.ai/v1/describe', { headers: { 'x-api-key': `token ${YOUR_API_KEY}`, 'content-type': 'application/json' }, body: JSON.stringify(body), method: 'POST' }) .then(async (resp) => { if (resp.ok) { const data = await resp.json(); console.log(data); } }); The payload’s data property is an array that can have several configurations, meaning you can batch-process your images via the API. Connecting AKIA to SceneXplain’s API via bot AKIA uses Lark for their internal messaging, which is a Chinese application similar to Slack, Microsoft Teams, and Discord. An employee of AKIA can simply send a message to their SceneXplain chatbot that includes an image and a topic. The chatbot sends back a detailed description of the carpet. Here’s how it would look in English: Behind the scenes, there’s a middleware service that connects Lark to the SceneXplain API: It shuttles the data between the two services and performs several key tasks: Message validation API payload generation API calling Message formatting The process is: Receive image and topic in message from Lark chatbot Check message format is valid. If not, return an error. Base64-encode the image and wrap both it and the topic into a payload, using the topic as the question in visual question answering (VQA) Send the payload to the API API generates a description and sends that back Format the message to fit Lark’s API Send the message back to the Lark chatbot 💡

We’re not going to go into the workings of the LarkAPI here. We want to keep this post as service-agnostic as possible, so it’s relevant to whatever service you want to integrate with SceneXplain. We’re just going to focus on the middleware (“Your service” in the diagram above).

All you need is a few lines of code to reformulatethe request, pass it on, and then do the same for the response. // Function to call SceneXplain `/describe` API const describe = async (image: string, name: string, topic: string) => { // prepare payload const newBody = { data: [ { image: image, features: [ "question_answer" ], languages: ['zh-CN'], algorithm: 'Jelly', question: `your prompt, incorporating ${name} and ${topic}, plus optional example for desired output format for in-context learning` } ] } // call SceneXplain API try { const resp = await fetch('https://api.scenex.jina.ai/v1/describe', { headers: { 'x-api-key': `token ${process.env.scenexKey}`, 'content-type': 'application/json' }, body: JSON.stringify(newBody), method: 'POST', }); if (!resp.ok) { const error = await resp.text(); throw error; } const data = await resp.json() as any; console.log(`describe result: ${JSON.stringify(data, null, 2)}`); if (data.code !== 200) throw data; const result = data.result[0]; // get result in the required language return result.i18n['zh-CN']; } catch (e) { console.log(`describe error: ${JSON.stringify(e, null, 2)}`); return ''; } } As you can see from the question field in the example payload above, you can include some example output to help the algorithm in generating the kind of description you desire. And, of course, you don’t have to use JavaScript to build your middleware service - any programming language with an HTTP library can access SceneXplain’s API. Wrapping up Do you want to follow in AKIA’s footsteps and use SceneXplain to build vivid product stories from your images and videos? Head over to https://scenex.jina.ai to get started. Or for business use cases, fill in our sales form and we’ll be happy to roll out the red carpet. Categories: Tech blog rss_feed Top-5 similar articles play_arrow GET TOP-5 Select reranker Read more August 26, 2024 • 13 minutes read The What and Why of Text-Image Modality Gap in CLIP Models You can't just use a CLIP model to retrieve text and images and sort the results by score. Why? Because of the modality gap. What is it, and where does it come from? August 22, 2024 • 8 minutes read Late Chunking in Long-Context Embedding Models Chunking long documents while preserving contextual information is challenging. We introduce the "Late Chunking" that leverages long-context embedding models to generate contextual chunk embeddings for better retrieval applications. July 31, 2024 • 17 minutes read Rephrased Labels Improve Zero-Shot Text Classification by 30% When using embedding models for zero-shot classification, rephrasing the class label to "This is seriously about 'LABEL'" gives higher accuracy vs. using LABEL alone. But how, and why? OFFICES location_on Berlin, Germany (HQ) Prinzessinnenstraße 19-20, 10969 Berlin, Germany Geschäftsanschrift: Leipzigerstr. 96, 10117 Berlin, Germany location_on Beijing, China Level 5, Building 6, No.48 Haidian West St. Beijing Haidian, China location_on Shenzhen, China 402, Floor 4, Fu'an Technology Building, Shenzhen Nanshan, China SEARCH FOUNDATION Embeddings Reranker Reader Segmenter Get Jina AI API key API Status COMPANY About us Contact sales Newsroom Intern program Join us open_in_new Download logo open_in_new TERMS Terms & Conditions Privacy Manage Cookies email language English science Jina AI GmbH © 2020-2024.

## COT_TOPIC_CHUNKING

#### 13 chunk(s)

search notifications NEWS PRODUCTS COMPANY Tech blog December 21, 2023 A Magic Carpet Ride: Building Vivid Product Stories with SceneXplain See how companies are integrating SceneXplain with their existing infrastructure to power their product descriptions and storytelling Lisa Li, Alex C-G • 7 minutes read We recently wrote about SceneXplain's new JSON Schema Store, which lets you use predefined JSON schemas to extract information from images in a structured format. In this post, we're going to see how that's used by our partner, AKIA Carpet & Rugs, for building up an AI-powered product stories generation bot to empower sales. In our prior examples, we've primarily used either cURL or Python to access SceneXplain's API. But in this post, we're switching things up a bit by using JavaScript.

About AKIA Carpet & Rugs In July 2008, Gary Chen founded AKIA Carpet & Rugs, which is now marking its 15th year of operation. The team, initially inspired by traditional Asian craftsmanship, has been dedicated to developing contemporary aesthetic styles. AKIA has grown into a brand known for its unique fusion of modern art with traditional design and weaving techniques.

As a carpet manufacturer, AKIA specializes in a range of products including mid-to-high-end decorative carpets, tapestries, and carpets for specific projects. The company integrates design, research, production, and sales, both domestically and internationally. Known for innovative design and high-quality products, AKIA has earned a solid reputation in China's high-end carpet market. Crafting a Winning Product Story with SceneXplain AKIA Carpet & Rugs primarily caters to the mid-to-high-end market, focusing on the aesthetic appeal of their products. Their clientele often looks for carpets that not only complement their home design but also express their unique taste. Recognizing this, AKIA collaborates with skilled designers to create a diverse range of styles, resulting in an extensive collection of carpet designs and images. The challenge lies in effectively communicating the artistic value of these designs to discerning customers, a crucial factor in attracting clients. Previously, crafting compelling narratives for a large array of product images, akin to artworks, was a daunting task. This required copywriters who were not only skilled in writing but also knowledgeable in design and art. Additionally, the need to swiftly identify the perfect product image from an extensive collection to meet specific customer preferences was a significant challenge. Traditional image labeling methods, focusing on basic attributes like color, shape, and material, proved insufficient for customers who often describe their needs in more abstract terms. SceneXplain offers a dual solution to these challenges. Its approach is based on narration rather than mere description, aiming to weave engaging stories around images. This aligns with SceneXplain's core philosophy: storytelling brings images to life. By providing stories that resonate with the artistic nature of AKIA's products, SceneXplain addresses their need for an intuitive, aesthetically aligned way of presenting their carpets.

"Embrace Yourself" is a piece of art in the form of a carpet, exuding minimalist charm and contemporary simplicity. This piece features the elegant, abstract depiction of a round, white figure at its center—an embodiment of purity and serenity. With meticulously crafted black outlines that grace the soothing white background, this carpet tells a subtle but impactful visual story. Each line is placed with thoughtful precision, evoking emotions and depth without cluttering the visual space. The characteristic round head of the figure in the design adds a touch of futuristic whimsy, creating a space for imagination to soar. The light gray tones and stark white spaces between the lines further enhance the abstract quality, offering a calm and peaceful atmosphere to any room. Whether adorning a modern living area or a chic office space, "Embrace Yourself" promises to be more than just a carpet—it is a promise of self-discovery and a celebration of space and form. Its simplicity and abstraction are not just visually appealing but are crafted to engage the observer in an almost meditative contemplation.

"Dancer" is an evocative piece of home decor where color and geometry resonate to a rhythm of their own. Adorning a rich navy blue background, this carpet features a dynamic composition of blue and orange lines and squares that glide across the fabric, suggesting movement and energy, much like a dancer in the spotlight. The striking orange lines dance diagonally, connecting a series of crisp white squares, which are themselves accented with black detailing, reminiscent of precise footwork on a dance stage. Unequivocally modern,

"Dancer" employs the contrast of deep blues with vibrant oranges and whites to create an abstract visual narrative that is open to interpretation, yet commands attention. Each element on "Dancer" is painstakingly arranged to bring a sense of balance and fluidity, paralleling a choreographed performance that tells a story with every twist and turn. The pattern encourages the eye to leap and land much like a viewer watching an enthralling solo dance performance, making "Dancer" not just a carpet, but a conversation piece that captivates and inspires.

Product story generation: A holistic solution In AKIA’s use case, their product manager wants to automatically create stories for all their products. The stories should use some high-quality examples as a guide, which contain aesthetic explanations. Their specific needs are: Textual descriptions of their products Stories for each product that follow the examples they provide Batch processing of images triggered by the chat channel Based on these requirements, visual question answering (VQA) is the best fit, because: Visual question answering outputs textual descriptions. In the question, you can also provide a prompt in a specific format on demand. You can inject your own examples into the prompt to guide the model’s output. Once you have the prompt’s basic structure, you can convert it to a template with variables that can be automatically populated each time you use it. SceneXplain’s API provides a wide range of options for configuring your request, including image captioning, alt-text generation, visual question answering, JSON output, and more. Several fields are required to execute a VQA task via the API: API endpoint: https://api.scenex.jina.ai/v1/describe API key: 'x-api-key': token ${YOUR_API_KEY}. You can generate and manage your API key on our API page. Request payload, which is your task configuration, providing the image you want to process, setting question_answer in the features property, and setting your prompt in the question property. Here’s a code snippet for such an API call in JavaScript: const body = { "data": [ { "image": "The image you want to process, it can be a base64 string or a URL", "features": [ "question_answer" ], "algorithm": "jelly", "languages": [ "en" ], "question": "your prompt" } ] }; const YOUR_API_KEY = 'your_generated_API_key_here'; fetch('https://api.scenex.jina.ai/v1/describe', { headers: { 'x-api-key': `token ${YOUR_API_KEY}`, 'content-type': 'application/json' }, body: JSON.stringify(body), method: 'POST' }) .then(async (resp) => { if (resp.ok) { const data = await resp.json(); console.log(data); } }); The payload’s data property is an array that can have several configurations, meaning you can batch-process your images via the API.

Connecting AKIA to SceneXplain’s API via bot AKIA uses Lark for their internal messaging, which is a Chinese application similar to Slack, Microsoft Teams, and Discord. An employee of AKIA can simply send a message to their SceneXplain chatbot that includes an image and a topic. The chatbot sends back a detailed description of the carpet. Here’s how it would look in English:

We’re not going to go into the workings of the LarkAPI here. We want to keep this post as service-agnostic as possible, so it’s relevant to whatever service you want to integrate with SceneXplain. We’re just going to focus on the middleware (“Your service” in the diagram above). All you need is a few lines of code to reformulate the request, pass it on, and then do the same for the response. // Function to call SceneXplain `/describe` API const describe = async (image: string, name: string, topic: string) => { // prepare payload const newBody = { data: [ { image: image, features: [ "question_answer" ], languages: ['zh-CN'], algorithm: 'Jelly', question: `your prompt, incorporating ${name} and ${topic}, plus optional example for desired output format for in-context learning` } ] } // call SceneXplain API try { const resp = await fetch('https://api.scenex.jina.ai/v1/describe', { headers: { 'x-api-key': `token ${process.env.scenexKey}`, 'content-type': 'application/json' }, body: JSON.stringify(newBody), method: 'POST', }); if (!resp.ok) { const error = await resp.text(); throw error; } const data = await resp.json() as any; console.log(`describe result: ${JSON.stringify(data, null, 2)}`); if (data.code !== 200) throw data; const result = data.result[0]; // get result in the required language return result.i18n['zh-CN']; } catch (e) { console.log(`describe error: ${JSON.stringify(e, null, 2)}`); return ''; } } As you can see from the question field in the example payload above, you can include some example output to help the algorithm in generating the kind of description you desire. And, of course, you don’t have to use JavaScript to build your middleware service - any programming language with an HTTP library can access SceneXplain’s API. Wrapping up Do you want to follow in AKIA’s footsteps and use SceneXplain to build vivid product stories from your images and videos? Head over to https://scenex.jina.ai to get started. Or for business use cases, fill in our sales form and we’ll be happy to roll out the red carpet. Categories: Tech blog rss_feed Top-5 similar articles play_arrow GET TOP-5 Select reranker Read more

August 26, 2024 • 13 minutes read The What and Why of Text-Image Modality Gap in CLIP Models You can't just use a CLIP model to retrieve text and images and sort the results by score. Why? Because of the modality gap. What is it, and where does it come from? August 22, 2024 • 8 minutes read

Late Chunking in Long-Context Embedding Models Chunking long documents while preserving contextual information is challenging. We introduce the "Late Chunking" that leverages long-context embedding models to generate contextual chunk embeddings for better retrieval applications.

July 31, 2024 • 17 minutes read Rephrased Labels Improve Zero-Shot Text Classification by 30% When using embedding models for zero-shot classification, rephrasing the class label to "This is seriously about 'LABEL'" gives higher accuracy vs. using LABEL alone. But how, and why?

OFFICES location_on Berlin, Germany (HQ) Prinzessinnenstraße 19-20, 10969 Berlin, Germany Geschäftsanschrift: Leipzigerstr. 96, 10117 Berlin, Germany location_on Beijing, China Level 5, Building 6, No.48 Haidian West St. Beijing Haidian, China location_on Shenzhen, China 402, Floor 4, Fu'an Technology Building, Shenzhen Nanshan, China SEARCH FOUNDATION Embeddings Reranker Reader Segmenter Get Jina AI API key API Status COMPANY About us Contact sales Newsroom Intern program Join us open_in_new Download logo open_in_new TERMS Terms & Conditions Privacy Manage Cookies email language English science Jina AI GmbH © 2020-2024.

## SUMMARY_CHUNKING

#### 5 chunk(s)

"Embrace Yourself" is a piece of art in the form of a carpet, exuding minimalist charm and contemporary simplicity. This piece features the elegant, abstract depiction of a round, white figure at its center—an embodiment of purity and serenity. With meticulously crafted black outlines that grace the soothing white background, this carpet tells a subtle but impactful visual story. Each line is placed with thoughtful precision, evoking emotions and depth without cluttering the visual space. The characteristic round head of the figure in the design adds a touch of futuristic whimsy, creating a space for imagination to soar. The light gray tones and stark white spaces between the lines further enhance the abstract quality, offering a calm and peaceful atmosphere to any room. Whether adorning a modern living area or a chic office space, "Embrace Yourself" promises to be more than just a carpet—it is a promise of self-discovery and a celebration of space and form. Its simplicity and abstraction are not just visually appealing but are crafted to engage the observer in an almost meditative contemplation.

"Dancer" is an evocative piece of home decor where color and geometry resonate to a rhythm of their own. Adorning a rich navy blue background, this carpet features a dynamic composition of blue and orange lines and squares that glide across the fabric, suggesting movement and energy, much like a dancer in the spotlight. The striking orange lines dance diagonally, connecting a series of crisp white squares, which are themselves accented with black detailing, reminiscent of precise footwork on a dance stage. Unequivocally modern, "Dancer" employs the contrast of deep blues with vibrant oranges and whites to create an abstract visual narrative that is open to interpretation, yet commands attention. Each element on "Dancer" is painstakingly arranged to bring a sense of balance and fluidity, paralleling a choreographed performance that tells a story with every twist and turn. The pattern encourages the eye to leap and land much like a viewer watching an enthralling solo dance performance, making "Dancer" not just a carpet, but a conversation piece that captivates and inspires.

Product story generation: A holistic solution In AKIA’s use case, their product manager wants to automatically create stories for all their products. The stories should use some high-quality examples as a guide, which contain aesthetic explanations. Their specific needs are: Textual descriptions of their products Stories for each product that follow the examples they provide Batch processing of images triggered by the chat channel Based on these requirements, visual question answering (VQA) is the best fit, because: Visual question answering outputs textual descriptions. In the question, you can also provide a prompt in a specific format on demand. You can inject your own examples into the prompt to guide the model’s output. Once you have the prompt’s basic structure, you can convert it to a template with variables that can be automatically populated each time you use it.

SceneXplain’s API provides a wide range of options for configuring your request, including image captioning, alt-text generation, visual question answering, JSON output, and more. Several fields are required to execute a VQA task via the API: API endpoint: https://api.scenex.jina.ai/v1/describe API key: 'x-api-key': token ${YOUR_API_KEY}. You can generate and manage your API key on our API page. Request payload, which is your task configuration, providing the image you want to process, setting question_answer in the features property, and setting your prompt in the question property. Here’s a code snippet for such an API call in JavaScript: const body = { "data": [ { "image": "The image you want to process, it can be a base64 string or a URL", "features": [ "question_answer" ], "algorithm": "jelly", "languages": [ "en" ], "question": "your prompt" } ] }; const YOUR_API_KEY = 'your_generated_API_key_here'; fetch('https://api.scenex.jina.ai/v1/describe', { headers: { 'x-api-key': `token ${YOUR_API_KEY}`, 'content-type': 'application/json' }, body: JSON.stringify(body), method: 'POST' }) .then(async (resp) => { if (resp.ok) { const data = await resp.json(); console.log(data); } }); The payload’s data property is an array that can have several configurations, meaning you can batch-process your images via the API.

Wrapping up Do you want to follow in AKIA’s footstepsand use SceneXplain to build vivid product stories from your images and videos? Head over to https://scenex.jina.ai to get started. Or for business use cases, fill in our sales form and we’ll be happy to roll out the red carpet. Categories: Tech blog rss_feed Top-5 similar articles play_arrow GET TOP-5 Select reranker Read more August 26, 2024 • 13 minutes read The What and Why of Text-Image Modality Gap in CLIP Models You can't just use a CLIP model to retrieve text and images and sort the results by score. Why? Because of the modality gap. What is it, and where does it come from? August 22, 2024 • 8 minutes read Late Chunking in Long-Context Embedding Models Chunking long documents while preserving contextual information is challenging. We introduce the "Late Chunking" that leverages long-context embedding models to generate contextual chunk embeddings for better retrieval applications. July 31, 2024 • 17 minutes read Rephrased Labels Improve Zero-Shot Text Classification by 30% When using embedding models for zero-shot classification, rephrasing the class label to "This is seriously about 'LABEL'" gives higher accuracy vs. using LABEL alone. But how, and why? OFFICES location_on Berlin, Germany (HQ) Prinzessinnenstraße 19-20, 10969 Berlin, Germany Geschäftsanschrift: Leipzigerstr. 96, 10117 Berlin, Germany location_on Beijing, China Level 5, Building 6, No.48 Haidian West St. Beijing Haidian, China location_on Shenzhen, China 402, Floor 4, Fu'an Technology Building, Shenzhen Nanshan, China SEARCH FOUNDATION Embeddings Reranker Reader Segmenter Get Jina AI API key API Status COMPANY About us Contact sales Newsroom Intern program Join us open_in_new Download logo open_in_new TERMS Terms & Conditions Privacy Manage Cookies email language English science Jina AI GmbH © 2020-2024.

## JINA-SEGMENTER-API

#### 168 chunk(s)

search


notifications


NEWS


PRODUCTS


COMPANY


Tech blog


December 21, 2023


A Magic Carpet Ride: Building Vivid Product Stories with SceneXplain


See how companies are integrating SceneXplain with their existing infrastructure to power their product descriptions and storytelling


Lisa Li, Alex C-G • 7 minutes read



We recently wrote about SceneXplain's new JSON Schema Store, which lets you use predefined JSON schemas to extract information from images in a structured format. In this post, we're going to see how that's used by our partner, AKIA Carpet & Rugs, for building up an AI-powered product stories generation bot to empower sales.



In our prior examples, we've primarily used either cURL or Python to access SceneXplain's API. But in this post, we're switching things up a bit by using JavaScript.



About AKIA Carpet & Rugs



In July 2008, Gary Chen founded AKIA Carpet & Rugs, which is now marking its 15th year of operation. The team, initially inspired by traditional Asian craftsmanship, has been dedicated to developing contemporary aesthetic styles. AKIA has grown into a brand known for its unique fusion of modern art with traditional design and weaving techniques.



As a carpet manufacturer, AKIA specializes in a range of products including mid-to-high-end decorative carpets, tapestries, and carpets for specific projects. The company integrates design, research, production, and sales, both domestically and internationally. Known for innovative design and high-quality products, AKIA has earned a solid reputation in China's high-end carpet market.



Crafting a Winning Product Story with SceneXplain



AKIA Carpet & Rugs primarily caters to the mid-to-high-end market, focusing on the aesthetic appeal of their products. Their clientele often looks for carpets that not only complement their home design but also express their unique taste. Recognizing this, AKIA collaborates with skilled designers to create a diverse range of styles, resulting in an extensive collection of carpet designs and images. The challenge lies in effectively communicating the artistic value of these designs to discerning customers, a crucial factor in attracting clients.



Previously, crafting compelling narratives for a large array of product images, akin to artworks, was a daunting task. This required copywriters who were not only skilled in writing but also knowledgeable in design and art. Additionally, the need to swiftly identify the perfect product image from an extensive collection to meet specific customer preferences was a significant challenge. Traditional image labeling methods, focusing on basic attributes like color, shape, and material, proved insufficient for customers who often describe their needs in more abstract terms.



SceneXplain offers a dual solution to these challenges. Its approach is based on narration rather than mere description, aiming to weave engaging stories around images. This aligns with SceneXplain's core philosophy: storytelling brings images to life. By providing stories that resonate with the artistic nature of AKIA's products, SceneXplain addresses their need for an intuitive, aesthetically aligned way of presenting their carpets.



"Embrace Yourself" is a piece of art in the form of a carpet, exuding minimalist charm and contemporary simplicity. This piece features the elegant, abstract depiction of a round, white figure at its center—an embodiment of purity and serenity. With meticulously crafted black outlines that grace the soothing white background, this carpet tells a subtle but impactful visual story. Each line is placed with thoughtful precision, evoking emotions and depth without cluttering the visual space. The characteristic round head of the figure in the design adds a touch of futuristic whimsy, creating a space for imagination to soar. The light gray tones and stark white spaces between the lines further enhance the abstract quality, offering a calm and peaceful atmosphere to any room. Whether adorning a modern living area or a chic office space, "Embrace Yourself" promises to be more than just a carpet—it is a promise of self-discovery and a celebration of space and form. Its simplicity and abstraction are not just visually appealing but are crafted to engage the observer in an almost meditative contemplation.


"Dancer" is an evocative piece of home decor where color and geometry resonate to a rhythm of their own. Adorning a rich navy blue background, this carpet features a dynamic composition of blue and orange lines and squares that glide across the fabric, suggesting movement and energy, much like a dancer in the spotlight. 

The striking orange lines dance diagonally, connecting a series of crisp white squares, which are themselves accented with black detailing, reminiscent of precise footwork on a dance stage. Unequivocally modern, "Dancer" employs the contrast of deep blues with vibrant oranges and whites to create an abstract visual narrative that is open to interpretation, yet commands attention. 

Each element on "Dancer" is painstakingly arranged to bring a sense of balance and fluidity, paralleling a choreographed performance that tells a story with every twist and turn. The pattern encourages the eye to leap and land much like a viewer watching an enthralling solo dance performance, making "Dancer" not just a carpet, but a conversation piece that captivates and inspires.


Product story generation: A holistic solution



In AKIA’s use case, their product manager wants to automatically create stories for all their products. The stories should use some high-quality examples as a guide, which contain aesthetic explanations. Their specific needs are:



Textual descriptions of their products


Stories for each product that follow the examples they provide


Batch processing of images triggered by the chat channel



Based on these requirements, visual question answering (VQA) is the best fit, because:



Visual question answering outputs textual descriptions.


In the question, you can also provide a prompt in a specific format on demand.


You can inject your own examples into the prompt to guide the model’s output.


Once you have the prompt’s basic structure, you can convert it to a template with variables that can be automatically populated each time you use it.



SceneXplain’s API provides a wide range of options for configuring your request, including image captioning, alt-text generation, visual question answering, JSON output, and more.



Several fields are required to execute a VQA task via the API:



API endpoint: https://api.scenex.jina.ai/v1/describe


API key: 'x-api-key': token ${YOUR_API_KEY}. You can generate and manage your API key on our API page.


Request payload, which is your task configuration, providing the image you want to process, setting question_answer in the features property, and setting your prompt in the question property.



Here’s a code snippet for such an API call in JavaScript:



const body = {


"data": [
    

{
			

"image": "The image you want to process, it can be a base64 string or a URL",
      

"features": [
        

"question_answer"
      ],
      

"algorithm": "jelly",
      

"languages": [
        

"en"
      ],
		

"question": "your prompt"
    }
  ]
};



const YOUR_API_KEY = 'your_generated_API_key_here';



fetch('https://api.scenex.jina.ai/v1/describe', {


headers: {
    '

x-api-key': `token ${YOUR_API_KEY}`,
    '

content-type': 'application/json'
  },
  

body: JSON.stringify(body),
  

method: 'POST'
})
.

then(async (resp) => {
  

if (resp.ok) {
    

const data = await resp.json();
    

console.log(data);
  }
});




The payload’s data property is an array that can have several configurations, meaning you can batch-process your images via the API.



Connecting AKIA to SceneXplain’s API via bot



AKIA uses Lark for their internal messaging, which is a Chinese application similar to Slack, Microsoft Teams, and Discord. An employee of AKIA can simply send a message to their SceneXplain chatbot that includes an image and a topic.



The chatbot sends back a detailed description of the carpet. Here’s how it would look in English:



Behind the scenes, there’s a middleware service that connects Lark to the SceneXplain API:



It shuttles the data between the two services and performs several key tasks:



Message validation


API payload generation


API calling


Message formatting



The process is:



Receive image and topic in message from Lark chatbot


Check message format is valid. If not, return an error.


Base64-encode the image and wrap both it and the topic into a payload, using the topic as the question in visual question answering (VQA)


Send the payload to the API


API generates a description and sends that back


Format the message to fit Lark’s API


Send the message back to the Lark chatbot


We’re not going to go into the workings of the Lark API here. We want to keep this post as service-agnostic as possible, so it’s relevant to whatever service you want to integrate with SceneXplain.



We’re just going to focus on the middleware (“Your service” in the diagram above). All you need is a few lines of code to reformulate the request, pass it on, and then do the same for the response.



// Function to call SceneXplain `/describe` API


const describe = async (image: string, name: string, topic: string) => {


// prepare payload
  

const newBody = {
    

data: [
      

{
        

image: image,
        

features: [
          

"question_answer"
        ],
        

languages: ['zh-CN'],
        

algorithm: 'Jelly',
        

question: `your prompt, incorporating ${name} and ${topic}, plus optional example for desired output format for in-context learning`
      }
    ]
  }

  

// call SceneXplain API
  

try {
    

const resp = await fetch('https://api.scenex.jina.ai/v1/describe', {
      

headers: {
        '

x-api-key': `token ${process.env.scenexKey}`,
        '

content-type': 'application/json'
      },
      

body: JSON.stringify(newBody),
      

method: 'POST',
    });
    

if (!resp.ok) {
      

const error = await resp.text();
      

throw error;
    }
    

const data = await resp.json() as any;
    

console.log(`describe result: ${JSON.stringify(data, null, 2)}`);
    

if (data.code !== 200) throw data;
    

const result = data.result[0];

    

// get result in the required language
    

return result.i18n['zh-CN'];
  } 

catch (e) {
    

console.log(`describe error: ${JSON.stringify(e, null, 2)}`);
    

return '';
  }
}




As you can see from the question field in the example payload above, you can include some example output to help the algorithm in generating the kind of description you desire. And, of course, you don’t have to use JavaScript to build your middleware service - any programming language with an HTTP library can access SceneXplain’s API.



Wrapping up



Do you want to follow in AKIA’s footsteps and use SceneXplain to build vivid product stories from your images and videos? Head over to https://scenex.jina.ai to get started. Or for business use cases, fill in our sales form and we’ll be happy to roll out the red carpet.



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