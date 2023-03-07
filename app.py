from flask import Flask, jsonify, request
import time
from timeout_decorator import timeout, TimeoutError

app = Flask(__name__)   

@timeout(3) 
def result_return(n):
    ## リクエストパラメータがあるか確認
    if not n:
        return jsonify({'status':400,'message': 'n is required'}), 400 
    ## nが数字かどうか判定
    if n.isdigit():
        n = int(n)
        if n == 0:
            return jsonify({'result': 0}), 200
        elif n == 1:
            return jsonify({'result': 1}), 200
        else:
            a, b = 0, 1
            for _ in range(n - 1):
                a, b = b, a + b
            return jsonify({'result': b}), 200
    ## 文字列や負の数、小数の処理
    else:
        return jsonify({'status': 400, 'message': f'n = {n} . n must be a positive integer'}), 400

@app.route("/fib",methods=['GET'])
def fib():
    try:
        return result_return(request.args.get('n'))
    except TimeoutError as e:
        print(e)
        return jsonify({'status': 504, 'message':'TimeoutError'}),504
    except Exception as e:
        print(e)
        return jsonify(message='Comment Error'),500
    

@app.route('/fib', methods=['POST', 'PUT', 'DELETE'])
def handle_other_methods():
    method = request.method
    return jsonify({'status': 405, 'message': f'Method ({method}) Not Allowed'}), 405


@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'status': 404, 'message': 'Not Found.'}), 404


if __name__ == "__main__":
    app.run(use_reloader=False, threaded=False) 