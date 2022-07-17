import test_cases as ts
from utils import *
import bangla_sandhi_rules as bs_rules

test_cases_add = ts.test_cases_add
test_cases_split = ts.test_cases_split

# generate_patterns(bs_rules.swara_sandhi_rules)
# generate_patterns(bs_rules.byanjan_sandhi_rules)
# create_word_library()

sandhi_adder_tester(ts.test_cases_add)
sandhi_splitter_tester(test_cases_split)


