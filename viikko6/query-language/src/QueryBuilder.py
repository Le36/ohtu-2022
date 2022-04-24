import matchers


class QueryBuilder:
    def __init__(self, pino=matchers.All()):
        self.stack = pino

    def build(self):
        return self.stack

    def playsIn(self, team):
        return QueryBuilder(matchers.And(self.stack, matchers.PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(matchers.And(self.stack, matchers.HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(matchers.And(self.stack, matchers.HasFewerThan(value, attr)))

    def oneOf(self, *queries):
        return QueryBuilder(matchers.Or(*queries))
