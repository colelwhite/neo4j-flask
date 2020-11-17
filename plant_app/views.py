from plant_app import plant_app
from flask import render_template, redirect, jsonify
from flask.helpers import url_for
from py2neo import Graph
# from webargs import fields
# from webargs.flaskparser import use_args, use_kwargs

# Connect to the graph. It is local so uri not specified
graph = Graph(user='neo4j', password='Typha2')

# url pattern and function
@plant_app.route('/')
def hello():

    query = '''
    MATCH (t:Taxon) WHERE t.scientificName CONTAINS "Abies"
    RETURN t.scientificName, t.acceptedNameUsageID, t.taxonRank, t.order,
           t.family, t.genus, t.specificEpithet
    '''
    data = graph.run(query)

    headers = ['Scientific Name', 'ID', 'Rank', 'Order', 'Family', 'Genus',
               'Specific Epithet']
    results=list(data)
    print(results)



    return render_template('public/index.html', results=results, headers=headers, query=query)

@plant_app.route('/about')
def about():
    return "All about Flask"

# Get everything from Taxon
@plant_app.route('/api/v0.1/taxon', methods=['GET'])
def get_taxa():
    query = '''
    MATCH (t:Taxon)
    RETURN t.scientificName, t.acceptedNameUsageID, t.taxonRank, t.order,
    t.family, t.genus, t.specificEpithet
    '''
    data = graph.run(query)

    results = list(data)
    print(results)
    return jsonify({'results': results})

# Query Taxon by acceptedNameUsageID
@plant_app.route('/api/v0.1/taxon/<acceptedNameUsageID>', methods=['GET'])
def get_taxa_by_acceptedID(acceptedNameUsageID):
    query = ('MATCH (t:Taxon) WHERE t.acceptedNameUsageID = "{}"'
             'RETURN t.scientificName, t.acceptedNameUsageID, t.taxonRank,'
             't.order, t.family, t.genus, t.specificEpithet').format(acceptedNameUsageID)
    data = graph.run(query)
    results = list(data)
    return jsonify({'results': results})

# Query by Genus
@plant_app.route('/api/v0.1/genus/<genus>', methods=['GET'])
def get_taxa_by_genus(genus):
    query = ('MATCH (t:Taxon) WHERE t.genus = "{}"'
             'RETURN t.scientificName, t.acceptedNameUsageID, t.taxonRank,'
             't.order, t.family, t.genus, t.specificEpithet').format(genus)
    data = graph.run(query)

    query2 = ('MATCH (t:Taxon) WHERE t.genus = "{}"'
             'RETURN t.scientificName, t.acceptedNameUsageID, t.taxonRank,'
             't.order, t.family, t.genus, t.specificEpithet').format(genus)
    data2 = graph.run(query2)
    print(data2)

    results = list(data)
    return jsonify({'results': results})

@plant_app.route('/static', methods=['GET'])
def show_static_files():
    return redirect(url_for('static',filename='html/static.html'))
