from usecase.syntax.execute_syntax import ExecuteSyntax


def lambda_handler(event, context):
    try:
        print('lambda-function')
        execute_sintaxe = ExecuteSyntax(event)
        execute_sintaxe.execute()
    except Exception as e:
        raise e
    return {'statusCode': '200'}
