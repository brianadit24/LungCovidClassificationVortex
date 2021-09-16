import vortex.runtime as vrt
from src.load_img_transform import transform_image

def predict_lung(input):
    runtime_device = 'cpu'
    export_path = 'model/lung_covid.onnx'
    model = vrt.create_runtime_model(model_path=export_path,
                                     runtime=runtime_device)
    labels = model.class_names
    input = transform_image(input)
    pred = model(input)
    result = pred[0]['class_label'][0][0].astype('int')
    result = labels[result]
    confidence = pred[0]['class_confidence'][0][0]

    return [result, confidence]