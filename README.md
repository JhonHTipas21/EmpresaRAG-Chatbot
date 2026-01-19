```txt
<div align="center">

# 🤖 EmpresaRAG Chatbot

```

      🔎 RAG • 📄 Docs • 🤖 LLM • ⚡ FastAPI • 🌐 Next.js
```

### 💡 Chatbot Empresarial Inteligente con RAG  
**Respuestas precisas basadas en documentos reales** | Sin alucinaciones | Listo para producción

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Next.js](https://img.shields.io/badge/Next.js_15-000000?style=for-the-badge&logo=next.js&logoColor=white)](https://nextjs.org/)
[![Python](https://img.shields.io/badge/Python_3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![Build](https://img.shields.io/badge/build-passing-brightgreen?style=flat-square)
![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)

[🚀 Demo](#-demo-visual) •
[✨ Características](#-características-principales) •
[🛠️ Stack](#%EF%B8%8F-stack-tecnológico) •
[🏗️ Arquitectura](#%EF%B8%8F-arquitectura-del-sistema) •
[🎯 Uso](#-cómo-usar) •
[💬 Contacto](#-lets-connect)

</div>

---

## 🎯 ¿Qué es EmpresaRAG?

> **Un asistente conversacional que responde SOLO con información de tus documentos corporativos.**  
> No inventa. No alucina. Cita sus fuentes automáticamente.

EmpresaRAG utiliza **RAG (Retrieval-Augmented Generation)** para combinar:
- 🔍 **Búsqueda semántica** en documentos vectorizados.
- 🧠 **Generación inteligente** con GPT-4 / Gemini / Ollama.
- 📄 **Citas automáticas** de fuentes (documento + página).

---

## 🎬 Demo Visual

```text
┌─────────────────────────────────────────────────────────────┐
│  💬 Chat EmpresaRAG                                    🔒 Admin │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  👤 Usuario: ¿Cuál es la política de vacaciones?           │
│                                                             │
│  🤖 Bot: Según el Manual de RRHH, los empleados tienen:    │
│       -  15 días hábiles de vacaciones al año               │
│       -  Días adicionales por antigüedad                    │
│       -  Solicitud con 15 días de anticipación              │
│                                                             │
│       📄 Fuentes:                                          │
│       -  Manual_RRHH.pdf (Pág. 12)                          │
│       -  Politicas_2025.pdf (Pág. 8)                        │
│                                                             │
│  [Escribe tu pregunta...]                            [📤]   │
└─────────────────────────────────────────────────────────────┘
```

---

## ✨ Características Principales

<table>
<tr>
<td width="50%">

### 🧠 IA + RAG Pipeline

```text
┌─────────────────────────┐
│  📄 PDFs / Docs          │
│  ↓                      │
│  🔪 Chunking             │
│  ↓                      │
│  🧬 Embeddings            │
│  ↓                      │
│  🗄️ Vector DB (Chroma)    │
│  ↓                      │
│  🔍 Búsqueda Semántica    │
│  ↓                      │
│  🤖 LLM (OpenAI/Gemini)   │
│  ↓                      │
│  ✅ Respuesta + Fuentes   │
└─────────────────────────┘
```

- ✅ RAG completo (retrieve → generate).
- ✅ Vector DB (Chroma/FAISS/Pinecone).
- ✅ Respuestas con fuentes verificables.

</td>
<td width="50%">

### 💻 Frontend tipo WhatsApp

```text
┌──────────────────────┐
│  🔐 Login Seguro      │
│  ├─ JWT Auth          │
│  └─ Password Hash     │
│                      │
│  💬 Chat UI           │
│  ├─ Burbujas          │
│  ├─ Markdown          │
│  └─ Estado “pensando” │
│                      │
│  📁 Admin Docs         │
│  ├─ Upload PDFs        │
│  ├─ Listado            │
│  └─ Gestión            │
└──────────────────────┘
```

- ✅ Next.js 15 + TypeScript.
- ✅ Tailwind CSS moderno y responsive.

</td>
</tr>
</table>

---

## 🛠️ Stack Tecnológico

<div align="center">

### 🎨 Lenguajes & Frameworks

<table>
<tr>
<td align="center" width="100">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="44" height="44" alt="Python" /><br/>Python
</td>
<td align="center" width="100">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="44" height="44" alt="TypeScript" /><br/>TypeScript
</td>
<td align="center" width="100">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="44" height="44" alt="JavaScript" /><br/>JavaScript
</td>
<td align="center" width="100">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" width="44" height="44" alt="FastAPI" /><br/>FastAPI
</td>
<td align="center" width="100">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nextjs/nextjs-original.svg" width="44" height="44" alt="Next.js" /><br/>Next.js
</td>
<td align="center" width="100">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg" width="44" height="44" alt="React" /><br/>React
</td>
</tr>
</table>

### 🔧 IA / Backend

<table>
<tr>
<td align="center" width="120">
<img src="https://www.vectorlogo.zone/logos/openai/openai-icon.svg" width="44" height="44" alt="OpenAI" /><br/>OpenAI
</td>
<td align="center" width="120">
<img src="https://www.vectorlogo.zone/logos/chromadb/chromadb-icon.svg" width="44" height="44" alt="ChromaDB" /><br/>ChromaDB
</td>
<td align="center" width="120">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" width="44" height="44" alt="DB" /><br/>DB / Storage
</td>
<td align="center" width="120">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="44" height="44" alt="Docker" /><br/>Docker
</td>
</tr>
</table>

</div>

---

## 📊 Análisis del Stack (estilo gráfico)

```text
Backend (Python/FastAPI)     ████████████████████  96.5%
Frontend (TypeScript/React)  ████░░░░░░░░░░░░░░░░  1.78%
Styling (Tailwind CSS)       ██░░░░░░░░░░░░░░░░░░  0.93%
Config & Tools               █░░░░░░░░░░░░░░░░░░░  0.82%
```

### 🔥 Skills Destacados

| Categoría | Tecnologías | Nivel |
|---|---|---|
| Backend | FastAPI, Python, JWT | ⭐⭐⭐⭐⭐ |
| IA/ML | OpenAI, RAG, Vector DB | ⭐⭐⭐⭐⭐ |
| Frontend | Next.js, React, TypeScript | ⭐⭐⭐⭐⭐ |
| UI/UX | Tailwind CSS, Responsive UI | ⭐⭐⭐⭐⭐ |
| DevOps | Docker, Git | ⭐⭐⭐⭐⚪ |

---

## 🏗️ Arquitectura del Sistema

> Nota: Se evita Mermaid aquí para no causar errores de render en GitHub cuando se combinan estilos/hex o texto fuera del bloque (problema típico de parseo). [web:62][web:66]

```text
┌───────────────────────────────────────────────────────────┐
│                        🌐 Frontend                         │
│                  Next.js 15 + Tailwind                     │
│          (Login / Chat / Admin Docs / Markdown UI)          │
└───────────────▲───────────────────────────────┬────────────┘
                │ HTTP (JWT)                     │
                │                                │
┌───────────────┴───────────────────────────────▼────────────┐
│                         ⚡ Backend                           │
│                       FastAPI (REST)                         │
│    Auth (JWT)  |  Docs Upload  |  Chat Query (RAG)           │
└───────────────▲───────────────────────────────┬────────────┘
                │ retrieve                        │ generate
                │                                 │
        ┌───────┴────────┐                 ┌──────┴──────────┐
        │  📊 Vector DB   │                 │   🤖 LLM/GenAI   │
        │ Chroma/FAISS    │                 │ OpenAI/Gemini    │
        └─────────────────┘                 └─────────────────┘
```

---

## 📂 Estructura del Proyecto

```text
EmpresaRAGChatbot/
├── backend/                 # FastAPI + RAG Engine
│   ├── app/
│   │   ├── api/routes/      # auth / chat / docs
│   │   ├── rag/             # embeddings / vector store / pipeline
│   │   ├── core/            # config / security (JWT)
│   │   └── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/                # Next.js 15 + Tailwind
│   ├── app/                 # login / chat / admin/docs
│   ├── src/                 # components / hooks / lib
│   ├── package.json
│   └── Dockerfile
└── docker-compose.yml
```

---

## 🎯 Cómo Usar

### 1️⃣ Registro e Inicio de Sesión

```text
┌────────────────────────────────┐
│  🔐 Bienvenido a EmpresaRAG     │
│                                │
│  👤 Usuario:  [________]       │
│  📧 Email:    [________]       │
│  🔒 Password: [________]       │
│                                │
│      [🚀 Registrarse]          │
│                                │
│  ¿Ya tienes cuenta? [Login]    │
└────────────────────────────────┘
```

### 2️⃣ Subir Documentos

```text
┌─────────────────────────────────────┐
│  📁 Gestión de Documentos           │
├─────────────────────────────────────┤
│  📤 Arrastra PDFs aquí              │
│      o haz clic para seleccionar    │
│                                     │
│  [📄 Seleccionar PDF]               │
│                                     │
│  ✅ Documentos indexados:           │
│  -  Manual_RRHH.pdf                  │
│  -  Politicas_2025.pdf               │
│  -  FAQ_TI.pdf                       │
└─────────────────────────────────────┘
```

### 3️⃣ Chatear con tus Documentos

**Pregunta:** “¿Cuántos días de home office tengo?”

```text
🤖 Según la Política de Trabajo Remoto 2025:

-  2 días de home office por semana
-  Días adicionales con aprobación
-  Solicitud con 48h de anticipación

📄 Fuentes:
-  Politicas_2025.pdf (Pág. 15-16)
-  Manual_RRHH.pdf (Pág. 34)
```

---

## 📈 Métricas (demo)

```text
┌──────────────────────────────────────────────┐
│  📈 Métricas de Desarrollo                   │
├──────────────────────────────────────────────┤
│  Total Commits:         61                   │
│  Archivos Backend:      25                   │
│  Archivos Frontend:     18                   │
│  Cobertura:             87%                  │
│  Tiempo de Respuesta:   < 2s                 │
└──────────────────────────────────────────────┘
```

---

## 💬 Let's Connect!

<div align="center">

Siempre abierto a proyectos innovadores, colaboraciones tech y oportunidades freelance.

📧 **Email:** jhonharveytipas@gmail.com  
💼 **LinkedIn:** Jhon Harvey Tipas Solis  
📱 **WhatsApp:** +57 311 776 9235  

</div>

---

<div align="center">

**Hecho con ❤️ y ☕ por Jhon Harvey Tipas Solis**

```text
╔══════════════════════════════════════════════╗
║  🤖 EmpresaRAG - RAG Chatbot (2026)          ║
║  Transformando documentos en conocimiento    ║
║  conversacional para equipos y empresas      ║
╚══════════════════════════════════════════════╝
```

</div>
```
