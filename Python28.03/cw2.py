#!/usr/bin/env python
#encoding: utf-8
import pickle

slownik = {
    'k1': 'w1',
    'k2': 'w2',
    3: [1,2,3],
    
}
pickle_str = json.dumps(slownik)

print(isinstance(pickle_str,basestring))
slownik2 = pickle.loads(pickle_str)
print slownik2.items()
