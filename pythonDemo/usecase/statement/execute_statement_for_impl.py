from usecase.statement.port.execute_statement import ExecuteStatement


class ExecuteStatementForImpl(ExecuteStatement):
    def execute(self):
        print('execute-statement-for-impl')
