access dict like an object

## Installation

```
pip install diob
```

## Usage

create a diob like you create a dict

```
>>> from diob import diob
>>> person = diob(name='john', age=42)
>>> cat = diob({'name': 'mr fluffy', age=5})
```

access it like a dict or an object

```
>>> person['name']
'john'
>>> person.name
'john'
>>> person.name = 'sam'
>>> person.name
'sam'
>>> person.country = 'china'
>>> person.country
'china'
>>> del person.country
>>> person
{'name': 'sam', 'age': 42}
```

object-style access to unkown key returns `None` whereas in dict-style raises **KeyError**

it can do whatever a dict can do

```
>>> len(person)
2
>>> 'name' in person
True
>>> 'unknown_key' in person
False
>>> for key in person: print(key, person[key]) 
name sam
age 42
>>> import json
>>> json.dumps(person)
'{"name": "sam", "age": 42}'
```

create deep diob with `diob.deep()`

```
>>> obj = diob.deep(a=1, b={'c': 2}, d=[3, {'e': 4}])
>>> obj.b.c = 'deep'
>>> obj.d[1].e = 'deeper'
>>> obj
{'a': 1, 'b': {'c': 'deep'}, 'd': [3, {'e': 'deeper'}]}
```

convert diob to dict by passing it to `dict`

```
>>> type(person)
<class 'diob.diob'>
>>> person_dict = dict(person)
>>> type(person_dict)
<class 'dict'>
>>> person_dict['name']
'sam'
```

use `.todict()` to perform deep diob to dict conversion

```
>>> type(obj.b)
<class 'diob.diob'>
>>> obj_dict = obj.todict()
>>> type(obj_dict['b'])
<class 'dict'>
>>> obj_dict['b']
{'c': 'deep'}
```

## License

MIT
