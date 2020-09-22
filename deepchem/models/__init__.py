"""
Gathers all models in one place for convenient imports
"""
# flake8: noqa
from deepchem.models.models import Model
from deepchem.models.keras_model import KerasModel
from deepchem.models.multitask import SingletaskToMultitask
from deepchem.models.callbacks import ValidationCallback

from deepchem.models.fcnet import MultitaskRegressor
from deepchem.models.fcnet import MultitaskClassifier
from deepchem.models.fcnet import MultitaskFitTransformRegressor
from deepchem.models.IRV import MultitaskIRVClassifier
from deepchem.models.robust_multitask import RobustMultitaskClassifier
from deepchem.models.robust_multitask import RobustMultitaskRegressor
from deepchem.models.progressive_multitask import ProgressiveMultitaskRegressor, ProgressiveMultitaskClassifier
from deepchem.models.graph_models import WeaveModel, DTNNModel, DAGModel, GraphConvModel, MPNNModel
from deepchem.models.scscore import ScScoreModel

from deepchem.models.seqtoseq import SeqToSeq
from deepchem.models.gan import GAN, WGAN
from deepchem.models.cnn import CNN
from deepchem.models.text_cnn import TextCNNModel
from deepchem.models.atomic_conv import AtomicConvModel
from deepchem.models.chemnet_models import Smiles2Vec, ChemCeption

# scikit-learn model
from deepchem.models.sklearn_models import SklearnModel

# XGBoost model
try:
  from deepchem.models.xgboost_models import XGBoostModel
except ModuleNotFoundError:
  pass

# PyTorch models
try:
  from deepchem.models.torch_models import TorchModel
  from deepchem.models.torch_models import CGCNN, CGCNNModel
  from deepchem.models.torch_models import GAT, GATModel
except ModuleNotFoundError:
  pass

#################### Compatibility imports for renamed TensorGraph models. Remove below with DeepChem 3.0. ####################

from deepchem.models.text_cnn import TextCNNTensorGraph
from deepchem.models.graph_models import WeaveTensorGraph, DTNNTensorGraph, DAGTensorGraph, GraphConvTensorGraph, MPNNTensorGraph
from deepchem.models.IRV import TensorflowMultitaskIRVClassifier
