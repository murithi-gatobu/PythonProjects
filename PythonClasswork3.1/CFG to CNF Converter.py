import copy
from collections import defaultdict

class CFGtoCNF:
    def __init__(self, rules, start_symbol):
        self.grammar = defaultdict(list)
        for lhs, rhs_list in rules.items():
            for rhs in rhs_list:
                self.grammar[lhs].append(rhs.split())
        self.start_symbol = start_symbol
        self.new_symbol_count = 0

    def get_new_symbol(self):
        self.new_symbol_count += 1
        return f"X{self.new_symbol_count}"

    def remove_null_productions(self):
        nullable = set()
        for lhs in self.grammar:
            for rhs in self.grammar[lhs]:
                if rhs == ['ε']:
                    nullable.add(lhs)

        while True:
            changed = False
            for lhs in self.grammar:
                for rhs in self.grammar[lhs]:
                    if all(symbol in nullable for symbol in rhs):
                        if lhs not in nullable:
                            nullable.add(lhs)
                            changed = True
            if not changed:
                break

        new_grammar = defaultdict(list)
       
