from flask import Flask, jsonify, request

app = Flask(__name__)              

@app.route("/fib",methods=['GET'])
def fib():
    n = request.args.get('n')
    ## リクエストパラメータがあるか確認
    if not n:
        return jsonify({'status':400,'message': 'n is required'}), 400 
    ## nが数字かどうか判定
    if n.isdigit():
        n = int(request.args.get('n'))
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
    

@app.route('/fib', methods=['POST', 'PUT', 'DELETE'])
def handle_other_methods():
    method = request.method
    return jsonify({'status': 405, 'message': f'Method ({method}) Not Allowed'}), 405


@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'status': 404, 'message': 'Not Found.'}), 404


if __name__ == "__main__":
    app.run() 