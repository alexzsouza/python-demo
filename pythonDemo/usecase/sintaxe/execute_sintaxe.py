from usecase.statement.execute_statement_date_impl import ExecuteStatementDateImpl
from usecase.statement.execute_statement_for_impl import ExecuteStatementForImpl
from usecase.statement.execute_statement_if_impl import ExecuteStatementIfImpl
from usecase.statement.port.execute_statement import ExecuteStatement


class ExecuteSintaxe:
    def __init__(self, event):
        self.event = event
        self.statement = ExecuteStatement()

    def execute(self):
        print('executar-demo-sintaxe')
        self.statement = [ExecuteStatementIfImpl(), ExecuteStatementForImpl(), ExecuteStatementDateImpl()]

        for sta in self.statement:
            sta.execute()

