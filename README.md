A python script that converts questions in json format like below:

{
  "question": "A flashing red traffic light signifies that a driver should do what?",
  "A": "stop",
  "B": "speed up",
  "C": "proceed with caution",
  "D": "honk the horn",
  "answer": "A"
}

into csv format matching Actions on Google's [Multiple Choice
spreadsheet](https://docs.google.com/spreadsheets/d/1lVQGbviQlHwNYALsajtTqj1lt_lgswV_MykiT1ug4vo/edit?usp=sharing)

The input data set is from [this reddit
post](https://www.reddit.com/r/datasets/comments/3j14vx/dataset_multiple_choice_trivia_questions_like/)
and is used to create [Random
Trivia](https://assistant.google.com/services/a/uid/00000051254c46ed?hl=en) app
on Google Assistant. 

# Usage: convert_json_action_csv.py input.json [output_file_name]
