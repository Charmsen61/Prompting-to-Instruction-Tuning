"""
From Prompting to Instruction Tuning

Name: calvin harmsen
Date: 10/21/26

"""

from dataclasses import dataclass
from typing import List


@dataclass
class ExperimentResult:
    task_name: str
    prompt_type: str
    prompt_text: str
    model_output: str
    followed_instructions: bool
    notes: str


# -----------------------------
# PRINTING FUNCTIONS
# -----------------------------
def print_result(result: ExperimentResult) -> None:
    print("=" * 70)
    print(f"Task: {result.task_name}")
    print(f"Prompt Type: {result.prompt_type}")

    print("\nPrompt:")
    print(result.prompt_text)

    print("\nModel Output:")
    print(result.model_output)

    print(f"\nFollowed Instructions: {result.followed_instructions}")
    print(f"Notes: {result.notes}")
    print("=" * 70)
    print()


def compare_results(prompt_only: ExperimentResult, instruction_tuned: ExperimentResult) -> None:
    print("#" * 70)
    print(f"COMPARISON FOR TASK: {prompt_only.task_name}")
    print("#" * 70)

    print("\nPrompt-Only Output:")
    print(prompt_only.model_output)

    print("\nInstruction-Tuned Output:")
    print(instruction_tuned.model_output)

    print("\nAnalysis:")
    if instruction_tuned.followed_instructions and not prompt_only.followed_instructions:
        print("-the instruction tuned version improved task following behavior")
    elif instruction_tuned.followed_instructions == prompt_only.followed_instructions:
        print("-the behavior stayed roughly the same")
    else:
        print("-the instruction tuned model did not improve the behavior")

    print(f"-prompt-only notes: {prompt_only.notes}")
    print(f"-instruction-tuned notes: {instruction_tuned.notes}")

    print()


# -----------------------------
# MAIN PROGRAM
# -----------------------------
def main() -> None:
    results: List[ExperimentResult] = []

    # ===================================================
    # TASK 1 (REQUIRED)
    # ===================================================

    #task1: Translation
    prompt_only_1 = ExperimentResult(
        task_name="Translation",
        prompt_type="Prompt-Only",
        prompt_text="Translate into spanish: Hello",
        model_output="Hello there,how are you today?",
        followed_instructions=False,
        notes="The response continued the phrase rather than translating it"
    )

    instruction_1 = ExperimentResult(
        task_name="Translation",
        prompt_type="Instruction-Tuned",
        prompt_text=(
            "Instruction:Translate to spanish \n"
            "Input:good morning\n"
            "Output:buenos dias\n\n"
            "Instruction: Translate to spanish\n"
            "Input: thank you\n"
            "Output: Gracias \n\n"
            "Instruction: Translate to spanish\n"
            "Input: hello\n"
            "Output:"
        ),
        model_output="hello",
        followed_instructions=True,
        notes="The demonstration helped the model produce the requested format"
    )

    results.append(prompt_only_1)
    results.append(instruction_1)

    # ===================================================
    # TASK 2 simple explanation
    # ===================================================

    prompt_only_2 = ExperimentResult(
        task_name="Explain to a child",
        prompt_type="Prompt-Only",
        prompt_text="Explain gravity to a 6-year old child",
        model_output="Gravity is a fundamental fore of attraction between objects with mass, described by classical and relativistic physics",
        followed_instructions=False,
        notes="The answer is relevant but not appropriate for a 6-year old"
    )

    instruction_2 = ExperimentResult(
        task_name="Explain to a child",
        prompt_type="Instruction-Tuned",
        prompt_text=(
            "Instruction:Explain a science idea to a young child using simple words \n"
            "Input:Photosynthesis\n"
            "Output: Plants use sunlight to make their own food\n\n"
            "Instruction:Explain a science idea to a young child using simple words \n"
            "Input:Evaporation \n"
            "Output: Water can turn into a invisible gas in the air  \n\n"
            "Instruction:Explain a science idea to a young child using simple words \n"
            "Input: Gravity\n"
            "Output:"
        ),
        model_output="gravity is what makes things fall down instead of floating away.",
        followed_instructions=True,
        notes="The example guide the tone, lengthen and difficulty level"
    )

    results.append(prompt_only_2)
    results.append(instruction_2)

    # ===================================================
    # TASK 3 summarization
    # ===================================================

    paragraph = (
        "the school science fair will take place next friday in the gymnasium."
        "Students from grade 6 though 8 will present projects on biology, chemistry,"
        "physics, and engineering. Families are invited ot attend in the evening"
    )

    prompt_only_3 = ExperimentResult(
        task_name="summarization",
        prompt_type="Prompt-Only",
        prompt_text=f"summarize the following paragraph {paragraph} ",
        model_output=(
            "The school science fair will take place in the gym and"
            "students will present projects"
        ),
        followed_instructions=True,
        notes="This one worked decently without demonstrations"
    )

    instruction_3 = ExperimentResult(
        task_name="summarization",
        prompt_type="Instruction-Tuned",
        prompt_text=(
            "Instruction: summerize the paragraph in one short sentence,\n"
            "input: the town library is holding a sale this weekend with fiction, history, and children's books\n"
            "output: The library is holding a weekend books sale\n"
            "Instruction: summerize the paragraph in one short sentence,\n"
            "input: The are club will meet Tuesday after school to prepare painting for spring showcase\n"
            "output:the art club will meet tuesday to prepare for the showcase\n"
            "Instruction: summerize the paragraph in one short sentence,\n"
            f"input:{paragraph}\n"
            "output:"

        ),
        model_output="The school will host a science fair next friday with student projects.",
        followed_instructions=True,
        notes="The demonstration made the summary more concise"
    )

    results.append(prompt_only_3)
    results.append(instruction_3)

    # ===================================================
    # REQUIRED FAILURE CASE
    # ===================================================

    failure_case = ExperimentResult(
        task_name="Failure Case: complex reasoning",
        prompt_type="Instruction-Tuned",
        prompt_text=(
            "Instruction: solve the problem step by tep and give the final answer,\n"
            "input: If a train leaves at 2.15pm and arrives at 5.45 pm, how long was the trip?\n"
            "output:The trip lasted 3 hours and 30 minutes\n"
            "Instruction: solve the problem step by tep and give the final answer,\n"
            "input:A store had 50 apples, sold 18, and received 12 more. how many apples ar there now?\n"
            "output:50-18=32 then 32+12=44 final answer = 44 apples\n" 
            "Instruction: solve the problem step by tep and give the final answer,\n"
            "input:John has 3 boxes with 8 markers in each box and buys 5 more markers. How many marker dose John have?\n"
            "output:"
        ),
        model_output="3+8+5=16 Final answer = 16",
        followed_instructions=False,
        notes=(
           "The model followed the format but failed the reasoning"
           "It added instead of multiplying 3*8 first"
        )
    )

    results.append(failure_case)

    # ===================================================
    # PRINT RESULTS
    # ===================================================
    print("\nALL RESULTS\n")

    for result in results:
        print_result(result)

    # ===================================================
    # COMPARISONS
    # ===================================================
    compare_results(prompt_only_1, instruction_1)
    compare_results(prompt_only_2, instruction_2)
    compare_results(prompt_only_3, instruction_3)


if __name__ == "__main__":
    main()