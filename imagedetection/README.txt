Dependencies
  yolo.h5
    https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5
  tensorflow (<2.0)
    pip3 install --upgrade tensorflow==1.14
  opencv (4.2.0.34)
    pip3 install opencv-python
  keras (2.3.1)
    pip3 install keras
  imageai (2.1.5)
    pip3 install imageai --upgrade

Flow

  detect2.py
    Runs through files in imagedetection/video_database
    Generates corresponding videos in imagedetection/processed_videos
    Generates .objects files in imagedetection/detected_objects. Open with any text editor.
  
  condense.py
    Counts and collects sum of all objects in .objects files in imagedetection/detected_objects
    Generates .condensed files in imagedetection/condensed_objects. Open with any text editor.

Sources
  https://imageai.readthedocs.io/en/latest/
