import os
# GoogleCloudStorageから音声ファイルをダウンロード
os.system("gsutil cp gs://rncloud/input/*.wav ./Input")
# wavでforループして、pcmに変換
os.system("for a in ./Input/*.wav; do sox "$a" -t sw -r 48000 -c1 ${a/.wav/.pcm}; done")
# pcmでforループして、RNnoiseを適用
os.system("for a in ./Input/*.pcm; do rnnoise_demo "$a" ${a/.pcm/.pcm}; done")