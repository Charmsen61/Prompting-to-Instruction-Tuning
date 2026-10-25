README.md
NLP_InstructionTuning

Name: Calvin Harmsen
 Course: Natural Language Processing
 Assignment: 9.5 - From Prompting to Instruction Tuning
 Date: 10/21/2026

Project Overview

This project explores the difference between prompt-only behavior and instruction-tuned behavior in language models. The goal is to demonstrate how providing examples can improve a model's ability to follow instructions.

The experiment compares model performance across three different tasks:

Translation,

Explanation for a child,

Summarization

A failure case is also included to show that instruction tuning improves behavior but does not completely eliminate reasoning mistakes.

Part 1: Prompt-Only Behavior

The model receives a direct instruction without examples and attempts to complete the task.

Part 2: Simulated Instruction Tuning

The model is given examples of the desired input-output format before completing the task.

Part 3: Comparison Analysis

The outputs from prompt-only and instruction-tuned approaches are compared to identify improvements in instruction following.

Part 4: Failure Case

A reasoning task demonstrates that even with instruction examples, the model can still generate incorrect answers.

Key Findings

Instruction examples improved consistency and formatting.

Translation and explanation tasks showed the largest improvements.

Summarization became more concise after examples were provided.

Instruction tuning helps guide behavior but does not guarantee correct reasoning.

Models can still fail on tasks that require multi-step calculations or logic.
