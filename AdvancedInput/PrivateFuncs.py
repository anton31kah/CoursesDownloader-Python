import re

import more_itertools as mit

from Common.CommonFuncs import CommonFuncs


class PrivateFuncs:
	@staticmethod
	def validate_input(input_str):
		valid_regex = r"^\d+((,\d+)*|(\-\d+)*)+(\d+)?$"
		input_str = CommonFuncs.remove_inner_spaces(input_str)
		if re.match(valid_regex, input_str):
			expanded = []
			sequences = input_str.split(',')
			for sequence in sequences:
				if '-' in sequence:
					limits = sequence.split('-')
					limits = tuple(int(limit) for limit in limits)
					if len(limits) == 2:
						lower_limit, upper_limit = limits
					else:
						limits = CommonFuncs.sorted_unique_list(limits)
						lower_limit, upper_limit = limits[0], limits[-1]
					if not CommonFuncs.are_ascending(limits):
						return None
					expanded.extend(range(lower_limit, upper_limit + 1))
				else:
					expanded.append(int(sequence))
			return CommonFuncs.sorted_unique_list(list(filter(lambda x: x > 0, CommonFuncs.sorted_unique_list(expanded))))
		else:
			return None

	@staticmethod
	def find_ranges(iterable):
		for group in mit.consecutive_groups(iterable):
			group = list(group)
			if len(group) == 1:
				yield (group[0],)
			else:
				yield group[0], group[-1]

	def build_ranges_str(self, iterable):
		# join everything with ', '
		# for single unit ranges just join them (those lone elements (not belonging to ranges))
		# for ranges join the limits with '-' and join them to the rest
		return ", ".join(
			str(doc_range[0])
			if len(doc_range) == 1
			else "-".join(
				str(limit) for limit in doc_range
			)
			for doc_range in self.find_ranges(iterable)
		)
