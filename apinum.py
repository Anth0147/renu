from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configura la conexión a la base de datos
db_config = {
    'user': 'root',
    'password': '123456',
    'host': '172.233.209.59',
    'database': 'basecel',
}

def search_in_table(table_name, lookup_value):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    query = f"SELECT telefono {table_name} WHERE documento = %s"
    cursor.execute(query, (lookup_value,))

    result = cursor.fetchone()
    cursor.close()
    conn.close()

    return result

@app.route('/claro/search', methods=['GET'])
def search_claro():
    lookup_value = request.args.get('value')
    result = search_in_table('claro', lookup_value)

    if result:
        return jsonify({'result': result[0]})
    else:
        return jsonify({'error': 'Not Found'}), 404

@app.route('/movistar/search', methods=['GET'])
def search_movistar():
    lookup_value = request.args.get('value')
    result = search_in_table('movistar', lookup_value)

    if result:
        return jsonify({'result': result[0]})
    else:
        return jsonify({'error': 'Not Found'}), 404

@app.route('/entel/search', methods=['GET'])
def search_entel():
    lookup_value = request.args.get('value')
    result = search_in_table('entel', lookup_value)

    if result:
        return jsonify({'result': result[0]})
    else:
        return jsonify({'error': 'Not Found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
