# Copyright 2019 The TensorFlow GAN Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""TF-GAN evaluation module.

This module supports techniques such as Inception Score, Frechet Inception
distance, and Sliced Wasserstein distance.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Collapse eval into a single namespace.
from tensorflow_gan.python.eval import classifier_metrics
from tensorflow_gan.python.eval import eval_utils
from tensorflow_gan.python.eval import sliced_wasserstein
from tensorflow_gan.python.eval import summaries

# pylint: disable=wildcard-import
from tensorflow_gan.python.eval.classifier_metrics import *
from tensorflow_gan.python.eval.eval_utils import *
from tensorflow_gan.python.eval.sliced_wasserstein import *
from tensorflow_gan.python.eval.summaries import *
# pylint: enable=wildcard-import

allowed_symbols = classifier_metrics.__all__
allowed_symbols += eval_utils.__all__
allowed_symbols += sliced_wasserstein.__all__
allowed_symbols += summaries.__all__
