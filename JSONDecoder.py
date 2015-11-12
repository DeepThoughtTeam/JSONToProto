import simplejson as json

# This JSON decoder decode JSON format file to
# caffe configuration format file

class JSONDecoder:
  def decodeFromFile(self, file_path, output_path):
    json_data=open(file_path).read()
    caffe_data = self.decode(json_data)
    f = open(output_path,'w+')
    f.write(caffe_data)
    f.close()

  def decode(self, j=''):
    if len(j) == 0:
      return
    data = json.loads(j)
    return self.decodeRootDictToStr(data, 0)

  def decodPairToStr(self, key, value):
    res = ""
    res += str(key)
    res += ": "
    if isinstance(value, str):
      if value.isupper():
        res += value
      else:
        res += "\"" + value +"\""
    else:
      res += str(value)
    res +="\n"
    return res

  def decodeValueToStr(self, value):
    res = ""
    if isinstance(value, str):
      if value.isupper():
        res += value
      else:
        res += "\"" + value +"\""
    else:
      res += str(value)
    res +="\n"
    return res

  def decodeRootDictToStr(self, dictionary, tab):
    tabs = "  " * tab
    res = ""
    for key,value in dictionary.iteritems():
      if isinstance(value, dict):
        res += tabs
        res += key
        res += " "
        res += self.decodeDictToStr(value, tab + 1);
      elif isinstance(value, list): # assume list only contains dicts
        for element in value:
          res += tabs
          res += key
          if isinstance(element, dict):
            res += " "
            res += self.decodeDictToStr(element, tab + 1)
          else:
            res += ": "
            res += self.decodeValueToStr(element)
      else:
        res += tabs
        res += self.decodPairToStr(key, value)
    res += (tab - 1) * "  "
    return res

  def decodeDictToStr(self, dictionary, tab):
    tabs = "  " * tab
    res = "{\n"
    for key,value in dictionary.iteritems():
      if isinstance(value, dict):
        res += tabs
        res += key
        res += " "
        res += self.decodeDictToStr(value, tab + 1);
      elif isinstance(value, list):
        for element in value:
          res += tabs
          res += key

          if isinstance(element, dict):
            res += " "
            res += self.decodeDictToStr(element, tab + 1)
          else:
            res += ": "
            res += self.decodeValueToStr(element)
      else:
        res += tabs
        res += self.decodPairToStr(key, value)
    res += (tab - 1) * "  "
    res += "}\n"
    return res

if __name__ == "__main__":
  decoder = JSONDecoder()
  decoder.decodeFromFile("data/test.json", "data/jsonsample.prototxt")
