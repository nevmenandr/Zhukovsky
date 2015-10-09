=== Run information ===

Evaluator:    weka.attributeSelection.CfsSubsetEval 
Search:weka.attributeSelection.ScatterSearchV1 -T 0.0 -Z -1 -R 0 -S 1 -D
Relation:     metrics_table_no_context
Instances:    12106
Attributes:   21
              anomalia
              position
              words_count
              accent_vowels
              tf_idf
              pos
              names
              punctuation_in_the_middle
              question
              negation
              line_sentence
              numerals
              subject
              verbs
              andjectives
              adverbs
              personal_pronomen
              prepositions
              part
              conjunction
              conj_constructions
Evaluation mode:evaluate on all training data



=== Attribute Selection on all input data ===

Search Method:
	Scatter Search 
	Init Population: 10
	Kind of Combination: Greedy Combination
	Random number seed: 1
	Debug: true
	Treshold:    0    
	Total number of subsets evaluated: 987
	Merit of best subset found:    0.036


Population: 10
merit    	subset
 0.02926	 [3, 16]
 0.02832	 [5, 8, 12, 15, 16]
 0.03183	 [3, 12, 15, 16]
 0.02747	 [3, 5, 8, 12]
 0.02419	 [8, 16, 19]
 0.01562	 [10, 11, 12]
 0.03385	 [3, 8, 15, 16, 21]
 0.03037	 [2, 3, 8, 16, 18, 19]
 0.02934	 [3, 9, 10, 12, 13, 15, 16, 19]
 0.01842	 [12, 18, 19]

ReferenceSet:
----------------Most Significants Solutions--------------
 0.03385	 [3, 8, 15, 16, 21]
 0.03183	 [3, 12, 15, 16]
----------------Most Diverses Solutions--------------
 0.01842	 [12, 18, 19]
 0.01562	 [10, 11, 12]

Last Reference Set Updated:
merit    	subset
 0.03564	 [3, 8, 11, 12, 15, 16, 21]
 0.01842	 [12, 18, 19]
 0.01562	 [10, 11, 12]
 0.03211	 [3, 8, 11, 12, 15, 18, 19]

Attribute Subset Evaluator (supervised, Class (numeric): 1 anomalia):
	CFS Subset Evaluator
	Including locally predictive attributes

Selected attributes: 3,8,11,12,15,16,21 : 7
                     words_count
                     punctuation_in_the_middle
                     line_sentence
                     numerals
                     andjectives
                     adverbs
                     conj_constructions

