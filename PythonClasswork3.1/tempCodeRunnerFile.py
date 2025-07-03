import copy

class CFGtoCNF:
    def __init__(self, productions):
        self.productions = productions  # Original grammar (dict of lists)
        self.cnf = {}  # Final CNF-form grammar
        self.new_var_count = 0  # For generating new variable names

    def get_new_var(self):
        self.new_var_count += 1
        return f"X{self.new_var_count}"

    def remove_epsilon(self):
        nullable = set()
        # Step 1: Find nullable variables
        for lhs, rules in self.productions.items():
            for rule in rules:
                if rule == ['ε']:
                    nullable.add(lhs)

        changed = True
        while changed:
            changed = False
            for lhs, rules in self.productions.items():
                for rule in rules:
                    if all(symbol in nullable for symbol in rule):
                        if lhs not in nullable:
                            nullable.add(lhs)
                            changed = True

        # Step 2: Remove epsilon-productions and update other rules
        new_productions = {}
        for lhs, rules in self.productions.items():
            new_rules = set()
            for rule in rules:
                if rule == ['ε']:
                    continue
                rule_len = len(rule)
                indices = [i for i, symbol in enumerate(rule) if symbol in nullable]
                for i in range(1 << len(indices)):
                    temp_rule = rule[:]
                    for j in range(len(indices)):
                        if (i >> j) & 1:
                            temp_rule[indices[j]] = None
                    new_rule = [s for s in temp_rule if s]
                    if new_rule:
                        new_rules.add(tuple(new_rule))
            new_productions[lhs] = [list(r) for r in new_rules]

        self.productions = new_productions

    def remove_unit(self):
        unit_pairs = set()
        for lhs, rules in self.productions.items():
            for rule in rules:
                if len(rule) == 1 and rule[0].isupper():
                    unit_pairs.add((lhs, rule[0]))

        changed = True
        while changed:
            changed = False
            new_pairs = set()
            for A, B in unit_pairs:
                if B in self.productions:
                    for rule in self.productions[B]:
                        if len(rule) == 1 and rule[0].isupper():
                            if (A, rule[0]) not in unit_pairs:
                                new_pairs.add((A, rule[0]))
            if new_pairs:
                unit_pairs |= new_pairs
                changed = True

        # Add non-unit rules from B to A
        new_productions = copy.deepcopy(self.productions)
        for A, B in unit_pairs:
            if B in self.productions:
                for rule in self.productions[B]:
                    if len(rule) != 1 or not rule[0].isupper():
                        if rule not in new_productions[A]:
                            new_productions[A].append(rule)
        # Remove unit rules
        for lhs in new_productions:
            new_productions[lhs] = [r for r in new_productions[lhs] if not (len(r) == 1 and r[0].isupper())]

        self.productions = new_productions

    def eliminate_terminals(self):
        # Replace terminals in long rules with new variables
        term_map = {}
        new_productions = copy.deepcopy(self.productions)
        for lhs, rules in new_productions.items():
            updated_rules = []
            for rule in rules:
                if len(rule) >= 2:
                    new_rule = []
                    for symbol in rule:
                        if symbol.islower() or symbol in ":yesnoabcdef":
                            if symbol not in term_map:
                                new_var = self.get_new_var()
                                term_map[symbol] = new_var
                                self.cnf[new_var] = [[symbol]]
                            new_rule.append(term_map[symbol])
                        else:
                            new_rule.append(symbol)
                    updated_rules.append(new_rule)
                else:
                    updated_rules.append(rule)
            new_productions[lhs] = updated_rules
        self.productions = new_productions

    def to_binary(self):
        # Ensure all productions are in binary form A → BC or A → a
        new_productions = {}
        for lhs, rules in self.productions.items():
            updated_rules = []
            for rule in rules:
                while len(rule) > 2:
                    new_var = self.get_new_var()
                    first, second = rule[0], rule[1]
                    updated_rules.append([first, new_var])
                    rule = [new_var] + rule[2:]
                    self.cnf[new_var] = [[second, rule[1]]] if len(rule) > 1 else [[second]]
                updated_rules.append(rule)
            new_productions[lhs] = updated_rules
        self.productions = new_productions

    def convert(self):
        self.remove_epsilon()
        self.remove_unit()
        self.eliminate_terminals()
        self.to_binary()
        self.cnf.update(self.productions)
        return self.cnf


# Sample extended grammar definition (partial)
grammar = {
    "S": [["V", "T", "B", "Sg"]],
    "V": [["id", "vote"]],
    "id": [["digit", "id"], ["digit"]],
    "vote": [["yes"], ["no"]],
    "T": [["ts"], ["T", "ts"]],
    "ts": [["digit", "digit", ":", "digit", "digit", ":", "digit", "digit"]],
    "digit": [["0"], ["1"], ["2"], ["3"], ["4"], ["5"], ["6"], ["7"], ["8"], ["9"]],
    "B": [["bio"]],
    "bio": [["Bchar", "Bchars"]],
    "Bchars": [["Bchar", "Bchars"], ["ε"]],
    "Bchar": [["A"], ["B"], ["C"], ["D"], ["E"], ["F"], ["G"], ["H"], ["I"], ["J"],
              ["K"], ["L"], ["M"], ["N"], ["O"], ["P"], ["Q"], ["R"], ["S"], ["T"],
              ["U"], ["V"], ["W"], ["X"], ["Y"], ["Z"]],
    "Sg": [["sig"]],
    "sig": [["hex", "hex", "hex", "hex"]],
    "hex": [["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["0"], ["1"], ["2"], ["3"],
            ["4"], ["5"], ["6"], ["7"], ["8"], ["9"]]
}

converter = CFGtoCNF(grammar)
cnf_result = converter.convert()
cnf_result
