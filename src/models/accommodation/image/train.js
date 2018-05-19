const tf = require('@tensorflow/tfjs');
const model = tf.sequential();
const labeled = require('./labeled.json');

const MOBILENET_MODEL_PATH =
    // tslint:disable-next-line:max-line-length
    'https://storage.googleapis.com/tfjs-models/tfjs/mobilenet_v1_0.25_224/model.json';

tf.loadModel(MOBILENET_MODEL_PATH)
  .then(mobilenet =>{
  // Warmup the model. This isn't necessary, but makes the first prediction
    // faster. Call `dispose` to release the WebGL memory allocated for the return
    // value of `predict`.
    var res = mobilenet.predict(tf.zeros([1, IMAGE_SIZE, IMAGE_SIZE, 3])).dispose();
    console.log(res);
  });
