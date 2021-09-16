import torch
import numpy as np

import vortex.runtime as vrt

def predict_lung(input):
    runtime_device = 'cpu'
    export_path = '/content/export_test_final_v2.onnx'
    model = vrt.create_runtime_model(model_path=export_path,
                                     runtime=runtime_device)
    pred = model(input)
    result = pred[0]['class_label'][0][0].astype('int')
    confidence = pred[0]['class_confidence'][0][0]

    return [result, confidence]