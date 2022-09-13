from prompts.gsm import gsm_task_id_to_prompt
from prompts.sports import sports_task_id_to_prompt
from prompts.date import date_task_id_to_prompt

task_id_to_prompt = dict()
task_id_to_prompt.update(gsm_task_id_to_prompt)
task_id_to_prompt.update(sports_task_id_to_prompt)
task_id_to_prompt.update(date_task_id_to_prompt)