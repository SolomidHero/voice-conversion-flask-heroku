import os

from flask import Flask, render_template, request, redirect

import torch
import soundfile as sf
import base64

from inference import get_prediction
from utils import transform_audio, read_audio, audio_to_bytes, required_sr, load_models

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
      wav, sr = read_audio(file_obj)
      wav = transform_audio(wav, sr)
      data.append(wav)

    result = get_prediction(data[0], data[1])
    output = audio_to_bytes(result)

    return render_template(
      'result.html',
      snd=output,
      src=audio_to_bytes(data[0].numpy()),
      tgt=audio_to_bytes(data[1].numpy())
    )

  return render_template('index.html')


if __name__ == '__main__':
  app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
