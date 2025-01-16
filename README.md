# End-to-end Waste Detection Using YOLOv5

## Introduction

This project implements an end-to-end object detection system using YOLOv5, specifically designed to identify three common objects: pens, bananas, and books. The system leverages the power of Ultralytics YOLOv5 pre-trained model, which has been fine-tuned on a custom dataset to achieve precise detection of these specific objects.

The dataset was carefully curated from the Open Images Dataset (available at [Open Images Visual Explorer](https://storage.googleapis.com/openimages/web/visualizer/index.html)). To streamline the data collection process, I developed a custom Python script that automatically downloads and formats the images in YOLO-compatible format, ensuring proper annotation and organization of the training data.

The model training was performed in Google Colab, taking advantage of its GPU resources for efficient computation. After successful training and validation, the entire system was transformed into a production-ready workflow, complete with a user-friendly web interface for real-time object detection.


## Project Structure
```
├── constants            # Configuration and constant values
├── entity              # Core data structures
├── components          # Modular components
├── pipelines           # Processing pipelines
├── app.py             # Main application file
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation
```


## How to Run?

### STEPS:

1. Clone the repository:
```bash
(https://github.com/guniyal24/Object-Detection-Using-Yolov5)
```

2. Create and activate a virtual environment:
```bash
python3.11 -m venv yolo
source yolo/bin/activate
```

3. Install the requirements:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python3.11 app.py
```

Now, open up your browser and navigate to the local host and port shown in the terminal to access the web interface.



## Technologies Used
- Python 3.11
- YOLOv5
- PyTorch
- Flask

## Future Improvements
- Add support for more object classes
- Implement real-time video detection
- Enhance the web interface with additional features
- Improve model performance through further fine-tuning

Feel free to contribute to this project by submitting pull requests or opening issues for any bugs or feature requests you may have.
