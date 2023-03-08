from usecase.statement.port.execute_statement import ExecuteStatement


class ExecuteStatementForImpl(ExecuteStatement):
    def execute(self):
        print('execute-statement-for-impl')

        users = {'Daiana': 'active', 'Lucas': 'block', 'Alex': 'block'}
        for user, status in users.items():
            if status == 'active':
                print(f'active user {user}')

        for i in range(2):
            print(i)

        for n in range(3, 5):
            print(n)

        for x in self.fruits:
            if x == 'strawberry':
                print(f'stop {x}')
                break
