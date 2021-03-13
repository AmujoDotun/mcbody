from flask import Flask, request ,jsonify
import json


app = Flask(__name__)


@app.route('/api/transactions',methods=["POST"])
def get_transactions():
    transaction_details = request.json["transaction_details"]
    print(transaction_details)
    with open('./db.json') as db:
        data = json.load(db)
        for transaction in data:
            if transaction['TRANSACTION DETAILS'] == transaction_details:
                    print(transaction)
                    results = []
                    results.append(transaction)
    return jsonify(results)


if __name__ == '__main__':
   app.run()



            
