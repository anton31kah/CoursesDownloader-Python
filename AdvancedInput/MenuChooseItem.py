from AdvancedInput.PrivateFuncs import PrivateFuncs
from Common.CommonFuncs import CommonFuncs
from Common.CommonVars import CommonVars
from SpecialActions.ActionState import ActionState
from SpecialActions.BaseAction import BaseAction


def ask_input_for_item_from_list(items_list, item_word, action_word="view", with_clear=True, inside_call=False):
	if with_clear:
		CommonFuncs.clear()

	if not inside_call:
		for prev_item in CommonVars.chosen_items_till_now.values():
			print(prev_item)

	print(f"Select the {item_word} you want to {action_word}:")

	width = len(str(len(items_list)))
	for i, item in enumerate(items_list, 1):
		print(f"[{i:{width}}] {item}")

	selected_item = None

	selected_item_isvalid = False
	while not selected_item_isvalid:
		chosen_item = input(f"And the {item_word} that you selected is >>> ")

		action = handle_action(chosen_item)
		if action.state == ActionState.found_and_handled:
			return action

		if not chosen_item.isdigit():
			continue

		item_idx = int(chosen_item) - 1

		if 0 <= item_idx < len(items_list):
			confirm_message = f"You chose: {CommonFuncs.trim_inner_spaces(items_list[item_idx])} right? [Y/N] "

			def on_yes_action():
				nonlocal selected_item
				nonlocal selected_item_isvalid

				selected_item = items_list[item_idx]
				selected_item_isvalid = True

			ask_yes_no_question(confirm_message, on_yes_action)
		else:
			print(f"The {item_word} you chose is out of bounds! Try again.")

	if not inside_call:
		CommonVars.chosen_items_till_now[item_word] = f"You chose {CommonFuncs.trim_inner_spaces(selected_item)}"

	return selected_item


def ask_input_for_items_from_list(items_list, items_word, action_word="download"):
	private_funcs = PrivateFuncs()
	validate_input = private_funcs.validate_input
	build_ranges_str = private_funcs.build_ranges_str
	del private_funcs

	CommonFuncs.clear()

	for prev_item in CommonVars.chosen_items_till_now.values():
		print(prev_item)

	print(f"Select the {items_word} you want to {action_word}: (range:x-y or set:x,y,z)")

	width = len(str(len(items_list)))
	for i, item in enumerate(items_list, 1):
		print(f"[{i:{width}}] {item}")

	selected_items = []

	selected_item_isvalid = False
	while not selected_item_isvalid:
		items_idx = input(f"And the {items_word} that you selected are >>> ")

		action = handle_action(items_idx)
		if action.state == ActionState.found_and_handled:
			return action

		result = validate_input(items_idx)

		if not result:
			continue

		result.extend(selected_items)
		result = CommonFuncs.sorted_unique_list(result)

		if result:
			fit_result = CommonFuncs.sorted_unique_list(list(filter(lambda x: x <= len(items_list), result)))

			valid = CommonFuncs.sorted_unique_list(fit_result)
			valid_str = build_ranges_str(valid)

			set_result = set(result)
			set_fit_result = set(fit_result)
			if set_result != set_fit_result:
				invalid = CommonFuncs.sorted_unique_list(list(set_result - set_fit_result))
				invalid_str = build_ranges_str(invalid)

				if valid_str:
					print(f"The following {items_word} are out of range: {invalid_str}")
					print(f"However these {items_word} are in range: {valid_str}")
					choices_possible = [
						f"Download only {valid_str} and ignore {invalid_str}",
						f"Download only {valid_str} and change {invalid_str}",
						f"Don't download {valid_str} and change the whole selection"
					]
				else:
					print(f"All of the following {items_word} are out of range: {invalid_str}")
					continue

				choice_selected = ask_input_for_item_from_list(
										choices_possible, "choice", "choose", with_clear=False, inside_call=True
									)

				if choice_selected == choices_possible[0]:
					selected_items.extend(valid)
					selected_item_isvalid = True
				elif choice_selected == choices_possible[1]:
					selected_items.extend(valid)
				elif choice_selected == choices_possible[2]:
					selected_items.clear()
			else:
				print(f"These {items_word} will be downloaded: {valid_str}")

				def on_yes_action():
					nonlocal selected_item_isvalid

					selected_items.extend(valid)
					selected_item_isvalid = True

				def on_no_action():
					selected_items.clear()

				ask_yes_no_question("Is that your choice? [Y/N] ", on_yes_action, on_no_action)

	selected_items = CommonFuncs.sorted_unique_list(selected_items)

	CommonVars.chosen_items_till_now[items_word] = f"You chose {build_ranges_str(selected_items)}"

	return list(map(lambda list_item: items_list[list_item - 1], selected_items))


def ask_yes_no_question(confirm_message, on_yes, on_no=None, on_other=None):
	final_answer = None

	confirmation_isvalid = False
	while not confirmation_isvalid:
		confirmation = input(confirm_message)
		confirmation = confirmation[0].lower() if confirmation else ''
		if confirmation == 'y':
			final_answer = True
			if on_yes:
				on_yes()
			confirmation_isvalid = True
		elif confirmation != 'n':
			if on_other:
				on_other()
			else:
				print("Wrong answer! Try again.")
		else:
			final_answer = False
			if on_no:
				on_no()
			confirmation_isvalid = True

	return final_answer


def handle_action(input_string):
	action = BaseAction()
	action = action.handle(input_string)
	return action
