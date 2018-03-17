"""
French Regex tokenizer for NLP using NLTK
"""

import nltk

data = "aujourd'hui L'astronomes  12,40€ amateurs 30% U.S.A. d'abord l'également un rôle important en recherche; les plus sérieux participant couramment au suivi d'étoiles variables, à la découverte de nouveaux astéroïdes et de nouvelles comètes, etc."

pattern = r'''(?x)              # set flag to allow verbose regexps
        aujourd'hui             # exception 1
        | prud'hom\w+           # exception 2
        | \w'                   # contractions d', l', j', t', s'
        | \d+(?:,\d+)?%?€?      # currency and percentages, e.g. 12,40€, 82%        
        | (?:[A-Z]\.)+          # abbreviations, e.g. U.S.A.
        | \w+(?:-\w+)*          # words with optional internal hyphens
        | \.\.\.                # ellipsis
        #| [][.,;"'?():_`-]     # these are separate tokens; includes ], [
    '''
print(nltk.regexp_tokenize(data, pattern))

"""
output :
["aujourd'hui", "L'", 'astronomes', '12,40€', 'amateurs', '30%', 
'U.S.A.', "d'", 'abord', "l'", 'également', 'un', 'rôle', 'important', 
'en', 'recherche', 'les', 'plus', 'sérieux', 'participant', 'couramment', 
'au', 'suivi', "d'", 'étoiles', 'variables', 'à', 'la', 'découverte', 'de', 
'nouveaux', 'astéroïdes', 'et', 'de', 'nouvelles', 'comètes', 'etc']

"""

