# Multi-Agent End-to-End Email Management System

An AI-powered enterprise email management pipeline built using **LangChain, LangGraph, and Weaviate**. The system orchestrates multiple specialized AI agents to analyze incoming emails, retrieve relevant information using Retrieval-Augmented Generation (RAG), generate context-aware responses, and incorporate human oversight through an approval and feedback-driven revision cycle.

## Problem Statement

Managing high volumes of enterprise emails is time-consuming and prone to inconsistencies. Manually categorizing messages, searching knowledge bases for relevant information, and drafting accurate, policy-aligned responses can create significant operational bottlenecks.

This project addresses these challenges by automating email analysis, contextual information retrieval, specialized response generation, and quality control while retaining human authority over outgoing communications.

## Key Features

- **Automated Email Triage and Summarization:** Classifies incoming emails, extracts relevant information, and generates concise summaries.
- **Dynamic RAG Pipeline:** Determines whether additional information is required and retrieves relevant context from a Weaviate vector database.
- **Category-Based Drafting:** Routes emails to specialized drafter agents based on their identified category.
- **Human-in-the-Loop (HITL) Approval:** Pauses workflow execution for human review before an email can be sent.
- **Feedback-Driven Revision:** Uses rejection feedback to identify issues and generate recommendations for improving drafts.
- **Cyclic Workflow Orchestration:** Supports iterative drafting, review, and approval using LangGraph's conditional routing and state management.
- **State Persistence and Resumability:** Supports pausing and resuming workflows using LangGraph checkpointing.

## Architecture and Technology Stack

| Component | Technology | Responsibility |
|---|---|---|
| Agent orchestration | LangGraph | Workflow execution, state management, conditional routing, and cyclic graphs |
| LLM integration | LangChain | Model invocation, prompt construction, and structured outputs |
| Language model | Groq-hosted LLM | Email analysis, summarization, drafting, and review |
| Vector database | Weaviate | Storage and retrieval of contextual information |
| Retrieval strategy | RAG | Grounding email responses in relevant retrieved information |
| State validation | Pydantic | Defining structured state models and validating agent outputs |
| Human oversight | LangGraph interrupts | Pausing execution for approval and resuming after a human decision |

## System Workflow

### 1. Email Ingestion and Analysis

An incoming email is added to the LangGraph workflow state. The Analyzer Agent:

- Identifies the email category.
- Extracts relevant information and generates a concise summary.
- Determines whether external or internal information retrieval is necessary.
- Generates a retrieval query when additional context is required.

### 2. Dynamic Data Retrieval

The workflow conditionally routes the email to the retrieval node when additional information is needed.

The Weaviate retriever searches the knowledge base for relevant documents, policies, or background information. The retrieved content is passed to the drafting stage as contextual input.

If retrieval is unnecessary, the workflow can proceed directly to drafting.

### 3. Category-Specific Email Drafting

Based on the identified category, the workflow routes the request to the appropriate specialized drafter.

The drafter uses the email summary, retrieved context when available, and any existing review feedback to generate a relevant and professional response.

### 4. Human-in-the-Loop Approval

The generated draft is presented for human review before any outgoing communication is sent.

Using LangGraph's interrupt and checkpointing capabilities, the workflow can pause while preserving its execution state.

The reviewer can:

- **Approve:** Continue to the email-sending stage.
- **Reject with feedback:** Send the draft for further analysis and revision.

No email should be sent without the required approval.

### 5. Feedback Analysis and Iterative Refinement

When a draft is rejected, a Reviewer Agent evaluates the human feedback and identifies potential issues.

The review output includes:

- Identified issues in the current draft.
- Recommendations for improvement.
- A rejection classification, such as `DATA_ISSUE` or `DRAFT_ISSUE`.

The workflow uses this information to determine the next step:

- **Data issue:** Revisit information retrieval when additional or corrected context is required.
- **Draft issue:** Return to the relevant drafter with the review findings and existing context.

The revised draft is presented for human approval again. This cycle continues until the draft is approved or the workflow reaches a configured stopping condition.

### 6. Email Dispatch

Once the draft receives approval, the workflow routes it to the email-sending stage. The approved response is then sent through the configured email integration.
