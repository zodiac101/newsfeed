import flask
from flask import request

from utils.db_interface import query_by_date, query_by_date_range

app = flask.Flask(__name__)
app.config['Debug'] = True



@app.route('/newsfeed/v1/getCount', methods=['GET'])
def get_count():
    if 'source' not in request.args:
        return 'source is required', 400
    source = str(request.args['source'])
    if 'query_date' in request.args:
        query_date = request.args['query_date']
        result = query_by_date(query_date, source)
        return {'count': result}, 200
    elif 'start_date' in request.args and 'end_date' in request.args:
        start_date = request.args['start_date']
        end_date = request.args['end_date']
        result = query_by_date_range(start_date, end_date, source)
        return {'count': result}, 200
    else:
        return 'Either query_date or both start_date and end_date are required', 400


app.run()



