# Contributing to the Project

Thank you for considering contributing to this project! We welcome contributions from the community to help improve and expand the capabilities of this AI-driven novel generation tool, which uses **LangChain**, **Ollama**, and **RAG (Retrieval-Augmented Generation)** technologies.

## How to Contribute

### 1. Fork the Repository
To get started, fork the repository to your own GitHub account by clicking the "Fork" button at the top right of this page.

### 2. Clone Your Fork
Clone your forked repository to your local machine:

```bash
git clone https://github.com/xiangmeng4geo/novellm.git
cd novellm
```

### 3. Create a New Branch
Before you start working on any changes, create a new branch to keep your changes isolated from the master branch:
```bash
git checkout -b feature/your-feature-name
```

### 4. Make Your Changes
Make the necessary changes to the codebase. Ensure that you follow the existing code style and practices.

Here are some areas where you can help:

* Data Module: Improving data preprocessing, vector embeddings, or adding new data sources.
* Model Module: Enhancing model integration with Ollama, or improving generation logic.
* Pipeline Module: Contributing to RAG pipeline development or creating new LangChain chains.
* API Module: Adding new API routes, improving error handling, or enhancing API functionality.
* Tests: Writing unit tests, integration tests, or performance tests to ensure code quality.
* Documentation: Updating README files, adding comments, or improving documentation.

### 5. Run Tests
Before submitting your changes, ensure that all tests pass successfully. You can run the tests using the following command:
```bash
pip install -r requirements.txt

pytest
```
### 6. Commit Your Changes
Commit your changes with a clear and descriptive message:

```bash
git add .
git commit -m "Add feature/bugfix description"
```


### 7. Push Your Changes
Push your changes to your forked repository:

```bash
git push origin feature/your-feature-name
```

### 8. Create a Pull Request
Go to the original repository on GitHub and click on the "New Pull Request" button. Provide a clear description of the changes you've made.

---
Project Structure
```bash
project/
│
├── src/
│   ├── data/                # Data processing, embedding, and vector store modules
│   ├── models/              # Model integration, including Ollama and generation logic
│   ├── pipelines/           # LangChain pipelines, RAG processes, and custom tools
│   ├── api/                 # REST API definitions and endpoints
│   ├── tests/               # Unit and integration tests
│   ├── config/              # Configuration files and settings
│   └── utils/               # Helper functions and utilities
│
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables
├── README.md                # Project overview
└── LICENSE                  # Project license
```

Thank you for your contributions! 🙏