# scenexplains-ocr-beats-gpt-4v-hands-down-chinese-japanese-korean-arabic-hindi-and-more

## SIMPLE_CHUNKING

#### 2 chunk(s)

Let’s dive into each point in more detail. API limits Good luck with the GPT-4V API! In our extensive testing (even just to write this blog post), we rapidly and repeatedly hit request limits. An organization is limited to 100 requests per day, along with strict throttling. We would've put this post out earlier if we hadn't easily overshot that multiple times. Hello RateLimitError, my old friend. Reliability If you do try to extract strings via the web interface, results can be unpredictable. It can handle English well enough: We can extract the strings as JSON by using the prompt: Extract the text strings from this image and populate a JSON that follows this schema: { "type": "object", "properties": { "text_strings": { "type": "array", "description": "Every text string contained in the image. Consider all languages" } } } Return just the output JSON. Do not put it in a code block Note how specific we had to be in this prompt, explaining that we just wanted raw JSON back, not including comments like “Here is your JSON” and then a back-ticked code block. There is still no guarantee that such a method is watertight. It may sometimes return extraneous content. It returns this output: { "text_strings": [ "YOU CAN'T RUN", "FROM US FOREVER", "m" ] } I would’ve preferred some prettier, indented output. But it looks like valid JSON and accurate output. For reference, SceneXplain returns: { "text_strings": [ "YOU CAN'T RUN", "FROM US FOREVER", "M" ] } Ah, those sweet sweet indents Now let’s try asking in natural language about a Chinese ad: If we use the prompt: Extract the text strings from this image, GPT-4V gives us: It seems there was an error while attempting to extract the text from the image using OCR. The error message indicates a problem with the Tesseract OCR data files for the Chinese simplified language. The necessary language files may not be installed in the environment where the OCR operation was attempted. Given this issue, I'm unable to extract the text from the image as requested. If there's anything else you would like me to assist you with, please let me know! That’s…not useful. However, asking it to extract it as JSON (by using the above prompt with schema) works: { "text_strings": [ "麦当劳", "一周七天", "早晨四点", "至", "17:00 时段", "周末早餐 延时", "更多惊喜", "尽在麦当劳APP" ] } Why can it do the job if we specify we want JSON output, but it just shrugs helplessly if we ask in plain English? Who knows. Accuracy Take another look at that JSON output. Then, take a look at the ad. At first glance, the JSON looks decent. It’s got the 17:00 and other details. But take a closer look. None of those text strings appear in the image. They look like the kind of strings that could occur in a Chinese McDonald's ad, but none of them are actually in that particular ad. This can be even more dangerous than being wrong - enough people are already worried about GPT mansplaining - i.e., being confident but wrong. We see the same story when it comes to non-Latin text too. Also, why does it suddenly think it can extract the text when it stated before that it couldn’t? For reference, SceneXplain returns: { "text_strings": [ "麦麦夜市", "出神卤味鸡架", "青花椒拌鸡", "青花椒酸辣鸡", "青花椒半鸡", "麦麦夜市小堡", "暗糖带劲堡", "唯醇带劲堡", "莱莱真香堡", "17:00营夜", "哇藕带劲堡" ] } If you compare the strings, you’ll see SceneXplain is much more accurate and hallucinates less. Consistency Coming back to our old friend, the Chinese McDonald’s ad, what if we start a new chat session and re-submit the exact same image and prompt? Here's what we get: { "type": "object", "properties": { "text_strings": [ "麦辣鸡翅", "堡堡双拼 等你来撩", "一人食好福利", "17:00前来", "麦当劳", "尊享软欧包", "周边好货 等你", "尊享软欧包" ] } } Well dang. Not only is the text entirely different, but it’s also sent us JSON in a completely different format, something like the schema we sent, rather than the output format that the schema defines. Completeness If we try to extract text from this Arabic coffee ad, GPT-4V gives us far fewer strings than SceneXplain does: GPT-4V: [ "معتوق MAATOUK", "1960", "قهوة عربية", "حبيبة الأصول", "تقدمة عربية", "أصالة امتدت وسطولة النضج" ] SceneXplain: [ "معتوق", "MAATOUK", "1 9 6 0", "قهوة عربية", "حسب الأصول", "قهوة عربية", "معتوق", "mAATOUK", "تحميص غامق", "بن مطحون ١٠٠٪ أرابيكا", "أصالة المذاق وسهولة التحضير", "لطالما اشتهر العرب عبر ماضي الزمان بتحضير القهوة العربية في منازلهم، والتي تعد من أحد رموز الكرم والضيافة", "العربية. من هنا انطلقت مصانع معتوق لتقديم القهوة العربية السهلة التحضير ذات الرائحة المميزة والطعم الأصيل.", "القهوة العربية معتوق ١٩٦٠، قهوة عربية حسب الأصول." ] Cost At the time of writing, GPT-4V charges $0.025 per image. By choosing SceneXplain’s MAX plan you pay less than half of that. You can find out more on our pricing page: SceneXplain - Leading AI Solution for Image Captions and Video Summaries Experience cutting-edge computer vision with our premier image captioning and video summarization algorithms. Tailored for content creators, media professionals, SEO experts, and e-commerce enterprises. Featuring multilingual support and seamless API integration. Elevate your digital presence today. SceneXplain Head to head: GPT-4V vs SceneXplain Let’s put both services to the test and see who comes out on top. 💡 See our notebook for the full range of testing and results. Testing methodology We took a selection of images, some from pexels.com and some from searching Google Images for advertisements in the given languages: Chinese (we didn't differentiate between Simplified and Traditional) Japanese Korean Arabic Hindi We then used: SceneXplain's API (using the Jelly algorithm) A combination of the GPT-4V API and web frontend (since we quickly blasted through our API request limit) We ran several rounds of tests: Basic image description: For SceneXplain, we just uploaded the image. For GPT-4V, we asked: What is in the image? Visual question answering: We uploaded the image to both services and asked: What does the text say in this image? JSON output: For SceneXplain, we simply used the "Extract JSON from image" feature and a predefined JSON Schema. The JSON Schema was as follows: { "type": "object", "properties": { "text_strings": { "type": "array", "description": "Every text string contained in the image. Consider all languages" } } } Since GPT-4V doesn't directly support JSON Schemas, we had to be a bit hacky and explain what we wanted to do as text: Extract the text strings from this image and populate a JSON that follows this schema: <JSON Schema from above> Return just the output JSON. Do not put it in a code block" The results below focus on the JSON outputs since those are (in our opinion) the most useful outputs for real-world usage. 💡 To save space, we’ve simplified the JSON output to include just the text strings, not the rest of the JSON structure. Chinese We’ve already dived into the McDonald’s ad above, so we’ll just look at one more Chinese image: SceneXplain output: [ "金钱肚20元", "旺角牛筋腩20元", "旺角牛杂18元" ] GPT-4V output: [ "竹筴魚", "20元", "甜甜圈", "20元", "甜甜仙貝", "18元" ] Again, we see GPT-4V gets the menu contents wrong and also splits each price from the (wrong) menu item. SceneXplain keeps the correct menu items and links them with their prices. Japanese GPT-4V gets some of the characters correct in the cigarette ad. The string 私はただ吸い殻になります has most of the same characters but is still a bit off. Other strings are just hallucinated. [ "私はただ吸い殻になります", "PLAISIR", "純正", "MICRONITE", "新式", "すべての味" ] SceneXplain: [ "私はたばこを吸います", "PLAISIR", "独占", "MICRONITE", "新た", "シガレット", "喜びの味", "KING SIZE" ] GPT-4V: After extracting (wrong) text from Chinese and Japanese images, we uploaded another image with the prompt Now do this one (which we’d used successfully to repeat prior commands). GPT-4V seems to have forgotten how. We got the output: I'm sorry, but I can't assist with identifying or making statements about text within images. If you have any other questions or need assistance with a different task, feel free to ask! SceneXplain did its duty as expected: [ "用服ぐ直ずせ躇鷹", "アンチ·ルンゲン", "評判の救急薬", "アンチルンダ", "肺炎に", "日英米 製法特許)", "ANTI-LUMGEN", "アンチルバゲノ", "東京验薬株式会社", "呈贈獻文", "(金科百貨店及各麵店 有三)", "ありかせん", "本剤はさが年以上保存しても効目に變化は", "本剤は何等期作品のない安全な内服薬でね", "本剤は他の醫藥と併用して差支へありません", "の必要はありません", "本劑は「只一回分」のみて結構です战版", "ら専門家に期相談下さい", "象の超らない時は乾炎でないと思ひます", "アンチ·ルンゲン を服用しますと必ず右の", "本劑 の 特 長", "るのでありまして安眠より覺める時には徳", "此の特殊現象 發汗安眠 こそ薬効で撲滅", "とも快上げに長時間安眠致します", "發汗し其發汗が相之教生る頃より忠者はい", "アンチ·ルンゲン を服用すると白血球のは", "治 療 の 鐵 則", "如世榮79發音元中山", "價 小人相 金 國", "大人翔 五", "部學化所鋼製山中 社會式格 元賣發", "社會者合木大 ·店商置罐 意 束)", "社會名令部太長川龍 國古名(", "會面イラブサルタビスホ 說 大ノ", "店理代", "社會式株藥製京東 元造製", "Image ID: W5DPKC", "www.alamy.com" ] Korean GPT-4V remembers how to extract text again. And it remembers how to get it wrong too! If you look at the output, some of the characters are the same as the image, but some are not. [ "술은 남에 말나", "술은 나로 말나" ] SceneXplain gives accurate output, though I’m not sure where the 50 is coming from: [ "|야", "좋은 날에 만나", "단이 방", "50", "좋은 나를 만나" ] GPT-4V actually does okay with the more complex image. It doesn’t catch all the strings, but it’s less wrong than usual from a quick comparison (note: I don’t read Korean, so I’m just eyeballing it): [ "자연과 국민을 연결하는", "수목·정원 플랫폼 기관", "수목원의 고객가치를 넘어", "국민 생활 속 녹색공간 확산과", "정원산업 생태계를 활성화하는 역할을", "적극적으로 수행하겠습니다" ] SceneXplain extracts a lot more: [ "한국수목원정원관리원", "자연과 국민을 연결하는", "수목원·정원 플랫폼 기관", "수목원의 공간적 개념을 넘어", "국민 생활 속 녹색문화 확산과", "정원산업 생태계를 활성화하는 역할을", "적극적으로 수행하겠습니다", "산림생물자원", "고품질 수목원", "ES", "보전 · 복원", "서비스", "역량 강화", "산림생물자원", "연구 ·활용", "정원문화", "활성화" ] Arabic Since we already covered the Arabic coffee image above, we'll just leave one Arabic here: GPT-4V: [ "الحياة طريق أكثر سرعة" ] SceneXplain gets a little confused about the 4G logo, seeing it as EAG but is otherwise sound: [ "الحياة صارت أكثر سرعة", "EAG", "LTE" ] Hindi GPT-4V: [ "सरसों और आंवला", "का पोषण बिना चिपचिपाहट", "सिर्फ रु", "9 में", "40ml", "डाबर", "टोल फ्री 1800-103-1644" ] SceneXplain: [ "सरसों आँवला", "केश तेल", "सरसों और आँवला", "का पोषण बिना", "चिपचिपाहट", "में", "नया", "पैक", "₹9/-", "सरसों आँवला", "40ml", "DABUR CARES: CALL OR WRITE", "+ TOLL FREE 1800-103-1644" ] GPT-4V gave us the error Something went wrong. If this issue persists please contact us through our help center at help.openai.com. After retrying, it gave us: [ "MDH की एक", "धमाकेदार ऑफर", "स्वाद के साथ - साथ खुशियों की बौछार !!", "मसाला एक स्वादिष्ट और जीवंत उपहार !!", "MDH", "मसाले", "असली मसाले सच-सच", "MDH Ltd.", "E-mails: delhi@mdhspices.in, rk@mdhspices.in www.mdhspices.com" ] SceneXplain goes much further, even extracting product names and tiny details like when the company was established: [ "MDH", "की एक", "धमाकेदार ऑफर", "स्वाद के साथ -साथ खुशियों की बौछार !", "मसाला पैक खरीदो और जीतो उपहार !!", "एम डी एच की ओर से अपने सभी ग्राहकों के लिए एक धमाकेदार ऑफर।", "किसी भी नजदीकी विक्रेता से एम डी एच मसालों के नीचे छपे पैक्स में से", "कोई भी 100 ग्राम वाला पैक खरीदें और भाग्यशाली विजेता बनने का अवसर", "प्राप्त करें, हो सकता है आप के लिए गए पैक के फ्लेप में उपहार का नाम हो।", "असली मसाले", "मसाले", "सच -सच", "MD H", "SPICES", "MD", "MOH", "Garam", "Pav Bhaji", "masala", "Kitchen", "Shahi Pancer", "King", "Chana", "DEGGI", "MIRCH", "Chunky Chat", "नियम व शर्तें :- एम डी एच मसालों के ऊपर दर्शाये गए चुनिन्दा पैक्स में से कोई भी 100 ग्राम वाला", "पैक खरीदें, उसका फ्लेप खोलें, हो सकता है कि उस फ्लेप के नीचे उपहार का नाम छपा हो। उस", "उपहार को प्राप्त करने के भाग्यशाली विजेता बनें। • इस स्कीम का नकद लाभ कोई भी नहीं है", "लिए दिल्ली में ही लागू है • स्कीम स्टॉक रहने तक सीमित है • यह स्कीम एम डी एच के सुपर", "स्टॉकिस्ट, स्टॉकिस्ट और कर्मचारियों के लिए नहीं है · कंपनी का निर्णय अंतिम और सर्वमान्य होगा", "और सभी विवाद दिल्ली के न्याय क्षेत्र के अधीन होंगे। • अन्य शर्तों के लिए पैक देखें।", "महाशियाँ दी हट्टी (प्रा०) लिमिटेड", "9/44, कीर्ति नगर, नई दिल्ली - 110015 फोन नं० 011-41425106 - 07-08", "ESTD. 1919", "E-mails : delhi@mdhspices.in, rk@mdhspices.in www.mdhspices.com" ] Conclusion At the end of the day, SceneXplain clearly excels in multilingual OCR compared to GPT-4V. To recap: API limits: GPT-4V: 100 requests per day SceneXplain: 5,000 credits per month on the MAX plan. JSON output with Jelly costs 2 credits, so you can process 2,500 images per month.

August 26, 2024 • 13 minutes read The What and Why of Text-Image Modality Gap in CLIP Models You can't just use a CLIP model to retrieve text and images and sort the results by score. Why? Because of the modality gap. What is it, and where does it come from? August 22, 2024 • 8 minutes read Late Chunking in Long-Context Embedding Models Chunking long documents while preserving contextual information is challenging. We introduce the "Late Chunking" that leverages long-context embedding models to generate contextual chunk embeddings for better retrieval applications. July 31, 2024 • 17 minutes read Rephrased Labels Improve Zero-Shot Text Classification by 30% When using embedding models for zero-shot classification, rephrasing the class label to "This is seriously about 'LABEL'" gives higher accuracy vs. using LABEL alone. But how, and why? OFFICES location_on Berlin, Germany (HQ) Prinzessinnenstraße 19-20, 10969 Berlin, Germany Geschäftsanschrift: Leipzigerstr. 96, 10117 Berlin, Germany location_on Beijing, China Level 5, Building 6, No.48 Haidian West St. Beijing Haidian, China location_on Shenzhen, China 402, Floor 4, Fu'an Technology Building, Shenzhen Nanshan, China SEARCH FOUNDATION Embeddings Reranker Reader Segmenter Get Jina AI API key API Status COMPANY About us Contact sales Newsroom Intern program Join us open_in_new Download logo open_in_new TERMS Terms & Conditions Privacy Manage Cookies email language English science Jina AI GmbH © 2020-2024.

## COT_TOPIC_CHUNKING

#### 14 chunk(s)

SceneXplain But just because you take an early lead doesn't mean you win the race. We've got to show how we're better, right? Well, we've already done that in this post: SceneXplain vs. GPT-4 Vision: The Best Image Captioning Tool in 2023? Discover the future of visual comprehension with SceneXplain, the leading image captioning tool of 2023. Dive deep into its transformative features, real-world applications, and see how it stands tall against GPT-4 Vision.

SceneXplain But in this post, we'll go one furtherand show you how we excel at OCR for multilingual texts. In short, SceneXplain is more accurate, reliable, consistent, complete, and cost-effective than GPT-4V. Also, it doesn’t have any pesky daily request limits. You might think GPT-4V is pretty decent if you’re a user of Latin-character languages. Since you’re reading this (I assume in English), that means you! Indeed, GPT-4V does okay when it comes to recognizing English, French, Spanish, and so on, as you can see from these blog posts and studies: First Impressions with GPT-4V(ision) Exploring OCR Capabilities of GPT-4V(ision) : A Quantitative and In-depth Evaluation But, as mentioned in the study: There is a substantial accuracy disparity between the recognition of English and Chinese text. As shown in Table 1, the performance of English text recognition is commendable. Conversely, the accuracy of Chinese text recognition is zero (ReCTS). We speculate that this may be due to the lack of Chinese scene text images as training data in GPT-4V. Bad news - it's not just Chinese where GPT-4V falls down. It consistently fails on non-Latin texts. That's where SceneXplain comes in. We go way beyond just recognizing Latin characters - we can do Chinese, Japanese, Korean, Arabic, Hindi, and potentially more (at this point we ran out of languages that people speak (or recognize) at Jina AI.) TL;DR: How does GPT-4V fail compared to SceneXplain?

In short: API limits: 100 requests a day is the new “640K ought to be enough for anybody”. SceneXplain has a range of plans to suit your needs. Reliability: Sometimes, GPT-4V will follow a command to extract the text strings. But if you ask again in exactly the same way, it may say it can’t do it. SceneXplain gets it done right every time. Accuracy: GPT-4V will often extract strings that are plausible for a given image, but not the actual strings. For example, if you give it a Chinese menu, it will hallucinate Chinese dish names. SceneXplain pretty much cured hallucinations in its Jelly algorithm. Consistency: GPT-4V doesn’t just hallucinate. It hallucinates different things each time. SceneXplain is generally consistent. Completeness: GPT-4V doesn’t always extract all the strings in the image. SceneXplain is more comprehensive. Cost: SceneXplain is up to 50% more affordable.

Let’s dive into each point in more detail. API limits Good luck with the GPT-4V API! In our extensive testing (even just to write this blog post), we rapidly and repeatedly hit request limits. An organization is limited to 100 requests per day, along with strict throttling. We would've put this post out earlier if we hadn't easily overshot that multiple times. Hello RateLimitError, my old friend. Reliability If you do try to extract strings via the web interface, results can be unpredictable. It can handle English well enough: We can extract the strings as JSON by using the prompt: Extract the text strings from this image and populate a JSON that follows this schema: { "type": "object", "properties": { "text_strings": { "type": "array", "description": "Every text string contained in the image. Consider all languages" } } } Return just the output JSON. Do not put it in a code block Note how specific we had to be in this prompt, explaining that we just wanted raw JSON back, not including comments like “Here is your JSON” and then a back-ticked code block. There is still no guarantee that such a method is watertight. It may sometimes return extraneous content. It returns this output: { "text_strings": [ "YOU CAN'T RUN", "FROM US FOREVER", "m" ] } I would’ve preferred some prettier, indented output. But it looks like valid JSON and accurate output. For reference, SceneXplain returns: { "text_strings": [ "YOU CAN'T RUN", "FROM US FOREVER", "M" ] } Ah, those sweet sweet indents Now let’s try asking in natural language about a Chinese ad: If we use the prompt: Extract the text strings from this image, GPT-4V gives us: It seems there was an error while attempting to extract the text from the image using OCR. The error message indicates a problem with the Tesseract OCR data files for the Chinese simplified language. The necessary language files may not be installed in the environment where the OCR operation was attempted. Given this issue, I'm unable to extract the text from the image as requested. If there's anything else you would like me to assist you with, please let me know! That’s…not useful. However, asking it to extract it as JSON (by using the above prompt with schema) works: { "text_strings": [ "麦当劳", "一周七天", "早晨四点", "至", "17:00 时段", "周末早餐 延时", "更多惊喜", "尽在麦当劳APP" ] } Why can it do the job if we specify we want JSON output, but it just shrugs helplessly if we ask in plain English? Who knows. Accuracy Take another look at that JSON output. Then, take a look at the ad. At first glance, the JSON looks decent. It’s got the 17:00 and other details. But take a closer look. None of those text strings appear in the image. They look like the kind of strings that could occur in a Chinese McDonald's ad, but none of them are actually in that particular ad. This can be even more dangerous than being wrong - enough people are already worried about GPT mansplaining - i.e., being confident but wrong. We see the same story when it comes to non-Latin text too. Also, why does it suddenly think it can extract the text when it stated before that it couldn’t? For reference, SceneXplain returns: { "text_strings": [ "麦麦夜市", "出神卤味鸡架", "青花椒拌鸡", "青花椒酸辣鸡", "青花椒半鸡", "麦麦夜市小堡", "暗糖带劲堡", "唯醇带劲堡", "莱莱真香堡", "17:00营夜", "哇藕带劲堡" ] } If you compare the strings, you’ll see SceneXplain is much more accurate and hallucinates less. Consistency Coming back to our old friend, the Chinese McDonald’s ad, what if we start a new chat session and re-submit the exact same image and prompt? Here's what we get: { "type": "object", "properties": { "text_strings": [ "麦辣鸡翅", "堡堡双拼 等你来撩", "一人食好福利", "17:00前来", "麦当劳", "尊享软欧包", "周边好货 等你", "尊享软欧包" ] } } Well dang. Not only is the text entirely different, but it’s also sent us JSON in a completely different format, something like the schema we sent, rather than the output format that the schema defines. Completeness If we try to extract text from this Arabic coffee ad, GPT-4V gives us far fewer strings than SceneXplain does: GPT-4V: [ "معتوق MAATOUK", "1960", "قهوة عربية", "حبيبة الأصول", "تقدمة عربية", "أصالة امتدت وسطولة النضج" ] SceneXplain: [ "معتوق", "MAATOUK", "1 9 6 0", "قهوة عربية", "حسب الأصول", "قهوة عربية", "معتوق", "mAATOUK", "تحميص غامق", "بن مطحون ١٠٠٪ أرابيكا", "أصالة المذاق وسهولة التحضير", "لطالما اشتهر العرب عبر ماضي الزمان بتحضير القهوة العربية في منازلهم، والتي تعد من أحد رموز الكرم والضيافة", "العربية. من هنا انطلقت مصانع معتوق لتقديم القهوة العربية السهلة التحضير ذات الرائحة المميزة والطعم الأصيل.", "القهوة العربية معتوق ١٩٦٠، قهوة عربية حسب الأصول." ] Cost At the time of writing, GPT-4V charges $0.025 per image. By choosing SceneXplain’s MAX plan you pay less than half of that. You can find out more on our pricing page: SceneXplain - Leading AI Solution for Image Captions and Video Summaries Experience cutting-edge computer vision with our premier image captioning and video summarization algorithms. Tailored for content creators, media professionals, SEO experts, and e-commerce enterprises. Featuring multilingual support and seamless API integration. Elevate your digital presence today. SceneXplain Head to head: GPT-4V vs SceneXplain Let’s put both services to the test and see who comes out on top. 💡 See our notebook for the full range of testing and results. Testing methodology We took a selection of images, some from pexels.com and some from searching Google Images for advertisements in the given languages: Chinese (we didn't differentiate between Simplified and Traditional) Japanese Korean Arabic Hindi We then used: SceneXplain's API (using the Jelly algorithm) A combination of the GPT-4V API and web frontend (since we quickly blasted through our API request limit) We ran several rounds of tests: Basic image description: For SceneXplain, we just uploaded the image. For GPT-4V, we asked: What is in the image? Visual question answering: We uploaded the image to both services and asked: What does the text say in this image? JSON output: For SceneXplain, we simply used the "Extract JSON from image" feature and a predefined JSON Schema. The JSON Schema was as follows: { "type": "object", "properties": { "text_strings": { "type": "array", "description": "Every text string contained in the image. Consider all languages" } } } Since GPT-4V doesn't directly support JSON Schemas, we had to be a bit hacky and explain what we wanted to do as text: Extract the text strings from this image and populate a JSON that follows this schema: <JSON Schema from above> Return just the output JSON. Do not put it in a code block" The results below focus on the JSON outputs since those are (in our opinion) the most useful outputs for real-world usage. 💡 To save space, we’ve simplified the JSON output to include just the text strings, not the rest of the JSON structure.

Chinese We’ve already dived into the McDonald’s adabove, so we’ll just look at one more Chinese image: SceneXplain output: [ "金钱肚20元", "旺角牛筋腩20元", "旺角牛杂18元" ] GPT-4V output: [ "竹筴魚", "20元", "甜甜圈", "20元", "甜甜仙貝", "18元" ] Again, we see GPT-4V gets the menu contents wrong and also splits each price from the (wrong) menu item. SceneXplain keeps the correct menu items and links them with their prices.

GPT-4V gave us the error Something went wrong. Ifthis issue persists please contact us through our help center at help.openai.com. After retrying, it gave us: [ "MDH की एक", "धमाकेदार ऑफर", "स्वाद के साथ - साथ खुशियों की बौछार !!", "मसाला एक स्वादिष्ट और जीवंत उपहार !!", "MDH", "मसाले", "असली मसाले सच-सच", "MDH Ltd.", "E-mails: delhi@mdhspices.in, rk@mdhspices.in www.mdhspices.com" ]

SceneXplain goes much further, even extracting product names and tiny details like when the company was established: [ "MDH", "की एक", "धमाकेदार ऑफर", "स्वाद के साथ -साथ खुशियों की बौछार !", "मसाला पैक खरीदो और जीतो उपहार !!", "एम डी एच की ओर से अपने सभी ग्राहकों के लिए एक धमाकेदार ऑफर।", "किसी भी नजदीकी विक्रेता से एम डी एच मसालों के नीचे छपे पैक्स में से", "कोई भी 100 ग्राम वाला पैक खरीदें और भाग्यशाली विजेता बनने का अवसर", "प्राप्त करें, हो सकता है आप के लिए गए पैक के फ्लेप में उपहार का नाम हो।", "असली मसाले", "मसाले", "सच -सच", "MD H", "SPICES", "MD", "MOH", "Garam", "Pav Bhaji", "masala", "Kitchen", "Shahi Pancer", "King", "Chana", "DEGGI", "MIRCH", "Chunky Chat", "नियम व शर्तें :- एम डी एच मसालों के ऊपर दर्शाये गए चुनिन्दा पैक्स में से कोई भी 100 ग्राम वाला", "पैक खरीदें, उसका फ्लेप खोलें, हो सकता है कि उस फ्लेप के नीचे उपहार का नाम छपा हो। उस", "उपहार को प्राप्त करने के भाग्यशाली विजेता बनें। • इस स्कीम का नकद लाभ कोई भी नहीं है", "लिए दिल्ली में ही लागू है • स्कीम स्टॉक रहने तक सीमित है • यह स्कीम एम डी एच के सुपर", "स्टॉकिस्ट, स्टॉकिस्ट और कर्मचारियों के लिए नहीं है · कंपनी का निर्णय अंतिम और सर्वमान्य होगा", "और सभी विवाद दिल्ली के न्याय क्षेत्र के अधीन होंगे। • अन्य शर्तों के लिए पैक देखें।", "महाशियाँ दी हट्टी (प्रा०) लिमिटेड", "9/44, कीर्ति नगर, नई दिल्ली - 110015 फोन नं० 011-41425106 - 07-08", "ESTD. 1919", "E-mails : delhi@mdhspices.in, rk@mdhspices.in www.mdhspices.com" ] Conclusion

At the end of the day, SceneXplain clearly excelsin multilingual OCR compared to GPT-4V. To recap: API limits: GPT-4V: 100 requests per day SceneXplain: 5,000 credits per month on the MAX plan. JSON output with Jelly costs 2 credits, so you can process 2,500 images per month.

It's a practical, user-friendly way to manage digital documents. Get started now and see the difference SceneXplain can make!

SceneXplain - Leading AI Solution for Image Captions and Video Summaries Experience cutting-edge computer vision with our premier image captioning and video summarization algorithms. Tailored for content creators, media professionals, SEO experts, and e-commerce enterprises. Featuring multilingual support and seamless API integration. Elevate your digital presence today. SceneXplain But just because you take an early lead doesn't mean you win the race. We've got to show how we're better, right? Well, we've already done that in this post: SceneXplain vs. GPT-4 Vision: The Best Image Captioning Tool in 2023? Discover the future of visual comprehension with SceneXplain, the leading image captioning tool of 2023. Dive deep into its transformative features, real-world applications, and see how it stands tall against GPT-4 Vision. SceneXplain But in this post, we'll go one further and show you how we excel at OCR for multilingual texts. In short, SceneXplain is more accurate, reliable, consistent, complete, and cost-effective than GPT-4V. Also, it doesn’t have any pesky daily request limits. You might think GPT-4V is pretty decent if you’re a user of Latin-character languages. Since you’re reading this (I assume in English), that means you! Indeed, GPT-4V does okay when it comes to recognizing English, French, Spanish, and so on, as you can see from these blog posts and studies: First Impressions with GPT-4V(ision) Exploring OCR Capabilities of GPT-4V(ision) : A Quantitative and In-depth Evaluation But, as mentioned in the study: There is a substantial accuracy disparity between the recognition of English and Chinese text. As shown in Table 1, the performance of English text recognition is commendable. Conversely, the accuracy of Chinese text recognition is zero (ReCTS). We speculate that this may be due to the lack of Chinese scene text images as training data in GPT-4V. Bad news - it's not just Chinese where GPT-4V falls down. It consistently fails on non-Latin texts. That's where SceneXplain comes in. We go way beyond just recognizing Latin characters - we can do Chinese, Japanese, Korean, Arabic, Hindi, and potentially more (at this point we ran out of languages that people speak (or recognize) at Jina AI.) TL;DR: How does GPT-4V fail compared to SceneXplain? In short: API limits: 100 requests a day is the new “640K ought to be enough for anybody”. SceneXplain has a range of plans to suit your needs. Reliability: Sometimes, GPT-4V will follow a command to extract the text strings. But if you ask again in exactly the same way, it may say it can’t do it. SceneXplain gets it done right every time. Accuracy: GPT-4V will often extract strings that are plausible for a given image, but not the actual strings. For example, if you give it a Chinese menu, it will hallucinate Chinese dish names. SceneXplain pretty much cured hallucinations in its Jelly algorithm. Consistency: GPT-4V doesn’t just hallucinate. It hallucinates different things each time. SceneXplain is generally consistent. Completeness: GPT-4V doesn’t always extract all the strings in the image. SceneXplain is more comprehensive. Cost: SceneXplain is up to 50% more affordable. Let’s dive into each point in more detail. API limits Good luck with the GPT-4V API! In our extensive testing (even just to write this blog post), we rapidly and repeatedly hit request limits. An organization is limited to 100 requests per day, along with strict throttling. We would've put this post out earlier if we hadn't easily overshot that multiple times. Hello RateLimitError, my old friend. Reliability If you do try to extract strings via the web interface, results can be unpredictable. It can handle English well enough: We can extract the strings as JSON by using the prompt: Extract the text strings from this image and populate a JSON that follows this schema: { "type": "object", "properties": { "text_strings": { "type": "array", "description": "Every text string contained in the image. Consider all languages" } } } Return just the output JSON. Do not put it in a code block Note how specific we had to be in this prompt, explaining that we just wanted raw JSON back, not including comments like “Here is your JSON” and then a back-ticked code block. There is still no guarantee that such a method is watertight. It may sometimes return extraneous content. It returns this output: { "text_strings": [ "YOU CAN'T RUN", "FROM US FOREVER", "m" ] } I would’ve preferred some prettier, indented output. But it looks like valid JSON and accurate output. For reference, SceneXplain returns: { "text_strings": [ "YOU CAN'T RUN", "FROM US FOREVER", "M" ] } Ah, those sweet sweet indents Now let’s try asking in natural language about a Chinese ad: If we use the prompt: Extract the text strings from this image, GPT-4V gives us: It seems there was an error while attempting to extract the text from the image using OCR. The error message indicates a problem with the Tesseract OCR data files for the Chinese simplified language. The necessary language files may not be installed in the environment where the OCR operation was attempted. Given this issue, I'm unable to extract the text from the image as requested. If there's anything else you would like me to assist you with, please let me know! That’s…not useful. However, asking it to extract it as JSON (by using the above prompt with schema) works: { "text_strings": [ "麦当劳", "一周七天", "早晨四点", "至", "17:00 时段", "周末早餐 延时", "更多惊喜", "尽在麦当劳APP" ] } Why can it do the job if we specify we want JSON output, but it just shrugs helplessly if we ask in plain English? Who knows. Accuracy Take another look at that JSON output. Then, take a look at the ad. At first glance, the JSON looks decent. It’s got the 17:00 and other details. But take a closer look. None of those text strings appear in the image. They look like the kind of strings that could occur in a Chinese McDonald's ad, but none of them are actually in that particular ad. This can be even more dangerous than being wrong - enough people are already worried about GPT mansplaining - i.e., being confident but wrong. We see the same story when it comes to non-Latin text too. Also, why does it suddenly think it can extract the text when it stated before that it couldn’t? For reference, SceneXplain returns: { "text_strings": [ "麦麦夜市", "出神卤味鸡架", "青花椒拌鸡", "青花椒酸辣鸡", "青花椒半鸡", "麦麦夜市小堡", "暗糖带劲堡", "唯醇带劲堡", "莱莱真香堡", "17:00营夜", "哇藕带劲堡" ] } If you compare the strings, you’ll see SceneXplain is much more accurate and hallucinates less. Consistency Coming back to our old friend, the Chinese McDonald’s ad, what if we start a new chat session and re-submit the exact same image and prompt? Here's what we get: { "type": "object", "properties": { "text_strings": [ "麦辣鸡翅", "堡堡双拼 等你来撩", "一人食好福利", "17:00前来", "麦当劳", "尊享软欧包", "周边好货 等你", "尊享软欧包" ] } } Well dang. Not only is the text entirely different, but it’s also sent us JSON in a completely different format, something like the schema we sent, rather than the output format that the schema defines. Completeness If we try to extract text from this Arabic coffee ad, GPT-4V gives us far fewer strings than SceneXplain does: GPT-4V: [ "معتوق MAATOUK", "1960", "قهوة عربية", "حبيبة الأصول", "تقدمة عربية", "أصالة امتدت وسطولة النضج" ] SceneXplain: [ "معتوق", "MAATOUK", "1 9 6 0", "قهوة عربية", "حسب الأصول", "قهوة عربية", "معتوق", "mAATOUK", "تحميص غامق", "بن مطحون ١٠٠٪ أرابيكا", "أصالة المذاق وسهولة التحضير", "لطالما اشتهر العرب عبر ماضي الزمان بتحضير القهوة العربية في منازلهم، والتي تعد من أحد رموز الكرم والضيافة", "العربية. من هنا انطلقت مصانع معتوق لتقديم القهوة العربية السهلة التحضير ذات الرائحة المميزة والطعم الأصيل.", "القهوة العربية معتوق ١٩٦٠، قهوة عربية حسب الأصول." ] Cost At the time of writing, GPT-4V charges $0.025 per image. By choosing SceneXplain’s MAX plan you pay less than half of that. You can find out more on our pricing page: SceneXplain - Leading AI Solution for Image Captions and Video Summaries Experience cutting-edge computer vision with our premier image captioning and video summarization algorithms. Tailored for content creators, media professionals, SEO experts, and e-commerce enterprises. Featuring multilingual support and seamless API integration. Elevate your digital presence today. SceneXplain Head to head: GPT-4V vs SceneXplain Let’s put both services to the test and see who comes out on top. 💡 See our notebook for the full range of testing and results. Testing methodology We took a selection of images, some from pexels.com and some from searching Google Images for advertisements in the given languages: Chinese (we didn't differentiate between Simplified and Traditional) Japanese Korean Arabic Hindi We then used: SceneXplain's API (using the Jelly algorithm) A combination of the GPT-4V API and web frontend (since we quickly blasted through our API request limit) We ran several rounds of tests: Basic image description: For SceneXplain, we just uploaded the image. For GPT-4V, we asked: What is in the image? Visual question answering: We uploaded the image to both services and asked: What does the text say in this image? JSON output: For SceneXplain, we simply used the "Extract JSON from image" feature and a predefined JSON Schema. The JSON Schema was as follows: { "type": "object", "properties": { "text_strings": { "type": "array", "description": "Every text string contained in the image. Consider all languages" } } } Since GPT-4V doesn't directly support JSON Schemas, we had to be a bit hacky and explain what we wanted to do as text: Extract the text strings from this image and populate a JSON that follows this schema: <JSON Schema from above> Return just the output JSON. Do not put it in a code block" The results below focus on the JSON outputs since those are (in our opinion) the most useful outputs for real-world usage. 💡 To save space, we’ve simplified the JSON output to include just the text strings, not the rest of the JSON structure. Chinese We’ve already dived into the McDonald’s ad above, so we’ll just look at one more Chinese image: SceneXplain output: [ "金钱肚20元", "旺角牛筋腩20元", "旺角牛杂18元" ] GPT-4V output: [ "竹筴魚", "20元", "甜甜圈", "20元", "甜甜仙貝", "18元" ] Again, we see GPT-4V gets the menu contents wrong and also splits each price from the (wrong) menu item. SceneXplain keeps the correct menu items and links them with their prices. Japanese GPT-4V gets some of the characters correct in the cigarette ad. The string 私はただ吸い殻になります has most of the same characters but is still a bit off. Other strings are just hallucinated. [ "私はただ吸い殻になります", "PLAISIR", "純正", "MICRONITE", "新式", "すべての味" ] SceneXplain: [ "私はたばこを吸います", "PLAISIR", "独占", "MICRONITE", "新た", "シガレット", "喜びの味", "KING SIZE" ] GPT-4V: After extracting (wrong) text from Chinese and Japanese images, we uploaded another image with the prompt Now do this one (which we’d used successfully to repeat prior commands). GPT-4V seems to have forgotten how. We got the output: I'm sorry, but I can't assist with identifying or making statements about text within images. If you have any other questions or need assistance with a different task, feel free to ask! SceneXplain did its duty as expected: [ "用服ぐ直ずせ躇鷹", "アンチ·ルンゲン", "評判の救急薬", "アンチルンダ", "肺炎に", "日英米 製法特許)", "ANTI-LUMGEN", "アンチルバゲノ", "東京验薬株式会社", "呈贈獻文", "(金科百貨店及各麵店 有三)", "ありかせん", "本剤はさが年以上保存しても効目に變化は", "本剤は何等期作品のない安全な内服薬でね", "本剤は他の醫藥と併用して差支へありません", "の必要はありません", "本劑は「只一回分」のみて結構です战版", "ら専門家に期相談下さい", "象の超らない時は乾炎でないと思ひます", "アンチ·ルンゲン を服用しますと必ず右の", "本劑 の 特 長", "るのでありまして安眠より覺める時には徳", "此の特殊現象 發汗安眠 こそ薬効で撲滅", "とも快上げに長時間安眠致します", "發汗し其發汗が相之教生る頃より忠者はい", "アンチ·ルンゲン を服用すると白血球のは", "治 療 の 鐵 則", "如世榮79發音元中山", "價 小人相 金 國", "大人翔 五", "部學化所鋼製山中 社會式格 元賣發", "社會者合木大 ·店商置罐 意 束)", "社會名令部太長川龍 國古名(", "會面イラブサルタビスホ 說 大ノ", "店理代", "社會式株藥製京東 元造製", "Image ID: W5DPKC", "www.alamy.com" ] Korean GPT-4V remembers how to extract text again. And it remembers how to get it wrong too! If you look at the output, some of the characters are the same as the image, but some are not. [ "술은 남에 말나", "술은 나로 말나" ] SceneXplain gives accurate output, though I’m not sure where the 50 is coming from: [ "|야", "좋은 날에 만나", "단이 방", "50", "좋은 나를 만나" ] GPT-4V actually does okay with the more complex image. It doesn’t catch all the strings, but it’s less wrong than usual from a quick comparison (note: I don’t read Korean, so I’m just eyeballing it): [ "자연과 국민을 연결하는", "수목·정원 플랫폼 기관", "수목원의 고객가치를 넘어", "국민 생활 속 녹색공간 확산과", "정원산업 생태계를 활성화하는 역할을", "적극적으로 수행하겠습니다" ] SceneXplain extracts a lot more: [ "한국수목원정원관리원", "자연과 국민을 연결하는", "수목원·정원 플랫폼 기관", "수목원의 공간적 개념을 넘어", "국민 생활 속 녹색문화 확산과", "정원산업 생태계를 활성화하는 역할을", "적극적으로 수행하겠습니다", "산림생물자원", "고품질 수목원", "ES", "보전 · 복원", "서비스", "역량 강화", "산림생물자원", "연구 ·활용", "정원문화", "활성화" ] Arabic Since we already covered the Arabic coffee image above, we'll just leave one Arabic here: GPT-4V: [ "الحياة طريق أكثر سرعة" ] SceneXplain gets a little confused about the 4G logo, seeing it as EAG but is otherwise sound: [ "الحياة صارت أكثر سرعة", "EAG", "LTE" ] Hindi GPT-4V: [ "सरसों और आंवला", "का पोषण बिना चिपचिपाहट", "सिर्फ रु", "9 में", "40ml", "डाबर", "टोल फ्री 1800-103-1644" ] SceneXplain: [ "सरसों आँवला", "केश तेल", "सरसों और आँवला", "का पोषण बिना", "चिपचिपाहट", "में", "नया", "पैक", "₹9/-", "सरसों आँवला", "40ml", "DABUR CARES: CALL OR WRITE", "+ TOLL FREE 1800-103-1644" ] GPT-4V gave us the error Something went wrong. If this issue persists please contact us through our help center at help.openai.com. After retrying, it gave us: [ "MDH की एक", "धमाकेदार ऑफर", "स्वाद के साथ - साथ खुशियों की बौछार !!", "मसाला एक स्वादिष्ट और जीवंत उपहार !!", "MDH", "मसाले", "असली मसाले सच-सच", "MDH Ltd.", "E-mails: delhi@mdhspices.in, rk@mdhspices.in www.mdhspices.com" ] SceneXplain goes much further, even extracting product names and tiny details like when the company was established: [ "MDH", "की एक", "धमाकेदार ऑफर", "स्वाद के साथ -साथ खुशियों की बौछार !", "मसाला पैक खरीदो और जीतो उपहार !!", "एम डी एच की ओर से अपने सभी ग्राहकों के लिए एक धमाकेदार ऑफर।", "किसी भी नजदीकी विक्रेता से एम डी एच मसालों के नीचे छपे पैक्स में से", "कोई भी 100 ग्राम वाला पैक खरीदें और भाग्यशाली विजेता बनने का अवसर", "प्राप्त करें, हो सकता है आप के लिए गए पैक के फ्लेप में उपहार का नाम हो।", "असली मसाले", "मसाले", "सच -सच", "MD H", "SPICES", "MD", "MOH", "Garam", "Pav Bhaji", "masala", "Kitchen", "Shahi Pancer", "King", "Chana", "DEGGI", "MIRCH", "Chunky Chat", "नियम व शर्तें :- एम डी एच मसालों के ऊपर दर्शाये गए चुनिन्दा पैक्स में से कोई भी 100 ग्राम वाला", "पैक खरीदें, उसका फ्लेप खोलें, हो सकता है कि उस फ्लेप के नीचे उपहार का नाम छपा हो। उस", "उपहार को प्राप्त करने के भाग्यशाली विजेता बनें। • इस स्कीम का नकद लाभ कोई भी नहीं है", "लिए दिल्ली में ही लागू है • स्कीम स्टॉक रहने तक सीमित है • यह स्कीम एम डी एच के सुपर", "स्टॉकिस्ट, स्टॉकिस्ट और कर्मचारियों के लिए नहीं है · कंपनी का निर्णय अंतिम और सर्वमान्य होगा", "और सभी विवाद दिल्ली के न्याय क्षेत्र के अधीन होंगे। • अन्य शर्तों के लिए पैक देखें।", "महाशियाँ दी हट्टी (प्रा०) लिमिटेड", "9/44, कीर्ति नगर, नई दिल्ली - 110015 फोन नं० 011-41425106 - 07-08", "ESTD. 1919", "E-mails : delhi@mdhspices.in, rk@mdhspices.in www.mdhspices.com" ] Conclusion At the end of the day, SceneXplain clearly excels in multilingual OCR compared to GPT-4V. To recap: API limits: GPT-4V: 100 requests per day SceneXplain: 5,000 credits per month on the MAX plan. JSON output with Jelly costs 2 credits, so you can process 2,500 images per month. Reliability: GPT-4V: Is often like “I’m sorry Dave, I’m afraid I can’t do that.” SceneXplain: Doggedly reliable. Gets the job done. Accuracy: GPT-4V: hallucinates strings it believes are plausible from a given image, rather than reading the actual text. SceneXplain: Extracts the correct text. Consistency: GPT-4V doesn’t just hallucinate. It hallucinates different things each time. SceneXplain gives much more consistent output. Completeness: GPT-4V: Often doesn’t always extract all the strings in the image. SceneXplain: Extracts more strings. Cost: GPT-4V: $0.025 per image. SceneXplain: As low as 0.02 USD per image on the MAX plan if you enable JSON output. As low as 0.01 USD without JSON output. When you take all those factors into account, it's clear that SceneXplain is the obvious choice. Get started with SceneXplain Ready to explore multilingual OCR? Sign up for a free account with SceneXplain and start converting images to text easily. It's a practical, user-friendly way to manage digital documents. Get started now and see the difference SceneXplain can make! SceneXplain - Leading AI Solution for Image Captions and Video Summaries Experience cutting-edge computer vision with our premier image captioning and video summarization algorithms. Tailored for content creators, media professionals, SEO experts, and e-commerce enterprises. Featuring multilingual support and seamless API integration. Elevate your digital presence today. SceneXplain Categories: Tech blog rss_feed Top-5 similar articles play_arrow GET TOP-5 Select reranker Read more

August 26, 2024 • 13 minutes read The What and Whyof Text-Image Modality Gap in CLIP Models You can't just use a CLIP model to retrieve text and images and sort the results by score. Why? Because of the modality gap. What is it, and where does it come from? August 22, 2024 • 8 minutes read

Late Chunking in Long-Context Embedding Models Chunking long documents while preserving contextual information is challenging. We introduce the "Late Chunking" that leverages long-context embedding models to generate contextual chunk embeddings for better retrieval applications.

July 31, 2024 • 17 minutes read Rephrased Labels Improve Zero-Shot Text Classification by 30%

When using embedding models for zero-shot classification, rephrasing the class label to "This is seriously about 'LABEL'" gives higher accuracy vs. using LABEL alone. But how, and why? OFFICES location_on Berlin, Germany (HQ) Prinzessinnenstraße 19-20, 10969 Berlin, Germany Geschäftsanschrift: Leipzigerstr. 96, 10117 Berlin, Germany location_on Beijing, China Level 5, Building 6, No.48 Haidian West St. Beijing Haidian, China location_on Shenzhen, China 402, Floor 4, Fu'an Technology Building, Shenzhen Nanshan, China SEARCH FOUNDATION Embeddings Reranker Reader Segmenter Get Jina AI API key API Status COMPANY About us Contact sales Newsroom Intern program Join us open_in_new Download logo open_in_new TERMS Terms & Conditions Privacy Manage Cookies email language English science Jina AI GmbH © 2020-2024.

## SUMMARY_CHUNKING

#### 8 chunk(s)

SceneXplain But just because you take an early lead doesn't mean you win the race. We've got to show how we're better, right? Well, we've already done that in this post: SceneXplain vs. GPT-4 Vision: The Best Image Captioning Tool in 2023? Discover the future of visual comprehension with SceneXplain, the leading image captioning tool of 2023. Dive deep into its transformative features, real-world applications, and see how it stands tall against GPT-4 Vision. SceneXplain But in this post, we'll go one further and show you how we excel at OCR for multilingual texts. In short, SceneXplain is more accurate, reliable, consistent, complete, and cost-effective than GPT-4V. Also, it doesn’t have any pesky daily request limits. You might think GPT-4V is pretty decent if you’re a user of Latin-character languages. Since you’re reading this (I assume in English), that means you! Indeed, GPT-4V does okay when it comes to recognizing English, French, Spanish, and so on, as you can see from these blog posts and studies:

SceneXplain But in this post, we'll go one furtherand show you how we excel at OCR for multilingual texts. In short, SceneXplain is more accurate, reliable, consistent, complete, and cost-effective than GPT-4V. Also, it doesn’t have any pesky daily request limits. You might think GPT-4V is pretty decent if you’re a user of Latin-character languages. Since you’re reading this (I assume in English), that means you! Indeed, GPT-4V does okay when it comes to recognizing English, French, Spanish, and so on, as you can see from these blog posts and studies: First Impressions with GPT-4V(ision) Exploring OCR Capabilities of GPT-4V(ision) : A Quantitative and In-depth Evaluation But, as mentioned in the study: There is a substantial accuracy disparity between the recognition of English and Chinese text. As shown in Table 1, the performance of English text recognition is commendable. Conversely, the accuracy of Chinese text recognition is zero (ReCTS). We speculate that this may be due to the lack of Chinese scene text images as training data in GPT-4V. Bad news - it's not just Chinese where GPT-4V falls down. It consistently fails on non-Latin texts. That's where SceneXplain comes in. We go way beyond just recognizing Latin characters - we can do Chinese, Japanese, Korean, Arabic, Hindi, and potentially more (at this point we ran out of languages that people speak (or recognize) at Jina AI.) TL;DR: How does GPT-4V fail compared to SceneXplain? In short: API limits: 100 requests a day is the new “640K ought to be enough for anybody”. SceneXplain has a range of plans to suit your needs. Reliability: Sometimes, GPT-4V will follow a command to extract the text strings. But if you ask again in exactly the same way, it may say it can’t do it. SceneXplain gets it done right every time. Accuracy: GPT-4V will often extract strings that are plausible for a given image, but not the actual strings. For example, if you give it a Chinese menu, it will hallucinate Chinese dish names. SceneXplain pretty much cured hallucinations in its Jelly algorithm. Consistency: GPT-4V doesn’t just hallucinate. It hallucinates different things each time.

SceneXplain gives accurate output, though I’m not sure where the 50 is coming from: [ "|야", "좋은 날에 만나", "단이 방", "50", "좋은 나를 만나" ]

GPT-4V actually does okay with the more complex image. It doesn’t catch all the strings, but it’s less wrong than usual from a quick comparison (note: I don’t read Korean, so I’m just eyeballing it): [ "자연과 국민을 연결하는", "수목·정원 플랫폼 기관", "수목원의 고객가치를 넘어", "국민 생활 속 녹색공간 확산과", "정원산업 생태계를 활성화하는 역할을", "적극적으로 수행하겠습니다" ] SceneXplain extracts a lot more: [ "한국수목원정원관리원", "자연과 국민을 연결하는", "수목원·정원 플랫폼 기관", "수목원의 공간적 개념을 넘어", "국민 생활 속 녹색문화 확산과", "정원산업 생태계를 활성화하는 역할을", "적극적으로 수행하겠습니다", "산림생물자원", "고품질 수목원", "ES", "보전 · 복원", "서비스", "역량 강화", "산림생물자원", "연구 ·활용", "정원문화", "활성화" ] Arabic Since we already covered the Arabic coffee image above, we'll just leave one Arabic here: GPT-4V: [ "الحياة طريق أكثر سرعة" ] SceneXplain gets a little confused about the 4G logo, seeing it as EAG but is otherwise sound: [ "الحياة صارت أكثر سرعة", "EAG", "LTE" ] Hindi GPT-4V: [ "सरसों और आंवला", "का पोषण बिना चिपचिपाहट", "सिर्फ रु", "9 में", "40ml", "डाबर", "टोल फ्री 1800-103-1644" ] SceneXplain: [ "सरसों आँवला", "केश तेल", "सरसों और आँवला", "का पोषण बिना", "चिपचिपाहट", "में", "नया", "पैक", "₹9/-", "सरसों आँवला", "40ml", "DABUR CARES: CALL OR WRITE", "+ TOLL FREE 1800-103-1644" ] GPT-4V gave us the error Something went wrong. If this issue persists please contact us through our help center at help.openai.com. After retrying, it gave us: [ "MDH की एक", "धमाकेदार ऑफर", "स्वाद के साथ - साथ खुशियों की बौछार !!", "मसाला एक स्वादिष्ट और जीवंत उपहार !!", "MDH", "मसाले", "असली मसाले सच-सच", "MDH Ltd.", "E-mails: delhi@mdhspices.in, rk@mdhspices.in www.mdhspices.com" ]

SceneXplain goes much further, even extracting product names and tiny details like when the company was established: [ "MDH", "की एक", "धमाकेदार ऑफर", "स्वाद के साथ -साथ खुशियों की बौछार !", "मसाला पैक खरीदो और जीतो उपहार !!", "एम डी एच की ओर से अपने सभी ग्राहकों के लिए एक धमाकेदार ऑफर।", "किसी भी नजदीकी विक्रेता से एम डी एच मसालों के नीचे छपे पैक्स में से", "कोई भी 100 ग्राम वाला पैक खरीदें और भाग्यशाली विजेता बनने का अवसर", "प्राप्त करें, हो सकता है आप के लिए गए पैक के फ्लेप में उपहार का नाम हो।", "असली मसाले", "मसाले", "सच -सच", "MD H", "SPICES", "MD", "MOH", "Garam", "Pav Bhaji", "masala", "Kitchen", "Shahi Pancer", "King", "Chana", "DEGGI", "MIRCH", "Chunky Chat", "नियम व शर्तें :- एम डी एच मसालों के ऊपर दर्शाये गए चुनिन्दा पैक्स में से कोई भी 100 ग्राम वाला", "पैक खरीदें, उसका फ्लेप खोलें, हो सकता है कि उस फ्लेप के नीचे उपहार का नाम छपा हो। उस", "उपहार को प्राप्त करने के भाग्यशाली विजेता बनें। • इस स्कीम का नकद लाभ कोई भी नहीं है", "लिए दिल्ली में ही लागू है • स्कीम स्टॉक रहने तक सीमित है • यह स्कीम एम डी एच के सुपर", "स्टॉकिस्ट, स्टॉकिस्ट और कर्मचारियों के लिए नहीं है · कंपनी का निर्णय अंतिम और सर्वमान्य होगा", "और सभी विवाद दिल्ली के न्याय क्षेत्र के अधीन होंगे। • अन्य शर्तों के लिए पैक देखें।", "महाशियाँ दी हट्टी (प्रा०) लिमिटेड", "9/44, कीर्ति नगर, नई दिल्ली - 110015 फोन नं० 011-41425106 - 07-08", "ESTD. 1919", "E-mails : delhi@mdhspices.in, rk@mdhspices.in www.mdhspices.com" ]

Conclusion At the end of the day, SceneXplain clearly excels in multilingual OCR compared to GPT-4V. To recap: API limits: GPT-4V: 100 requests per day SceneXplain: 5,000 credits per month on the MAX plan. JSON output with Jelly costs 2 credits, so you can process 2,500 images per month. Reliability: GPT-4V: Is often like “I’m sorry Dave, I’m afraid I can’t do that.” SceneXplain: Doggedly reliable. Gets the job done. Accuracy: GPT-4V: hallucinates strings it believes are plausible from a given image, rather than reading the actual text. SceneXplain: Extracts the correct text. Consistency: GPT-4V doesn’t just hallucinate. It hallucinates different things each time. SceneXplain gives much more consistent output. Completeness: GPT-4V: Often doesn’t always extract all the strings in the image. SceneXplain: Extracts more strings. Cost: GPT-4V: $0.025 per image. SceneXplain: As low as 0.02 USD per image on the MAX plan if you enable JSON output. As low as 0.01 USD without JSON output. When you take all those factors into account, it's clear that SceneXplain is the obvious choice.

Get started with SceneXplain Ready to explore multilingual OCR? Sign up for a free account with SceneXplain and start converting images to text easily. It's a practical, user-friendly way to manage digital documents. Get started now and see the difference SceneXplain can make! SceneXplain - Leading AI Solution for Image Captions and Video Summaries Experience cutting-edge computer vision with our premier image captioning and video summarization algorithms. Tailored for content creators, media professionals, SEO experts, and e-commerce enterprises. Featuring multilingual support and seamless API integration. Elevate your digital presence today. SceneXplain Categories: Tech blog rss_feed Top-5 similar articles play_arrow GET TOP-5 Select reranker Read more August 26, 2024 • 13 minutes read The What and Why of Text-Image Modality Gap in CLIP Models You can't just use a CLIP model to retrieve text and images and sort the results by score. Why? Because of the modality gap. What is it, and where does it come from? August 22, 2024 • 8 minutes read Late Chunking in Long-Context Embedding Models Chunking long documents while preserving contextual information is challenging. We introduce the "Late Chunking" that leverages long-context embedding models to generate contextual chunk embeddings for better retrieval applications. July 31, 2024 • 17 minutes read Rephrased Labels Improve Zero-Shot Text Classification by 30% When using embedding models for zero-shot classification, rephrasing the class label to "This is seriously about 'LABEL'" gives higher accuracy vs. using LABEL alone. But how, and why?

OFFICES location_on Berlin, Germany (HQ) Prinzessinnenstraße 19-20, 10969 Berlin, Germany Geschäftsanschrift: Leipzigerstr. 96, 10117 Berlin, Germany location_on Beijing, China Level 5, Building 6, No.48 Haidian West St. Beijing Haidian, China location_on Shenzhen, China 402, Floor 4, Fu'an Technology Building, Shenzhen Nanshan, China SEARCH FOUNDATION Embeddings Reranker Reader Segmenter Get Jina AI API key API Status COMPANY About us Contact sales Newsroom Intern program Join us open_in_new Download logo open_in_new TERMS Terms & Conditions Privacy Manage Cookies email language English science Jina AI GmbH © 2020-2024.

## JINA-SEGMENTER-API

#### 331 chunk(s)

search


notifications


NEWS


PRODUCTS


COMPANY


Tech blog


November 16, 2023


SceneXplain's OCR beats GPT-4V hands down: Chinese, Japanese, Korean, Arabic, Hindi, and more!


SceneXplain beats GPT-4V by going beyond English, offering multilingual OCR for Chinese, Japanese, Korean, Arabic, Hindi and more


Alex C-G • 13 minutes read



There's been a lot of noise recently about the release of GPT-4V - a model that can analyze the content of images and summarize that into human language. Sound familiar? It may, because SceneXplain has been doing just that for months already!



SceneXplain - Leading AI Solution for Image Captions and Video Summaries


Experience cutting-edge computer vision with our premier image captioning and video summarization algorithms. Tailored for content creators, media professionals, SEO experts, and e-commerce enterprises. Featuring multilingual support and seamless API integration. Elevate your digital presence today.


SceneXplain



But just because you take an early lead doesn't mean you win the race. We've got to show how we're better, right? Well, we've already done that in this post:



SceneXplain vs. GPT-4 Vision: The Best Image Captioning Tool in 2023?


Discover the future of visual comprehension with SceneXplain, the leading image captioning tool of 2023. Dive deep into its transformative features, real-world applications, and see how it stands tall against GPT-4 Vision.


SceneXplain



But in this post, we'll go one further and show you how we excel at OCR for multilingual texts. In short, SceneXplain is more accurate, reliable, consistent, complete, and cost-effective than GPT-4V. Also, it doesn’t have any pesky daily request limits.



You might think GPT-4V is pretty decent if you’re a user of Latin-character languages. Since you’re reading this (I assume in English), that means you!



Indeed, GPT-4V does okay when it comes to recognizing English, French, Spanish, and so on, as you can see from these blog posts and studies:



First Impressions with GPT-4V(ision)


Exploring OCR Capabilities of GPT-4V(ision) : A Quantitative and In-depth Evaluation



But, as mentioned in the study:



There is a substantial accuracy disparity between the recognition of English and Chinese text. As shown in Table 1, the performance of English text recognition is commendable. Conversely, the accuracy of Chinese text recognition is zero (ReCTS). We speculate that this may be due to the lack of Chinese scene text images as training data in GPT-4V.



Bad news - it's not just Chinese where GPT-4V falls down. It consistently fails on non-Latin texts.



That's where SceneXplain comes in. We go way beyond just recognizing Latin characters - we can do Chinese, Japanese, Korean, Arabic, Hindi, and potentially more (at this point we ran out of languages that people speak (or recognize) at Jina AI.)



TL;DR: How does GPT-4V fail compared to SceneXplain?



In short:



API limits: 100 requests a day is the new “640K ought to be enough for anybody”. SceneXplain has a range of plans to suit your needs.


Reliability: Sometimes, GPT-4V will follow a command to extract the text strings. But if you ask again in exactly the same way, it may say it can’t do it. SceneXplain gets it done right every time.


Accuracy: GPT-4V will often extract strings that are plausible for a given image, but not the actual strings. For example, if you give it a Chinese menu, it will hallucinate Chinese dish names. SceneXplain pretty much cured hallucinations in its Jelly algorithm.


Consistency: GPT-4V doesn’t just hallucinate. It hallucinates different things each time. SceneXplain is generally consistent.


Completeness: GPT-4V doesn’t always extract all the strings in the image. SceneXplain is more comprehensive.


Cost: SceneXplain is up to 50% more affordable.



Let’s dive into each point in more detail.



API limits



Good luck with the GPT-4V API! In our extensive testing (even just to write this blog post), we rapidly and repeatedly hit request limits. An organization is limited to 100 requests per day, along with strict throttling. We would've put this post out earlier if we hadn't easily overshot that multiple times.



Hello RateLimitError, my old friend.


Reliability



If you do try to extract strings via the web interface, results can be unpredictable. It can handle English well enough:



We can extract the strings as JSON by using the prompt:



Extract the text strings from this image and populate a JSON that follows this schema:



{


"type": "object",
  

"properties": {
    

"text_strings": {
      

"type": "array",
      

"description": "Every text string contained in the image. Consider all languages"
    }
  }
}



Return just the output JSON. Do not put it in a code block




Note how specific we had to be in this prompt, explaining that we just wanted raw JSON back, not including comments like “Here is your JSON” and then a back-ticked code block. There is still no guarantee that such a method is watertight. It may sometimes return extraneous content.



It returns this output:



{


"text_strings": [


"YOU CAN'T RUN",


"FROM US FOREVER",


"m"
]
}




I would’ve preferred some prettier, indented output. But it looks like valid JSON and accurate output. For reference, SceneXplain returns:



{


"text_strings": [
    

"YOU CAN'T RUN",
    

"FROM US FOREVER",
    

"M"
  ]
}



Ah, those sweet sweet indents



Now let’s try asking in natural language about a Chinese ad:



If we use the prompt: Extract the text strings from this image, GPT-4V gives us:



It seems there was an error while attempting to extract the text from the image using OCR. The error message indicates a problem with the Tesseract OCR data files for the Chinese simplified language. The necessary language files may not be installed in the environment where the OCR operation was attempted.



Given this issue, I'm unable to extract the text from the image as requested. If there's anything else you would like me to assist you with, please let me know!




That’s…not useful. However, asking it to extract it as JSON (by using the above prompt with schema) works:



{


"text_strings": [


"麦当劳",


"一周七天",


"早晨四点",


"至",


"17:00 时段",


"周末早餐 延时",


"更多惊喜",


"尽在麦当劳APP"
]
}




Why can it do the job if we specify we want JSON output, but it just shrugs helplessly if we ask in plain English? Who knows.



Accuracy



Take another look at that JSON output. Then, take a look at the ad.



At first glance, the JSON looks decent. It’s got the 17:00 and other details. But take a closer look. None of those text strings appear in the image. They look like the kind of strings that could occur in a Chinese McDonald's ad, but none of them are actually in that particular ad.



This can be even more dangerous than being wrong - enough people are already worried about GPT mansplaining - i.e., being confident but wrong. We see the same story when it comes to non-Latin text too.



Also, why does it suddenly think it can extract the text when it stated before that it couldn’t?



For reference, SceneXplain returns:



{


"text_strings": [
    

"麦麦夜市",
    

"出神卤味鸡架",
    

"青花椒拌鸡",
    

"青花椒酸辣鸡",
    

"青花椒半鸡",
    

"麦麦夜市小堡",
    

"暗糖带劲堡",
    

"唯醇带劲堡",
    

"莱莱真香堡",
    

"17:00营夜",
    

"哇藕带劲堡"
  ]
}




If you compare the strings, you’ll see SceneXplain is much more accurate and hallucinates less.



Consistency



Coming back to our old friend, the Chinese McDonald’s ad, what if we start a new chat session and re-submit the exact same image and prompt? Here's what we get:



{


"type": "object",


"properties": {


"text_strings": [


"麦辣鸡翅",


"堡堡双拼 等你来撩",


"一人食好福利",


"17:00前来",


"麦当劳",


"尊享软欧包",


"周边好货 等你",


"尊享软欧包"
]
}
}




Well dang. Not only is the text entirely different, but it’s also sent us JSON in a completely different format, something like the schema we sent, rather than the output format that the schema defines.



Completeness



If we try to extract text from this Arabic coffee ad, GPT-4V gives us far fewer strings than SceneXplain does:



GPT-4V:


[


"معتوق MAATOUK",


"1960",


"قهوة عربية",


"حبيبة الأصول",


"تقدمة عربية",


"أصالة امتدت وسطولة النضج"
]



SceneXplain:


[


    "معتوق",
    "MAATOUK",
    "1 9 6 0",
    "قهوة عربية",
    "حسب الأصول",
    "قهوة عربية",
    "معتوق",
    "mAATOUK",
    "تحميص غامق",
    "بن مطحون ١٠٠٪ أرابيكا",
    "أصالة المذاق وسهولة التحضير",
    "لطالما اشتهر العرب عبر ماضي الزمان بتحضير القهوة العربية في منازلهم، والتي تعد من أحد رموز الكرم والضيافة",
    "العربية. من هنا انطلقت مصانع معتوق لتقديم القهوة العربية السهلة التحضير ذات الرائحة المميزة والطعم الأصيل.",
    "القهوة العربية معتوق ١٩٦٠، قهوة عربية حسب الأصول."


Cost



At the time of writing, GPT-4V charges $0.025 per image. By choosing SceneXplain’s MAX plan you pay less than half of that. You can find out more on our pricing page:



SceneXplain - Leading AI Solution for Image Captions and Video Summaries


Experience cutting-edge computer vision with our premier image captioning and video summarization algorithms. Tailored for content creators, media professionals, SEO experts, and e-commerce enterprises. Featuring multilingual support and seamless API integration. Elevate your digital presence today.


SceneXplain


Head to head: GPT-4V vs SceneXplain



Let’s put both services to the test and see who comes out on top.



See our notebook for the full range of testing and results.


Testing methodology



We took a selection of images, some from pexels.com and some from searching Google Images for advertisements in the given languages:



Chinese (we didn't differentiate between Simplified and Traditional)


Japanese


Korean


Arabic


Hindi



We then used:



SceneXplain's API (using the Jelly algorithm)


A combination of the GPT-4V API and web frontend (since we quickly blasted through our API request limit)



We ran several rounds of tests:



Basic image description: For SceneXplain, we just uploaded the image. For GPT-4V, we asked: What is in the image?


Visual question answering: We uploaded the image to both services and asked: What does the text say in this image?


JSON output: For SceneXplain, we simply used the "Extract JSON from image" feature and a predefined JSON Schema.



The JSON Schema was as follows:



{


"type": "object",
  

"properties": {
    

"text_strings": {
      

"type": "array",
      

"description": "Every text string contained in the image. Consider all languages"
    }
  }
}



Since GPT-4V doesn't directly support JSON Schemas, we had to be a bit hacky and explain what we wanted to do as text:



Extract the text strings from this image and populate a JSON that follows this schema:



<JSON Schema from above>



Return just the output JSON. Do not put it in a code block"



The results below focus on the JSON outputs since those are (in our opinion) the most useful outputs for real-world usage.



To save space, we’ve simplified the JSON output to include just the text strings, not the rest of the JSON structure.


Chinese



We’ve already dived into the McDonald’s ad above, so we’ll just look at one more Chinese image:



SceneXplain output:


[


"金钱肚20元",
  

"旺角牛筋腩20元",
  

"旺角牛杂18元"
]


GPT-4V output:


[


"竹筴魚",
  

"20元", 
  

"甜甜圈",
  

"20元",
  

"甜甜仙貝",
  

"18元"
]



Again, we see GPT-4V gets the menu contents wrong and also splits each price from the (wrong) menu item. SceneXplain keeps the correct menu items and links them with their prices.



Japanese


GPT-4V gets some of the characters correct in the cigarette ad. The string 私はただ吸い殻になります has most of the same characters but is still a bit off. Other strings are just hallucinated.


[


"私はただ吸い殻になります",


"PLAISIR",


"純正",


"MICRONITE",


"新式",


"すべての味"
]



SceneXplain:


[


    "私はたばこを吸います",
    "PLAISIR",
    "独占",
    "MICRONITE",
    "新た",
    "シガレット",
    "喜びの味",
    "KING SIZE"


GPT-4V: After extracting (wrong) text from Chinese and Japanese images, we uploaded another image with the prompt Now do this one (which we’d used successfully to repeat prior commands). GPT-4V seems to have forgotten how. We got the output:


I'm sorry, but I can't assist with identifying or making statements about text within images. If you have any other questions or need assistance with a different task, feel free to ask!



SceneXplain did its duty as expected:


[


    "用服ぐ直ずせ躇鷹",
    "アンチ·ルンゲン",
    "評判の救急薬",
    "アンチルンダ",
    "肺炎に",
    "日英米 製法特許)",
    "ANTI-LUMGEN",
    "アンチルバゲノ",
    "東京验薬株式会社",
    "呈贈獻文",
    "(金科百貨店及各麵店 有三)",
    "ありかせん",
    "本剤はさが年以上保存しても効目に變化は",
    "本剤は何等期作品のない安全な内服薬でね",
    "本剤は他の醫藥と併用して差支へありません",
    "の必要はありません",
    "本劑は「只一回分」のみて結構です战版",
    "ら専門家に期相談下さい",
    "象の超らない時は乾炎でないと思ひます",
    "アンチ·ルンゲン を服用しますと必ず右の",
    "本劑 の 特 長",


    "るのでありまして安眠より覺める時には徳",
    "此の特殊現象 發汗安眠 こそ薬効で撲滅",
    "とも快上げに長時間安眠致します",
    "發汗し其發汗が相之教生る頃より忠者はい",
    "アンチ·ルンゲン を服用すると白血球のは",
    "治 療 の 鐵 則",
    "如世榮79發音元中山",
    "價 小人相 金 國",
    "大人翔 五",
    "部學化所鋼製山中 社會式格 元賣發",
    "社會者合木大 ·店商置罐 意 束)",
    "社會名令部太長川龍 國古名(",
    "會面イラブサルタビスホ 說 大ノ",
    "店理代",
    "社會式株藥製京東 元造製",
    "Image ID: W5DPKC",
    "www.alamy.com"


Korean


GPT-4V remembers how to extract text again. And it remembers how to get it wrong too! If you look at the output, some of the characters are the same as the image, but some are not.


[


"술은 남에 말나",


"술은 나로 말나"
]



SceneXplain gives accurate output, though I’m not sure where the 50 is coming from:


[


    "|야",
    "좋은 날에 만나",
    "단이 방",
    "50",
    "좋은 나를 만나"


GPT-4V actually does okay with the more complex image. It doesn’t catch all the strings, but it’s less wrong than usual from a quick comparison (note: I don’t read Korean, so I’m just eyeballing it):


[


"자연과 국민을 연결하는",


"수목·정원 플랫폼 기관",


"수목원의 고객가치를 넘어",


"국민 생활 속 녹색공간 확산과",


"정원산업 생태계를 활성화하는 역할을",


"적극적으로 수행하겠습니다"
]



SceneXplain extracts a lot more:


[


    "한국수목원정원관리원",
    "자연과 국민을 연결하는",
    "수목원·정원 플랫폼 기관",
    "수목원의 공간적 개념을 넘어",
    "국민 생활 속 녹색문화 확산과",
    "정원산업 생태계를 활성화하는 역할을",
    "적극적으로 수행하겠습니다",
    "산림생물자원",
    "고품질 수목원",
    "ES",
    "보전 · 복원",
    "서비스",
    "역량 강화",
    "산림생물자원",
    "연구 ·활용",
    "정원문화",
    "활성화"


Arabic



Since we already covered the Arabic coffee image above, we'll just leave one Arabic here:



GPT-4V:


[


"الحياة طريق أكثر سرعة"
]



SceneXplain gets a little confused about the 4G logo, seeing it as EAG but is otherwise sound:


[


    "الحياة صارت أكثر سرعة",
    "EAG",
    "LTE"


Hindi


GPT-4V:


[


"सरसों और आंवला",


"का पोषण बिना चिपचिपाहट",


"सिर्फ रु",


"9 में",


"40ml",


"डाबर",


"टोल फ्री 1800-103-1644"
]



SceneXplain:


[


    "सरसों आँवला",
    "केश तेल",
    "सरसों और आँवला",
    "का पोषण बिना",
    "चिपचिपाहट",
    "में",
    "नया",
    "पैक",
    "₹9/-",
    "सरसों आँवला",
    "40ml",
    "DABUR CARES: CALL OR WRITE",
    "+ TOLL FREE 1800-103-1644"


GPT-4V gave us the error Something went wrong. If this issue persists please contact us through our help center at help.openai.com. After retrying, it gave us:


[


"MDH की एक",


"धमाकेदार ऑफर",


"स्वाद के साथ - साथ खुशियों की बौछार !!",


"मसाला एक स्वादिष्ट और जीवंत उपहार !!",


"MDH",


"मसाले",


"असली मसाले सच-सच",


"MDH Ltd.",


"E-mails: delhi@mdhspices.in, rk@mdhspices.in www.mdhspices.com"
]



SceneXplain goes much further, even extracting product names and tiny details like when the company was established:


[


    "MDH",
    "की एक",
    "धमाकेदार ऑफर",
    "स्वाद के साथ -साथ खुशियों की बौछार !",
    "मसाला पैक खरीदो और जीतो उपहार !!",
    "एम डी एच की ओर से अपने सभी ग्राहकों के लिए एक धमाकेदार ऑफर।",
    "किसी भी नजदीकी विक्रेता से एम डी एच मसालों के नीचे छपे पैक्स में से",
    "कोई भी 100 ग्राम वाला पैक खरीदें और भाग्यशाली विजेता बनने का अवसर",
    "प्राप्त करें, हो सकता है आप के लिए गए पैक के फ्लेप में उपहार का नाम हो।",
    "असली मसाले",
    "मसाले",
    "सच -सच",
    "MD H",
    "SPICES",
    "MD",
    "MOH",
    "Garam",
    "Pav Bhaji",
    "masala",
    "Kitchen",
    "Shahi Pancer",


    "King",
    "Chana",
    "DEGGI",
    "MIRCH",
    "Chunky Chat",
    "नियम व शर्तें :- एम डी एच मसालों के ऊपर दर्शाये गए चुनिन्दा पैक्स में से कोई भी 100 ग्राम वाला",
    "पैक खरीदें, उसका फ्लेप खोलें, हो सकता है कि उस फ्लेप के नीचे उपहार का नाम छपा हो। उस",
    "उपहार को प्राप्त करने के भाग्यशाली विजेता बनें। • इस स्कीम का नकद लाभ कोई भी नहीं है",
    "लिए दिल्ली में ही लागू है • स्कीम स्टॉक रहने तक सीमित है • यह स्कीम एम डी एच के सुपर",
    "स्टॉकिस्ट, स्टॉकिस्ट और कर्मचारियों के लिए नहीं है · कंपनी का निर्णय अंतिम और सर्वमान्य होगा",
    "और सभी विवाद दिल्ली के न्याय क्षेत्र के अधीन होंगे। • अन्य शर्तों के लिए पैक देखें।",
    "महाशियाँ दी हट्टी (प्रा०) लिमिटेड",
    "9/44, कीर्ति नगर, नई दिल्ली - 110015 फोन नं० 011-41425106 - 07-08",
    "ESTD. 1919",
    "E-mails : delhi@mdhspices.in, rk@mdhspices.in www.mdhspices.com"


Conclusion



At the end of the day, SceneXplain clearly excels in multilingual OCR compared to GPT-4V. To recap:



API limits:



GPT-4V: 100 requests per day


SceneXplain: 5,000 credits per month on the MAX plan. JSON output with Jelly costs 2 credits, so you can process 2,500 images per month.



Reliability:



GPT-4V: Is often like “I’m sorry Dave, I’m afraid I can’t do that.”


SceneXplain: Doggedly reliable. Gets the job done.



Accuracy:



GPT-4V: hallucinates strings it believes are plausible from a given image, rather than reading the actual text.


SceneXplain: Extracts the correct text.



Consistency:



GPT-4V doesn’t just hallucinate. It hallucinates different things each time.


SceneXplain gives much more consistent output.



Completeness:



GPT-4V: Often doesn’t always extract all the strings in the image.


SceneXplain: Extracts more strings.



Cost:



GPT-4V: $0.025 per image.


SceneXplain: As low as 0.02 USD per image on the MAX plan if you enable JSON output. As low as 0.01 USD without JSON output.



When you take all those factors into account, it's clear that SceneXplain is the obvious choice.



Get started with SceneXplain



Ready to explore multilingual OCR? Sign up for a free account with SceneXplain and start converting images to text easily. It's a practical, user-friendly way to manage digital documents. Get started now and see the difference SceneXplain can make!



SceneXplain - Leading AI Solution for Image Captions and Video Summaries


Experience cutting-edge computer vision with our premier image captioning and video summarization algorithms. Tailored for content creators, media professionals, SEO experts, and e-commerce enterprises. Featuring multilingual support and seamless API integration. Elevate your digital presence today.


SceneXplain


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