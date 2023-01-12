# NEON AI (TM) SOFTWARE, Software Development Kit & Application Framework
# All trademark and other rights reserved by their respective owners
# Copyright 2008-2022 Neongecko.com Inc.
# Contributors: Daniel McKnight, Guy Daniels, Elon Gasper, Richard Leeds,
# Regina Bloomstine, Casimiro Ferreira, Andrii Pernatii, Kirill Hrymailo
# BSD-3 License
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from this
#    software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS  BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
# OR PROFITS;  OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE,  EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
import json
import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from neon_audio_normalizer_plugin import *
from speech_recognition import AudioData

import wave
from scipy.io import wavfile
#samplerate, data = wavfile.read('where is pandora store.wav')
#
# segment = AudioSegment.from_file('/home/dmytro/Documents/GitHub/neon-audio-plugin-normalizer/neon_audio_normalizer_plugin/where is pandora store.wav')
# audio_data = AudioData(segment.raw_data, segment.frame_rate,
# segment.sample_width)
#
# instance = AudioNormalizer()
# a= instance.transform(audio_data)
# print(a[-1])

class NormalaizerTransformerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.extractor = AudioNormalizer()

    def test_transform(self):
        from pathlib import Path
        current=Path.cwd()
        path = str(current) + '/where is pandora store.wav'
        print(path)
        segment = AudioSegment.from_file(path)
        audio_data = AudioData(segment.raw_data, segment.frame_rate,segment.sample_width)
        lang = (self.extractor.transform(audio_data))
        print(type(lang))
        test=lang[-1]
        #print(type(test))
        self.assertIsInstance(lang,tuple)
        self.assertTrue(os.path.isfile(test['audio_filename']))