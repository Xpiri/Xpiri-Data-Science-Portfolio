## Roberta fine-tuning for ambiguous text classification 

This notebook is a simple application of transformers (Roberta) for the data challenge ConvAI3: Clarifying Questions for Open-Domain Dialogue Systems (ClariQ) that was held in 2020. 

The challenge was composed of several steps: 
- Step 1: When to ask clarifying questions during dialogues? 
This essentially means identifying whenever an user query requires clarification and, instead of providing an answer, the system should instead return a clarifying question.
- Step 2: How to generate the clarifying questions? 
Once the system has decided that it should ask a clarifying question, the system should pick the best one for the topic of interest.

The notebook *clariq_RQ1.ipynb* aims at tackling the first step by fine-tuning a RoBERTa transformer on the clariQ test set. This script only needs some finishing touches (slightly improving the model's performance).

The notebook for step 2 is still a work-in-progress that I hope to be able to release soon! 
