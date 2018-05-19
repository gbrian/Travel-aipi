
function TravelAIPI(){

}

TravelAIPI.prototype.start = function(){
  const express = require('express');
  const app = express();
  const bodyParser = require('body-parser');
  const port = process.env.PORT || 5000

  app.use(bodyParser.urlencoded({ extended: true }));
  app.use(bodyParser.json());

  var router = express.Router();

  function register(path){
    var _function = require(path);
    var service = new _function();
    Object.keys(_function.prototype)
      .map(k => /(get|post)\_(.*)/.exec(k))
      .filter(k => k)
      .map(match => console.log(`Registering: /${service.apiRoute()}/${match[2]}`) +
        router[match[1]](`/${service.apiRoute()}/${match[2]}`.toLocaleLowerCase(), function(req, res){
          _function.prototype[match[0]].call(service, req, res);
        })
      );
  }
  ['./src/service/accommodation/image/service.js'].map(register);

  app.use('/', router);
  // START THE SERVER
  // =============================================================================
  app.listen(port);
  console.log('Magic happens on port ' + port);
}

new TravelAIPI().start();