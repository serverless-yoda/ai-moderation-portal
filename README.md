# 🛡️ AI Moderation Portal

A FastAPI microservice for **Content Moderation of User‑Generated Content (UGC)** using **Azure AI Content Moderator** and **Text Analytics APIs**.

---

## 🚨 Pain Point

Enterprises face increasing challenges in managing UGC that may contain:

- ❌ Toxic or abusive language  
- 🧃 Spam or promotional content  
- 🔐 Personally Identifiable Information (PII)

---

## ✅ Solution

This microservice provides a scalable and secure way to screen and flag problematic content using:

- **FastAPI** for high-performance RESTful endpoints  
- **Azure AI Content Moderator** for detecting profanity, PII, and unwanted content  
- **Azure Text Analytics** for sentiment analysis and language detection

---

## 📦 Features

- 🔍 Real-time content screening via REST API  
- 🧠 Sentiment and language analysis  
- 🧹 PII detection and redaction  
- 📊 JSON-based moderation reports  
- 🛠️ Easy integration with frontend portals or backend pipelines

---

## 📁 Folder Structure and Purpose

| Folder/File                                      | Description                                                                                          |
|--------------------------------------------------|------------------------------------------------------------------------------------------------------|
| `/api/v1/routes.py`                              | Defines API endpoints, e.g., `/moderate`. Maps requests to service layer.                           |
| `/api/middleware.py`                             | Implements middleware for rate limiting, request correlation, and logging.                          |
| `/application/dto/`                              | Defines Pydantic DTOs for request (`ModerationRequestDTO`) and response (`ModerationResultDTO`) validation and serialization. |
| `/application/services/moderation_service.py`    | Orchestration layer `ModerationService` connecting API to domain and infrastructure.                |
| `/common/config.py`                              | Centralized environment configuration loader using Pydantic `BaseSettings`.                         |
| `/common/error_handlers.py`                      | Exception handlers mapping domain errors to HTTP responses, plus shared correlation middleware.     |
| `/common/logging.py`                             | Logging setup with correlation ID context and filter for structured observability.                  |
| `/domain/contracts/i_content_moderator.py`       | Domain interface defining contract to moderate content asynchronously.                              |
| `/domain/entities/moderation_result.py`          | Core domain entity representing standardized moderation result.                                     |
| `/domain/exceptions.py`                          | Domain-specific exceptions hierarchy with `ModerationFailedError`.                                  |
| `/infrastructure/azure_content_moderator.py`     | Azure content moderation client, calling Azure API securely and asynchronously.                     |
| `/tests/integration/test_moderation_api.py`      | Integration test verifying end-to-end API request flow.                                             |
| `/tests/unit/test_moderation_service.py`         | Unit test for `ModerationService` with mocked moderator dependency.                                 |
| `main.py`                                        | Entry point wiring FastAPI app, middleware, exception handling, and API router inclusion.           |

---
## 🏗️ Architectural Design

### Layered Architecture

| Layer             | Purpose                                                  | Examples/Components                                                                 | Design Principles                                                                 |
|-------------------|----------------------------------------------------------|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| **API Layer**     | Handles HTTP routing, validation, middleware             | `main.py`, `api/v1/routes.py`, `api/middleware.py`                                  | Separation of concerns, routing, dependency injection for services                |
| **Application Layer** | Business orchestration and use case logic           | `ModerationService`, DTOs                                                           | Dependency inversion to depend on abstractions, DTO-to-domain mapping            |
| **Domain Layer**  | Core business models, contracts, exceptions              | `IContentModerator`, `ModerationResult`, `exceptions`                               | Strict domain modeling, interface segregation, exception handling                |
| **Infrastructure**| Concrete external service implementations (Azure)        | `AzureContentModerator`                                                             | Encapsulation of external integrations, async communication                      |
| **Common Layer**  | Cross-cutting concerns (config, logging, error handling) | `common/config.py`, `common/logging.py`, `common/error_handlers.py`                 | Reusability, centralized config, structured logging                              |

---

## 📦 Important Packages Used and Why

| Package/Library                  | Usage                                                                 |
|----------------------------------|-----------------------------------------------------------------------|
| `fastapi`                        | Rapid API framework with async support                               |
| `pydantic` / `pydantic-settings`| Validation and configuration management using Python type hints      |
| `httpx`                          | Asynchronous HTTP client for calling external APIs                   |
| `azure.identity.aio`            | Asynchronous Azure credential management                             |
| `azure.keyvault.secrets.aio`    | Secure, async retrieval of secrets from Azure Key Vault              |
| `pytest` / `pytest-asyncio`     | Unit and integration testing for asynchronous Python code            |
| `logging`                        | Structured logging with correlation ID support for observability     |


---

## 🚀 Quickstart

```bash
# Clone the repo
git clone https://github.com/serverless-yoda/ai-moderation-portal.git
cd ai-moderation-portal

# Install dependencies
pip install -r requirements.txt

# Run the service
uvicorn main:app --reload --port 8000

# run the streamlit test app
streamlit run streamlit_app.py


