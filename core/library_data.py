"""Library database with categories and packages"""

LIBRARY_CATEGORIES = {
    "GUI Development": [
        {
            "name": "PyQt6",
            "description": "Professional cross-platform GUI framework with modern widgets and themes",
            "install_cmd": "pip install PyQt6"
        },
        {
            "name": "PyQt6-WebEngine",
            "description": "Web browser widget for PyQt6 applications",
            "install_cmd": "pip install PyQt6-WebEngine"
        },
        {
            "name": "Tkinter",
            "description": "Built-in Python GUI toolkit (usually pre-installed)",
            "install_cmd": "pip install tk"
        },
        {
            "name": "Kivy",
            "description": "Open-source Python library for developing multitouch applications",
            "install_cmd": "pip install kivy"
        },
        {
            "name": "wxPython",
            "description": "Cross-platform GUI toolkit for Python",
            "install_cmd": "pip install wxPython"
        },
        {
            "name": "PySimpleGUI",
            "description": "Simple and elegant GUI framework",
            "install_cmd": "pip install PySimpleGUI"
        },
        {
            "name": "PySide6",
            "description": "Official Python bindings for Qt (alternative to PyQt6)",
            "install_cmd": "pip install PySide6"
        },
        {
            "name": "DearPyGui",
            "description": "Fast and powerful GUI toolkit using GPU rendering",
            "install_cmd": "pip install dearpygui"
        }
    ],

    "WhatsApp API": [
        {
            "name": "yowsup",
            "description": "Python library for WhatsApp protocol (unofficial)",
            "install_cmd": "pip install yowsup"
        },
        {
            "name": "whatsapp-cloud-api",
            "description": "Official WhatsApp Cloud API client",
            "install_cmd": "pip install whatsapp-cloud-api"
        },
        {
            "name": "pywhatkit",
            "description": "Python library to send WhatsApp messages at scheduled time",
            "install_cmd": "pip install pywhatkit"
        },
        {
            "name": "selenium",
            "description": "Browser automation tool (can be used for WhatsApp Web automation)",
            "install_cmd": "pip install selenium"
        },
        {
            "name": "pyautogui",
            "description": "GUI automation for WhatsApp Desktop",
            "install_cmd": "pip install pyautogui"
        }
    ],

    "Artificial Intelligence": [
        {
            "name": "torch",
            "description": "PyTorch deep learning framework",
            "install_cmd": "pip install torch torchvision torchaudio"
        },
        {
            "name": "tensorflow",
            "description": "Google's machine learning framework",
            "install_cmd": "pip install tensorflow"
        },
        {
            "name": "transformers",
            "description": "Hugging Face transformers for NLP models",
            "install_cmd": "pip install transformers"
        },
        {
            "name": "sentencepiece",
            "description": "Tokenization library for NLP",
            "install_cmd": "pip install sentencepiece"
        },
        {
            "name": "diffusers",
            "description": "Hugging Face library for diffusion models (Stable Diffusion)",
            "install_cmd": "pip install diffusers"
        },
        {
            "name": "accelerate",
            "description": "Easy training and inference optimization",
            "install_cmd": "pip install accelerate"
        },
        {
            "name": "openai",
            "description": "Official OpenAI Python library",
            "install_cmd": "pip install openai"
        },
        {
            "name": "langchain",
            "description": "Framework for developing LLM applications",
            "install_cmd": "pip install langchain"
        },
        {
            "name": "llama-cpp-python",
            "description": "Python bindings for llama.cpp (run LLMs locally)",
            "install_cmd": "pip install llama-cpp-python"
        },
        {
            "name": "opencv-python",
            "description": "Computer vision library",
            "install_cmd": "pip install opencv-python"
        },
        {
            "name": "mediapipe",
            "description": "Google's ML solution for live and streaming media",
            "install_cmd": "pip install mediapipe"
        }
    ],

    "Data Science": [
        {
            "name": "pandas",
            "description": "Powerful data manipulation and analysis library",
            "install_cmd": "pip install pandas"
        },
        {
            "name": "numpy",
            "description": "Fundamental package for scientific computing",
            "install_cmd": "pip install numpy"
        },
        {
            "name": "scikit-learn",
            "description": "Machine learning library with various algorithms",
            "install_cmd": "pip install scikit-learn"
        },
        {
            "name": "matplotlib",
            "description": "Comprehensive library for creating visualizations",
            "install_cmd": "pip install matplotlib"
        },
        {
            "name": "seaborn",
            "description": "Statistical data visualization based on matplotlib",
            "install_cmd": "pip install seaborn"
        },
        {
            "name": "plotly",
            "description": "Interactive graphing library",
            "install_cmd": "pip install plotly"
        },
        {
            "name": "scipy",
            "description": "Scientific computing and technical computing library",
            "install_cmd": "pip install scipy"
        },
        {
            "name": "statsmodels",
            "description": "Statistical modeling and econometrics",
            "install_cmd": "pip install statsmodels"
        },
        {
            "name": "jupyter",
            "description": "Interactive computing environment (Jupyter Notebook)",
            "install_cmd": "pip install jupyter"
        },
        {
            "name": "openpyxl",
            "description": "Read/write Excel 2010 xlsx/xlsm files",
            "install_cmd": "pip install openpyxl"
        },
        {
            "name": "xlrd",
            "description": "Read Excel files",
            "install_cmd": "pip install xlrd"
        }
    ],

    "ERPNext / Frappe": [
        {
            "name": "frappe-client",
            "description": "Python client for Frappe/ERPNext REST API",
            "install_cmd": "pip install frappe-client"
        },
        {
            "name": "frappe-bench",
            "description": "Bench CLI tool for managing Frappe/ERPNext sites",
            "install_cmd": "pip install frappe-bench"
        },
        {
            "name": "erpnext-client",
            "description": "ERPNext API wrapper",
            "install_cmd": "pip install erpnext-client"
        }
    ],

    "Networking / Automation": [
        {
            "name": "paramiko",
            "description": "SSH protocol library for remote server access",
            "install_cmd": "pip install paramiko"
        },
        {
            "name": "netmiko",
            "description": "Multi-vendor library for SSH connections to network devices",
            "install_cmd": "pip install netmiko"
        },
        {
            "name": "routeros-api",
            "description": "MikroTik RouterOS API client",
            "install_cmd": "pip install routeros-api"
        },
        {
            "name": "scapy",
            "description": "Powerful packet manipulation library",
            "install_cmd": "pip install scapy"
        },
        {
            "name": "nmap",
            "description": "Python wrapper for Nmap network scanner",
            "install_cmd": "pip install python-nmap"
        },
        {
            "name": "fabric",
            "description": "High-level SSH automation library",
            "install_cmd": "pip install fabric"
        },
        {
            "name": "ansible",
            "description": "IT automation platform (install via pip or system package manager)",
            "install_cmd": "pip install ansible"
        },
        {
            "name": "ping3",
            "description": "Pure Python ICMP ping implementation",
            "install_cmd": "pip install ping3"
        },
        {
            "name": "speedtest-cli",
            "description": "Command-line internet speed test",
            "install_cmd": "pip install speedtest-cli"
        }
    ],

    "Web Development": [
        {
            "name": "flask",
            "description": "Lightweight web framework",
            "install_cmd": "pip install flask"
        },
        {
            "name": "django",
            "description": "High-level Python web framework",
            "install_cmd": "pip install django"
        },
        {
            "name": "fastapi",
            "description": "Modern, fast web framework for building APIs",
            "install_cmd": "pip install fastapi uvicorn"
        },
        {
            "name": "requests",
            "description": "HTTP library for Python",
            "install_cmd": "pip install requests"
        },
        {
            "name": "beautifulsoup4",
            "description": "Web scraping library",
            "install_cmd": "pip install beautifulsoup4"
        },
        {
            "name": "scrapy",
            "description": "Web crawling and scraping framework",
            "install_cmd": "pip install scrapy"
        },
        {
            "name": "aiohttp",
            "description": "Async HTTP client/server framework",
            "install_cmd": "pip install aiohttp"
        },
        {
            "name": "httpx",
            "description": "Next-generation HTTP client",
            "install_cmd": "pip install httpx"
        },
        {
            "name": "streamlit",
            "description": "Create data apps quickly",
            "install_cmd": "pip install streamlit"
        },
        {
            "name": "jinja2",
            "description": "Template engine for Python",
            "install_cmd": "pip install jinja2"
        }
    ],

    "General Python Packages": [
        {
            "name": "requests",
            "description": "HTTP library for making API calls",
            "install_cmd": "pip install requests"
        },
        {
            "name": "pillow",
            "description": "Python Imaging Library (PIL fork) for image processing",
            "install_cmd": "pip install pillow"
        },
        {
            "name": "python-dotenv",
            "description": "Read key-value pairs from .env files",
            "install_cmd": "pip install python-dotenv"
        },
        {
            "name": "pyinstaller",
            "description": "Package Python applications into standalone executables",
            "install_cmd": "pip install pyinstaller"
        },
        {
            "name": "pytest",
            "description": "Testing framework",
            "install_cmd": "pip install pytest"
        },
        {
            "name": "black",
            "description": "Code formatter",
            "install_cmd": "pip install black"
        },
        {
            "name": "flake8",
            "description": "Code linter",
            "install_cmd": "pip install flake8"
        },
        {
            "name": "pylint",
            "description": "Static code analyzer",
            "install_cmd": "pip install pylint"
        },
        {
            "name": "click",
            "description": "Command-line interface creation kit",
            "install_cmd": "pip install click"
        },
        {
            "name": "colorama",
            "description": "Cross-platform colored terminal text",
            "install_cmd": "pip install colorama"
        },
        {
            "name": "tqdm",
            "description": "Progress bar library",
            "install_cmd": "pip install tqdm"
        },
        {
            "name": "loguru",
            "description": "Modern logging library",
            "install_cmd": "pip install loguru"
        },
        {
            "name": "pydantic",
            "description": "Data validation using Python type annotations",
            "install_cmd": "pip install pydantic"
        },
        {
            "name": "schedule",
            "description": "Job scheduling library",
            "install_cmd": "pip install schedule"
        }
    ],

    "Database": [
        {
            "name": "pymongo",
            "description": "MongoDB driver for Python",
            "install_cmd": "pip install pymongo"
        },
        {
            "name": "psycopg2",
            "description": "PostgreSQL adapter",
            "install_cmd": "pip install psycopg2-binary"
        },
        {
            "name": "mysql-connector",
            "description": "MySQL database connector",
            "install_cmd": "pip install mysql-connector-python"
        },
        {
            "name": "sqlalchemy",
            "description": "SQL toolkit and ORM",
            "install_cmd": "pip install sqlalchemy"
        },
        {
            "name": "redis",
            "description": "Redis database client",
            "install_cmd": "pip install redis"
        },
        {
            "name": "elasticsearch",
            "description": "Elasticsearch client",
            "install_cmd": "pip install elasticsearch"
        }
    ],

    "Security & Cryptography": [
        {
            "name": "cryptography",
            "description": "Cryptographic recipes and primitives",
            "install_cmd": "pip install cryptography"
        },
        {
            "name": "pycryptodome",
            "description": "Cryptographic library",
            "install_cmd": "pip install pycryptodome"
        },
        {
            "name": "bcrypt",
            "description": "Password hashing library",
            "install_cmd": "pip install bcrypt"
        },
        {
            "name": "pyotp",
            "description": "One-time password (OTP) library",
            "install_cmd": "pip install pyotp"
        },
        {
            "name": "pyjwt",
            "description": "JSON Web Token implementation",
            "install_cmd": "pip install pyjwt"
        }
    ],

    "Testing & QA": [
        {
            "name": "pytest",
            "description": "Feature-rich Python testing framework",
            "install_cmd": "pip install pytest"
        },
        {
            "name": "pytest-cov",
            "description": "Code coverage plugin for pytest",
            "install_cmd": "pip install pytest-cov"
        },
        {
            "name": "unittest-mock",
            "description": "Mock object library for testing",
            "install_cmd": "pip install mock"
        },
        {
            "name": "selenium",
            "description": "Browser automation for web testing",
            "install_cmd": "pip install selenium"
        },
        {
            "name": "playwright",
            "description": "Modern web automation and testing",
            "install_cmd": "pip install playwright"
        },
        {
            "name": "behave",
            "description": "Behavior-driven development (BDD) framework",
            "install_cmd": "pip install behave"
        },
        {
            "name": "locust",
            "description": "Performance/load testing tool",
            "install_cmd": "pip install locust"
        },
        {
            "name": "hypothesis",
            "description": "Property-based testing library",
            "install_cmd": "pip install hypothesis"
        },
        {
            "name": "robotframework",
            "description": "Generic test automation framework",
            "install_cmd": "pip install robotframework"
        },
        {
            "name": "tox",
            "description": "Test automation across multiple Python versions",
            "install_cmd": "pip install tox"
        }
    ],

    "DevOps & CI/CD": [
        {
            "name": "docker",
            "description": "Docker SDK for Python",
            "install_cmd": "pip install docker"
        },
        {
            "name": "docker-compose",
            "description": "Docker Compose for Python",
            "install_cmd": "pip install docker-compose"
        },
        {
            "name": "kubernetes",
            "description": "Kubernetes client for Python",
            "install_cmd": "pip install kubernetes"
        },
        {
            "name": "ansible",
            "description": "Infrastructure automation and configuration management",
            "install_cmd": "pip install ansible"
        },
        {
            "name": "terraform",
            "description": "Terraform Python bindings",
            "install_cmd": "pip install python-terraform"
        },
        {
            "name": "jenkins-job-builder",
            "description": "Jenkins job configuration tool",
            "install_cmd": "pip install jenkins-job-builder"
        },
        {
            "name": "gitpython",
            "description": "Git integration library",
            "install_cmd": "pip install gitpython"
        },
        {
            "name": "pre-commit",
            "description": "Git pre-commit hooks framework",
            "install_cmd": "pip install pre-commit"
        },
        {
            "name": "invoke",
            "description": "Task execution tool (like Make)",
            "install_cmd": "pip install invoke"
        }
    ],

    "API Development": [
        {
            "name": "fastapi",
            "description": "Modern, high-performance API framework",
            "install_cmd": "pip install fastapi uvicorn"
        },
        {
            "name": "flask-restful",
            "description": "Flask extension for building REST APIs",
            "install_cmd": "pip install flask-restful"
        },
        {
            "name": "django-rest-framework",
            "description": "Powerful Django REST API toolkit",
            "install_cmd": "pip install djangorestframework"
        },
        {
            "name": "graphene",
            "description": "GraphQL framework for Python",
            "install_cmd": "pip install graphene"
        },
        {
            "name": "strawberry-graphql",
            "description": "Modern GraphQL library with type hints",
            "install_cmd": "pip install strawberry-graphql"
        },
        {
            "name": "connexion",
            "description": "OpenAPI-first REST framework",
            "install_cmd": "pip install connexion"
        },
        {
            "name": "marshmallow",
            "description": "Object serialization/deserialization library",
            "install_cmd": "pip install marshmallow"
        },
        {
            "name": "apispec",
            "description": "API specification generator (OpenAPI/Swagger)",
            "install_cmd": "pip install apispec"
        },
        {
            "name": "httpie",
            "description": "User-friendly HTTP client for API testing",
            "install_cmd": "pip install httpie"
        }
    ],

    "Data Processing & ETL": [
        {
            "name": "apache-airflow",
            "description": "Workflow orchestration platform",
            "install_cmd": "pip install apache-airflow"
        },
        {
            "name": "luigi",
            "description": "Batch job pipeline framework",
            "install_cmd": "pip install luigi"
        },
        {
            "name": "prefect",
            "description": "Modern workflow orchestration",
            "install_cmd": "pip install prefect"
        },
        {
            "name": "dask",
            "description": "Parallel computing library for analytics",
            "install_cmd": "pip install dask"
        },
        {
            "name": "pyspark",
            "description": "Apache Spark Python API",
            "install_cmd": "pip install pyspark"
        },
        {
            "name": "polars",
            "description": "Lightning-fast DataFrame library",
            "install_cmd": "pip install polars"
        },
        {
            "name": "petl",
            "description": "Extract, transform, and load tables of data",
            "install_cmd": "pip install petl"
        },
        {
            "name": "great-expectations",
            "description": "Data validation and documentation",
            "install_cmd": "pip install great-expectations"
        }
    ],

    "File & Document Processing": [
        {
            "name": "pypdf2",
            "description": "PDF toolkit for reading and manipulating PDFs",
            "install_cmd": "pip install PyPDF2"
        },
        {
            "name": "pdfplumber",
            "description": "Extract text and tables from PDFs",
            "install_cmd": "pip install pdfplumber"
        },
        {
            "name": "reportlab",
            "description": "PDF generation library",
            "install_cmd": "pip install reportlab"
        },
        {
            "name": "python-docx",
            "description": "Create and modify Word documents",
            "install_cmd": "pip install python-docx"
        },
        {
            "name": "openpyxl",
            "description": "Read/write Excel files",
            "install_cmd": "pip install openpyxl"
        },
        {
            "name": "xlsxwriter",
            "description": "Write Excel files with formatting",
            "install_cmd": "pip install xlsxwriter"
        },
        {
            "name": "python-pptx",
            "description": "Create and modify PowerPoint presentations",
            "install_cmd": "pip install python-pptx"
        },
        {
            "name": "markdown",
            "description": "Markdown to HTML converter",
            "install_cmd": "pip install markdown"
        },
        {
            "name": "pyyaml",
            "description": "YAML parser and emitter",
            "install_cmd": "pip install pyyaml"
        },
        {
            "name": "toml",
            "description": "TOML configuration file parser",
            "install_cmd": "pip install toml"
        }
    ],

    "Image & Video Processing": [
        {
            "name": "pillow",
            "description": "Python Imaging Library for image processing",
            "install_cmd": "pip install pillow"
        },
        {
            "name": "opencv-python",
            "description": "Computer vision and image processing",
            "install_cmd": "pip install opencv-python"
        },
        {
            "name": "imageio",
            "description": "Read and write image data",
            "install_cmd": "pip install imageio"
        },
        {
            "name": "scikit-image",
            "description": "Image processing algorithms",
            "install_cmd": "pip install scikit-image"
        },
        {
            "name": "moviepy",
            "description": "Video editing library",
            "install_cmd": "pip install moviepy"
        },
        {
            "name": "ffmpeg-python",
            "description": "Python bindings for FFmpeg",
            "install_cmd": "pip install ffmpeg-python"
        },
        {
            "name": "face-recognition",
            "description": "Face recognition library",
            "install_cmd": "pip install face-recognition"
        },
        {
            "name": "pytesseract",
            "description": "OCR (Optical Character Recognition)",
            "install_cmd": "pip install pytesseract"
        }
    ],

    "Audio Processing": [
        {
            "name": "pydub",
            "description": "Audio manipulation with simple interface",
            "install_cmd": "pip install pydub"
        },
        {
            "name": "librosa",
            "description": "Audio and music analysis",
            "install_cmd": "pip install librosa"
        },
        {
            "name": "soundfile",
            "description": "Read and write sound files",
            "install_cmd": "pip install soundfile"
        },
        {
            "name": "pyaudio",
            "description": "Audio I/O library",
            "install_cmd": "pip install pyaudio"
        },
        {
            "name": "speech-recognition",
            "description": "Speech recognition engine",
            "install_cmd": "pip install SpeechRecognition"
        },
        {
            "name": "pyttsx3",
            "description": "Text-to-speech conversion",
            "install_cmd": "pip install pyttsx3"
        },
        {
            "name": "sounddevice",
            "description": "Play and record sound",
            "install_cmd": "pip install sounddevice"
        }
    ],

    "Game Development": [
        {
            "name": "pygame",
            "description": "Game development library",
            "install_cmd": "pip install pygame"
        },
        {
            "name": "pyglet",
            "description": "Cross-platform windowing and multimedia",
            "install_cmd": "pip install pyglet"
        },
        {
            "name": "arcade",
            "description": "Easy-to-use 2D game framework",
            "install_cmd": "pip install arcade"
        },
        {
            "name": "panda3d",
            "description": "3D game engine",
            "install_cmd": "pip install panda3d"
        },
        {
            "name": "ursina",
            "description": "Game engine powered by Panda3D",
            "install_cmd": "pip install ursina"
        },
        {
            "name": "pyopengl",
            "description": "OpenGL bindings for Python",
            "install_cmd": "pip install PyOpenGL"
        }
    ],

    "Desktop Automation": [
        {
            "name": "pyautogui",
            "description": "GUI automation and control",
            "install_cmd": "pip install pyautogui"
        },
        {
            "name": "keyboard",
            "description": "Keyboard event hooks and control",
            "install_cmd": "pip install keyboard"
        },
        {
            "name": "mouse",
            "description": "Mouse control and automation",
            "install_cmd": "pip install mouse"
        },
        {
            "name": "pywinauto",
            "description": "Windows GUI automation (Windows only)",
            "install_cmd": "pip install pywinauto"
        },
        {
            "name": "pygetwindow",
            "description": "Window manipulation library",
            "install_cmd": "pip install pygetwindow"
        },
        {
            "name": "watchdog",
            "description": "File system monitoring",
            "install_cmd": "pip install watchdog"
        },
        {
            "name": "schedule",
            "description": "Job scheduling for humans",
            "install_cmd": "pip install schedule"
        }
    ],

    "Email & Communication": [
        {
            "name": "email-validator",
            "description": "Email address validation",
            "install_cmd": "pip install email-validator"
        },
        {
            "name": "sendgrid",
            "description": "SendGrid email service API",
            "install_cmd": "pip install sendgrid"
        },
        {
            "name": "twilio",
            "description": "Twilio SMS/Voice API",
            "install_cmd": "pip install twilio"
        },
        {
            "name": "python-telegram-bot",
            "description": "Telegram Bot API wrapper",
            "install_cmd": "pip install python-telegram-bot"
        },
        {
            "name": "discord.py",
            "description": "Discord API wrapper",
            "install_cmd": "pip install discord.py"
        },
        {
            "name": "slackclient",
            "description": "Slack API client",
            "install_cmd": "pip install slack-sdk"
        },
        {
            "name": "yagmail",
            "description": "Simple Gmail/SMTP client",
            "install_cmd": "pip install yagmail"
        }
    ],

    "Code Quality & Formatting": [
        {
            "name": "black",
            "description": "Uncompromising code formatter",
            "install_cmd": "pip install black"
        },
        {
            "name": "isort",
            "description": "Sort Python imports automatically",
            "install_cmd": "pip install isort"
        },
        {
            "name": "autopep8",
            "description": "Automatically format Python code to PEP 8",
            "install_cmd": "pip install autopep8"
        },
        {
            "name": "flake8",
            "description": "Code linting tool",
            "install_cmd": "pip install flake8"
        },
        {
            "name": "pylint",
            "description": "Comprehensive code analyzer",
            "install_cmd": "pip install pylint"
        },
        {
            "name": "mypy",
            "description": "Static type checker",
            "install_cmd": "pip install mypy"
        },
        {
            "name": "bandit",
            "description": "Security issue finder",
            "install_cmd": "pip install bandit"
        },
        {
            "name": "radon",
            "description": "Code complexity analyzer",
            "install_cmd": "pip install radon"
        },
        {
            "name": "prospector",
            "description": "All-in-one code analysis tool",
            "install_cmd": "pip install prospector"
        }
    ],

    "Blockchain & Cryptocurrency": [
        {
            "name": "web3",
            "description": "Ethereum blockchain interaction",
            "install_cmd": "pip install web3"
        },
        {
            "name": "bitcoin",
            "description": "Bitcoin library",
            "install_cmd": "pip install bitcoin"
        },
        {
            "name": "ccxt",
            "description": "Cryptocurrency exchange trading library",
            "install_cmd": "pip install ccxt"
        },
        {
            "name": "brownie",
            "description": "Ethereum smart contract development",
            "install_cmd": "pip install eth-brownie"
        },
        {
            "name": "python-binance",
            "description": "Binance exchange API",
            "install_cmd": "pip install python-binance"
        }
    ],

    "IoT & Hardware": [
        {
            "name": "pyserial",
            "description": "Serial port communication",
            "install_cmd": "pip install pyserial"
        },
        {
            "name": "gpiozero",
            "description": "Raspberry Pi GPIO interface",
            "install_cmd": "pip install gpiozero"
        },
        {
            "name": "adafruit-circuitpython",
            "description": "Adafruit CircuitPython libraries",
            "install_cmd": "pip install adafruit-circuitpython-bundle"
        },
        {
            "name": "paho-mqtt",
            "description": "MQTT protocol client",
            "install_cmd": "pip install paho-mqtt"
        },
        {
            "name": "bleak",
            "description": "Bluetooth Low Energy platform",
            "install_cmd": "pip install bleak"
        },
        {
            "name": "pyusb",
            "description": "USB access library",
            "install_cmd": "pip install pyusb"
        }
    ],

    "Scientific Computing": [
        {
            "name": "sympy",
            "description": "Symbolic mathematics library",
            "install_cmd": "pip install sympy"
        },
        {
            "name": "scipy",
            "description": "Scientific and technical computing",
            "install_cmd": "pip install scipy"
        },
        {
            "name": "astropy",
            "description": "Astronomy and astrophysics library",
            "install_cmd": "pip install astropy"
        },
        {
            "name": "biopython",
            "description": "Biological computation tools",
            "install_cmd": "pip install biopython"
        },
        {
            "name": "networkx",
            "description": "Network analysis and graph theory",
            "install_cmd": "pip install networkx"
        },
        {
            "name": "pymc3",
            "description": "Probabilistic programming",
            "install_cmd": "pip install pymc3"
        }
    ],

    "CLI Tools & Productivity": [
        {
            "name": "click",
            "description": "Command-line interface creation",
            "install_cmd": "pip install click"
        },
        {
            "name": "typer",
            "description": "Modern CLI framework based on type hints",
            "install_cmd": "pip install typer"
        },
        {
            "name": "rich",
            "description": "Rich text and beautiful formatting in terminal",
            "install_cmd": "pip install rich"
        },
        {
            "name": "tqdm",
            "description": "Progress bars for loops",
            "install_cmd": "pip install tqdm"
        },
        {
            "name": "colorama",
            "description": "Cross-platform colored terminal output",
            "install_cmd": "pip install colorama"
        },
        {
            "name": "questionary",
            "description": "Interactive command-line prompts",
            "install_cmd": "pip install questionary"
        },
        {
            "name": "fire",
            "description": "Automatically generate CLIs",
            "install_cmd": "pip install fire"
        },
        {
            "name": "argparse",
            "description": "Command-line argument parser (built-in, but can upgrade)",
            "install_cmd": "pip install argparse"
        }
    ]
}
