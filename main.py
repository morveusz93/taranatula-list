from db_connection import connect
from flask import Flask, jsonify, make_response, abort


app = Flask(__name__)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/tarantulas')
def index():
    routes = {
        'list of families': '[hostname]/tarantulas/families',
        'list of genus in family': '[hostname]/tarantulas/family/<name of family>',
        'list of species in genus': '[hostname]/tarantulas/genus/<name of genus>',
        'list of species in location': '[hostname]/tarantulas/location/<name of location>',
    }
    return(jsonify(routes))

@app.route('/tarantulas/families')
def get_families():
    query = """SELECT family, COUNT(species) FROM species GROUP BY family ORDER BY 1;"""
    rows = connect(query)
    families = {
        'allFamilies': [
            {
            'name': row[0],
            'numberOfSpecies': row[1],
            'genusList': f'/tarantulas/family/{row[0].lower()}'
            }
        for row in rows
    ]}
    return jsonify(families)

@app.route('/tarantulas/family/<name>')
def get_family(name):
    if not name.isalpha(): abort(400)
    name = name.capitalize()
    query = f"""SELECT genus, COUNT(species) FROM species WHERE family = '{name}' GROUP BY genus ORDER BY 1;"""
    rows = connect(query)
    if len(rows) < 1: abort(404)
    family = {
        name: [
            {
                'family': name,
                'genus': row[0],
                'numberOfSpecies': row[1],
                'speciesList': f'/tarantulas/genus/{row[0].lower()}'
            }
            for row in rows
        ]
    }
    return jsonify(family)

@app.route('/tarantulas/genus/<name>')
def get_genus(name):
    if not name.isalpha(): abort(400)
    name = name.capitalize()
    query = f"""SELECT family, species, country FROM species WHERE genus = '{name}' ORDER BY 1;"""
    rows = connect(query)
    if len(rows) < 1: abort(404)
    genus = {
        name: [
            {
                'family': row[0],
                'species': row[1],
                'location': row[2]
            }
            for row in rows
        ]
    }
    return jsonify(genus)

@app.route('/tarantulas/location/<name>')
def get_species_by_loacation(name):
    if not name.isalpha(): abort(400)
    name = name.capitalize()
    query = f"""SELECT family, species, country FROM species WHERE '{name}' = ANY(country) ORDER BY 2;"""
    rows = connect(query)
    if len(rows) < 1: abort(404)
    genus = {
        name: [
            {
                'family': row[0],
                'species': row[1],
                'location': row[2]
            }
            for row in rows
        ]
    }
    return jsonify(genus)


if __name__ == '__main__':
    app.run()