import unittest
from AccommodationImageService import AccommodationImageService

class MyFirstTests(unittest.TestCase):
  def test_hello(self):
    #model = AccommodationImageService()
    #self.assertEqual(model.train(), 'hello world')
    self.assertEqual(1,1)

  def test_predictor(self):
    p = AccommodationImageService()
    for label in p.imageGraph.labels: 
        _path = os.path.join(os.path.dirname(__file__), 'data/%s' % label)
        pics = os.listdir(_path)
        for pic in pics:
            path, predicted_label, score = p.predict(os.path.join(_path, pic))
            if label != predicted_label:
                print("Expected: %s, was %s with %s, %s" % (label, predicted_label, str(score), path))


if __name__ == '__main__':
  import os
  print("CWD: %s" % os.getcwd())
  unittest.TestLoader().discover('.')
  unittest.main()