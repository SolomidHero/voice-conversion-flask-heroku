import os
import io

from flask import Flask, render_template, request, redirect

import torch
import soundfile as sf
import base64

from inference import get_prediction
from utils import transform_audio, required_sr, load_models
from scipy.io.wavfile import write


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
  if request.method == 'POST':
    load_models()
    data = []
    for key in ['source', 'target']:
      if key not in request.files:
        print(f"no {key}")
        return redirect(request.url)
      file_obj = request.files.get(key)
      if not file_obj:
        print("incorrect file_obj")
        return

      print(f"FILE {key}: {file_obj}")
      wav, sr = sf.read(file_obj)
      wav = transform_audio(wav, sr)
      data.append(wav)

    result = get_prediction(data[0], data[1])
    # result = data[0].cpu().numpy()
    bytes_wav = bytes()
    byte_io = io.BytesIO(bytes_wav)
    write(byte_io, required_sr, result)
    result_bytes = byte_io.read()
    output = base64.b64encode(result_bytes).decode('UTF-8')

    # print(output)

    return render_template('result.html', snd=output)

  return render_template('index.html')


if __name__ == '__main__':
  app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
