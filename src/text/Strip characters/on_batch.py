def strip(s):
    fn_map = {"both": s.str.strip, "left": s.str.lstrip, "right": s.str.rstrip}    
    return fn_map[params['side(s) to strip'][0]](params['characters'])

df[attributes['columns to strip']] = df[attributes['columns to strip']].apply(strip)