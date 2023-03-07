from usecase.statement.port.execute_statement import ExecuteStatement


class ExecuteStatementDateImpl(ExecuteStatement):
    def execute(self):
        print('execute-statement-date-imp')
