<div align="center">

<!-- Animated Header -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,40:1a0533,100:0d2137&height=220&section=header&text=Aayush%20Katoch&fontSize=65&fontColor=c792ea&animation=fadeIn&fontAlignY=35&desc=MS%20Data%20Science%20%40%20Northeastern%20%7C%20Data%20Science%20%7C%20AI%20Researcher&descAlignY=58&descSize=17&descColor=79c0ff" width="100%"/>

<!-- Typing Animation -->
[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=C792EA&center=true&vCenter=true&multiline=true&repeat=false&width=900&height=100&lines=Computer+Vision+%7C+NLP+%7C+Medical+Imaging+%7C+Satellite+AI;Published+Researcher+%7C+Ex-ISRO+%7C+Ex-DRDO+%7C+NEU+TA)](https://git.io/typing-svg)

<!-- Social Badges -->
<p>
<a href="https://linkedin.com/in/aayush-katoch-a47413175"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
<a href="https://github.com/Aayush99000"><img src="https://img.shields.io/badge/GitHub-c792ea?style=for-the-badge&logo=github&logoColor=black"/></a>
<a href="mailto:katoch.aa@northeastern.edu"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
<a href="https://leetcode.com/u/aayush99000/"><img src="https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black"/></a>
<a href="https://kaggle.com/aayushkatoch/"><img src="https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white"/></a>
<a href="https://www.tensortonic.com/profile"><img src="https://img.shields.io/badge/TensorTonic-c792ea?style=for-the-badge&logo=tensorflow&logoColor=white"/></a>
</p>

<img src="https://komarev.com/ghpvc/?username=Aayush99000&style=for-the-badge&color=c792ea" alt="Profile Views"/>

</div>

---

## 🧠 About Me

```python
import torch
import torch.nn as nn
from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class ResearcherConfig:
    name:       str  = "Aayush Katoch"
    location:   str  = "Fremont, CA 🌉"
    education:  str  = "MS Data Science @ Northeastern University (Silicon Valley)"
    gpa_track:  str  = "Expected Dec 2027"

    # Current roles
    roles: List[str] = field(default_factory=lambda: [
        "Teaching Assistant — CS5800 Algorithms @ NEU",
        "Published Researcher — Satellite AI & Medical Imaging",
    ])

    # Research background
    experience: Dict[str, str] = field(default_factory=lambda: {
        "ISRO (SAC)"  : "Cloud segmentation · Image captioning · 98% acc · BLEU-1 0.8406",
        "DRDO (SSPL)" : "Military vehicle detection · YOLOv8-m · 80.41% mAP · 22% faster inference",
    })

    # Model specializations
    expertise: List[str] = field(default_factory=lambda: [
        "Computer Vision & Segmentation",
        "NLP · LLMs · RAG Pipelines",
        "Medical Imaging under Data Scarcity",
        "Satellite & Geospatial AI",
        "Generative Models & Motion Synthesis",
    ])

    optimizer:   str  = "Curiosity-driven learning 🔍"
    loss_fn:     str  = "Impact on real-world systems"
    convergence: str  = "Deep understanding over surface familiarity"


class AayushKatoch(nn.Module):
    def __init__(self, config: ResearcherConfig):
        super().__init__()
        self.config   = config
        self.backbone = "Research @ ISRO + DRDO"
        self.head     = "MS Data Science @ Northeastern"

    def forward(self, problem: str) -> str:
        features   = self._extract_deep_features(problem)
        solution   = self._reason_and_build(features)
        return f"📦 Portfolio-worthy output: {solution}"

    def _extract_deep_features(self, x): ...
    def _reason_and_build(self, x): ...

    def say_hi(self):
        print("Let's build something that actually ships 🚀")


model = AayushKatoch(ResearcherConfig())
model.say_hi()
# >>> Let's build something that actually ships 🚀
```

---

## 🚀 What I'm Currently Working On

<table>
<tr>
<td width="50%">

### ✈️ TripCraft (NLP Course Project)
AI-powered travel itinerary generator
- Slot filling for intent & entity extraction
- RAG pipeline with **ChromaDB** + **Groq (Llama 3)**
- Streamlit frontend for interactive planning
- End-to-end NLP architecture from scratch

</td>
<td width="50%">

### 🎯 Active Research Interests
- 🛰️ **Satellite AI** — Segmentation, Captioning, GIS
- 🤖 **LLMs & RAG** — ChromaDB, LangChain, Groq
- 🩺 **Medical Imaging** — Low-resource transfer learning
- 🕺 **Motion Generation** — Sign language, SMPL-X, diffusion
- 📚 **Algorithms** — DP, Greedy, Graph Theory (TA)

</td>
</tr>
</table>

---

## 🗺️ My Journey

```mermaid
timeline
    title Career & Research Timeline
    2020-2024 : Manipal University Jaipur
              : B.Tech — Computer & Communication Engineering
    2023      : ISRO — Space Applications Centre (SAC)
              : Research Intern · Ahmedabad, India
              : Cloud Segmentation · Image Captioning · Published @ Springer 2024
    2024      : DRDO — SSPL
              : Research & Technical Intern · New Delhi, India
              : Military Vehicle Detection · YOLOv8 · Published @ IEEE SCES 2024
    2025-2027 : Northeastern University
              : MS Data Science · Silicon Valley Campus
              : TA for CS5800 Algorithms · Jan–May 2026
```

---

## 🛠️ Tech Arsenal

### 🤖 Deep Learning & Computer Vision
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0097A7?style=for-the-badge&logo=google&logoColor=white)
![CUDA](https://img.shields.io/badge/CUDA-76B900?style=for-the-badge&logo=nvidia&logoColor=white)

### 🔍 NLP, LLMs & RAG
![HuggingFace](https://img.shields.io/badge/🤗_HuggingFace-FFD21E?style=for-the-badge&logoColor=black)
![LangChain](https://img.shields.io/badge/🦜_LangChain-1C3C3C?style=for-the-badge&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6F00?style=for-the-badge&logoColor=white)
![Groq](https://img.shields.io/badge/Groq_Llama3-F54E27?style=for-the-badge&logoColor=white)
![spaCy](https://img.shields.io/badge/spaCy-09A3D5?style=for-the-badge&logo=spacy&logoColor=white)

### 💻 Languages
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![R](https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)

### 🌐 Backend, Tools & Cloud
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

---

## 🔬 Featured Projects

<div align="center">
<table>
<tr>
<td width="50%">
<h3 align="center">🛰️ Cloud Detection on Satellite Data</h3>
<p align="center">
<img src="https://img.shields.io/badge/UNet-Attention_UNet-c792ea?style=flat-square"/>
<img src="https://img.shields.io/badge/Acc-98%25-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Dice-93%25-success?style=flat-square"/>
</p>
<p>Deep learning segmentation on LANDSAT satellite imagery. Transfer Learning outperformed scratch-trained CNN by 6% Dice score. <strong>Published @ IEEE SCES 2024.</strong></p>
</td>
<td width="50%">
<h3 align="center">🖼️ Satellite Image Captioning</h3>
<p align="center">
<img src="https://img.shields.io/badge/EfficientNet_B7-LSTM-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/BLEU--1-0.8406-orange?style=flat-square"/>
<img src="https://img.shields.io/badge/Acc-94.05%25-success?style=flat-square"/>
</p>
<p>Encoder-decoder benchmarking (VGG-19, ResNet-50, DenseNet-201, EfficientNet-B7 + LSTM) on Sydney & RSICD datasets. Best: EfficientNet-B7 + LSTM. <strong>Published @ Springer ISMS 2023.</strong></p>
</td>
</tr>
<tr>
<td width="50%">
<h3 align="center">🩺 <a href="https://github.com/Aayush99000">Low-Resource Medical Imaging</a></h3>
<p align="center">
<img src="https://img.shields.io/badge/DenseNet121-ResNet50-EE4C2C?style=flat-square"/>
<img src="https://img.shields.io/badge/AUC-0.9875-blueviolet?style=flat-square"/>
<img src="https://img.shields.io/badge/~300_samples-K--Fold-yellow?style=flat-square"/>
</p>
<p>Empirical study under extreme data scarcity (~300 samples) — scratch vs ImageNet vs MedSIGLIP. ImageNet pretraining gave <strong>+14% accuracy</strong> (78% → 92%). AUC: 0.9875.</p>
</td>
<td width="50%">
<h3 align="center">💪 <a href="https://github.com/Aayush99000/RAG-Fitness-Assistant">RAG Fitness Assistant</a></h3>
<p align="center">
<img src="https://img.shields.io/badge/MediaPipe-Pose-0097A7?style=flat-square"/>
<img src="https://img.shields.io/badge/LangChain-RAG-1C3C3C?style=flat-square"/>
<img src="https://img.shields.io/badge/500%2B_exercises-DB-green?style=flat-square"/>
</p>
<p>Real-time AI fitness coach — Groq/Llama 3 + ChromaDB + MediaPipe pose estimation. Personalized workout plans with live form feedback via Streamlit.</p>
</td>
</tr>
<tr>
<td width="50%">
<h3 align="center">🕺 Text-to-Sign Motion Generation</h3>
<p align="center">
<img src="https://img.shields.io/badge/SMPL--X-BVH-c792ea?style=flat-square"/>
<img src="https://img.shields.io/badge/55_joints-30_FPS-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/~12k-Training_Samples-orange?style=flat-square"/>
</p>
<p>Baseline pipeline mapping natural language → realistic sign language motion sequences (T × 668 skeletal features). Modular Text → Gloss → Motion stages with extensibility for diffusion synthesis.</p>
</td>
<td width="50%">
<h3 align="center">🔍 RAG Job Filter Extension</h3>
<p align="center">
<img src="https://img.shields.io/badge/Chrome-Extension-4285F4?style=flat-square"/>
<img src="https://img.shields.io/badge/BERT-Embeddings-yellow?style=flat-square"/>
<img src="https://img.shields.io/badge/Flask-Backend-000000?style=flat-square"/>
</p>
<p>Chrome extension for semantic job filtering using BERT-based embeddings and a Flask backend. RAG-powered relevance scoring against your profile in real time.</p>
</td>
</tr>
</table>
</div>

---

## 📊 GitHub & LeetCode Stats

<div align="center">

<img height="180em" src="https://github-readme-stats.vercel.app/api?username=Aayush99000&show_icons=true&theme=midnight-purple&include_all_commits=true&count_private=true&hide_border=true&bg_color=0d1117&title_color=c792ea&icon_color=79c0ff&text_color=cdd9e5"/>
<img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Aayush99000&layout=compact&theme=midnight-purple&hide_border=true&bg_color=0d1117&title_color=c792ea&text_color=cdd9e5"/>

<img src="https://github-readme-streak-stats.herokuapp.com/?user=Aayush99000&theme=midnight-purple&hide_border=true&background=0d1117&ring=c792ea&fire=79c0ff&currStreakLabel=c792ea" />

<br/>

<a href="https://leetcode.com/u/aayush99000/">
<img src="https://leetcard.jacoblin.cool/aayush99000?theme=dark&font=Fira%20Code&ext=heatmap&border=0&radius=20" alt="LeetCode Stats"/>
</a>

</div>

---

## 📄 Publications

<div align="center">

| Year | Title | Venue |
|:----:|:------|:------|
| 2024 | **Image Captioning of Satellite Images Using Transfer Learning and LSTM Blending** | Springer — AI Technologies for Information Systems (ISMS 2023), LNNS vol. 1136 |
| 2024 | **Enhancing Cloud Detection Performance: A Comparative Study of CNN Models** | IEEE Students Conference on Engineering and Systems (SCES), Prayagraj |

</div>

---

## 🏆 Impact at a Glance

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                                                                                  │
│  🛰️  ISRO (SAC)          →  98% accuracy · 93% Dice · BLEU-1 0.8406            │
│  🔬  DRDO (SSPL)         →  80.41% mAP · 22% faster inference · 96.5% cls acc  │
│  🩺  Medical Imaging     →  +14% accuracy · AUC 0.9875 · ~300 sample regime    │
│  📖  Publications        →  IEEE SCES 2024 · Springer LNNS 2024                │
│  📚  CS5800 TA @ NEU     →  Algorithms — DP, Greedy, Graph Theory              │
│  🕺  Motion Generation   →  Text → Sign · 55-joint SMPL-X · 12k samples        │
│                                                                                  │
└──────────────────────────────────────────────────────────────────────────────────┘
```

---

<div align="center">

### 🤝 Let's Connect & Collaborate!

**Open to research collaborations, ML engineering roles, and everything at the intersection of AI + real-world impact.**

<a href="https://linkedin.com/in/aayush-katoch-a47413175">
<img src="https://img.shields.io/badge/Connect_on_LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/>
</a>

<br><br>

<i>"The model only generalizes if you understand the distribution." 📊</i>

</div>

<!-- Footer Wave -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,40:1a0533,100:0d2137&height=120&section=footer" width="100%"/>
