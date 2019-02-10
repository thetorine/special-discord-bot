import re

# Exact
# Separated by a non-alphanumeric character
# Subset

def contains_pattern(string, pattern):
    merged_string = re.sub(r'(\W|_)+', '', string)
    return merged_string.find(pattern) != -1
