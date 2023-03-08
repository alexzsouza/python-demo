from usecase.statement.port.execute_statement import ExecuteStatement


class ExecuteStatementIfImpl(ExecuteStatement):

    def execute(self):
        print('execute-statement-if-impl')
        if self.parameter is None:
            print('no parameter')

        if self.parameter is not None:
            print('parameter is different none')

        if self.parameter >= 0:
            print('parameter greater than or equal to zero')

        if self.parameter < 0:
            print('parameter less than zero')

        if 'orange' in self.fruits:
            print('there is orange in the list')

        if self.validate is True:
            print('validated')

        print(False) if self.validate is False else print(True)

        if self.validate is True: print('One line if statement')

        if self.parameter < 0 and self.validate is True:
            print('Both parameters are true')

        if self.parameter < 0 or self.validate is True:
            print('One of the parameters must be true')

        if self.parameter > 0:
            print('is greater to zero')
        else:
            print('is less to zero')


