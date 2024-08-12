ultimate_modified = {
    "name": "AmirMasoud Azadfar",
    "title": "Data Scientist and AI Engineer",
    "city": "Thunder Bay",
    "state/province": "ON",
    "country": "Canada",
    "email": "amirmazadfar@gmail.com",
    "phone": "+1 (343) 988-3995",
    "social_media": [
        {
            "platform": "LinkedIn",
            "handle/url": "https://www.linkedin.com/in/amazadfar"
        },
        {
            "platform": "GitHub",
            "handle/url": "https://github.com/amirmasoudaz"
        }
    ],
    "summary": "Dynamic and results-driven Data Scientist and AI Engineer with over five years of experience in developing innovative data-driven solutions. Proven expertise in building robust data pipelines, creating advanced recommendation systems, and engineering AI-driven chatbots. Adept at utilizing machine learning frameworks and libraries to drive business insights and optimize decision-making processes. Proficient in Python, SQL, and various data science tools, with a strong background in financial modeling, AI automation, and recommendation systems. Recognized for delivering high-quality, scalable solutions in fast-paced environments and demonstrated success in leading complex projects from concept to completion.",
    "skills": [
        {
            "title": "Programming Languages",
            "skills": ["Python", "C/C++", "C#", "SQL", "Cypher", "Bash (Unix Shell)", "HTML/CSS", "JavaScript"]
        },
        {
            "title": "Frameworks & Libraries",
            "skills": ["FastAPI", "Flask", "Django", "MFC", ".NET", "Bootstrap", "Matplotlib", "Seaborn", "Selenium", "BeautifulSoup"]
        },
        {
            "title": "Machine Learning",
            "skills": ["PyTorch", "TensorFlow", "Scikit-Learn", "Hugging Face", "LangChain", "Pandas", "NumPy", "SpaCy", "NLTK"]
        },
        {
            "title": "DevOps & Databases",
            "skills": ["Git", "Docker", "Uvicorn ASGI", "Hetzner", "AWS EC2", "Neo4j", "MongoDB", "MariaDB MySQL", "Redis"],
        },
        {
            "title": "Domains",
            "skills": ["AI Automation", "Recommendation Systems", "Data Engineering", "Financial Modeling", "Retrieval-Augmented Generation (RAG)"]
        }
    ],
    "work": [
        {
            "company": "CanApply",
            "position": "Data Scientist and AI Engineer",
            "duration": "Mar 2023 - Jul 2024",
            "url": {
                "title": "Smart Platform",
                "link": "https://platform.canapply.ca"
            },
            "details": {
                "Web Scraping and NLP-Driven Data Pipeline": "Developed a data pipeline for 223 Canadian universities and colleges, collecting and processing over 13,000 degree programs. Used Selenium, BeautifulSoup, and proxy rotation for web scraping, and Pandas and RegEx for data cleaning. Fine-tuned a SpaCy NLP model for NER and relation extraction, built a Neo4j knowledge graph for knowledge retrieval, and used MariaDB for front-end data storage and retrieval.",
                "Degree Program Recommendation System": "Designed a content-filtering recommendation system to help students find suitable degree programs based on their preferences and academic background. Utilized text embeddings for semantic similarity, achieving nearly 100% accuracy in top-10 recommendations across 11 program categories. Maintained <800ms response time for recommendations and <500ms for filtration and pagination. Deployed using Docker containers on Hetzner VPS, and handled 100+ daily requests using FastAPI and Uvicorn ASGI.",
                "GraphRAG-Enabled Study Abroad AI Assistant": "Engineered 'Dana', an AI chatbot using retrieval-augmented generation (RAG) for personalized study abroad guidance based on real-time educational data. Employed multi-agent architecture and integrated OpenAI's GPT models API. Achieved 1.8-7.2 seconds RAG response latency on Hetzner production servers, handling 1000+ monthly conversations with FastAPI, Uvicorn ASGI, and Pusher WebSocket for real-time chat token streaming.",
                "Admission Chance Approximation Service": "Developed a scoring metric to approximate admission likelihood for Canadian universities, using 14 weighted features based on admission data, university requirements, and student profiles. Implemented a feature to generate an Instagram story image with the admission score, scoring between 300 to 1000, for a marketing campaign.",
                "Data-Driven Analysis and Business Intelligence": "Conducted analyses on the Canadian educational technology market, identifying key segments, growth areas, and potential partnerships. Implemented an ARIMA forecasting model to estimate future trends in international student enrollment, aiding in strategic decision-making for marketing and recruitment.",
            }
        },
        {
            "company": "Sepanta IT Co.",
            "position": "Data Engineer and Software Developer",
            "duration": "Feb 2018 - Nov 2022",
            "details": {
                "Financial Data Pipeline Development": "Developed and updated data pipelines for TSE stocks and cryptocurrencies, collecting and processing technical, fundamental, and news data. Utilized Python, Selenium, Beautiful Soup, Pandas, and MongoDB for data retrieval and preprocessing. Achieved real-time data retrieval with sub-5000ms latency for TSE and sub-500ms latency for 1000+ cryptocurrency pairs using asynchronous API calls and WebSocket streams.",
                "Algorithmic Trading Strategy Development": "Created an option bonds pricing model using the Black-Scholes and Binomial Option Pricing Models. Designed strategies including Mean Reversion, Momentum Trading Strategies, Buyer/Seller Pressure, and Market Microstructure Analysis (Order Book Analysis). Developed a consensus clustering model for sector and industry analysis of stocks based on historical technical and fundamental data using K-Means and DBSCAN algorithms.",
                "NLP Model for TSE Stocks News Sentiment Analysis": "Built a sentiment analysis model for TSE stocks Farsi news and analyst reports. Manually labeled a dataset of over 15,000 Farsi news articles and reports. Used Hazm, a Persian NLP toolkit for sentence and word tokenization and preprocessing and implemented TF-IDF for vectorization. Trained a Multinomial Naive Bayes binary classifier for sentiment analysis and reached a macro average F1 score of 0.85.",
                "Market Analysis and Automatic Reporting Platform": "Designed and deployed a backend API for a Telegram-based platform providing market analysis and automatic reporting for TSE stocks using FastAPI and Uvicorn ASGI on Hetzner Cloud and MongoDB for date warehousing and user profiling, offering proprietary market analysis reports, news sentiment analysis, trading signals, and custom alerts.",
                "Cryptocurrency Triangular Arbitrage System": "Developed a real-time system for identifying triangular arbitrage opportunities on the Binance exchange in Python. Handled and scanned over 1000 trading pairs concurrently through asynchronous design and multithreading, with a latency of under 100ms, deployed on AWS EC2 Asia Pacific (Tokyo) zone for data feed latency reduction."
            }
        }
    ],
    "project": [
        {
            "name": "Automatic Job Hunting AI Assistant",
            "duration": "2024",
            "url": {
                "title": "GitHub",
                "link": "https://github.com/amirmasoudaz/job-hunting-ai-assistant"
            },
            "details": [
                "Developed an automated job hunting software that scrapes and interacts with major job listing sites, extracting job listings based on user preferences on roles and locations. Implemented a scoring system to match job descriptions with user resumes, automating the application process for high-scoring jobs, including resume customization and cover letter generation. Enabled batch processing to handle thousands of job descriptions, powered by OpenAI GPT-4 completions API for efficient decision-making and alignment analysis, streamlining the job hunting process.",
            ],
        },
        {
            "name": "RL-Driven Bidirectional Automatic Trading System",
            "duration": "2023 - Present",
            "url": {
                "title": "GitHub",
                "link": "https://github.com/amirmasoudaz/rl-trading-system"
            },
            "details": [
                "Developing an RL-Driven Bidirectional Auto Trading System using a Deep Q-Network (DQN) to analyze historical and live trading data, technical indicators, and segmentation patterns for optimal trading decisions. Implemented a segmentation module to identify profitable trading zones via pivot points, guiding the DQN agent in making long, short, or hold decisions based on past market behaviors and technical indicators. Included real-time data fetching, order execution, and risk management modules to ensure continuous market updates, execute trades, and minimize losses while optimizing the portfolio.",
            ]
        },
        {
            "name": "GNN-Based Drug Interactions Recommendation System",
            "duration": "2023 - Present",
            "url": {
                "title": "GitHub",
                "link": "https://github.com/amirmasoudaz/drug-interactions-gnn"
            },
            "details": [
                "Developing a Graph Neural Network (GNN) model to predict drug-drug interactions based on chemical structures, side effects, and pharmacological properties. Utilizing a multi-layered graph architecture to represent drug compounds and their interactions, the model aims to provide accurate recommendations for potential drug interactions, contraindications, and adverse effects. Implementing a knowledge graph for drug compounds and their properties, the system will enable healthcare professionals to make informed decisions regarding drug prescriptions and patient safety.",
            ]
        }
    ],
    "education": [
        {
            "degree": "HBSc. in Computer Science",
            "institution": "Lakehead University, Canada",
            "duration": "Sep 2023 - Present"
        }
    ],
    "certificates": [
        {
            "title": "Deep Learning Specialization",
            "institution": "Coursera",
            "date": "2022",
            "url": {
                "title": "Certificate",
                "link": "https://coursera.org/amirmasoudaz/deep-learning"
            }
        }
    ]
}


ultimate = {
    "name": "AmirMasoud Azadfar",
    "title": "Data Scientist and AI Engineer",
    "city": "Thunder Bay",
    "state/province": "ON",
    "country": "Canada",
    "email": "amirmazadfar@gmail.com",
    "phone": "+1 (343) 988-3995",
    "social_media": [
        {
            "platform": "LinkedIn",
            "handle/url": "https://www.linkedin.com/in/amazadfar"
        },
        {
            "platform": "GitHub",
            "handle/url": "https://github.com/amirmasoudaz"
        }
    ],
    "summary": "Dynamic and results-driven Data Scientist and AI Engineer with over five years of experience in developing innovative data-driven solutions. Proven expertise in building robust data pipelines, creating advanced recommendation systems, and engineering AI-driven chatbots. Adept at utilizing machine learning frameworks and libraries to drive business insights and optimize decision-making processes. Proficient in Python, SQL, and various data science tools, with a strong background in financial modeling, AI automation, and recommendation systems. Recognized for delivering high-quality, scalable solutions in fast-paced environments and demonstrated success in leading complex projects from concept to completion.",
    "skills": [
        {
            "title": "Programming Languages",
            "skills": ["Python", "C/C++", "C#", "SQL", "Cypher", "Bash (Unix Shell)", "HTML/CSS", "JavaScript"]
        },
        {
            "title": "Libraries",
            "skills": ["Pandas", "NumPy", "Matplotlib", "Scikit-Learn", "SpaCy", "NLTK", "Selenium", "BeautifulSoup"]
        },
        {
            "title": "Frameworks",
            "skills": ["PyTorch", "TensorFlow", "Hugging Face", "LangChain", "FastAPI", "Flask", "AIOHTTP", "Django", "MFC", ".NET", "Bootstrap"]
        },
        {
            "title": "DevOps & Databases",
            "skills": ["Git", "Docker", "Uvicorn ASGI", "Hetzner", "AWS EC2", "Neo4j", "MongoDB", "MariaDB MySQL", "Redis"],
        },
        {
            "title": "Domains",
            "skills": ["AI Automation", "Recommendation Systems", "Data Engineering", "Financial Modeling", "Retrieval-Augmented Generation (RAG)"]
        }
    ],
    "work": [
        {
            "company": "CanApply",
            "position": "Data Scientist and AI Engineer",
            "duration": "Mar 2023 - Jul 2024",
            "details": {
                "Web Scraping and NLP-Driven Data Pipeline": "Developed a data pipeline for 223 Canadian universities and colleges, collecting and processing over 13,000 degree programs. Used Selenium, BeautifulSoup, and proxy rotation for web scraping, and Pandas and RegEx for data cleaning. Fine-tuned a SpaCy NLP model for NER and relation extraction, built a Neo4j knowledge graph for knowledge retrieval, and used MariaDB for front-end data storage and retrieval.",
                "Degree Program Recommendation System": "Designed a content-filtering recommendation system to help students find suitable degree programs based on their preferences and academic background. Utilized text embeddings for semantic similarity, achieving nearly 100% accuracy in top-10 recommendations across 11 program categories. Maintained <800ms response time for recommendations and <500ms for filtration and pagination. Deployed using Docker containers on Hetzner VPS, and handled 100+ daily requests using FastAPI and Uvicorn ASGI.",
                "GraphRAG-Enabled Study Abroad AI Assistant": "Engineered 'Dana', an AI chatbot using retrieval-augmented generation (RAG) for personalized study abroad guidance based on real-time educational data. Employed multi-agent architecture and integrated OpenAI's GPT models API. Achieved 1.8-7.2 seconds RAG response latency on Hetzner production servers, handling 1000+ monthly conversations with FastAPI, Uvicorn ASGI, and Pusher WebSocket for real-time chat token streaming.",
                "Admission Chance Approximation Service": "Developed a scoring metric to approximate admission likelihood for Canadian universities, using 14 weighted features based on admission data, university requirements, and student profiles. Implemented a feature to generate an Instagram story image with the admission score, scoring between 300 to 1000, for a marketing campaign.",
                "Data-Driven Analysis and Business Intelligence": "Conducted analyses on the Canadian educational technology market, identifying key segments, growth areas, and potential partnerships. Implemented an ARIMA forecasting model to estimate future trends in international student enrollment, aiding in strategic decision-making for marketing and recruitment.",
            }
        },
        {
            "company": "Sepanta IT Co.",
            "position": "Data Engineer and Software Developer",
            "duration": "Feb 2018 - Nov 2022",
            "details": {
                "Financial Data Pipeline Development": "Developed and updated data pipelines for TSE stocks and cryptocurrencies, collecting and processing technical, fundamental, and news data. Utilized Python, Selenium, Beautiful Soup, Pandas, and MongoDB for data retrieval and preprocessing. Achieved real-time data retrieval with sub-5000ms latency for TSE and sub-500ms latency for 1000+ cryptocurrency pairs using asynchronous API calls and WebSocket streams.",
                "Algorithmic Trading Strategy Development": "Created an option bonds pricing model using the Black-Scholes and Binomial Option Pricing Models. Designed strategies including Mean Reversion, Momentum Trading Strategies, Buyer/Seller Pressure, and Market Microstructure Analysis (Order Book Analysis). Developed a consensus clustering model for sector and industry analysis of stocks based on historical technical and fundamental data using K-Means and DBSCAN algorithms.",
                "NLP Model for TSE Stocks News Sentiment Analysis": "Built a sentiment analysis model for TSE stocks Farsi news and analyst reports. Manually labeled a dataset of over 15,000 Farsi news articles and reports. Used Hazm, a Persian NLP toolkit for sentence and word tokenization and preprocessing and implemented TF-IDF for vectorization. Trained a Multinomial Naive Bayes binary classifier for sentiment analysis and reached a macro average F1 score of 0.85.",
                "Market Analysis and Automatic Reporting Platform": "Designed and deployed a backend API for a Telegram-based platform providing market analysis and automatic reporting for TSE stocks using FastAPI and Uvicorn ASGI on Hetzner Cloud and MongoDB for date warehousing and user profiling, offering proprietary market analysis reports, news sentiment analysis, trading signals, and custom alerts.",
                "Cryptocurrency Triangular Arbitrage System": "Developed a real-time system for identifying triangular arbitrage opportunities on the Binance exchange in Python. Handled and scanned over 1000 trading pairs concurrently through asynchronous design and multithreading, with a latency of under 100ms, deployed on AWS EC2 Asia Pacific (Tokyo) zone for data feed latency reduction."
            }
        }
    ],
    "project": [
        {
            "name": "Automatic Job Hunting AI Assistant",
            "duration": "Apr 2024 - Jul 2024",
            "details": [
                "Developed an automated job hunting software that scrapes and interacts with major job listing sites, extracting job listings based on user preferences on roles and locations. Implemented a scoring system to match job descriptions with user resumes, automating the application process for high-scoring jobs, including resume customization and cover letter generation. Enabled batch processing to handle thousands of job descriptions, powered by OpenAI GPT-4 completions API for efficient decision-making and alignment analysis, streamlining the job hunting process.",
            ],
        },
        {
            "name": "RL-Driven Bidirectional Automatic Trading System",
            "duration": "Mar 2024 - Present",
            "details": [
                "Developing an RL-Driven Bidirectional Auto Trading System using a Deep Q-Network (DQN) to analyze historical and live trading data, technical indicators, and segmentation patterns for optimal trading decisions. Implemented a segmentation module to identify profitable trading zones via pivot points, guiding the DQN agent in making long, short, or hold decisions based on past market behaviors and technical indicators. Included real-time data fetching, order execution, and risk management modules to ensure continuous market updates, execute trades, and minimize losses while optimizing the portfolio.",
            ]
        }
    ],
    "education": [
        {
            "degree": "HBSc. in Computer Science",
            "institution": "Lakehead University, Canada",
            "duration": "Sep 2023 - Present"
        }
    ]
}


sample_resume = {
    "name": "AmirMasoud Azadfar",
    "expertise": "Data Scientist and AI Engineer",
    "city": "Thunder Bay",
    "state/province": "ON",
    "country": "Canada",
    "email": "amirmazadfar@gmail.com",
    "phone": "+1 (343) 988-3995",
    "social_media": [
        {
            "platform": "LinkedIn",
            "handle/url": "https://www.linkedin.com/in/amazadfar"
        },
        {
            "platform": "GitHub",
            "handle/url": "https://github.com/amirmasoudaz"
        }
    ],
    "summary": "Dynamic and innovative Lead Data Scientist and Machine Learning Engineer with extensive experience in Python development, specializing in application of AI in automation and data-driven technologies. Adept in crafting advanced solutions in NLP and LLMs, I excel at developing robust data pipelines and AI-driven applications. Led the design and implementation of scalable API infrastructures and multifunctional AI systems, significantly enhancing data processing, system personalization, and decision-making capabilities. My expertise extends to creating high-performance web crawlers and recommendation engines, integrating cutting-edge machine learning techniques to deliver precise, user-specific outcomes. Committed to continuous professional development, I am eager to apply my skills in new and challenging contexts to drive technological innovation and business success.",
    "skills": {

        "Programming & Languages": ["Python", "C/C++", "C#", "BASIC", "Visual Basic", "SQL", "Cypher", "Bash", "JavaScript", "HTML/CSS", "PineScript"],
        "Frameworks & Libraries": ["Pandas", "NumPy", "PyTorch", "Scikit-Learn", "Hugging Face", "SpaCy", "LangChain", "FastAPI", "Flask"],
        "Machine Learning": ["NLP (Topic Modeling/NER/Clustering)", "LLMs (Fine-Tuning/RAG/GraphRAG)", "Time-Series Analysis (Supervised Learning/Deep Learning)"],
        "DevOps & Databases": ["Git", "Docker", "Uvicorn", "Neo4j", "MariaDB", "MongoDB", "S3", "Linux", "Hetzner", "AWS"],
        "Domains": ["AI Automation", "Recommendation Systems", "Data Engineering", "Web Scraping", "Financial Modeling"],
    },
    "work_experience": [
        {
            "company": "CanApply",
            "position": "Data Scientist and AI Engineer",
            "duration": "Mar 2023 - Jul 2024",
            "details": [
                "**NLP-Driven Web Crawler**: Developed a fully automatic, asynchronous recursive web scraping engine to collect and organize the data of **220+ universities** and their **13000+ programs** across Canada. Utilized **Selenium** for scrapping and the Knowledge Extraction Engine for content validation. Implemented a **hierarchical indexing system** for efficient data storage and retrieval on **AWS S3**. Rebuilt a replica of the uniform data in a **MySQL database**. Constructed a **Neo4j-Based Knowledge Graph** for research purposes.",
                "**Central Knowledge Extraction Engine**: Developed an automatic **knowledge clustering** and **relation matching** engine by integrating **SpaCy**, **BERT**, **text embeddings**, and **RegEx** for **rule-based NER**, **TF-IDF** and **LDA** for thematic clustering to build a **revolutionary data classification algorithm**.",
                "**Multifunctional Recommendation Engine**: Created a recommendation system, serving both as a **search engine** and a **degree program recommender**. Utilized **transformer-based text embeddings** and **vector similarity** to analyze user profiles and preferences, along with AI Assistant's search queries, delivering personalized program suggestions and accurate search results with **low latency** and **pagination**.",
                "**Dana, a GraphRAG-enabled AI Assistant**: Utilized **GPT-4o** within a **multi-layered query processing architecture** and a **retrieval-augmented generation model** by querying the recommendation engine to deliver real-time, data-driven responses based on conversation context for study abroad consultation.",
                "**Admission Chance Service**: Developed a predictive tool that assesses the likelihood of admission to specific degree programs at Canadian universities. Used **historical data** and **university requirements** to achieve 90% accuracy through **data analysis** and **feature engineering**.",
                "**Asynchronous API Infrastructure**: Designed a **scalable API infrastructure** using **FastAPI** and **Uvicorn ASGI** to manage and route requests across various AI product backend services. Integrated **WebSocket technology** to enable real-time interactions by streaming response tokens to the UI."
            ]
        },
        {
            "company": "Sepanta IT Co.",
            "position": "Data Analyst",
            "duration": "Feb 2018 - Nov 2022",
            "details": [
                "**Data Retrieval Pipeline**: Collaborated in building an asynchronous and comprehensive data retrieval system to collect and organize real-time financial data from various sources, including **Tehran Securities Exchange** and **Binance Exchange**, using **Python**. Utilized **BS4**, **Pandas**, **RegEx** for data extraction and manipulation and **SQLAlchemy** for database management.",
                "**Real-Time Option Bonds Trading Engine**: Developed a **trading engine** that **estimates the real value of option bonds** based on real-time financial data and executes buy or sell positions in the opposite direction on the **Tehran Securities Exchange**. Created a **risk management strategy** to automatically close and sell bonds when risk levels surpass a calculated threshold.",
                "**Automatic Triangular Arbitrage Hunter**: Programmed a system for **real-time detection** and **execution** of **triangular arbitrage opportunities** on **Binance exchange**. Utilizing **asynchronous API calls and threaded WebSocket streams**, the system **scans 600+ trading pairs**, triggers a **chain trading mechanism** when profitability exceeds fees and automatically executes trades.",
                "**Financial Data Analysis**: Developed multiple market analysis algorithms such as **Market Trend Identification** and **Hot Asset Detection** in Python and PineScript to get automatic market insights to recommend clients and traders with **profitable trading strategies**.",
                "**C++ Instruction**: Taught **C++ programming language** to a group of colleagues, focusing on **data structures**, **algorithms**, and **object-oriented programming** concepts as a volunteer instructor.",
            ]
        }
    ],
    "projects": [
        {
            "title": "AI Job Hunting Assistant",
            "duration": "Apr 2024 - Present",
            "details": "**'SmartHunt'** revolutionizes **job searching** by **automating the discovery, analysis, and application processes**. This platform scans job sites like **Glassdoor**, **Indeed**, and **LinkedIn**, offering **personalized recommendations** and automatically **tailoring CVs and cover letters**. With features like **compatibility analysis** and **application tracking**, SmartHunt **transforms a typically lengthy job search into a swift, efficient experience**, significantly enhancing users' chances of securing desired positions quickly."
        },
        {
            "title": "Bidirectional Auto Quant Trading System",
            "duration": "Mar 2022 - Present",
            "details": "Developed **'Infinity'**, a sophisticated ML-driven trading engine that leverages novel strategies for **market trend identification** and **risk adjustment**. Utilizing **GridSearch** and a **Random Forest** model, the system optimizes parameters and **enhances decision accuracy** based on real-time Binance Exchange market data. A robust **API requestor suite** supports seamless data retrieval and automated order execution, ensuring **high operational efficiency**. Through extensive backtesting and adaptive strategy tuning, Infinity has **demonstrated profitability and effective risk management**, significantly enhancing trading performance.",
        }
    ],
    "education": [
        {
            "degree": "HBSc. in Computer Science",
            "institution": "Lakehead University, Canada",
            "duration": "Sep 2023 - Present"
        }
    ]
}

sample_old = {
    "name": "AmirMasoud Azadfar",
    "city": "Thunder Bay",
    "state/province": "ON",
    "country": "Canada",
    "email": "amirmazadfar@gmail.com",
    "phone": "+1 (343) 988-3995",
    "social_media": [
        {
            "platform": "LinkedIn",
            "handle/url": "https://www.linkedin.com/in/amazadfar"
        },
        {
            "platform": "GitHub",
            "handle/url": "https://github.com/amirmasoudaz"
        }
    ],
    "professional_summary": "Dynamic and innovative Lead Data Scientist and Machine Learning Engineer with extensive experience in Python development, specializing in application of AI in automation and data-driven technologies. Adept in crafting advanced solutions in NLP and LLMs, I excel at developing robust data pipelines and AI-driven applications. Led the design and implementation of scalable API infrastructures and multifunctional AI systems, significantly enhancing data processing, system personalization, and decision-making capabilities. My expertise extends to creating high-performance web crawlers and recommendation engines, integrating cutting-edge machine learning techniques to deliver precise, user-specific outcomes. Committed to continuous professional development, I am eager to apply my skills in new and challenging contexts to drive technological innovation and business success.",
    "skills": {
        "Programming Languages": ["Python", "C++", "C#", "JavaScript", "HTML", "CSS", "PineScript"],
        "Frameworks & Libraries": ["FastAPI", ".NET", "MFC", "Flask", "Django", "Node.js", "React", "Bootstrap"],
        "Machine Learning": ["NLP", "Recommendation Systems", "LLMs", "Transformers", "GPT", "SpaCy", "BERT", "TensorFlow", "Scikit-Learn"],
        "Databases & DevOps": ["GitHub", "MySQL", "Neo4j", "S3", "Redis", "MongoDB", "Linux", "AWS", "Hetzner", "Uvicorn"],
        "Languages": ["Persian (Native)", "English (Bilingual)", "German (B1)", "Armenian (A1)"]
    },
    "work_experience": [
        {
            "company": "CanApply Inc.",
            "position": "Lead Data Scientist",
            "type": "Remote",
            "duration": "Mar 2023 - Present",
            "details": [
                "**NLP-Driven Web Crawler**: Developed a fully automatic, asynchronous recursive web scraping engine to collect and organize the data of **220+ universities** and their **13000+ programs** across Canada. Utilized **Selenium** for scrapping and the Knowledge Extraction Engine for content validation. Implemented a **hierarchical indexing system** for efficient data storage and retrieval on **AWS S3**. Rebuilt a replica of the uniform data in a **MySQL database**. Constructed a **Neo4j-Based Knowledge Graph** for research purposes.",
                "**Central Knowledge Extraction Engine**: Developed an automatic **knowledge clustering** and **relation matching** engine by integrating **SpaCy**, **BERT**, **text embeddings**, and **RegEx** for **rule-based NER**, **TF-IDF** and **LDA** for thematic clustering to build a **revolutionary data classification algorithm**.",
                "**Multifunctional Recommendation Engine**: Created a recommendation system, serving both as a **search engine** and a **degree program recommender**. Utilized **transformer-based text embeddings** and **vector similarity** to analyze user profiles and preferences, along with AI Assistant's search queries, delivering personalized program suggestions and accurate search results with **low latency** and **pagination**.",
                "**Dana, a RAG-enabled AI Assistant**: Utilized **GPT-4** within a **multi-layered query processing architecture** and a **retrieval-augmented generation model** by querying the recommendation engine to deliver real-time, data-driven responses based on conversation context for study abroad consultation.",
                "**Admission Chance Service**: Developed a predictive tool that assesses the likelihood of admission to specific degree programs at Canadian universities. Used **historical data** and **university requirements** to achieve 90% accuracy through **data analysis** and **feature engineering**.",
                "**Asynchronous API Infrastructure**: Designed a **scalable API infrastructure** using **FastAPI** and **Uvicorn ASGI** to manage and route requests across various AI product backend services. Integrated **WebSocket technology** to enable real-time interactions by streaming response tokens to the UI."
            ]
        },
        {
            "company": "Sepanta IT Co.",
            "position": "Data Analyst and Python Developer",
            "type": "Full-Time",
            "duration": "Dec 2017 - Jan 2023",
            "details": [
                "**Data Retrieval Pipeline**: Collaborated in building an asynchronous and comprehensive data retrieval system to collect and organize real-time financial data from various sources, including **Tehran Securities Exchange** and **Binance Exchange**, using **Python**. Utilized **BS4**, **Pandas**, **RegEx** for data extraction and manipulation and **SQLAlchemy** for database management.",
                "**Real-Time Option Bonds Trading Engine**: Developed a **trading engine** that **estimates the real value of option bonds** based on real-time financial data and executes buy or sell positions in the opposite direction on the **Tehran Securities Exchange**. Created a **risk management strategy** to automatically close and sell bonds when risk levels surpass a calculated threshold.",
                "**Automatic Triangular Arbitrage Hunter**: Programmed a system for **real-time detection** and **execution** of **triangular arbitrage opportunities** on **Binance exchange**. Utilizing **asynchronous API calls and threaded WebSocket streams**, the system **scans 600+ trading pairs**, triggers a **chain trading mechanism** when profitability exceeds fees and automatically executes trades.",
                "**Financial Data Analysis**: Developed multiple market analysis algorithms such as **Market Trend Identification** and **Hot Asset Detection** in Python and PineScript to get automatic market insights to recommend clients and traders with **profitable trading strategies**.",
                "**Market Alerts Robot**: Created an asynchronous backend infrastructure for a Telegram bot to automatically provide 1000+ subscribers with **real-time financial data** and **market insights** based on the outputs of our market analysis indicators. Leveraged **Telegram API** and **Django** to manage requests and real-time data updates, and **Celery** for scheduled alerts.",
                "**C++ Instruction**: Taught **C++ programming language** to a group of colleagues, focusing on **data structures**, **algorithms**, and **object-oriented programming** concepts as a volunteer instructor.",
            ]
        }
    ],
    "projects": [
        {
            "title": "SmartHunt - AI-Driven Automatic Job Search Platform",
            "duration": "Apr 2024 - Present",
            "details": "**'SmartHunt'** revolutionizes **job searching** by **automating the discovery, analysis, and application processes**. This platform scans job sites like **Glassdoor**, **Indeed**, and **LinkedIn**, offering **personalized recommendations** and automatically **tailoring CVs and cover letters**. With features like **compatibility analysis** and **application tracking**, SmartHunt **transforms a typically lengthy job search into a swift, efficient experience**, significantly enhancing users' chances of securing desired positions quickly."
        },
        {
            "title": "Infinity - ML-Driven Automatic Trading Engine",
            "duration": "Mar 2022 - Present",
            "details": "Developed **'Infinity'**, a sophisticated ML-driven trading engine that leverages novel strategies for **market trend identification** and **risk adjustment**. Utilizing **GridSearch** and a **Random Forest** model, the system optimizes parameters and **enhances decision accuracy** based on real-time Binance Exchange market data. A robust **API requestor suite** supports seamless data retrieval and automated order execution, ensuring **high operational efficiency**. Through extensive backtesting and adaptive strategy tuning, Infinity has **demonstrated profitability and effective risk management**, significantly enhancing trading performance.",
        }
    ],
    "education": [
        {
            "degree": "HBSc. in Computer Science",
            "institution": "Lakehead University, Canada",
            "duration": "Sep 2023 - Present"
        }
    ]
}

resume_sepanta_incl = {
    "name": "AmirMasoud Azadfar",
    "city": "Thunder Bay",
    "state/province": "ON",
    "country": "Canada",
    "email": "amirmazadfar@gmail.com",
    "phone": "+1 (343) 988-3995",
    "social_media": [
        {
            "platform": "LinkedIn",
            "handle/url": "https://www.linkedin.com/in/amazadfar/"
        },
        {
            "platform": "GitHub",
            "handle/url": "https://github.com/amirmasoudaz"
        }
    ],
    "professional_summary": "Dynamic and innovative Lead Data Scientist and Machine Learning Engineer with extensive experience in Python development, specializing in application of AI in automation and data-driven technologies. Adept in crafting advanced solutions in NLP and LLMs, I excel at developing robust data pipelines and AI-driven applications. Led the design and implementation of scalable API infrastructures and multifunctional AI systems, significantly enhancing data processing, system personalization, and decision-making capabilities. My expertise extends to creating high-performance web crawlers and recommendation engines, integrating cutting-edge machine learning techniques to deliver precise, user-specific outcomes. Committed to continuous professional development, I am eager to apply my skills in new and challenging contexts to drive technological innovation and business success.",
    "skills": {
        "Programming Languages": ["Python", "C++", "C#", "JavaScript", "HTML", "CSS", "PineScript"],
        "Frameworks & Libraries": ["FastAPI", ".NET", "MFC", "Flask", "Django", "Node.js", "React", "Bootstrap"],
        "Machine Learning": ["NLP", "Recommendation Systems", "LLMs", "Transformers", "GPT", "SpaCy", "BERT", "TensorFlow", "Scikit-Learn"],
        "Databases & DevOps": ["GitHub", "MySQL", "Neo4j", "S3", "Redis", "MongoDB", "Linux", "AWS", "Hetzner", "Uvicorn"],
        "Languages": ["Persian (Native)", "English (Bilingual)", "German (B1)", "Armenian (A1)"]
    },
    "work_experience": [
        {
            "company": "CanApply Inc.",
            "position": "Lead Data Scientist and ML Engineer",
            "type": "Remote",
            "duration": "Mar 2023 - Present",
            "details": [
                "**NLP-Driven Web Crawler**: Developed a fully automatic, asynchronous recursive web scraping engine to collect and organize the data of **220+ universities** and their **13000+ programs** across Canada. Utilized **Selenium** for scrapping and the Knowledge Extraction Engine for content validation. Implemented a **hierarchical indexing system** for efficient data storage and retrieval on **AWS S3**. Rebuilt a replica of the uniform data in a **MySQL database**. Constructed a **Neo4j-Based Knowledge Graph** for research purposes.",
                "**Central Knowledge Extraction Engine**: Developed an automatic **knowledge clustering** and **relation matching** engine by integrating **SpaCy**, **BERT**, **text embeddings**, and **RegEx** for **rule-based NER**, **TF-IDF** and **LDA** for thematic clustering to build a **revolutionary data classification algorithm**.",
                "**Multifunctional Recommendation Engine**: Created a recommendation system, serving both as a **search engine** and a **degree program recommender**. Utilized **transformer-based text embeddings** and **vector similarity** to analyze user profiles and preferences, along with AI Assistant's search queries, delivering personalized program suggestions and accurate search results with **low latency** and **pagination**.",
                "**Dana, a RAG-enabled AI Assistant**: Utilized **GPT-4** within a **multi-layered query processing architecture** and a **retrieval-augmented generation model** by querying the recommendation engine to deliver real-time, data-driven responses based on conversation context for study abroad consultation.",
                "**Admission Chance Service**: Developed a predictive tool that assesses the likelihood of admission to specific degree programs at Canadian universities. Used **historical data** and **university requirements** to achieve 90% accuracy through **data analysis** and **feature engineering**.",
                "**Asynchronous API Infrastructure**: Designed a **scalable API infrastructure** using **FastAPI** and **Uvicorn ASGI** to manage and route requests across various AI product backend services. Integrated **WebSocket technology** to enable real-time interactions by streaming response tokens to the UI."
            ]
        },
        {
            "company": "Sepanta IT Co.",
            "position": "Data Analyst and Python Developer",
            "type": "Full-Time",
            "duration": "Dec 2017 - Jan 2023",
            "details": [
                "**Data Retrieval Pipeline**: Collaborated in building an asynchronous and comprehensive data retrieval system to collect and organize real-time financial data from various sources, including **Tehran Securities Exchange** and **Binance Exchange**, using **Python**. Utilized **BS4**, **Pandas**, **RegEx** for data extraction and manipulation and **SQLAlchemy** for database management.",
                "**Real-Time Option Bonds Trading Engine**: Developed a **trading engine** that **estimates the real value of option bonds** based on real-time financial data and executes buy or sell positions in the opposite direction on the **Tehran Securities Exchange**. Created a **risk management strategy** to automatically close and sell bonds when risk levels surpass a calculated threshold.",
                "**Automatic Triangular Arbitrage Hunter**: Programmed a system for **real-time detection** and **execution** of **triangular arbitrage opportunities** on **Binance exchange**. Utilizing **asynchronous API calls and threaded WebSocket streams**, the system **scans 600+ trading pairs**, triggers a **chain trading mechanism** when profitability exceeds fees and automatically executes trades.",
                "**Financial Data Analysis**: Developed multiple market analysis algorithms such as **Market Trend Identification** and **Hot Asset Detection** in Python and PineScript to get automatic market insights to recommend clients and traders with **profitable trading strategies**.",
                "**Market Alerts Robot**: Created an asynchronous backend infrastructure for a Telegram bot to automatically provide 1000+ subscribers with **real-time financial data** and **market insights** based on the outputs of our market analysis indicators. Leveraged **Telegram API** and **Django** to manage requests and real-time data updates, and **Celery** for scheduled alerts.",
                "**C++ Instruction**: Taught **C++ programming language** to a group of colleagues, focusing on **data structures**, **algorithms**, and **object-oriented programming** concepts as a volunteer instructor.",
            ]
        }
    ],
    "projects": [
        {
            "title": "SmartHunt - AI-Driven Automatic Job Search Platform",
            "duration": "Apr 2024 - Present",
            "details": "**'SmartHunt'** revolutionizes **job searching** by **automating the discovery, analysis, and application processes**. This platform scans job sites like **Glassdoor**, **Indeed**, and **LinkedIn**, offering **personalized recommendations** and automatically **tailoring CVs and cover letters**. With features like **compatibility analysis** and **application tracking**, SmartHunt **transforms a typically lengthy job search into a swift, efficient experience**, significantly enhancing users' chances of securing desired positions quickly."
        },
        {
            "title": "Infinity - ML-Driven Automatic Trading Engine",
            "duration": "Mar 2022 - Present",
            "details": "Developed **'Infinity'**, a sophisticated ML-driven trading engine that leverages novel strategies for **market trend identification** and **risk adjustment**. Utilizing **GridSearch** and a **Random Forest** model, the system optimizes parameters and **enhances decision accuracy** based on real-time Binance Exchange market data. A robust **API requestor suite** supports seamless data retrieval and automated order execution, ensuring **high operational efficiency**. Through extensive backtesting and adaptive strategy tuning, Infinity has **demonstrated profitability and effective risk management**, significantly enhancing trading performance.",
        }
    ],
    "education": [
        {
            "degree": "HBSc. in Computer Science",
            "institution": "Lakehead University, Canada",
            "duration": "Sep 2023 - Present"
        }
    ]
}


resume_act = {
    "name": "AmirMasoud Azadfar",
    "city": "Thunder Bay",
    "state/province": "ON",
    "country": "Canada",
    "email": "amirmazadfar@gmail.com",
    "phone": "+1 (343) 988-3995",
    "social_media": [
        {
            "platform": "LinkedIn",
            "handle/url": "https://www.linkedin.com/in/amazadfar/"
        },
        {
            "platform": "GitHub",
            "handle/url": "https://github.com/amirmasoudaz"
        }
    ],
    "professional_summary": "Dynamic and innovative Lead Data Scientist and Machine Learning Engineer with extensive experience in Python development, specializing in application of AI in automation and data-driven technologies. Adept in crafting advanced solutions in NLP and LLMs, I excel at developing robust data pipelines and AI-driven applications. Led the design and implementation of scalable API infrastructures and multifunctional AI systems, significantly enhancing data processing, system personalization, and decision-making capabilities. My expertise extends to creating high-performance web crawlers and recommendation engines, integrating cutting-edge machine learning techniques to deliver precise, user-specific outcomes. Committed to continuous professional development, I am eager to apply my skills in new and challenging contexts to drive technological innovation and business success.",
    "skills": {
        "Programming Languages": ["Python", "C++", "C#", "JavaScript", "HTML", "CSS", "PineScript"],
        "Frameworks & Libraries": ["FastAPI", ".NET", "MFC", "Flask", "Django", "Node.js", "React", "Bootstrap"],
        "Machine Learning": ["NLP", "Recommendation Systems", "LLMs", "Transformers", "GPT", "SpaCy", "BERT", "TensorFlow", "Scikit-Learn"],
        "Databases & DevOps": ["GitHub", "MySQL", "Neo4j", "S3", "Redis", "MongoDB", "Linux", "AWS", "Hetzner", "Uvicorn"],
        "Languages": ["Persian (Native)", "English (Bilingual)", "German (B1)", "Armenian (A1)"]
    },
    "work_experience": [
        {
            "company": "CanApply Inc.",
            "position": "Lead Data Scientist and ML Engineer",
            "type": "Remote",
            "duration": "Mar 2023 - Present",
            "details": [
                "**Automatic Web Scrapping Engines**: Programmed multiple crawler engines using **Selenium Chromedriver** to collect the data of **220+ universities** and their **15000+ program**s across Canada. Implemented data preprocessing and standardization using a **fine-tuned SpaCy model**, **regular expressions (RegEx)**, and **rule-based entity extraction algorithms**. Stored the uniform data in a centralized **MariaDB MySQL server database**.",
                "**Multifunctional Recommendation Engine**: Created a recommendation system, serving both as a **search engine** and a **degree program recommender**. Utilized **transformer-based text embeddings** and **vector similarity** to analyze user profiles and preferences, along with AI Assistant's search queries, delivering personalized program suggestions and accurate search results with **low latency** and **pagination**.",
                "**Dana, a RAG-enabled AI Assistant**: Utilized **GPT-4** within a **multi-layered query processing architecture** and a **retrieval-augmented generation model** by querying the recommendation engine to deliver real-time, data-driven responses based on conversation context for study abroad consultation.",
                "**Admission Chance Service**: Developed a predictive tool that assesses the likelihood of admission to specific degree programs at Canadian universities. Used **historical data** and **university requirements** to achieve 90% accuracy through **data analysis** and **feature engineering**.",
                "**Asynchronous API Infrastructure**: Designed a scalable API infrastructure using **FastAPI** on **Uvicorn ASGI** to manage and route requests across various AI product backend services. Integrated **WebSocket technology** to enable real-time interactions by streaming response tokens to the UI.",
                "**CanSpider, an ML-Driven Web Scraping Engine**: Developed an automatic, asynchronous recursive web scraping engine to digitally replicate partner institutions' websites. Utilized **Selenium Chromedriver**, **text embeddings**, and a **dynamic URL and context validation algorithm**. Implemented a **hierarchical data indexing system** for efficient data storage and retrieval on **AWS S3**.",
                "**NLP-Based Knowledge Extraction Engine**: Fine-tuned a **SpaCy model** to create a knowledge extraction engine. Employed **TF-IDF** and **LDA** for thematic clustering, **named entity recognition (NER)**, and context relation extraction, foundational for a knowledge graph.",
                "**Neo4j-Based Knowledge Graph**: Developed an automatic relation matching engine integrating **text embeddings** and **ML-driven Cypher query optimizations**, serving as a central knowledge hub to enhance personalized recommendations and search functionalities."
            ]
        },
    ],
    "projects": [
        {
            "title": "SmartHunt - AI-Driven Automatic Job Search Platform",
            "duration": "Apr 2024 - Present",
            "details": "**'SmartHunt'** revolutionizes **job searching** by **automating the discovery, analysis, and application processes**. This platform scans job sites like **Glassdoor**, **Indeed**, and **LinkedIn**, offering **personalized recommendations** and automatically **tailoring CVs and cover letters**. With features like **compatibility analysis** and **application tracking**, SmartHunt **transforms a typically lengthy job search into a swift, efficient experience**, significantly enhancing users' chances of securing desired positions quickly."
        },
        {
            "title": "Infinity - ML-Driven Automatic Trading Engine",
            "duration": "Mar 2022 - Present",
            "details": "Developed **'Infinity'**, a sophisticated ML-driven trading engine that leverages novel strategies for **market trend identification** and **risk adjustment**. Utilizing **GridSearch** and a **Random Forest** model, the system optimizes parameters and **enhances decision accuracy** based on real-time Binance Exchange market data. A robust **API requestor suite** supports seamless data retrieval and automated order execution, ensuring **high operational efficiency**. Through extensive backtesting and adaptive strategy tuning, Infinity has **demonstrated profitability and effective risk management**, significantly enhancing trading performance.",
        },
        {
            "title": "TriArbit - Automatic Triangular Arbitrage Hunter",
            "duration": "2021 - 2022",
            "details": "Developed **'TriArbit'**, a Python-based system for **real-time detection** and **execution** of **triangular arbitrage opportunities** on the Binance exchange. Utilizing **asynchronous data retrieval**, the system **scans over 600 trading pairs**, automates trades when profitability exceeds fees, and **incorporates risk management** features to ensure safe and efficient operations.",
        }
    ],
    "education": [
        {
            "degree": "HBSc. in Computer Science",
            "institution": "Lakehead University, Canada",
            "duration": "Sep 2023 - Present"
        },
        {
            "degree": "BSc. in Genetics",
            "institution": "University of Kerman, Iran",
            "duration": "2018 - 2021"
        }
    ]
}


resume_comprehensive_act = {
    "name": "AmirMasoud Azadfar",
    "city": "Thunder Bay",
    "state/province": "ON",
    "country": "Canada",
    "email": "amirmazadfar@gmail.com",
    "phone": "+1 (343) 988-3995",
    "social_media": [
        {
            "platform": "LinkedIn",
            "handle/url": "https://www.linkedin.com/in/amazadfar/"
        },
        {
            "platform": "GitHub",
            "handle/url": "https://github.com/amirmasoudaz"
        }
    ],
    "professional_summary": "Dynamic and innovative Lead Data Scientist and Machine Learning Engineer with extensive experience in Python development, specializing in application of AI in automation and data-driven technologies. Adept in crafting advanced solutions in NLP and LLMs, I excel at developing robust data pipelines and AI-driven applications. Led the design and implementation of scalable API infrastructures and multifunctional AI systems, significantly enhancing data processing, system personalization, and decision-making capabilities. My expertise extends to creating high-performance web crawlers and recommendation engines, integrating cutting-edge machine learning techniques to deliver precise, user-specific outcomes. Committed to continuous professional development, I am eager to apply my skills in new and challenging contexts to drive technological innovation and business success.",
    "skills": {
        "Programming Languages": ["Python", "C++", "C#", "JavaScript", "HTML", "CSS", "PineScript"],
        "Frameworks & Libraries": ["FastAPI", ".NET", "MFC", "Flask", "Django", "Node.js", "React", "Bootstrap"],
        "Machine Learning": ["NLP", "Recommendation Systems", "LLMs", "Transformers", "GPT", "SpaCy", "BERT", "TensorFlow", "Scikit-Learn"],
        "Databases & DevOps": ["GitHub", "MySQL", "Neo4j", "S3", "Redis", "MongoDB", "Linux", "AWS", "Hetzner", "Uvicorn"],
        "Languages": ["Persian (Native)", "English (Bilingual)", "German (B1)", "Armenian (A1)"]
    },
    "work_experience": [
        {
            "company": "CanApply Inc.",
            "position": "Lead Data Scientist and ML Engineer",
            "type": "Remote",
            "duration": "Mar 2023 - Present",
            "details": [
                "**Automatic Web Scrapping Engines**: Programmed multiple crawler engines using **Selenium Chromedriver** to collect the data of **220+ universities** and their **15000+ program**s across Canada. Implemented data preprocessing and standardization using a **fine-tuned SpaCy model**, **regular expressions (RegEx)**, and **rule-based entity extraction algorithms**. Stored the uniform data in a centralized **MariaDB MySQL server database**.",
                "**Multifunctional Recommendation Engine**: Created a recommendation system, serving both as a **search engine** and a **degree program recommender**. Utilized **transformer-based text embeddings** and **vector similarity** to analyze user profiles and preferences, along with AI Assistant's search queries, delivering personalized program suggestions and accurate search results with **low latency** and **pagination**.",
                "**Dana, a RAG-enabled AI Assistant**: Utilized **GPT-4** within a **multi-layered query processing architecture** and a **retrieval-augmented generation model** by querying the recommendation engine to deliver real-time, data-driven responses based on conversation context for study abroad consultation.",
                "**Admission Chance Service**: Developed a predictive tool that assesses the likelihood of admission to specific degree programs at Canadian universities. Used **historical data** and **university requirements** to achieve 90% accuracy through **data analysis** and **feature engineering**.",
                "**Asynchronous API Infrastructure**: Designed a scalable API infrastructure using **FastAPI** on **Uvicorn ASGI** to manage and route requests across various AI product backend services. Integrated **WebSocket technology** to enable real-time interactions by streaming response tokens to the UI.",
                "**CanSpider, an ML-Driven Web Scraping Engine**: Developed an automatic, asynchronous recursive web scraping engine to digitally replicate partner institutions' websites. Utilized **Selenium Chromedriver**, **text embeddings**, and a **dynamic URL and context validation algorithm**. Implemented a **hierarchical data indexing system** for efficient data storage and retrieval on **AWS S3**.",
                "**NLP-Based Knowledge Extraction Engine**: Fine-tuned a **SpaCy model** to create a knowledge extraction engine. Employed **TF-IDF** and **LDA** for thematic clustering, **named entity recognition (NER)**, and context relation extraction, foundational for a knowledge graph.",
                "**Neo4j-Based Knowledge Graph**: Developed an automatic relation matching engine integrating **text embeddings** and **ML-driven Cypher query optimizations**, serving as a central knowledge hub to enhance personalized recommendations and search functionalities."
            ]
        },
    ],
    "projects": [
        {
            "title": "SmartHunt - AI-Driven Automatic Job Search Platform",
            "duration": "Apr 2024 - Present",
            "details": "**'SmartHunt'** revolutionizes **job searching** by **automating the discovery, analysis, and application processes**. This platform scans job sites like **Glassdoor**, **Indeed**, and **LinkedIn**, offering **personalized recommendations** and automatically **tailoring CVs and cover letters**. With features like **compatibility analysis** and **application tracking**, SmartHunt **transforms a typically lengthy job search into a swift, efficient experience**, significantly enhancing users' chances of securing desired positions quickly."
        },
        {
            "title": "Infinity - ML-Driven Automatic Trading Engine",
            "duration": "Mar 2022 - Present",
            "details": "Developed **'Infinity'**, a sophisticated ML-driven trading engine that leverages novel strategies for **market trend identification** and **risk adjustment**. Utilizing **GridSearch** and a **Random Forest** model, the system optimizes parameters and **enhances decision accuracy** based on real-time Binance Exchange market data. A robust **API requestor suite** supports seamless data retrieval and automated order execution, ensuring **high operational efficiency**. Through extensive backtesting and adaptive strategy tuning, Infinity has **demonstrated profitability and effective risk management**, significantly enhancing trading performance.",
        },
        {
            "title": "TriArbit - Automatic Triangular Arbitrage Hunter",
            "duration": "2021 - 2022",
            "details": "Developed **'TriArbit'**, a Python-based system for **real-time detection** and **execution** of **triangular arbitrage opportunities** on the Binance exchange. Utilizing **asynchronous data retrieval**, the system **scans over 600 trading pairs**, automates trades when profitability exceeds fees, and **incorporates risk management** features to ensure safe and efficient operations.",
        },
        {
            "title": "Real-Time Option Bonds Trading Robot",
            "duration": "2020 - 2021",
            "details": "As **Team Leader and Programmer**, contributed to the development of a **trading robot** that **evaluates the value of option bonds** and executes positions in the opposite direction on the **Tehran Securities Exchange**. The system, developed in **Python**, utilizes **advanced risk management strategies** to close and sell positions when risk levels hit a pre-set threshold, ensuring **efficient and secure trading operations**."
        },
        {
            "title": "Smart Gardener Robot",
            "duration": "2011 - 2012",
            "details": "Programmed a **'Smart Gardener Robot'** to compete in the **Robotics Competition of Sharif Technology University**. Developed in **C++** with **MFC**, the software utilizes **machine vision algorithms** to detect paths, barcodes, and colors in real-time images, directing the robot to water plants accurately. The project **achieved 4th place** at the **Sharif Cup 2012**."
        }
    ],
    "education": [
        {
            "degree": "HBSc. in Computer Science",
            "institution": "Lakehead University, Canada",
            "duration": "Sep 2023 - Present"
        },
        {
            "degree": "BSc. in Genetics",
            "institution": "University of Kerman, Iran",
            "duration": "2018 - 2021"
        }
    ]
}