sample = {
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
            "url": "https://www.linkedin.com/in/amazadfar"
        },
        {
            "platform": "GitHub",
            "url": "https://github.com/amirmasoudaz"
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
            "url": {
                "title": "",
                "link": ""
            },
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
        },
        {
            "name": "Smart Gardener Robot",
            "duration": "2012",
            "url": {
                "title": "",
                "link": ""
            },
            "details": [
                "Developed machine vision and decision-making software for an autonomous gardening robot in Sharif University of Technology's Robotic Competition. Implemented real-time image processing in C++ for tasks like line following, obstacle avoidance, and water level detection. Built a control system GUI using the MFC framework and deployed on an Intel Atom MINI ITX motherboard. Programmed an ATmega32 AVR microcontroller in C programming language for motor control and water pump activation, ensuring precise task execution."
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
    "certifications": [
        {
            "title": "Deep Learning Specialization",
            "institution": "Coursera",
            "date": "2022",
            "url": {
                "title": "",
                "link": ""
            }
        },
        {
            "title": "Artificial Intelligence",
            "institution": "IPM Advanced School on Computing",
            "date": "2021",
            "url": {
                "title": "",
                "link": ""
            }
        },
        {
            "title": "MikroTik Certified Network Associate",
            "institution": "Forat Technical Institute",
            "date": "2020",
            "url": {
                "title": "",
                "link": ""
            }
        }
    ]
}
