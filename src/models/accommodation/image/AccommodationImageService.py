
import json, os, base64
from six.moves import urllib
from src.models.accommodation.image.ImageGraph import ImageGraph
    
class AccommodationImageService():
  def __init__(self):
    self.path = os.path.dirname(__file__)
    self.imageGraph = ImageGraph()
  
  def predict(self, path):
    return self.imageGraph.predict(path)