import json
import torch
import sys

from common_utils import transform_audio
from engine.data import load_wav, log_mel_spectrogram, plot_mel, plot_attn
from engine.models import load_pretrained_wav2vec
from vocoder.env import AttrDict

sys.path.append("./vocoder")
from vocoder.models import Generator


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
ckpt_path = "./fragmentvc.pt"
wav2vec_path = "facebook/wav2vec2-base"
vocoder_path = "./generator.pt"
vocoder_config_path = "./generator_config.json"
preemph = 0.97
sample_rate = 16000
n_mels = 80
n_fft = 1280
hop_len = 320
win_len = 1280
f_min = 50
f_max = None

def convert(src_wav, tgt_wav):

  wav2vec = load_pretrained_wav2vec(wav2vec_path).to(device)
  print("[INFO] Wav2Vec is loaded from", wav2vec_path)

  model = torch.jit.load(ckpt_path).to(device).eval()
  print("[INFO] FragmentVC is loaded from", ckpt_path)

  vocoder_config = json.loads(open(vocoder_config_path).read())
  vocoder = Generator(AttrDict(vocoder_config)).to(device).eval()
  vocoder_state_dict = torch.load(vocoder_path, map_location=device)
  vocoder.load_state_dict(vocoder_state_dict['generator'])
  print("[INFO] Vocoder is loaded from", vocoder_path)

  src_wav = torch.FloatTensor(src_wav).unsqueeze(0).to(device)
  print("[INFO] source waveform shape:", src_wav.shape)

  tgt_mel = log_mel_spectrogram(
    tgt_wav, preemph, sample_rate, n_mels, n_fft, hop_len, win_len, f_min, f_max
  )

  tgt_mel = torch.FloatTensor(tgt_mel.T).unsqueeze(0).to(device)
  print("[INFO] target spectrograms shape:", tgt_mel.shape)

  with torch.no_grad():
    src_feat = wav2vec.extract_features(src_wav, None)[0]
    print("[INFO] source Wav2Vec feature shape:", src_feat.shape)

    out_mel, _ = model(src_feat, tgt_mel)
    print("[INFO] converted spectrogram shape:", out_mel.shape)

    out_wav = vocoder(out_mel).squeeze()
    out_wav = out_wav.cpu().numpy()
    print("[INFO] generated waveform shape:", out_wav.shape)

  return out_wav

def get_prediction(src, tgt):
  result_wav = convert(src, tgt)
  # try:
  #   result_wav = convert(src, tgt)
  # except Exception:
  #   print(Exception)
  #   return 0, 'error'

  return result_wav
