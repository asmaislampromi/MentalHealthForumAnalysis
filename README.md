# MentalHealthForumAnalysis

## Project Description

This repository explores mental health risks by analyzing user-generated content from Reddit and Beyond Blue forums using large language models (LLMs) and network analysis. The project aims to detect, classify, and measure emotional expressions, flag high-risk posts, and track trends to support early detection and awareness.

## Objectives

- Detect and classify forum posts containing mental health-related content using LLMs and machine learning.
- Identify emotion subtypes (such as grief, hopelessness, guilt) and assign severity scores.
- Flag high-risk content with rule-based alerts.
- Track emotional trends over time and visualize symptom co-occurrence through network graphs.
- Compare emotional expression, risk indicators, and discussion patterns between global (Reddit) and Australian (Beyond Blue) forums.

## Methods

- Data collection via web scraping and keyword filtering from Reddit and Beyond Blue.
- Preprocessing: text cleaning, tokenization, and normalization.
- Model development: fine-tuning transformer models (RoBERTa, BERT) and testing classical ML baselines as needed.
- Emotion subtype and severity detection, crisis flagging, and temporal analysis.
- Network analysis for symptom clustering and emotional trajectories.

## Background

Inspired by recent research:
- Han et al. (2023): Subclassifying negative emotions in social media for enhanced sentiment analysis.
- Wu et al. (2024): Hybrid LLM and rule-based systems for crisis detection.
- Xu et al. (2021): Hybrid statistical and semantic models with social network analysis.
- Kaiser et al. (2023): Tracking emotional transitions during crises.
- Uddin et al. (2022): Sentiment analysis and ML for mental health signals.

## References

Han, J., Zhao, Y. & Qian, C. (2023). Subclassifying sadness: Enhancing sentiment analysis in social media with large language models. Proceedings of the 12th International Conference on Affective Computing and Intelligent Interaction.

Kaiser, M., Ahmad, T. & Lin, J. (2023). Emotional transitions and resilience during crises: Insights from social media data. Journal of Medical Internet Research, 25, e32731.

Uddin, M., Salah, A. & Karray, F. (2022). Sentiment analysis of public social media as a tool for health-related topics. Information Systems Frontiers.

Wu, Z., Zhang, Y., Liu, M. & Xu, H. (2024). Psychological health knowledge-enhanced llm-based social network crisis intervention text transfer recognition method. arXiv preprint arXiv:2401.00012.

Xu, L., Zhang, M. & Zhang, Z. (2021). A hybrid statistical and semantic model for identification of mental health and behavioral disorders using social network analysis. Soft Computing, 25(18), 12023–12038.
