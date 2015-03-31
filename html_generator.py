def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text


def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

# This is an example of what a list of concepts might look like.
LIST_OF_CONCEPTS = [ ['Lists', 'Lists are very powerful data structure. It is an ordered collection of objects.'],
                             ['For Loop', 'For Loops allow you to iterate over lists'] ]


def make_HTML_for_many_concepts(list_of_concepts):
    res = ''
    for row in list_of_concepts:
        concept_title = row[0]
        concept_description = row[1]
        res += generate_concept_HTML(concept_title, concept_description)
    return res



print make_HTML_for_many_concepts(LIST_OF_CONCEPTS)

