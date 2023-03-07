from usecase.sintaxe.execute_sintaxe import ExecuteSintaxe


def lambda_handler(event, context):
    try:
        print('lambda-function')
        execute_sintaxe = ExecuteSintaxe(event)
        execute_sintaxe.execute()
    except Exception as e:
        raise e
    return {'statusCode': '200'}
