# theres-a-time-and-a-place-unleashing-dynamic-variables-in-promptperfect

## SIMPLE_CHUNKING

#### 10 chunk(s)

Alex C-G • 8 minutes read Back in the mists of time, PromptPerfect introduced its Prompt-as-a-Service feature, allowing you to serve your prompts via a RESTful API and call them from Python, JavaScript or cURL. What’s Next for Prompt Engineering? PromptPerfect’s Prompt as a Service! Deploy prompts and flexible template prompts as REST API services, and integrate them into your applications with just a few clicks PromptPerfect Let’s imagine we’re building an AI-powered recipe website. We want users to be able to click a button that suggests a delicious recipe for them. To do that, we can create a prompt and deploy it as a service. We would then incorporate that into our website via Prompt-as-a-Service’s RESTful API. For example, we could have a prompt that suggested recipes to users: 💡 Incorporating a RESTful API into your website is way outside the scope of this post, so we’ll just use cURL moving forwards. But rest assured, you can do this in any language or framework with an HTTP library. By calling the prompt, a user could get a new recipe each time: curl "https://api.promptperfect.jina.ai/RYNiqoT3txBjPoALnV46" \ -H "x-api-key: token $YOUR_GENERATED_SECRET" \ -H "content-type: application/json" View output Certainly!

Below is a recipe for a classic Italian dish, Spaghetti Carbonara. This dish is known for its creamy texture and rich flavors, achieved with minimal ingredients. Enjoy! Spaghetti Carbonara Ingredients 400g spaghetti 150g pancetta or guanciale, diced 3 large eggs 1 cup (100g) freshly grated Parmesan cheese, plus extra for serving 2 cloves garlic, peeled and left whole 2 tablespoons extra-virgin olive oil Salt and freshly ground black pepper A small handful of fresh parsley, chopped (optional) Instructions Cook the Pasta Bring a large pot of salted water to a boil. Add the spaghetti and cook according to the package instructions until al dente. Reserve 1 cup of pasta water before draining the spaghetti. Prepare the Sauce In a small bowl, whisk together the eggs and grated Parmesan cheese until well combined. Set aside. Cook the Pancetta While the pasta is cooking, heat the olive oil in a large skillet over medium heat. Add the pancetta or guanciale and the whole garlic cloves. Cook, stirring frequently, until the meat is crispy and golden, about 5 minutes. Remove and discard the garlic cloves. Combine Pasta and Pancetta Add the drained spaghetti to the skillet with the pancetta. Toss well to coat the pasta in the pancetta's fat. Make Carbonara Remove the skillet from the heat. Quickly pour the egg and cheese mixture into the pasta, stirring vigorously with tongs or a fork until the eggs thicken but do not scramble. Add a little reserved pasta water if the sauce is too thick. The heat from the pasta will cook the eggs and melt the cheese to create a creamy sauce. Season generously with freshly ground black pepper and add a pinch of salt if needed. Garnish and Serve Serve immediately with extra grated Parmesan cheese and a sprinkle of chopped parsley, if desired. Enjoy your delicious Spaghetti Carbonara!

This recipe serves 4 people and is best enjoyed fresh. Template prompts Now, static prompts are fine and all, but we also allow template prompts. This means a user could set options (like ingredients or dietary restrictions) each time they called the prompt: Which would give the user something like: curl "https://api.promptperfect.jina.ai/RYNiqoT3txBjPoALnV46" \ -H "x-api-key: token $YOUR_GENERATED_SECRET" \ -H "content-type: application/json" \ --data '{"parameters": {"ingredients":"apples, cinnamon, nutmeg"}}' View output Classic Apple Crisp Recipe Enjoy the sweet and spicy flavors of apples, cinnamon, and nutmeg in this deliciously easy-to-make apple crisp. Perfect for a cozy night in or a festive gathering! Ingredients: 6 medium-sized apples, peeled, cored, and thinly sliced 1 teaspoon ground cinnamon 1/4 teaspoon ground nutmeg 3/4 cup granulated sugar 2 tablespoons lemon juice For the Topping: 3/4 cup all-purpose flour 3/4 cup old-fashioned rolled oats 1/2 cup light brown sugar, packed 1/2 teaspoon baking powder 1/4 teaspoon ground cinnamon 1/4 teaspoon salt 1/3 cup unsalted butter, melted Instructions: Preheat Oven and Prepare Apples: Preheat your oven to 350°F (175°C). In a large mixing bowl, combine the sliced apples with granulated sugar, 1 teaspoon cinnamon, nutmeg, and lemon juice. Toss to coat the apples evenly. Transfer the apple mixture to a greased 9-inch square baking dish, spreading them out evenly. Make the Topping: In a separate bowl, mix the flour, oats, brown sugar, baking powder, 1/4 teaspoon cinnamon, and salt. Pour the melted butter over the dry ingredients and mix until the mixture is crumbly. Assemble and Bake: Sprinkle the crumbly oat topping evenly over the apples in the baking dish. Bake in the preheated oven for about 45 minutes, or until the topping is golden brown and the apples are bubbling around the edges. Serve: Allow the apple crisp to cool slightly before serving. Serve warm, optionally with a scoop of vanilla ice cream or a dollop of whipped cream. Notes: Choosing Apples: For the best texture and flavor, use a mix of tart and sweet apples like Granny Smith and Honeycrisp. Storage: Leftover apple crisp can be stored in the refrigerator for up to 3 days. Reheat in the oven or microwave before serving.

A time and a place for everything Now we're taking it up a notch with environmental awareness. Rather than the end-user having to specify where (and when) they are, you can choose to have that information automatically inserted. That means you can create a prompt once, and end-users will get different results depending on their location, date, and time. Since recipes don’t usually need a specified time and place, let’s consider a new example: Building a website to suggest activities for a user to take part in: We also need to enable Environment Awareness: Now, I (in Berlin at noon) get something like this when I call the prompt: - Visit the Berlin Wall Memorial at Bernauer Straße - Explore the Museum Island, especially the Pergamon Museum - Take a walk through the Tiergarten Park - Enjoy panoramic views from the Berliner Fernsehturm (TV Tower) - Discover German history at the German Historical Museum - Stroll along the East Side Gallery - Check out the Brandenburg Gate at dusk - Experience contemporary art at the Hamburger Bahnhof museum - Shop or window-shop at Kurfürstendamm - Relax in the evening at a traditional German beer garden" Whereas if my colleague in Tokyo called the prompt, she'd get: - Visit Tokyo Skytree for panoramic views of the city at night. - Explore the vibrant streets of Shibuya and see the famous Shibuya Crossing. - Enjoy the illuminated Tokyo Tower and consider an evening visit. - Take a stroll through the historic Asakusa district and see Senso-ji Temple. - Experience the nightlife in Roppongi, known for its clubs and bars. - Relax at Odaiba Seaside Park and enjoy the night view of Rainbow Bridge. - Try out some local izakayas (Japanese pubs) for food and drinks. - Visit a themed café, like a cat café or an owl café, for a unique experience. - Check out the latest gadgets and tech in Akihabara, the electronics district. - Attend a traditional Kabuki performance at Kabukiza Theatre in Ginza (if available). - Indulge in a sushi dinner at one of Tokyo's renowned sushi restaurants.

These variables are great when you're crafting prompts that deliver relevant output based on the user’s time, date, and location. This is ideal for building websites and apps with a global audience.

Fetching remote data We can go even further though. With the crawler feature, you can download the main body text of the URL you specify: This makes it ideal for, say, a summarizer/translator prompt. Here we summarize an article and convert it to a sea shanty:

If I pass the URL for this story on Elon Musk's spaceship exploding, I get this (abridged) output: (Verse 1) Oh, gather 'round, me hearties, and a tale I'll tell to thee, Of SpaceX's Starship, and its flight so brief at sea. Launched on a morn in November, with power so fierce and grand, She climbed into the heavens, but 'twas not as Musk had planned. (Chorus) Heave ho, lift high, to the stars we aim to fly, But the rocket's dreams did shatter, and into the sea did die. Heave ho, lift high, with a fiery tail in sky, SpaceX's Starship faltered, and we're left to wonder why. (Verse 2) The booster and the spacecraft, they parted with a roar, The engines blazed like comets, as they'd never done before. The booster met its ending, in a ball of flame it fell, While Starship soared a moment more, then silence cast its spell. Calling other prompt services The above example wasn't exactly modular. I had both the summarizer and shantyizer in one prompt. That isn't so useful if I want to shanty all my things in full detail. Luckily, you can also call one prompt from another, allowing for a lot more modularity: So, if I create a summarizer prompt (named summarizer, which has the sole function of summarizing a web page)… …I can easily call it from a new shantyizer prompt: Sending a URL to the shantyizer prompt in turn processes the URL through the summarizer to download and summarize its contents. And of course, the summarizer can be used in any other prompt you like, acting more like a traditional programming language function. That opens up many more possibilities. Especially when it comes to more complex tasks like cooking a dish.

If I’m cooking, for any given recipe I may want one or more of the following steps, but perhaps not all steps for all recipes. Download the content of a recipe page If it's not in English, translate it (if I'm cooking an authentic Chinese recipe, I want it from a real Chinese website) Make it vegetarian (if I'm eating with vegetarian friends) Convert it to metric (because reasons) Change serving size (depending on how many people I'm eating with) Exercise for the reader As you can imagine, if I'm eating alone (and I'm not a vegetarian), my needs are quite different from when I'm eating with my buddies at the local sea kitten appreciation society. Either way, it means combining several of these "functions". We can also go multi-modal, combining text and image prompts: Create an image generation prompt from the given recipe Generate an image of how the food should look The exercise for you, dear reader, is to build a prompt that performs the above recipe steps (or similar). Share your results on our Discord! Make the magic happen

To get started with magic variables, head to promptperfect.jina.ai and get started. Let us know what you cook up on our Discord! PromptPerfect - Elevate Your Prompts to Perfection. Prompt Engineering, Optimizing, Debugging and Hosting. Unlock advanced prompt engineering and prompt optimization for large models such as GPT-4, ChatGPT, Midjourney and Stable Diffusion. Seamlessly deploy your text and image prompts as dedicated services with our free prompt hosting plan. Enhance your large models with superior performance and efficiency. PromptPerfect Categories: Tech blog rss_feed Top-5 similar articles play_arrow GET TOP-5 Select reranker Read more

August 26, 2024 • 13 minutes read The What and Whyof Text-Image Modality Gap in CLIP Models You can't just use a CLIP model to retrieve text and images and sort the results by score. Why? Because of the modality gap. What is it, and where does it come from? August 22, 2024 • 8 minutes read Late Chunking in Long-Context Embedding Models Chunking long documents while preserving contextual information is challenging. We introduce the "Late Chunking" that leverages long-context embedding models to generate contextual chunk embeddings for better retrieval applications. July 31, 2024 • 17 minutes read Rephrased Labels Improve Zero-Shot Text Classification by 30% When using embedding models for zero-shot classification, rephrasing the class label to "This is seriously about 'LABEL'" gives higher accuracy vs. using LABEL alone. But how, and why? OFFICES location_on Berlin, Germany (HQ) Prinzessinnenstraße 19-20, 10969 Berlin, Germany Geschäftsanschrift: Leipzigerstr. 96, 10117 Berlin, Germany location_on Beijing, China Level 5, Building 6, No.48 Haidian West St. Beijing Haidian, China location_on Shenzhen, China 402, Floor 4, Fu'an Technology Building, Shenzhen Nanshan, China SEARCH FOUNDATION Embeddings Reranker Reader Segmenter Get Jina AI API key API Status COMPANY About us Contact sales Newsroom Intern program Join us open_in_new Download logo open_in_new TERMS Terms & Conditions Privacy Manage Cookies email language English science Jina AI GmbH © 2020-2024.

## COT_TOPIC_CHUNKING

#### 6 chunk(s)

Classic Apple Crisp Recipe Enjoy the sweet and spicy flavors of apples, cinnamon, and nutmeg in this deliciously easy-to-make apple crisp. Perfect for a cozy night in or a festive gathering! Ingredients: 6 medium-sized apples, peeled, cored, and thinly sliced 1 teaspoon ground cinnamon 1/4 teaspoon ground nutmeg 3/4 cup granulated sugar 2 tablespoons lemon juice For the Topping: 3/4 cup all-purpose flour 3/4 cup old-fashioned rolled oats 1/2 cup light brown sugar, packed 1/2 teaspoon baking powder 1/4 teaspoon ground cinnamon 1/4 teaspoon salt 1/3 cup unsalted butter, melted Instructions: Preheat Oven and Prepare Apples: Preheat your oven to 350°F (175°C). In a large mixing bowl, combine the sliced apples with granulated sugar, 1 teaspoon cinnamon, nutmeg, and lemon juice. Toss to coat the apples evenly. Transfer the apple mixture to a greased 9-inch square baking dish, spreading them out evenly. Make the Topping: In a separate bowl, mix the flour, oats, brown sugar, baking powder, 1/4 teaspoon cinnamon, and salt. Pour the melted butter over the dry ingredients and mix until the mixture is crumbly. Assemble and Bake: Sprinkle the crumbly oat topping evenly over the apples in the baking dish. Bake in the preheated oven for about 45 minutes, or until the topping is golden brown and the apples are bubbling around the edges. Serve: Allow the apple crisp to cool slightly before serving. Serve warm, optionally with a scoop of vanilla ice cream or a dollop of whipped cream. Notes: Choosing Apples: For the best texture and flavor, use a mix of tart and sweet apples like Granny Smith and Honeycrisp. Storage: Leftover apple crisp can be stored in the refrigerator for up to 3 days. Reheat in the oven or microwave before serving.

If I pass the URL for this story on Elon Musk's spaceship exploding, I get this (abridged) output: (Verse 1) Oh, gather 'round, me hearties, and a tale I'll tell to thee, Of SpaceX's Starship, and its flight so brief at sea. Launched on a morn in November, with power so fierce and grand, She climbed into the heavens, but 'twas not as Musk had planned. (Chorus) Heave ho, lift high, to the stars we aim to fly, But the rocket's dreams did shatter, and into the sea did die. Heave ho, lift high, with a fiery tail in sky, SpaceX's Starship faltered, and we're left to wonder why. (Verse 2) The booster and the spacecraft, they parted with a roar, The engines blazed like comets, as they'd never done before. The booster met its ending, in a ball of flame it fell, While Starship soared a moment more, then silence cast its spell. Calling other prompt services The above example wasn't exactly modular. I had both the summarizer and shantyizer in one prompt. That isn't so useful if I want to shanty all my things in full detail. Luckily, you can also call one prompt from another, allowing for a lot more modularity: So, if I create a summarizer prompt (named summarizer, which has the sole function of summarizing a web page)… …I can easily call it from a new shantyizer prompt: Sending a URL to the shantyizer prompt in turn processes the URL through the summarizer to download and summarize its contents. And of course, the summarizer can be used in any other prompt you like, acting more like a traditional programming language function. That opens up many more possibilities. Especially when it comes to more complex tasks like cooking a dish. If I’m cooking, for any given recipe I may want one or more of the following steps, but perhaps not all steps for all recipes. Download the content of a recipe page If it's not in English, translate it (if I'm cooking an authentic Chinese recipe, I want it from a real Chinese website) Make it vegetarian (if I'm eating with vegetarian friends) Convert it to metric (because reasons) Change serving size (depending on how many people I'm eating with) Exercise for the reader As you can imagine, if I'm eating alone (and I'm not a vegetarian), my needs are quite different from when I'm eating with my buddies at the local sea kitten appreciation society. Either way, it means combining several of these "functions". We can also go multi-modal, combining text and image prompts: Create an image generation prompt from the given recipe Generate an image of how the food should look The exercise for you, dear reader, is to build a prompt that performs the above recipe steps (or similar). Share your results on our Discord! Make the magic happen To get started with magic variables, head to promptperfect.jina.ai and get started. Let us know what you cook up on our Discord!

PromptPerfect - Elevate Your Prompts to Perfection.Prompt Engineering, Optimizing, Debugging and Hosting. Unlock advanced prompt engineering and prompt optimization for large models such as GPT-4, ChatGPT, Midjourney and Stable Diffusion. Seamlessly deploy your text and image prompts as dedicated services with our free prompt hosting plan. Enhance your large models with superior performance and efficiency. PromptPerfect Categories: Tech blog rss_feed Top-5 similar articles play_arrow GET TOP-5 Select reranker Read more August 26, 2024 • 13 minutes read The What and Why of Text-Image Modality Gap in CLIP Models

You can't just use a CLIP model to retrieve text and images and sort the results by score. Why? Because of the modality gap. What is it, and where does it come from? August 22, 2024 • 8 minutes read

Late Chunking in Long-Context Embedding Models Chunking long documents while preserving contextual information is challenging. We introduce the "Late Chunking" that leverages long-context embedding models to generate contextual chunk embeddings for better retrieval applications. July 31, 2024 • 17 minutes read Rephrased Labels Improve Zero-Shot Text Classification by 30% When using embedding models for zero-shot classification, rephrasing the class label to "This is seriously about 'LABEL'" gives higher accuracy vs. using LABEL alone. But how, and why?

OFFICES location_on Berlin, Germany (HQ) Prinzessinnenstraße 19-20, 10969 Berlin, Germany Geschäftsanschrift: Leipzigerstr. 96, 10117 Berlin, Germany location_on Beijing, China Level 5, Building 6, No.48 Haidian West St. Beijing Haidian, China location_on Shenzhen, China 402, Floor 4, Fu'an Technology Building, Shenzhen Nanshan, China SEARCH FOUNDATION Embeddings Reranker Reader Segmenter Get Jina AI API key API Status COMPANY About us Contact sales Newsroom Intern program Join us open_in_new Download logo open_in_new TERMS Terms & Conditions Privacy Manage Cookies email language English science Jina AI GmbH © 2020-2024.

## SUMMARY_CHUNKING

#### 4 chunk(s)

A time and a place for everything Now we're taking it up a notch with environmental awareness. Rather than the end-user having to specify where (and when) they are, you can choose to have that information automatically inserted. That means you can create a prompt once, and end-users will get different results depending on their location, date, and time. Since recipes don’t usually need a specified time and place, let’s consider a new example: Building a website to suggest activities for a user to take part in: We also need to enable Environment Awareness: Now, I (in Berlin at noon) get something like this when I call the prompt: - Visit the Berlin Wall Memorial at Bernauer Straße - Explore the Museum Island, especially the Pergamon Museum - Take a walk through the Tiergarten Park - Enjoy panoramic views from the Berliner Fernsehturm (TV Tower) - Discover German history at the German Historical Museum - Stroll along the East Side Gallery - Check out the Brandenburg Gate at dusk - Experience contemporary art at the Hamburger Bahnhof museum - Shop or window-shop at Kurfürstendamm - Relax in the evening at a traditional German beer garden" Whereas if my colleague in Tokyo called the prompt, she'd get: - Visit Tokyo Skytree for panoramic views of the city at night. - Explore the vibrant streets of Shibuya and see the famous Shibuya Crossing. - Enjoy the illuminated Tokyo Tower and consider an evening visit. - Take a stroll through the historic Asakusa district and see Senso-ji Temple. - Experience the nightlife in Roppongi, known for its clubs and bars. - Relax at Odaiba Seaside Park and enjoy the night view of Rainbow Bridge. - Try out some local izakayas (Japanese pubs) for food and drinks. - Visit a themed café, like a cat café or an owl café, for a unique experience. - Check out the latest gadgets and tech in Akihabara, the electronics district. - Attend a traditional Kabuki performance at Kabukiza Theatre in Ginza (if available). - Indulge in a sushi dinner at one of Tokyo's renowned sushi restaurants. These variables are great when you're crafting prompts that deliver relevant output based on the user’s time, date, and location. This is ideal for building websites and apps with a global audience.

Fetching remote data We can go even further though. With the crawler feature, you can download the main body text of the URL you specify: This makes it ideal for, say, a summarizer/translator prompt. Here we summarize an article and convert it to a sea shanty: If I pass the URL for this story on Elon Musk's spaceship exploding, I get this (abridged) output: (Verse 1) Oh, gather 'round, me hearties, and a tale I'll tell to thee, Of SpaceX's Starship, and its flight so brief at sea. Launched on a morn in November, with power so fierce and grand, She climbed into the heavens, but 'twas not as Musk had planned. (Chorus) Heave ho, lift high, to the stars we aim to fly, But the rocket's dreams did shatter, and into the sea did die. Heave ho, lift high, with a fiery tail in sky, SpaceX's Starship faltered, and we're left to wonder why. (Verse 2) The booster and the spacecraft, they parted with a roar, The engines blazed like comets, as they'd never done before. The booster met its ending, in a ball of flame it fell, While Starship soared a moment more, then silence cast its spell. Calling other prompt services The above example wasn't exactly modular. I had both the summarizer and shantyizer in one prompt. That isn't so useful if I want to shanty all my things in full detail. Luckily, you can also call one prompt from another, allowing for a lot more modularity: So, if I create a summarizer prompt (named summarizer, which has the sole function of summarizing a web page)… …I can easily call it from a new shantyizer prompt: Sending a URL to the shantyizer prompt in turn processes the URL through the summarizer to download and summarize its contents. And of course, the summarizer can be used in any other prompt you like, acting more like a traditional programming language function. That opens up many more possibilities.

Especially when it comes to more complex tasks like cooking a dish. If I’m cooking, for any given recipe I may want one or more of the following steps, but perhaps not all steps for all recipes. Download the content of a recipe page If it's not in English, translate it (if I'm cooking an authentic Chinese recipe, I want it from a real Chinese website) Make it vegetarian (if I'm eating with vegetarian friends) Convert it to metric (because reasons) Change serving size (depending on how many people I'm eating with) Exercise for the reader As you can imagine, if I'm eating alone (and I'm not a vegetarian), my needs are quite different from when I'm eating with my buddies at the local sea kitten appreciation society. Either way, it means combining several of these "functions". We can also go multi-modal, combining text and image prompts: Create an image generation prompt from the given recipe Generate an image of how the food should look The exercise for you, dear reader, is to build a prompt that performs the above recipe steps (or similar). Share your results on our Discord! Make the magic happen To get started with magic variables, head to promptperfect.jina.ai and get started. Let us know what you cook up on our Discord!

PromptPerfect - Elevate Your Prompts to Perfection.Prompt Engineering, Optimizing, Debugging and Hosting. Unlock advanced prompt engineering and prompt optimization for large models such as GPT-4, ChatGPT, Midjourney and Stable Diffusion. Seamlessly deploy your text and image prompts as dedicated services with our free prompt hosting plan. Enhance your large models with superior performance and efficiency. PromptPerfect Categories: Tech blog rss_feed Top-5 similar articles play_arrow GET TOP-5 Select reranker Read more August 26, 2024 • 13 minutes read The What and Why of Text-Image Modality Gap in CLIP Models You can't just use a CLIP model to retrieve text and images and sort the results by score. Why? Because of the modality gap. What is it, and where does it come from? August 22, 2024 • 8 minutes read Late Chunking in Long-Context Embedding Models Chunking long documents while preserving contextual information is challenging. We introduce the "Late Chunking" that leverages long-context embedding models to generate contextual chunk embeddings for better retrieval applications. July 31, 2024 • 17 minutes read Rephrased Labels Improve Zero-Shot Text Classification by 30% When using embedding models for zero-shot classification, rephrasing the class label to "This is seriously about 'LABEL'" gives higher accuracy vs. using LABEL alone. But how, and why? OFFICES location_on Berlin, Germany (HQ) Prinzessinnenstraße 19-20, 10969 Berlin, Germany Geschäftsanschrift: Leipzigerstr. 96, 10117 Berlin, Germany location_on Beijing, China Level 5, Building 6, No.48 Haidian West St. Beijing Haidian, China location_on Shenzhen, China 402, Floor 4, Fu'an Technology Building, Shenzhen Nanshan, China SEARCH FOUNDATION Embeddings Reranker Reader Segmenter Get Jina AI API key API Status COMPANY About us Contact sales Newsroom Intern program Join us open_in_new Download logo open_in_new TERMS Terms & Conditions Privacy Manage Cookies email language English science Jina AI GmbH © 2020-2024.

## JINA-SEGMENTER-API

#### 219 chunk(s)

search


notifications


NEWS


PRODUCTS


COMPANY


Tech blog


December 07, 2023


There's a Time and a Place: Unleashing Dynamic Variables in PromptPerfect


Incorporate users' time, date and location into your prompts. Plus contents of other websites, and outputs of other prompts themselves!


Alex C-G • 8 minutes read



Back in the mists of time, PromptPerfect introduced its Prompt-as-a-Service feature, allowing you to serve your prompts via a RESTful API and call them from Python, JavaScript or cURL.



What’s Next for Prompt Engineering? PromptPerfect’s Prompt as a Service!


Deploy prompts and flexible template prompts as REST API services, and integrate them into your applications with just a few clicks


PromptPerfect



Let’s imagine we’re building an AI-powered recipe website. We want users to be able to click a button that suggests a delicious recipe for them. To do that, we can create a prompt and deploy it as a service. We would then incorporate that into our website via Prompt-as-a-Service’s RESTful API.



For example, we could have a prompt that suggested recipes to users:



Incorporating a RESTful API into your website is way outside the scope of this post, so we’ll just use cURL moving forwards. But rest assured, you can do this in any language or framework with an HTTP library.



By calling the prompt, a user could get a new recipe each time:



curl "https://api.promptperfect.jina.ai/RYNiqoT3txBjPoALnV46" \


-H "x-api-key: token $YOUR_GENERATED_SECRET" \
  

-H "content-type: application/json"


View output



Certainly! Below is a recipe for a classic Italian dish, Spaghetti Carbonara. This dish is known for its creamy texture and rich flavors, achieved with minimal ingredients. Enjoy!



Spaghetti Carbonara



Ingredients



400g spaghetti


150g pancetta or guanciale, diced


3 large eggs


1 cup (100g) freshly grated Parmesan cheese, plus extra for serving


2 cloves garlic, peeled and left whole


2 tablespoons extra-virgin olive oil


Salt and freshly ground black pepper


A small handful of fresh parsley, chopped (optional)



Instructions



Cook the Pasta



Bring a large pot of salted water to a boil.


Add the spaghetti and cook according to the package instructions until al dente.


Reserve 1 cup of pasta water before draining the spaghetti.



Prepare the Sauce



In a small bowl, whisk together the eggs and grated Parmesan cheese until well combined. Set aside.



Cook the Pancetta



While the pasta is cooking, heat the olive oil in a large skillet over medium heat.


Add the pancetta or guanciale and the whole garlic cloves. Cook, stirring frequently, until the meat is crispy and golden, about 5 minutes.


Remove and discard the garlic cloves.



Combine Pasta and Pancetta



Add the drained spaghetti to the skillet with the pancetta.


Toss well to coat the pasta in the pancetta's fat.



Make Carbonara



Remove the skillet from the heat.


Quickly pour the egg and cheese mixture into the pasta, stirring vigorously with tongs or a fork until the eggs thicken but do not scramble.


Add a little reserved pasta water if the sauce is too thick. The heat from the pasta will cook the eggs and melt the cheese to create a creamy sauce.


Season generously with freshly ground black pepper and add a pinch of salt if needed.



Garnish and Serve



Serve immediately with extra grated Parmesan cheese and a sprinkle of chopped parsley, if desired.



Enjoy your delicious Spaghetti Carbonara!



This recipe serves 4 people and is best enjoyed fresh.



Template prompts



Now, static prompts are fine and all, but we also allow template prompts. This means a user could set options (like ingredients or dietary restrictions) each time they called the prompt:



Which would give the user something like:



curl "https://api.promptperfect.jina.ai/RYNiqoT3txBjPoALnV46" \


-H "x-api-key: token $YOUR_GENERATED_SECRET" \
  

-H "content-type: application/json" \
  

--data '{"parameters": {"ingredients":"apples, cinnamon, nutmeg"}}'


View output



Classic Apple Crisp Recipe



Enjoy the sweet and spicy flavors of apples, cinnamon, and nutmeg in this deliciously easy-to-make apple crisp. Perfect for a cozy night in or a festive gathering!



Ingredients:



6 medium-sized apples, peeled, cored, and thinly sliced


1 teaspoon ground cinnamon


1/4 teaspoon ground nutmeg


3/4 cup granulated sugar


2 tablespoons lemon juice



For the Topping:



3/4 cup all-purpose flour


3/4 cup old-fashioned rolled oats


1/2 cup light brown sugar, packed


1/2 teaspoon baking powder


1/4 teaspoon ground cinnamon


1/4 teaspoon salt


1/3 cup unsalted butter, melted



Instructions:



Preheat Oven and Prepare Apples:



Preheat your oven to 350°F (175°C).


In a large mixing bowl, combine the sliced apples with granulated sugar, 1 teaspoon cinnamon, nutmeg, and lemon juice. Toss to coat the apples evenly.


Transfer the apple mixture to a greased 9-inch square baking dish, spreading them out evenly.



Make the Topping:



In a separate bowl, mix the flour, oats, brown sugar, baking powder, 1/4 teaspoon cinnamon, and salt.


Pour the melted butter over the dry ingredients and mix until the mixture is crumbly.



Assemble and Bake:



Sprinkle the crumbly oat topping evenly over the apples in the baking dish.


Bake in the preheated oven for about 45 minutes, or until the topping is golden brown and the apples are bubbling around the edges.



Serve:



Allow the apple crisp to cool slightly before serving.


Serve warm, optionally with a scoop of vanilla ice cream or a dollop of whipped cream.



Notes:



Choosing Apples: For the best texture and flavor, use a mix of tart and sweet apples like Granny Smith and Honeycrisp.


Storage: Leftover apple crisp can be stored in the refrigerator for up to 3 days. Reheat in the oven or microwave before serving.


A time and a place for everything



Now we're taking it up a notch with environmental awareness. Rather than the end-user having to specify where (and when) they are, you can choose to have that information automatically inserted. That means you can create a prompt once, and end-users will get different results depending on their location, date, and time.



Since recipes don’t usually need a specified time and place, let’s consider a new example: Building a website to suggest activities for a user to take part in:



We also need to enable Environment Awareness:



Now, I (in Berlin at noon) get something like this when I call the prompt:



- Visit the Berlin Wall Memorial at Bernauer Straße


- Explore the Museum Island, especially the Pergamon Museum


- Take a walk through the Tiergarten Park


- Enjoy panoramic views from the Berliner Fernsehturm (TV Tower)


- Discover German history at the German Historical Museum


- Stroll along the East Side Gallery


- Check out the Brandenburg Gate at dusk


- Experience contemporary art at the Hamburger Bahnhof museum


- Shop or window-shop at Kurfürstendamm


- Relax in the evening at a traditional German beer garden"


Whereas if my colleague in Tokyo called the prompt, she'd get:



- Visit Tokyo Skytree for panoramic views of the city at night.


- Explore the vibrant streets of Shibuya and see the famous Shibuya Crossing.


- Enjoy the illuminated Tokyo Tower and consider an evening visit.


- Take a stroll through the historic Asakusa district and see Senso-ji Temple.


- Experience the nightlife in Roppongi, known for its clubs and bars.


- Relax at Odaiba Seaside Park and enjoy the night view of Rainbow Bridge.


- Try out some local izakayas (Japanese pubs) for food and drinks.


- Visit a themed café, like a cat café or an owl café, for a unique experience.


- Check out the latest gadgets and tech in Akihabara, the electronics district.


- Attend a traditional Kabuki performance at Kabukiza Theatre in Ginza (if available).


- Indulge in a sushi dinner at one of Tokyo's renowned sushi restaurants.


These variables are great when you're crafting prompts that deliver relevant output based on the user’s time, date, and location. This is ideal for building websites and apps with a global audience.



Fetching remote data



We can go even further though. With the crawler feature, you can download the main body text of the URL you specify:



This makes it ideal for, say, a summarizer/translator prompt. Here we summarize an article and convert it to a sea shanty:



If I pass the URL for this story on Elon Musk's spaceship exploding, I get this (abridged) output:



(Verse 1)


Oh, gather 'round, me hearties, and a tale I'll tell to thee,


Of SpaceX's Starship, and its flight so brief at sea.


Launched on a morn in November, with power so fierce and grand,


She climbed into the heavens, but 'twas not as Musk had planned.



(Chorus)


Heave ho, lift high, to the stars we aim to fly,


But the rocket's dreams did shatter, and into the sea did die.


Heave ho, lift high, with a fiery tail in sky,


SpaceX's Starship faltered, and we're left to wonder why.



(Verse 2)


The booster and the spacecraft, they parted with a roar,


The engines blazed like comets, as they'd never done before.


The booster met its ending, in a ball of flame it fell,


While Starship soared a moment more, then silence cast its spell.



Calling other prompt services



The above example wasn't exactly modular. I had both the summarizer and shantyizer in one prompt. That isn't so useful if I want to shanty all my things in full detail. Luckily, you can also call one prompt from another, allowing for a lot more modularity:



So, if I create a summarizer prompt (named summarizer, which has the sole function of summarizing a web page)…



I can easily call it from a new shantyizer prompt:



Sending a URL to the shantyizer prompt in turn processes the URL through the summarizer to download and summarize its contents. And of course, the summarizer can be used in any other prompt you like, acting more like a traditional programming language function.



That opens up many more possibilities. Especially when it comes to more complex tasks like cooking a dish. If I’m cooking, for any given recipe I may want one or more of the following steps, but perhaps not all steps for all recipes.



Download the content of a recipe page


If it's not in English, translate it (if I'm cooking an authentic Chinese recipe, I want it from a real Chinese website)


Make it vegetarian (if I'm eating with vegetarian friends)


Convert it to metric (because reasons)


Change serving size (depending on how many people I'm eating with)


Exercise for the reader



As you can imagine, if I'm eating alone (and I'm not a vegetarian), my needs are quite different from when I'm eating with my buddies at the local sea kitten appreciation society. Either way, it means combining several of these "functions".



We can also go multi-modal, combining text and image prompts:



Create an image generation prompt from the given recipe


Generate an image of how the food should look



The exercise for you, dear reader, is to build a prompt that performs the above recipe steps (or similar). Share your results on our Discord!



Make the magic happen



To get started with magic variables, head to promptperfect.jina.ai and get started. Let us know what you cook up on our Discord!



PromptPerfect - Elevate Your Prompts to Perfection. Prompt Engineering, Optimizing, Debugging and Hosting.


Unlock advanced prompt engineering and prompt optimization for large models such as GPT-4, ChatGPT, Midjourney and Stable Diffusion. Seamlessly deploy your text and image prompts as dedicated services with our free prompt hosting plan. Enhance your large models with superior performance and efficiency.


PromptPerfect


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