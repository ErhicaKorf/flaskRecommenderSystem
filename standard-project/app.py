from flask import Flask
import recommender
from flask import Flask,request

app = Flask(__name__)


@app.route('/api/getMovies', methods=['POST'])
def api_getBalances():
    print(request.json)
    result = recommender.content_based_recommender(str(request.json["movie"]))
    print(result)
    return result

if __name__ == '__main__':
    app.run()