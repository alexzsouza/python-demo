from usecase.statement.port.execute_statement import ExecuteStatement
from datetime import datetime, timedelta, timezone


class ExecuteStatementDateImpl(ExecuteStatement):
    def execute(self):
        print('execute-statement-date-imp')

        date_time_one = datetime.now()
        print(f'one - {date_time_one}')
        print(f'one - {date_time_one.strftime("%d-%m-%Y")}')

        date_time_two = datetime.today()
        print(f'two - {date_time_two}')
        print(f'two - {date_time_two.strftime("%d-%m-%Y")}')

        date_time_three = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]
        print(f'three - {str(date_time_three)}-03:00')

        data_time_four = datetime.now().astimezone(timezone.utc) - timedelta(hours=3)
        print(f"four - {data_time_four.isoformat(timespec='milliseconds').replace('+00:00', '-03:00')}")

        data_time_six = '09-03-2023 09:46:30'
        print(str('{}'.format(datetime.strptime(data_time_six, '%d-%m-%Y %H:%M:%S').date().strftime('%d-%m-%Y'))))
        print(str('{}'.format(datetime.strptime(data_time_six, '%d-%m-%Y %H:%M:%S').time())))


