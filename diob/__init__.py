class diob(dict):
    def __getattr__(self, key):
        if key in self:
            return self[key]
        else:
            return None

    def __setattr__(self, key, val):
        self[key] = val

    def __delattr__(self, key):
        if key in self:
            del self[key]

    @classmethod
    def deep(klass, arg=None, **kwargs):
        res = klass(arg) if arg else klass(kwargs)
        for key in res:
            val = res[key]
            if type(val) is dict:
                res[key] = klass.deep(val)
            elif isinstance(val, list):
                for idx, item in enumerate(val):
                    if type(item) is dict:
                        val[idx] = klass.deep(item)
        return res

    def todict(self):
        res = dict(self)
        for key in res:
            val = res[key]
            if isinstance(val, self.__class__):
                res[key] = dict(val)
            elif isinstance(val, list):
                for idx, item in enumerate(val):
                    if isinstance(item, self.__class__):
                        val[idx] = dict(item)
        return res
