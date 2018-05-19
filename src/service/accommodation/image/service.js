function AccommodationImageService(){
  this.URL_BASE = 'accommmodation/image';
};
AccommodationImageService.prototype.apiRoute = function(){
  return this.URL_BASE;
}
AccommodationImageService.prototype.get_Classify = function(req, res) {
  res.json({ message: `Classify service`});   
};
AccommodationImageService.prototype.post_Classify = function(req, res) {
  res.json({ message: `Classify service`});   
};
module.exports = AccommodationImageService;