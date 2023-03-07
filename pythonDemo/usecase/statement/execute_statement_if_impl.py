from usecase.statement.port.execute_statement import ExecuteStatement


class ExecuteStatementIfImpl(ExecuteStatement):
    def execute(self):
        print('execute-statement-if-impl')
