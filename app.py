from flask import Flask, render_template
from flask import jsonify, json
from flask_cors import CORS
from Data.Dataquery.WebQuery import *

app = Flask(__name__, static_folder='./static', static_url_path='')
CORS(app, resources='/*')
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRNT_REGULAR'] = False
app.config['JSON_SORT_KEYS'] = False

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/issuerank")
def taskissue():
    cfpath = 'D:\\bigdata\\config.ini'
    data = QueryIssue(cfpath)
    print(jsonify(data))
    return jsonify(data)

@app.route("/webimrank")
def taskwebim():
    cfpath = 'D:\\bigdata\\config.ini'
    data = QueryWebim(cfpath)
    print(jsonify(data))
    return jsonify(data)

@app.route("/communityrank")
def taskcommunity():
    cfpath = 'D:\\bigdata\\config.ini'
    data = QueryCommunity(cfpath)
    print(jsonify(data))
    return jsonify(data)

@app.route("/hotline")
def taskhotline():
    cfpath = 'D:\\bigdata\\config.ini'
    data = QueryHotline(cfpath)
    print(jsonify(data))
    return jsonify(data)

@app.route("/hotlineweek")
def taskhotweek():
    cfpath = 'D:\\bigdata\\config.ini'
    data = QueryHotlineweek(cfpath)
    print(jsonify(data))
    return jsonify(data)

@app.route("/webimweek")
def taskwebimweek():
    cfpath = 'D:\\bigdata\\config.ini'
    data = QueryWebimweek(cfpath)
    print(jsonify(data))
    return jsonify(data)

@app.route("/kpi")
def taskkpi():
    cfpath = 'D:\\bigdata\\config.ini'
    data = QueryKpi(cfpath)
    print(jsonify(data))
    return jsonify(data)

@app.route("/topkpi")
def tasktopkpi():
    cfpath = 'D:\\bigdata\\config.ini'
    data = QueryTopkpi(cfpath)[0]
    print(jsonify(data))
    return jsonify(data)

@app.route("/tophotline")
def tasktophotline():
    cfpath = 'D:\\bigdata\\config.ini'
    data = QueryTophotline(cfpath)[0]
    print(jsonify(data))
    return jsonify(data)

@app.route("/topissue")
def tasktopissue():
    cfpath = 'D:\\bigdata\\config.ini'
    data = QueryTopissue(cfpath)[0]
    print(jsonify(data))
    return jsonify(data)

@app.route("/topwebim")
def tasktopwebim():
    cfpath = 'D:\\bigdata\\config.ini'
    data = QueryTopwebim(cfpath)[0]
    print(jsonify(data))
    return jsonify(data)

@app.route("/topcommunity")
def tasktopcommunity():
    cfpath = 'D:\\bigdata\\config.ini'
    data = QueryTopcommunity(cfpath)[0]
    print(jsonify(data))
    return jsonify(data)


@app.route("/topstudy")
def tasktopstudy():
    cfpath = 'D:\\bigdata\\config.ini'
    data = QueryTopstudy(cfpath)[0]
    print(jsonify(data))
    return jsonify(data)







if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=True)