import torch
import resampy
import os

required_sr = 16000

models_info = [
  ("./wav2vec_small.pt", "https://dl.fbaipublicfiles.com/fairseq/wav2vec/wav2vec_small.pt"),
  ("./vocoder.pt", "https://github.com/SolomidHero/FragmentVC-with-RAdam/releases/download/v1.2/vocoder.pt"),
  ("./fragmentvc.pt", "https://github.com/SolomidHero/FragmentVC-with-RAdam/releases/download/v1.2/fragmentvc.pt"),
]

def _download(filepath, url, refresh=False, agent='wget'):
  '''
  Download from url into filepath using agent if needed

  Ref: https://github.com/s3prl/s3prl
  '''

  dirpath = os.path.dirname(filepath)
  os.makedirs(dirpath, exist_ok=True)

  if not os.path.isfile(filepath) or refresh:
    if agent == 'wget':
      os.system(f'wget {url} -O {filepath}')
    else:
      print('[Download] - Unknown download agent. Only \'wget\' are supported.')
      raise NotImplementedError
  else:
    print(f'Using checkpoint found in {filepath}')


def load_models():
  for path, url in models_info:
    _download(path, url)


def transform_audio(audio, sr):
  if len(audio.shape) >= 2:
    audio = audio.mean(-1)
  audio = resampy.resample(audio, sr, required_sr)
  return torch.from_numpy(audio).float()
